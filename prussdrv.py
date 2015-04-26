'''Wrapper for prussdrv.h

Generated with:
/usr/local/bin/ctypesgen.py -o prussdrv.py /usr/include/prussdrv.h /usr/include/pruss_intc_mapping.h

Do not modify this file.
'''

__docformat__ =  'restructuredtext'

# Begin preamble

import ctypes, os, sys
from ctypes import *

_int_types = (c_int16, c_int32)
if hasattr(ctypes, 'c_int64'):
    # Some builds of ctypes apparently do not have c_int64
    # defined; it's a pretty good bet that these builds do not
    # have 64-bit pointers.
    _int_types += (c_int64,)
for t in _int_types:
    if sizeof(t) == sizeof(c_size_t):
        c_ptrdiff_t = t
del t
del _int_types

class c_void(Structure):
    # c_void_p is a buggy return type, converting to int, so
    # POINTER(None) == c_void_p is actually written as
    # POINTER(c_void), so it can be treated as a real pointer.
    _fields_ = [('dummy', c_int)]

def POINTER(obj):
    p = ctypes.POINTER(obj)

    # Convert None to a real NULL pointer to work around bugs
    # in how ctypes handles None on 64-bit platforms
    if not isinstance(p.from_param, classmethod):
        def from_param(cls, x):
            if x is None:
                return cls()
            else:
                return x
        p.from_param = classmethod(from_param)

    return p

class UserString:
    def __init__(self, seq):
        if isinstance(seq, basestring):
            self.data = seq
        elif isinstance(seq, UserString):
            self.data = seq.data[:]
        else:
            self.data = str(seq)
    def __str__(self): return str(self.data)
    def __repr__(self): return repr(self.data)
    def __int__(self): return int(self.data)
    def __long__(self): return long(self.data)
    def __float__(self): return float(self.data)
    def __complex__(self): return complex(self.data)
    def __hash__(self): return hash(self.data)

    def __cmp__(self, string):
        if isinstance(string, UserString):
            return cmp(self.data, string.data)
        else:
            return cmp(self.data, string)
    def __contains__(self, char):
        return char in self.data

    def __len__(self): return len(self.data)
    def __getitem__(self, index): return self.__class__(self.data[index])
    def __getslice__(self, start, end):
        start = max(start, 0); end = max(end, 0)
        return self.__class__(self.data[start:end])

    def __add__(self, other):
        if isinstance(other, UserString):
            return self.__class__(self.data + other.data)
        elif isinstance(other, basestring):
            return self.__class__(self.data + other)
        else:
            return self.__class__(self.data + str(other))
    def __radd__(self, other):
        if isinstance(other, basestring):
            return self.__class__(other + self.data)
        else:
            return self.__class__(str(other) + self.data)
    def __mul__(self, n):
        return self.__class__(self.data*n)
    __rmul__ = __mul__
    def __mod__(self, args):
        return self.__class__(self.data % args)

    # the following methods are defined in alphabetical order:
    def capitalize(self): return self.__class__(self.data.capitalize())
    def center(self, width, *args):
        return self.__class__(self.data.center(width, *args))
    def count(self, sub, start=0, end=sys.maxint):
        return self.data.count(sub, start, end)
    def decode(self, encoding=None, errors=None): # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.decode(encoding, errors))
            else:
                return self.__class__(self.data.decode(encoding))
        else:
            return self.__class__(self.data.decode())
    def encode(self, encoding=None, errors=None): # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.encode(encoding, errors))
            else:
                return self.__class__(self.data.encode(encoding))
        else:
            return self.__class__(self.data.encode())
    def endswith(self, suffix, start=0, end=sys.maxint):
        return self.data.endswith(suffix, start, end)
    def expandtabs(self, tabsize=8):
        return self.__class__(self.data.expandtabs(tabsize))
    def find(self, sub, start=0, end=sys.maxint):
        return self.data.find(sub, start, end)
    def index(self, sub, start=0, end=sys.maxint):
        return self.data.index(sub, start, end)
    def isalpha(self): return self.data.isalpha()
    def isalnum(self): return self.data.isalnum()
    def isdecimal(self): return self.data.isdecimal()
    def isdigit(self): return self.data.isdigit()
    def islower(self): return self.data.islower()
    def isnumeric(self): return self.data.isnumeric()
    def isspace(self): return self.data.isspace()
    def istitle(self): return self.data.istitle()
    def isupper(self): return self.data.isupper()
    def join(self, seq): return self.data.join(seq)
    def ljust(self, width, *args):
        return self.__class__(self.data.ljust(width, *args))
    def lower(self): return self.__class__(self.data.lower())
    def lstrip(self, chars=None): return self.__class__(self.data.lstrip(chars))
    def partition(self, sep):
        return self.data.partition(sep)
    def replace(self, old, new, maxsplit=-1):
        return self.__class__(self.data.replace(old, new, maxsplit))
    def rfind(self, sub, start=0, end=sys.maxint):
        return self.data.rfind(sub, start, end)
    def rindex(self, sub, start=0, end=sys.maxint):
        return self.data.rindex(sub, start, end)
    def rjust(self, width, *args):
        return self.__class__(self.data.rjust(width, *args))
    def rpartition(self, sep):
        return self.data.rpartition(sep)
    def rstrip(self, chars=None): return self.__class__(self.data.rstrip(chars))
    def split(self, sep=None, maxsplit=-1):
        return self.data.split(sep, maxsplit)
    def rsplit(self, sep=None, maxsplit=-1):
        return self.data.rsplit(sep, maxsplit)
    def splitlines(self, keepends=0): return self.data.splitlines(keepends)
    def startswith(self, prefix, start=0, end=sys.maxint):
        return self.data.startswith(prefix, start, end)
    def strip(self, chars=None): return self.__class__(self.data.strip(chars))
    def swapcase(self): return self.__class__(self.data.swapcase())
    def title(self): return self.__class__(self.data.title())
    def translate(self, *args):
        return self.__class__(self.data.translate(*args))
    def upper(self): return self.__class__(self.data.upper())
    def zfill(self, width): return self.__class__(self.data.zfill(width))

