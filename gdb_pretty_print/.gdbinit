python
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, "/home/debugger/gdb_renderer")
from default.printers import register_default_printers
register_default_printers(None)
from default.libstdcxx_printers import patch_libstdcxx_printers_module
patch_libstdcxx_printers_module()
from libstdcxx.v6.printers import register_libstdcxx_printers
register_libstdcxx_printers(None);
