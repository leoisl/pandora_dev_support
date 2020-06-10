# Copyright 2000-2018 JetBrains s.r.o.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from __future__ import (absolute_import, division, print_function)

import gdb


from libstdcxx.v6.printers import (Iterator,
                                   strip_versioned_namespace,
                                   is_specialization_of)


def safe_cast(value, new_type):
    return value.address.cast(new_type.pointer()).dereference()


class StdListPrinter:

    def __init__(self, typename, value):
        self.typename = typename
        self.value = value
        self.elt_type = value.type.template_argument(0)

        self.head = value['_M_impl']['_M_node']

        self.is_cxx11_abi = not self.head.type.name.endswith('::_List_node_base')
        try:
            self.node_type = gdb.lookup_type('%s::_Node' % value.type)
        except gdb.error:
            if self.is_cxx11_abi:
                self.node_type = self.head.type
            else:
                raise

        self._data_field = self.node_type.fields()[1]  # _M_data or _M_storage
        if self._data_field.name not in ('_M_data', '_M_storage'):
            raise ValueError('Unknown implementation: %s' % self.value.type)

    def _get_data(self, varobj):
        if self._data_field.name == '_M_storage':
            storage = varobj['_M_storage']
            return storage.cast(storage.type.template_argument(0))

        return varobj[self._data_field.name]

    def is_empty(self):
        return self.head.address == self.head['_M_next'] or (self.is_cxx11_abi and self._get_data(self.head) == 0)

    def children(self):
        if self.is_cxx11_abi and self._get_data(self.head) == 0:
            return
        head_ptr = self.head.address
        node_ptr = self.head['_M_next']
        count = 0

        while node_ptr != head_ptr:
            node = node_ptr.dereference().cast(self.node_type)  # not a real node type
            yield ('[%d]' % count, safe_cast(node[self._data_field], self.elt_type))

            count += 1
            node_ptr = node['_M_next']

    def to_string(self):
        return ('empty %s' if self.is_empty() else '%s') % self.typename


class SmartPtrIterator(Iterator):
    "An iterator for smart pointer types with a single 'child' value"

    def __init__(self, val, valtype):
        self.val = val
        self.valtype = valtype

    def __iter__(self):
        return self

    def __next__(self):
        if self.val is None:
            raise StopIteration
        self.val, val = None, self.val
        return ('get()', val.cast(self.valtype.pointer()))

class SharedPointerPrinter:
    "Print a shared_ptr or weak_ptr"

    def __init__ (self, typename, val):
        self.typename = strip_versioned_namespace(typename)
        self.val = val
        self.pointer = val['_M_ptr']

    def children (self):
        return SmartPtrIterator(self.pointer, self.val.type.template_argument(0))

    def to_string (self):
        state = 'empty'
        refcounts = self.val['_M_refcount']['_M_pi']
        if refcounts != 0:
            usecount = refcounts['_M_use_count']
            weakcount = refcounts['_M_weak_count']
            if usecount == 0:
                state = 'expired, weak count %d' % weakcount
            else:
                state = 'use count %d, weak count %d' % (usecount, weakcount - 1)
        return '%s<%s> (%s)' % (self.typename, str(self.val.type.template_argument(0)), state)

class UniquePointerPrinter:
    "Print a unique_ptr"

    def __init__ (self, typename, val):
        self.val = val
        impl_type = val.type.fields()[0].type.strip_typedefs().tag
        if is_specialization_of(impl_type, '__uniq_ptr_impl'): # New implementation
            self.pointer = val['_M_t']['_M_t']['_M_head_impl']
        elif is_specialization_of(impl_type, 'tuple'):
            self.pointer = val['_M_t']['_M_head_impl']
        else:
            raise ValueError("Unsupported implementation for unique_ptr: %s" % impl_type)

    def children (self):
        return SmartPtrIterator(self.pointer, self.val.type.template_argument(0))

    def to_string (self):
        return ('std::unique_ptr<%s>' % (str(self.val.type.template_argument(0))))


def patch_libstdcxx_printers_module():
    from libstdcxx.v6 import printers
    printers.StdListPrinter = StdListPrinter
    printers.SmartPtrIterator = SmartPtrIterator
    printers.SharedPointerPrinter = SharedPointerPrinter
    printers.UniquePointerPrinter = UniquePointerPrinter
    printers.build_libstdcxx_dictionary()