class MutableString(UserString):
    """mutable string objects

    Python strings are immutable objects.  This has the advantage, that
    strings may be used as dictionary keys.  If this property isn't needed
    and you insist on changing string values in place instead, you may cheat
    and use MutableString.

    But the purpose of this class is an educational one: to prevent
    people from inventing their own mutable string class derived
    from UserString and than forget thereby to remove (override) the
    __hash__ method inherited from UserString.  This would lead to
    errors that would be very hard to track down.

    A faster and better solution is to rewrite your program using lists."""
    def __init__(self, string=""):
        self.data = string
    def __hash__(self):
        raise TypeError("unhashable type (it is mutable)")
    def __setitem__(self, index, sub):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data): raise IndexError
        self.data = self.data[:index] + sub + self.data[index+1:]
    def __delitem__(self, index):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data): raise IndexError
        self.data = self.data[:index] + self.data[index+1:]
    def __setslice__(self, start, end, sub):
        start = max(start, 0); end = max(end, 0)
        if isinstance(sub, UserString):
            self.data = self.data[:start]+sub.data+self.data[end:]
        elif isinstance(sub, basestring):
            self.data = self.data[:start]+sub+self.data[end:]
        else:
            self.data =  self.data[:start]+str(sub)+self.data[end:]
    def __delslice__(self, start, end):
        start = max(start, 0); end = max(end, 0)
        self.data = self.data[:start] + self.data[end:]
    def immutable(self):
        return UserString(self.data)
    def __iadd__(self, other):
        if isinstance(other, UserString):
            self.data += other.data
        elif isinstance(other, basestring):
            self.data += other
        else:
            self.data += str(other)
        return self
    def __imul__(self, n):
        self.data *= n
        return self

class String(MutableString, Union):

    _fields_ = [('raw', POINTER(c_char)),
                ('data', c_char_p)]

    def __init__(self, obj=""):
        if isinstance(obj, (str, unicode, UserString)):
            self.data = str(obj)
        else:
            self.raw = obj

    def __len__(self):
        return self.data and len(self.data) or 0

    def from_param(cls, obj):
        # Convert None or 0
        if obj is None or obj == 0:
            return cls(POINTER(c_char)())

        # Convert from String
        elif isinstance(obj, String):
            return obj

        # Convert from str
        elif isinstance(obj, str):
            return cls(obj)

        # Convert from c_char_p
        elif isinstance(obj, c_char_p):
            return obj

        # Convert from POINTER(c_char)
        elif isinstance(obj, POINTER(c_char)):
            return obj

        # Convert from raw pointer
        elif isinstance(obj, int):
            return cls(cast(obj, POINTER(c_char)))

        # Convert from object
        else:
            return String.from_param(obj._as_parameter_)
    from_param = classmethod(from_param)

def ReturnString(obj, func=None, arguments=None):
    return String.from_param(obj)

