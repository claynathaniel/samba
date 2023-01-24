from waflib import Build
import jinja2
from samba_utils import SUBDIR
def RUST_BINDINGS(bld, public_headers):
    bld.SET_BUILD_GROUP("rust-bindings")