# As of ctypes 1.0, ctypes does not support custom error-checking
# functions on callbacks, nor does it support custom datatypes on
# callbacks, so we must ensure that all callbacks return
# primitive datatypes.
#
# Non-primitive return values wrapped with UNCHECKED won't be
# typechecked, and will be converted to c_void_p.
def UNCHECKED(type):
    if (hasattr(type, "_type_") and isinstance(type._type_, str)
        and type._type_ != "P"):
        return type
    else:
        return c_void_p

# ctypes doesn't have direct support for variadic functions, so we have to write
# our own wrapper class
class _variadic_function(object):
    def __init__(self,func,restype,argtypes):
        self.func=func
        self.func.restype=restype
        self.argtypes=argtypes
    def _as_parameter_(self):
        # So we can pass this variadic function as a function pointer
        return self.func
    def __call__(self,*args):
        fixed_args=[]
        i=0
        for argtype in self.argtypes:
            # Typecheck what we can
            fixed_args.append(argtype.from_param(args[i]))
            i+=1
        return self.func(*fixed_args+list(args[i:]))

# End preamble

_libs = {}
_libdirs = []

# Begin loader

# ----------------------------------------------------------------------------
# Copyright (c) 2008 David James
# Copyright (c) 2006-2008 Alex Holkner
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in
#    the documentation and/or other materials provided with the
#    distribution.
#  * Neither the name of pyglet nor the names of its
#    contributors may be used to endorse or promote products
#    derived from this software without specific prior written
#    permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
# ----------------------------------------------------------------------------

import os.path, re, sys, glob
import ctypes
import ctypes.util

def _environ_path(name):
    if name in os.environ:
        return os.environ[name].split(":")
    else:
        return []

class LibraryLoader(object):
    def __init__(self):
        self.other_dirs=[]

    def load_library(self,libname):
        """Given the name of a library, load it."""
        paths = self.getpaths(libname)

        for path in paths:
            if os.path.exists(path):
                return self.load(path)

        raise ImportError("%s not found." % libname)

    def load(self,path):
        """Given a path to a library, load it."""
        try:
            # Darwin requires dlopen to be called with mode RTLD_GLOBAL instead
            # of the default RTLD_LOCAL.  Without this, you end up with
            # libraries not being loadable, resulting in "Symbol not found"
            # errors
            if sys.platform == 'darwin':
                return ctypes.CDLL(path, ctypes.RTLD_GLOBAL)
            else:
                return ctypes.cdll.LoadLibrary(path)
        except OSError,e:
            raise ImportError(e)

    def getpaths(self,libname):
        """Return a list of paths where the library might be found."""
        if os.path.isabs(libname):
            yield libname

        else:
            for path in self.getplatformpaths(libname):
                yield path

            path = ctypes.util.find_library(libname)
            if path: yield path

    def getplatformpaths(self, libname):
        return []

# Darwin (Mac OS X)

class DarwinLibraryLoader(LibraryLoader):
    name_formats = ["lib%s.dylib", "lib%s.so", "lib%s.bundle", "%s.dylib",
                "%s.so", "%s.bundle", "%s"]

    def getplatformpaths(self,libname):
        if os.path.pathsep in libname:
            names = [libname]
        else:
            names = [format % libname for format in self.name_formats]

        for dir in self.getdirs(libname):
            for name in names:
                yield os.path.join(dir,name)

    def getdirs(self,libname):
        '''Implements the dylib search as specified in Apple documentation:

        http://developer.apple.com/documentation/DeveloperTools/Conceptual/
            DynamicLibraries/Articles/DynamicLibraryUsageGuidelines.html

        Before commencing the standard search, the method first checks
        the bundle's ``Frameworks`` directory if the application is running
        within a bundle (OS X .app).
        '''

        dyld_fallback_library_path = _environ_path("DYLD_FALLBACK_LIBRARY_PATH")
        if not dyld_fallback_library_path:
            dyld_fallback_library_path = [os.path.expanduser('~/lib'),
                                          '/usr/local/lib', '/usr/lib']

        dirs = []

        if '/' in libname:
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))
        else:
            dirs.extend(_environ_path("LD_LIBRARY_PATH"))
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))

        dirs.extend(self.other_dirs)
        dirs.append(".")

        if hasattr(sys, 'frozen') and sys.frozen == 'macosx_app':
            dirs.append(os.path.join(
                os.environ['RESOURCEPATH'],
                '..',
                'Frameworks'))

        dirs.extend(dyld_fallback_library_path)

        return dirs

# Posix

class PosixLibraryLoader(LibraryLoader):
    _ld_so_cache = None

    def _create_ld_so_cache(self):
        # Recreate search path followed by ld.so.  This is going to be
        # slow to build, and incorrect (ld.so uses ld.so.cache, which may
        # not be up-to-date).  Used only as fallback for distros without
        # /sbin/ldconfig.
        #
        # We assume the DT_RPATH and DT_RUNPATH binary sections are omitted.

        directories = []
        for name in ("LD_LIBRARY_PATH",
                     "SHLIB_PATH", # HPUX
                     "LIBPATH", # OS/2, AIX
                     "LIBRARY_PATH", # BE/OS
                    ):
            if name in os.environ:
                directories.extend(os.environ[name].split(os.pathsep))
        directories.extend(self.other_dirs)
        directories.append(".")

        try: directories.extend([dir.strip() for dir in open('/etc/ld.so.conf')])
        except IOError: pass

        directories.extend(['/lib', '/usr/lib', '/lib64', '/usr/lib64'])

        cache = {}
        lib_re = re.compile(r'lib(.*)\.s[ol]')
        ext_re = re.compile(r'\.s[ol]$')
        for dir in directories:
            try:
                for path in glob.glob("%s/*.s[ol]*" % dir):
                    file = os.path.basename(path)

                    # Index by filename
                    if file not in cache:
                        cache[file] = path

                    # Index by library name
                    match = lib_re.match(file)
                    if match:
                        library = match.group(1)
                        if library not in cache:
                            cache[library] = path
            except OSError:
                pass

        self._ld_so_cache = cache

    def getplatformpaths(self, libname):
        if self._ld_so_cache is None:
            self._create_ld_so_cache()

        result = self._ld_so_cache.get(libname)
        if result: yield result

        path = ctypes.util.find_library(libname)
        if path: yield os.path.join("/lib",path)

# Windows

class _WindowsLibrary(object):
    def __init__(self, path):
        self.cdll = ctypes.cdll.LoadLibrary(path)
        self.windll = ctypes.windll.LoadLibrary(path)

    def __getattr__(self, name):
        try: return getattr(self.cdll,name)
        except AttributeError:
            try: return getattr(self.windll,name)
            except AttributeError:
                raise

class WindowsLibraryLoader(LibraryLoader):
    name_formats = ["%s.dll", "lib%s.dll", "%slib.dll"]

    def load_library(self, libname):
        try:
            result = LibraryLoader.load_library(self, libname)
        except ImportError:
            result = None
            if os.path.sep not in libname:
                for name in self.name_formats:
                    try:
                        result = getattr(ctypes.cdll, name % libname)
                        if result:
                            break
                    except WindowsError:
                        result = None
            if result is None:
                try:
                    result = getattr(ctypes.cdll, libname)
                except WindowsError:
                    result = None
            if result is None:
                raise ImportError("%s not found." % libname)
        return result

    def load(self, path):
        return _WindowsLibrary(path)

    def getplatformpaths(self, libname):
        if os.path.sep not in libname:
            for name in self.name_formats:
                dll_in_current_dir = os.path.abspath(name % libname)
                if os.path.exists(dll_in_current_dir):
                    yield dll_in_current_dir
                path = ctypes.util.find_library(name % libname)
                if path:
                    yield path

# Platform switching

# If your value of sys.platform does not appear in this dict, please contact
# the Ctypesgen maintainers.

loaderclass = {
    "darwin":   DarwinLibraryLoader,
    "cygwin":   WindowsLibraryLoader,
    "win32":    WindowsLibraryLoader
}

loader = loaderclass.get(sys.platform, PosixLibraryLoader)()

def add_library_search_dirs(other_dirs):
    loader.other_dirs = other_dirs

load_library = loader.load_library

del loaderclass

# End loader

add_library_search_dirs([])

# No libraries

# No modules

# /usr/include/prussdrv.h: 92
class struct___sysevt_to_channel_map(Structure):
    pass

struct___sysevt_to_channel_map.__slots__ = [
    'sysevt',
    'channel',
]
struct___sysevt_to_channel_map._fields_ = [
    ('sysevt', c_short),
    ('channel', c_short),
]

tsysevt_to_channel_map = struct___sysevt_to_channel_map # /usr/include/prussdrv.h: 92

# /usr/include/prussdrv.h: 96
class struct___channel_to_host_map(Structure):
    pass

struct___channel_to_host_map.__slots__ = [
    'channel',
    'host',
]
struct___channel_to_host_map._fields_ = [
    ('channel', c_short),
    ('host', c_short),
]

tchannel_to_host_map = struct___channel_to_host_map # /usr/include/prussdrv.h: 96

# /usr/include/prussdrv.h: 109
class struct___pruss_intc_initdata(Structure):
    pass

struct___pruss_intc_initdata.__slots__ = [
    'sysevts_enabled',
    'sysevt_to_channel_map',
    'channel_to_host_map',
    'host_enable_bitmask',
]
struct___pruss_intc_initdata._fields_ = [
    ('sysevts_enabled', c_char * 64),
    ('sysevt_to_channel_map', tsysevt_to_channel_map * 64),
    ('channel_to_host_map', tchannel_to_host_map * 10),
    ('host_enable_bitmask', c_uint),
]

tpruss_intc_initdata = struct___pruss_intc_initdata # /usr/include/prussdrv.h: 109

# /usr/include/prussdrv.h: 111
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'prussdrv_init'):
        continue
    prussdrv_init = _lib.prussdrv_init
    prussdrv_init.argtypes = []
    prussdrv_init.restype = c_int
    break

# /usr/include/prussdrv.h: 113
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'prussdrv_open'):
        continue
    prussdrv_open = _lib.prussdrv_open
    prussdrv_open.argtypes = [c_uint]
    prussdrv_open.restype = c_int
    break

# /usr/include/prussdrv.h: 116
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'prussdrv_version'):
        continue
    prussdrv_version = _lib.prussdrv_version
    prussdrv_version.argtypes = []
    prussdrv_version.restype = c_int
    break

# /usr/include/prussdrv.h: 119
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'prussdrv_strversion'):
        continue
    prussdrv_strversion = _lib.prussdrv_strversion
    prussdrv_strversion.argtypes = [c_int]
    if sizeof(c_int) == sizeof(c_void_p):
        prussdrv_strversion.restype = ReturnString
    else:
        prussdrv_strversion.restype = String
        prussdrv_strversion.errcheck = ReturnString
    break

# /usr/include/prussdrv.h: 121
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'prussdrv_pru_reset'):
        continue
    prussdrv_pru_reset = _lib.prussdrv_pru_reset
    prussdrv_pru_reset.argtypes = [c_uint]
    prussdrv_pru_reset.restype = c_int
    break

# /usr/include/prussdrv.h: 123
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'prussdrv_pru_disable'):
        continue
    prussdrv_pru_disable = _lib.prussdrv_pru_disable
    prussdrv_pru_disable.argtypes = [c_uint]
    prussdrv_pru_disable.restype = c_int
    break

# /usr/include/prussdrv.h: 125
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'prussdrv_pru_enable'):
        continue
    prussdrv_pru_enable = _lib.prussdrv_pru_enable
    prussdrv_pru_enable.argtypes = [c_uint]
    prussdrv_pru_enable.restype = c_int
    break

# /usr/include/prussdrv.h: 126
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'prussdrv_pru_enable_at'):
        continue
    prussdrv_pru_enable_at = _lib.prussdrv_pru_enable_at
    prussdrv_pru_enable_at.argtypes = [c_uint, c_size_t]
    prussdrv_pru_enable_at.restype = c_int
    break

# /usr/include/prussdrv.h: 128
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'prussdrv_pru_write_memory'):
        continue
    prussdrv_pru_write_memory = _lib.prussdrv_pru_write_memory
    prussdrv_pru_write_memory.argtypes = [c_uint, c_uint, POINTER(c_uint), c_uint]
    prussdrv_pru_write_memory.restype = c_int
    break

# /usr/include/prussdrv.h: 133
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'prussdrv_pruintc_init'):
        continue
    prussdrv_pruintc_init = _lib.prussdrv_pruintc_init
    prussdrv_pruintc_init.argtypes = [POINTER(tpruss_intc_initdata)]
    prussdrv_pruintc_init.restype = c_int
    break

# /usr/include/prussdrv.h: 142
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'prussdrv_get_event_to_channel_map'):
        continue
    prussdrv_get_event_to_channel_map = _lib.prussdrv_get_event_to_channel_map
    prussdrv_get_event_to_channel_map.argtypes = [c_uint]
    prussdrv_get_event_to_channel_map.restype = c_short
    break

# /usr/include/prussdrv.h: 151
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'prussdrv_get_channel_to_host_map'):
        continue
    prussdrv_get_channel_to_host_map = _lib.prussdrv_get_channel_to_host_map
    prussdrv_get_channel_to_host_map.argtypes = [c_uint]
    prussdrv_get_channel_to_host_map.restype = c_short
    break

# /usr/include/prussdrv.h: 158
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'prussdrv_get_event_to_host_map'):
        continue
    prussdrv_get_event_to_host_map = _lib.prussdrv_get_event_to_host_map
    prussdrv_get_event_to_host_map.argtypes = [c_uint]
    prussdrv_get_event_to_host_map.restype = c_short
    break

# /usr/include/prussdrv.h: 160
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'prussdrv_map_l3mem'):
        continue
    prussdrv_map_l3mem = _lib.prussdrv_map_l3mem
    prussdrv_map_l3mem.argtypes = [POINTER(POINTER(None))]
    prussdrv_map_l3mem.restype = c_int
    break

# /usr/include/prussdrv.h: 162
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'prussdrv_map_extmem'):
        continue
    prussdrv_map_extmem = _lib.prussdrv_map_extmem
    prussdrv_map_extmem.argtypes = [POINTER(POINTER(None))]
    prussdrv_map_extmem.restype = c_int
    break

# /usr/include/prussdrv.h: 164
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'prussdrv_extmem_size'):
        continue
    prussdrv_extmem_size = _lib.prussdrv_extmem_size
    prussdrv_extmem_size.argtypes = []
    prussdrv_extmem_size.restype = c_uint
    break

# /usr/include/prussdrv.h: 166
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'prussdrv_map_prumem'):
        continue
    prussdrv_map_prumem = _lib.prussdrv_map_prumem
    prussdrv_map_prumem.argtypes = [c_uint, POINTER(POINTER(None))]
    prussdrv_map_prumem.restype = c_int
    break

# /usr/include/prussdrv.h: 168
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'prussdrv_map_peripheral_io'):
        continue
    prussdrv_map_peripheral_io = _lib.prussdrv_map_peripheral_io
    prussdrv_map_peripheral_io.argtypes = [c_uint, POINTER(POINTER(None))]
    prussdrv_map_peripheral_io.restype = c_int
    break

# /usr/include/prussdrv.h: 170
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'prussdrv_get_phys_addr'):
        continue
    prussdrv_get_phys_addr = _lib.prussdrv_get_phys_addr
    prussdrv_get_phys_addr.argtypes = [POINTER(None)]
    prussdrv_get_phys_addr.restype = c_uint
    break

# /usr/include/prussdrv.h: 172
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'prussdrv_get_virt_addr'):
        continue
    prussdrv_get_virt_addr = _lib.prussdrv_get_virt_addr
    prussdrv_get_virt_addr.argtypes = [c_uint]
    prussdrv_get_virt_addr.restype = POINTER(None)
    break

# /usr/include/prussdrv.h: 176
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'prussdrv_pru_wait_event'):
        continue
    prussdrv_pru_wait_event = _lib.prussdrv_pru_wait_event
    prussdrv_pru_wait_event.argtypes = [c_uint]
    prussdrv_pru_wait_event.restype = c_uint
    break

# /usr/include/prussdrv.h: 178
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'prussdrv_pru_event_fd'):
        continue
    prussdrv_pru_event_fd = _lib.prussdrv_pru_event_fd
    prussdrv_pru_event_fd.argtypes = [c_uint]
    prussdrv_pru_event_fd.restype = c_int
    break

# /usr/include/prussdrv.h: 180
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'prussdrv_pru_send_event'):
        continue
    prussdrv_pru_send_event = _lib.prussdrv_pru_send_event
    prussdrv_pru_send_event.argtypes = [c_uint]
    prussdrv_pru_send_event.restype = c_int
    break

# /usr/include/prussdrv.h: 183
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'prussdrv_pru_clear_event'):
        continue
    prussdrv_pru_clear_event = _lib.prussdrv_pru_clear_event
    prussdrv_pru_clear_event.argtypes = [c_uint, c_uint]
    prussdrv_pru_clear_event.restype = c_int
    break

# /usr/include/prussdrv.h: 186
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'prussdrv_pru_send_wait_clear_event'):
        continue
    prussdrv_pru_send_wait_clear_event = _lib.prussdrv_pru_send_wait_clear_event
    prussdrv_pru_send_wait_clear_event.argtypes = [c_uint, c_uint, c_uint]
    prussdrv_pru_send_wait_clear_event.restype = c_int
    break

# /usr/include/prussdrv.h: 190
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'prussdrv_exit'):
        continue
    prussdrv_exit = _lib.prussdrv_exit
    prussdrv_exit.argtypes = []
    prussdrv_exit.restype = c_int
    break

# /usr/include/prussdrv.h: 192
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'prussdrv_exec_program'):
        continue
    prussdrv_exec_program = _lib.prussdrv_exec_program
    prussdrv_exec_program.argtypes = [c_int, String]
    prussdrv_exec_program.restype = c_int
    break

# /usr/include/prussdrv.h: 193
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'prussdrv_exec_program_at'):
        continue
    prussdrv_exec_program_at = _lib.prussdrv_exec_program_at
    prussdrv_exec_program_at.argtypes = [c_int, String, c_size_t]
    prussdrv_exec_program_at.restype = c_int
    break

# /usr/include/prussdrv.h: 195
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'prussdrv_exec_code'):
        continue
    prussdrv_exec_code = _lib.prussdrv_exec_code
    prussdrv_exec_code.argtypes = [c_int, POINTER(c_uint), c_int]
    prussdrv_exec_code.restype = c_int
    break

# /usr/include/prussdrv.h: 196
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'prussdrv_exec_code_at'):
        continue
    prussdrv_exec_code_at = _lib.prussdrv_exec_code_at
    prussdrv_exec_code_at.argtypes = [c_int, POINTER(c_uint), c_int, c_size_t]
    prussdrv_exec_code_at.restype = c_int
    break

# /usr/include/prussdrv.h: 197
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'prussdrv_load_data'):
        continue
    prussdrv_load_data = _lib.prussdrv_load_data
    prussdrv_load_data.argtypes = [c_int, POINTER(c_uint), c_int]
    prussdrv_load_data.restype = c_int
    break

# /usr/include/prussdrv.h: 198
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'prussdrv_load_datafile'):
        continue
    prussdrv_load_datafile = _lib.prussdrv_load_datafile
    prussdrv_load_datafile.argtypes = [c_int, String]
    prussdrv_load_datafile.restype = c_int
    break

# /usr/include/prussdrv.h: 57
try:
    NUM_PRU_HOSTIRQS = 8
except:
    pass

# /usr/include/prussdrv.h: 58
try:
    NUM_PRU_HOSTS = 10
except:
    pass

# /usr/include/prussdrv.h: 59
try:
    NUM_PRU_CHANNELS = 10
except:
    pass

# /usr/include/prussdrv.h: 60
try:
    NUM_PRU_SYS_EVTS = 64
except:
    pass

# /usr/include/prussdrv.h: 62
try:
    PRUSS0_PRU0_DATARAM = 0
except:
    pass

# /usr/include/prussdrv.h: 63
try:
    PRUSS0_PRU1_DATARAM = 1
except:
    pass

# /usr/include/prussdrv.h: 64
try:
    PRUSS0_PRU0_IRAM = 2
except:
    pass

# /usr/include/prussdrv.h: 65
try:
    PRUSS0_PRU1_IRAM = 3
except:
    pass

# /usr/include/prussdrv.h: 67
try:
    PRUSS_V1 = 1
except:
    pass

# /usr/include/prussdrv.h: 68
try:
    PRUSS_V2 = 2
except:
    pass

# /usr/include/prussdrv.h: 71
try:
    PRUSS0_SHARED_DATARAM = 4
except:
    pass

# /usr/include/prussdrv.h: 72
try:
    PRUSS0_CFG = 5
except:
    pass

# /usr/include/prussdrv.h: 73
try:
    PRUSS0_UART = 6
except:
    pass

# /usr/include/prussdrv.h: 74
try:
    PRUSS0_IEP = 7
except:
    pass

# /usr/include/prussdrv.h: 75
try:
    PRUSS0_ECAP = 8
except:
    pass

# /usr/include/prussdrv.h: 76
try:
    PRUSS0_MII_RT = 9
except:
    pass

# /usr/include/prussdrv.h: 77
try:
    PRUSS0_MDIO = 10
except:
    pass

# /usr/include/prussdrv.h: 80
try:
    PRU_EVTOUT_0 = 0
except:
    pass

# /usr/include/prussdrv.h: 81
try:
    PRU_EVTOUT_1 = 1
except:
    pass

# /usr/include/prussdrv.h: 82
try:
    PRU_EVTOUT_2 = 2
except:
    pass

# /usr/include/prussdrv.h: 83
try:
    PRU_EVTOUT_3 = 3
except:
    pass

# /usr/include/prussdrv.h: 84
try:
    PRU_EVTOUT_4 = 4
except:
    pass

# /usr/include/prussdrv.h: 85
try:
    PRU_EVTOUT_5 = 5
except:
    pass

# /usr/include/prussdrv.h: 86
try:
    PRU_EVTOUT_6 = 6
except:
    pass

# /usr/include/prussdrv.h: 87
try:
    PRU_EVTOUT_7 = 7
except:
    pass

# /usr/include/pruss_intc_mapping.h: 50
try:
    PRU0_PRU1_INTERRUPT = 17
except:
    pass

# /usr/include/pruss_intc_mapping.h: 51
try:
    PRU1_PRU0_INTERRUPT = 18
except:
    pass

# /usr/include/pruss_intc_mapping.h: 52
try:
    PRU0_ARM_INTERRUPT = 19
except:
    pass

# /usr/include/pruss_intc_mapping.h: 53
try:
    PRU1_ARM_INTERRUPT = 20
except:
    pass

# /usr/include/pruss_intc_mapping.h: 54
try:
    ARM_PRU0_INTERRUPT = 21
except:
    pass

# /usr/include/pruss_intc_mapping.h: 55
try:
    ARM_PRU1_INTERRUPT = 22
except:
    pass

# /usr/include/pruss_intc_mapping.h: 64
try:
    CHANNEL0 = 0
except:
    pass

# /usr/include/pruss_intc_mapping.h: 65
try:
    CHANNEL1 = 1
except:
    pass

# /usr/include/pruss_intc_mapping.h: 66
try:
    CHANNEL2 = 2
except:
    pass

# /usr/include/pruss_intc_mapping.h: 67
try:
    CHANNEL3 = 3
except:
    pass

# /usr/include/pruss_intc_mapping.h: 68
try:
    CHANNEL4 = 4
except:
    pass

# /usr/include/pruss_intc_mapping.h: 69
try:
    CHANNEL5 = 5
except:
    pass

# /usr/include/pruss_intc_mapping.h: 70
try:
    CHANNEL6 = 6
except:
    pass

# /usr/include/pruss_intc_mapping.h: 71
try:
    CHANNEL7 = 7
except:
    pass

# /usr/include/pruss_intc_mapping.h: 72
try:
    CHANNEL8 = 8
except:
    pass

# /usr/include/pruss_intc_mapping.h: 73
try:
    CHANNEL9 = 9
except:
    pass

# /usr/include/pruss_intc_mapping.h: 75
try:
    PRU0 = 0
except:
    pass

# /usr/include/pruss_intc_mapping.h: 76
try:
    PRU1 = 1
except:
    pass

# /usr/include/pruss_intc_mapping.h: 77
try:
    PRU_EVTOUT0 = 2
except:
    pass

# /usr/include/pruss_intc_mapping.h: 78
try:
    PRU_EVTOUT1 = 3
except:
    pass

# /usr/include/pruss_intc_mapping.h: 79
try:
    PRU_EVTOUT2 = 4
except:
    pass

# /usr/include/pruss_intc_mapping.h: 80
try:
    PRU_EVTOUT3 = 5
except:
    pass

# /usr/include/pruss_intc_mapping.h: 81
try:
    PRU_EVTOUT4 = 6
except:
    pass

# /usr/include/pruss_intc_mapping.h: 82
try:
    PRU_EVTOUT5 = 7
except:
    pass

# /usr/include/pruss_intc_mapping.h: 83
try:
    PRU_EVTOUT6 = 8
except:
    pass

# /usr/include/pruss_intc_mapping.h: 84
try:
    PRU_EVTOUT7 = 9
except:
    pass

# /usr/include/pruss_intc_mapping.h: 86
try:
    PRU0_HOSTEN_MASK = 1
except:
    pass

# /usr/include/pruss_intc_mapping.h: 87
try:
    PRU1_HOSTEN_MASK = 2
except:
    pass

# /usr/include/pruss_intc_mapping.h: 88
try:
    PRU_EVTOUT0_HOSTEN_MASK = 4
except:
    pass

# /usr/include/pruss_intc_mapping.h: 89
try:
    PRU_EVTOUT1_HOSTEN_MASK = 8
except:
    pass

# /usr/include/pruss_intc_mapping.h: 90
try:
    PRU_EVTOUT2_HOSTEN_MASK = 16
except:
    pass

# /usr/include/pruss_intc_mapping.h: 91
try:
    PRU_EVTOUT3_HOSTEN_MASK = 32
except:
    pass

# /usr/include/pruss_intc_mapping.h: 92
try:
    PRU_EVTOUT4_HOSTEN_MASK = 64
except:
    pass

# /usr/include/pruss_intc_mapping.h: 93
try:
    PRU_EVTOUT5_HOSTEN_MASK = 128
except:
    pass

# /usr/include/pruss_intc_mapping.h: 94
try:
    PRU_EVTOUT6_HOSTEN_MASK = 256
except:
    pass

# /usr/include/pruss_intc_mapping.h: 95
try:
    PRU_EVTOUT7_HOSTEN_MASK = 512
except:
    pass

__sysevt_to_channel_map = struct___sysevt_to_channel_map # /usr/include/prussdrv.h: 92

__channel_to_host_map = struct___channel_to_host_map # /usr/include/prussdrv.h: 96

__pruss_intc_initdata = struct___pruss_intc_initdata # /usr/include/prussdrv.h: 109

# No inserted files

