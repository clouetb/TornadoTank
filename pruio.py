'''Wrapper for pruio.h

Generated with:
/usr/local/bin/ctypesgen.py -o pruio.py --insert-file=pruio_include.py ../c_wrapper/pruio.h ../c_wrapper/pruio_pins.h ../c_wrapper/pruio.hp -l libpruio.so -L ../c_wrapper/

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
_libdirs = ['../c_wrapper/']

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

add_library_search_dirs(['../c_wrapper/'])

# Begin libraries

_libs["libpruio.so"] = load_library("libpruio.so")

# 1 libraries
# End libraries

# No modules

int8 = c_char # /root/libpruio-0.2/src/c_wrapper/pruio.h: 34

int16 = c_short # /root/libpruio-0.2/src/c_wrapper/pruio.h: 35

int32 = c_int # /root/libpruio-0.2/src/c_wrapper/pruio.h: 36

uint8 = c_ubyte # /root/libpruio-0.2/src/c_wrapper/pruio.h: 37

uint16 = c_ushort # /root/libpruio-0.2/src/c_wrapper/pruio.h: 38

uint32 = c_uint # /root/libpruio-0.2/src/c_wrapper/pruio.h: 39

float_t = c_float # /root/libpruio-0.2/src/c_wrapper/pruio.h: 40

# /root/libpruio-0.2/src/c_wrapper/pruio.h: 46
class struct_pruIo(Structure):
    pass

pruIo = struct_pruIo # /root/libpruio-0.2/src/c_wrapper/pruio.h: 46

# /root/libpruio-0.2/src/c_wrapper/pruio.h: 70
class struct_adcSteps(Structure):
    pass

struct_adcSteps.__slots__ = [
    'Confg',
    'Delay',
]
struct_adcSteps._fields_ = [
    ('Confg', uint32),
    ('Delay', uint32),
]

# /root/libpruio-0.2/src/c_wrapper/pruio.h: 114
class struct_adcSet(Structure):
    pass

struct_adcSet.__slots__ = [
    'DeAd',
    'ClAd',
    'ClVa',
    'REVISION',
    'SYSCONFIG',
    'IRQSTATUS_RAW',
    'IRQSTATUS',
    'IRQENABLE_SET',
    'IRQENABLE_CLR',
    'IRQWAKEUP',
    'DMAENABLE_SET',
    'DMAENABLE_CLR',
    'CTRL',
    'ADCSTAT',
    'ADCRANGE',
    'ADC_CLKDIV',
    'ADC_MISC',
    'STEPENABLE',
    'IDLECONFIG',
    'St_p',
    'FIFO0COUNT',
    'FIFO0THRESHOLD',
    'DMA0REQ',
    'FIFO1COUNT',
    'FIFO1THRESHOLD',
    'DMA1REQ',
]
struct_adcSet._fields_ = [
    ('DeAd', uint32),
    ('ClAd', uint32),
    ('ClVa', uint32),
    ('REVISION', uint32),
    ('SYSCONFIG', uint32),
    ('IRQSTATUS_RAW', uint32),
    ('IRQSTATUS', uint32),
    ('IRQENABLE_SET', uint32),
    ('IRQENABLE_CLR', uint32),
    ('IRQWAKEUP', uint32),
    ('DMAENABLE_SET', uint32),
    ('DMAENABLE_CLR', uint32),
    ('CTRL', uint32),
    ('ADCSTAT', uint32),
    ('ADCRANGE', uint32),
    ('ADC_CLKDIV', uint32),
    ('ADC_MISC', uint32),
    ('STEPENABLE', uint32),
    ('IDLECONFIG', uint32),
    ('St_p', struct_adcSteps * (16 + 1)),
    ('FIFO0COUNT', uint32),
    ('FIFO0THRESHOLD', uint32),
    ('DMA0REQ', uint32),
    ('FIFO1COUNT', uint32),
    ('FIFO1THRESHOLD', uint32),
    ('DMA1REQ', uint32),
]

adcSet = struct_adcSet # /root/libpruio-0.2/src/c_wrapper/pruio.h: 114

# /root/libpruio-0.2/src/c_wrapper/pruio.h: 134
class struct_adcUdt(Structure):
    pass

struct_adcUdt.__slots__ = [
    'Top',
    'Init',
    'Conf',
    'Samples',
    'TimerVal',
    'InitParA',
    'LslMode',
    'ChAz',
    'Value',
]
struct_adcUdt._fields_ = [
    ('Top', POINTER(pruIo)),
    ('Init', POINTER(adcSet)),
    ('Conf', POINTER(adcSet)),
    ('Samples', uint32),
    ('TimerVal', uint32),
    ('InitParA', uint32),
    ('LslMode', uint16),
    ('ChAz', uint16),
    ('Value', POINTER(uint16)),
]

adcUdt = struct_adcUdt # /root/libpruio-0.2/src/c_wrapper/pruio.h: 134

# /root/libpruio-0.2/src/c_wrapper/pruio.h: 174
class struct_gpioSet(Structure):
    pass

struct_gpioSet.__slots__ = [
    'DeAd',
    'ClAd',
    'ClVa',
    'REVISION',
    'SYSCONFIG',
    'EOI',
    'IRQSTATUS_RAW_0',
    'IRQSTATUS_RAW_1',
    'IRQSTATUS_0',
    'IRQSTATUS_1',
    'IRQSTATUS_SET_0',
    'IRQSTATUS_SET_1',
    'IRQSTATUS_CLR_0',
    'IRQSTATUS_CLR_1',
    'IRQWAKEN_0',
    'IRQWAKEN_1',
    'SYSSTATUS',
    'CTRL',
    'OE',
    'DATAIN',
    'DATAOUT',
    'LEVELDETECT0',
    'LEVELDETECT1',
    'RISINGDETECT',
    'FALLINGDETECT',
    'DEBOUNCENABLE',
    'DEBOUNCINGTIME',
    'CLEARDATAOUT',
    'SETDATAOUT',
]
struct_gpioSet._fields_ = [
    ('DeAd', uint32),
    ('ClAd', uint32),
    ('ClVa', uint32),
    ('REVISION', uint32),
    ('SYSCONFIG', uint32),
    ('EOI', uint32),
    ('IRQSTATUS_RAW_0', uint32),
    ('IRQSTATUS_RAW_1', uint32),
    ('IRQSTATUS_0', uint32),
    ('IRQSTATUS_1', uint32),
    ('IRQSTATUS_SET_0', uint32),
    ('IRQSTATUS_SET_1', uint32),
    ('IRQSTATUS_CLR_0', uint32),
    ('IRQSTATUS_CLR_1', uint32),
    ('IRQWAKEN_0', uint32),
    ('IRQWAKEN_1', uint32),
    ('SYSSTATUS', uint32),
    ('CTRL', uint32),
    ('OE', uint32),
    ('DATAIN', uint32),
    ('DATAOUT', uint32),
    ('LEVELDETECT0', uint32),
    ('LEVELDETECT1', uint32),
    ('RISINGDETECT', uint32),
    ('FALLINGDETECT', uint32),
    ('DEBOUNCENABLE', uint32),
    ('DEBOUNCINGTIME', uint32),
    ('CLEARDATAOUT', uint32),
    ('SETDATAOUT', uint32),
]

gpioSet = struct_gpioSet # /root/libpruio-0.2/src/c_wrapper/pruio.h: 174

# /root/libpruio-0.2/src/c_wrapper/pruio.h: 187
class struct_gpioArr(Structure):
    pass

struct_gpioArr.__slots__ = [
    'DeAd',
    'DATAIN',
    'DATAOUT',
    'Mix',
]
struct_gpioArr._fields_ = [
    ('DeAd', uint32),
    ('DATAIN', uint32),
    ('DATAOUT', uint32),
    ('Mix', uint32),
]

gpioArr = struct_gpioArr # /root/libpruio-0.2/src/c_wrapper/pruio.h: 187

# /root/libpruio-0.2/src/c_wrapper/pruio.h: 202
class struct_gpioUdt(Structure):
    pass

struct_gpioUdt.__slots__ = [
    'Top',
    'Init',
    'Conf',
    'Raw',
    'InitParA',
]
struct_gpioUdt._fields_ = [
    ('Top', POINTER(pruIo)),
    ('Init', POINTER(gpioSet) * (3 + 1)),
    ('Conf', POINTER(gpioSet) * (3 + 1)),
    ('Raw', POINTER(gpioArr) * (3 + 1)),
    ('InitParA', uint32),
]

gpioUdt = struct_gpioUdt # /root/libpruio-0.2/src/c_wrapper/pruio.h: 202

# /root/libpruio-0.2/src/c_wrapper/pruio.h: 309
class struct_pwmssSet(Structure):
    pass

struct_pwmssSet.__slots__ = [
    'DeAd',
    'ClAd',
    'ClVa',
    'IDVER',
    'SYSCONFIG',
    'CLKCONFIG',
    'CLKSTATUS',
    'TSCTR',
    'CTRPHS',
    'CAP1',
    'CAP2',
    'CAP3',
    'CAP4',
    'ECCTL1',
    'ECCTL2',
    'ECEINT',
    'ECFLG',
    'ECCLR',
    'ECFRC',
    'CAP_REV',
    'QPOSCNT',
    'QPOSINIT',
    'QPOSMAX',
    'QPOSCMP',
    'QPOSILAT',
    'QPOSSLAT',
    'QPOSLAT',
    'QUTMR',
    'QUPRD',
    'QWDTMR',
    'QWDPRD',
    'QDECCTL',
    'QEPCTL',
    'QCASCTL',
    'QPOSCTL',
    'QEINT',
    'QFLG',
    'QCLR',
    'QFRC',
    'QEPSTS',
    'QCTMR',
    'QCPRD',
    'QCTMRLAT',
    'QCPRDLAT',
    'empty',
    'QEP_REV',
    'TBCTL',
    'TBSTS',
    'TBPHSHR',
    'TBPHS',
    'TBCNT',
    'TBPRD',
    'CMPCTL',
    'CMPAHR',
    'CMPA',
    'CMPB',
    'AQCTLA',
    'AQCTLB',
    'AQSFRC',
    'AQCSFRC',
    'DBCTL',
    'DBRED',
    'DBFED',
    'TZSEL',
    'TZCTL',
    'TZEINT',
    'TZFLG',
    'TZCLR',
    'TZFRC',
    'ETSEL',
    'ETPS',
    'ETFLG',
    'ETCLR',
    'ETFRC',
    'PCCTL',
    'HRCTL',
]
struct_pwmssSet._fields_ = [
    ('DeAd', uint32),
    ('ClAd', uint32),
    ('ClVa', uint32),
    ('IDVER', uint32),
    ('SYSCONFIG', uint32),
    ('CLKCONFIG', uint32),
    ('CLKSTATUS', uint32),
    ('TSCTR', uint32),
    ('CTRPHS', uint32),
    ('CAP1', uint32),
    ('CAP2', uint32),
    ('CAP3', uint32),
    ('CAP4', uint32),
    ('ECCTL1', uint16),
    ('ECCTL2', uint16),
    ('ECEINT', uint16),
    ('ECFLG', uint16),
    ('ECCLR', uint16),
    ('ECFRC', uint16),
    ('CAP_REV', uint32),
    ('QPOSCNT', uint32),
    ('QPOSINIT', uint32),
    ('QPOSMAX', uint32),
    ('QPOSCMP', uint32),
    ('QPOSILAT', uint32),
    ('QPOSSLAT', uint32),
    ('QPOSLAT', uint32),
    ('QUTMR', uint32),
    ('QUPRD', uint32),
    ('QWDTMR', uint16),
    ('QWDPRD', uint16),
    ('QDECCTL', uint16),
    ('QEPCTL', uint16),
    ('QCASCTL', uint16),
    ('QPOSCTL', uint16),
    ('QEINT', uint16),
    ('QFLG', uint16),
    ('QCLR', uint16),
    ('QFRC', uint16),
    ('QEPSTS', uint16),
    ('QCTMR', uint16),
    ('QCPRD', uint16),
    ('QCTMRLAT', uint16),
    ('QCPRDLAT', uint16),
    ('empty', uint16),
    ('QEP_REV', uint32),
    ('TBCTL', uint16),
    ('TBSTS', uint16),
    ('TBPHSHR', uint16),
    ('TBPHS', uint16),
    ('TBCNT', uint16),
    ('TBPRD', uint16),
    ('CMPCTL', uint16),
    ('CMPAHR', uint16),
    ('CMPA', uint16),
    ('CMPB', uint16),
    ('AQCTLA', uint16),
    ('AQCTLB', uint16),
    ('AQSFRC', uint16),
    ('AQCSFRC', uint16),
    ('DBCTL', uint16),
    ('DBRED', uint16),
    ('DBFED', uint16),
    ('TZSEL', uint16),
    ('TZCTL', uint16),
    ('TZEINT', uint16),
    ('TZFLG', uint16),
    ('TZCLR', uint16),
    ('TZFRC', uint16),
    ('ETSEL', uint16),
    ('ETPS', uint16),
    ('ETFLG', uint16),
    ('ETCLR', uint16),
    ('ETFRC', uint16),
    ('PCCTL', uint16),
    ('HRCTL', uint16),
]

pwmssSet = struct_pwmssSet # /root/libpruio-0.2/src/c_wrapper/pruio.h: 309

# /root/libpruio-0.2/src/c_wrapper/pruio.h: 327
class struct_pwmssArr(Structure):
    pass

struct_pwmssArr.__slots__ = [
    'DeAd',
    'CMax',
    'C1',
    'C2',
    'fe1',
    'fe2',
    'fe3',
    'fe4',
]
struct_pwmssArr._fields_ = [
    ('DeAd', uint32),
    ('CMax', uint32),
    ('C1', uint32),
    ('C2', uint32),
    ('fe1', uint32),
    ('fe2', uint32),
    ('fe3', uint32),
    ('fe4', uint32),
]

pwmssArr = struct_pwmssArr # /root/libpruio-0.2/src/c_wrapper/pruio.h: 327

# /root/libpruio-0.2/src/c_wrapper/pruio.h: 344
class struct_pwmssUdt(Structure):
    pass

struct_pwmssUdt.__slots__ = [
    'Top',
    'Init',
    'Conf',
    'Raw',
    'InitParA',
    'CapMod',
]
struct_pwmssUdt._fields_ = [
    ('Top', POINTER(pruIo)),
    ('Init', POINTER(pwmssSet) * (2 + 1)),
    ('Conf', POINTER(pwmssSet) * (2 + 1)),
    ('Raw', POINTER(pwmssArr) * (2 + 1)),
    ('InitParA', uint32),
    ('CapMod', uint16),
]

pwmssUdt = struct_pwmssUdt # /root/libpruio-0.2/src/c_wrapper/pruio.h: 344

# /root/libpruio-0.2/src/c_wrapper/pruio.h: 351
class struct_pwmMod(Structure):
    pass

pwmMod = struct_pwmMod # /root/libpruio-0.2/src/c_wrapper/pruio.h: 351

# /root/libpruio-0.2/src/c_wrapper/pruio.h: 357
class struct_capMod(Structure):
    pass

capMod = struct_capMod # /root/libpruio-0.2/src/c_wrapper/pruio.h: 357

# /root/libpruio-0.2/src/c_wrapper/pruio.h: 363
class struct_qepMod(Structure):
    pass

qepMod = struct_qepMod # /root/libpruio-0.2/src/c_wrapper/pruio.h: 363

enum_activateDevice = c_int # /root/libpruio-0.2/src/c_wrapper/pruio.h: 375

PRUIO_ACT_PRU1 = 1 # /root/libpruio-0.2/src/c_wrapper/pruio.h: 375

PRUIO_ACT_ADC = (1 << 1) # /root/libpruio-0.2/src/c_wrapper/pruio.h: 375

PRUIO_ACT_GPIO0 = (1 << 2) # /root/libpruio-0.2/src/c_wrapper/pruio.h: 375

PRUIO_ACT_GPIO1 = (1 << 3) # /root/libpruio-0.2/src/c_wrapper/pruio.h: 375

PRUIO_ACT_GPIO2 = (1 << 4) # /root/libpruio-0.2/src/c_wrapper/pruio.h: 375

PRUIO_ACT_GPIO3 = (1 << 5) # /root/libpruio-0.2/src/c_wrapper/pruio.h: 375

PRUIO_ACT_PWM0 = (1 << 6) # /root/libpruio-0.2/src/c_wrapper/pruio.h: 375

PRUIO_ACT_PWM1 = (1 << 7) # /root/libpruio-0.2/src/c_wrapper/pruio.h: 375

PRUIO_ACT_PWM2 = (1 << 8) # /root/libpruio-0.2/src/c_wrapper/pruio.h: 375

PRUIO_DEF_ACTIVE = 65535 # /root/libpruio-0.2/src/c_wrapper/pruio.h: 375

enum_pinMuxing = c_int # /root/libpruio-0.2/src/c_wrapper/pruio.h: 388

PRUIO_PULL_DOWN = 0 # /root/libpruio-0.2/src/c_wrapper/pruio.h: 388

PRUIO_NO_PULL = (1 << 3) # /root/libpruio-0.2/src/c_wrapper/pruio.h: 388

PRUIO_PULL_UP = (1 << 4) # /root/libpruio-0.2/src/c_wrapper/pruio.h: 388

PRUIO_RX_ACTIV = (1 << 5) # /root/libpruio-0.2/src/c_wrapper/pruio.h: 388

PRUIO_GPIO_OUT0 = (7 + PRUIO_NO_PULL) # /root/libpruio-0.2/src/c_wrapper/pruio.h: 388

PRUIO_GPIO_OUT1 = ((7 + PRUIO_NO_PULL) + 128) # /root/libpruio-0.2/src/c_wrapper/pruio.h: 388

PRUIO_GPIO_IN = ((7 + PRUIO_NO_PULL) + PRUIO_RX_ACTIV) # /root/libpruio-0.2/src/c_wrapper/pruio.h: 388

PRUIO_GPIO_IN_0 = ((7 + PRUIO_PULL_DOWN) + PRUIO_RX_ACTIV) # /root/libpruio-0.2/src/c_wrapper/pruio.h: 388

PRUIO_GPIO_IN_1 = ((7 + PRUIO_PULL_UP) + PRUIO_RX_ACTIV) # /root/libpruio-0.2/src/c_wrapper/pruio.h: 388

PRUIO_PIN_RESET = 255 # /root/libpruio-0.2/src/c_wrapper/pruio.h: 388

# /root/libpruio-0.2/src/c_wrapper/pruio.h: 409
class struct_ballSet(Structure):
    pass

struct_ballSet.__slots__ = [
    'DeAd',
    'Value',
]
struct_ballSet._fields_ = [
    ('DeAd', uint32),
    ('Value', uint8 * (109 + 1)),
]

ballSet = struct_ballSet # /root/libpruio-0.2/src/c_wrapper/pruio.h: 409

# /root/libpruio-0.2/src/c_wrapper/pruio.h: 470
if hasattr(_libs['libpruio.so'], 'pruio_new'):
    pruio_new = _libs['libpruio.so'].pruio_new
    pruio_new.argtypes = [uint16, uint8, uint32, uint8]
    pruio_new.restype = POINTER(pruIo)

# /root/libpruio-0.2/src/c_wrapper/pruio.h: 477
if hasattr(_libs['libpruio.so'], 'pruio_destroy'):
    pruio_destroy = _libs['libpruio.so'].pruio_destroy
    pruio_destroy.argtypes = [POINTER(pruIo)]
    pruio_destroy.restype = None

# /root/libpruio-0.2/src/c_wrapper/pruio.h: 489
if hasattr(_libs['libpruio.so'], 'pruio_config'):
    pruio_config = _libs['libpruio.so'].pruio_config
    pruio_config.argtypes = [POINTER(pruIo), uint32, uint32, uint32, uint16]
    if sizeof(c_int) == sizeof(c_void_p):
        pruio_config.restype = ReturnString
    else:
        pruio_config.restype = String
        pruio_config.errcheck = ReturnString

# /root/libpruio-0.2/src/c_wrapper/pruio.h: 498
if hasattr(_libs['libpruio.so'], 'pruio_Pin'):
    pruio_Pin = _libs['libpruio.so'].pruio_Pin
    pruio_Pin.argtypes = [POINTER(pruIo), uint8]
    if sizeof(c_int) == sizeof(c_void_p):
        pruio_Pin.restype = ReturnString
    else:
        pruio_Pin.restype = String
        pruio_Pin.errcheck = ReturnString

# /root/libpruio-0.2/src/c_wrapper/pruio.h: 510
if hasattr(_libs['libpruio.so'], 'pruio_mm_start'):
    pruio_mm_start = _libs['libpruio.so'].pruio_mm_start
    pruio_mm_start.argtypes = [POINTER(pruIo), uint32, uint32, uint32, uint32]
    if sizeof(c_int) == sizeof(c_void_p):
        pruio_mm_start.restype = ReturnString
    else:
        pruio_mm_start.restype = String
        pruio_mm_start.errcheck = ReturnString

# /root/libpruio-0.2/src/c_wrapper/pruio.h: 518
if hasattr(_libs['libpruio.so'], 'pruio_rb_start'):
    pruio_rb_start = _libs['libpruio.so'].pruio_rb_start
    pruio_rb_start.argtypes = [POINTER(pruIo)]
    if sizeof(c_int) == sizeof(c_void_p):
        pruio_rb_start.restype = ReturnString
    else:
        pruio_rb_start.restype = String
        pruio_rb_start.errcheck = ReturnString

# /root/libpruio-0.2/src/c_wrapper/pruio.h: 529
if hasattr(_libs['libpruio.so'], 'pruio_gpio_config'):
    pruio_gpio_config = _libs['libpruio.so'].pruio_gpio_config
    pruio_gpio_config.argtypes = [POINTER(pruIo), uint8, uint8]
    if sizeof(c_int) == sizeof(c_void_p):
        pruio_gpio_config.restype = ReturnString
    else:
        pruio_gpio_config.restype = String
        pruio_gpio_config.errcheck = ReturnString

# /root/libpruio-0.2/src/c_wrapper/pruio.h: 540
if hasattr(_libs['libpruio.so'], 'pruio_gpio_setValue'):
    pruio_gpio_setValue = _libs['libpruio.so'].pruio_gpio_setValue
    pruio_gpio_setValue.argtypes = [POINTER(pruIo), uint8, uint8]
    if sizeof(c_int) == sizeof(c_void_p):
        pruio_gpio_setValue.restype = ReturnString
    else:
        pruio_gpio_setValue.restype = String
        pruio_gpio_setValue.errcheck = ReturnString

# /root/libpruio-0.2/src/c_wrapper/pruio.h: 549
if hasattr(_libs['libpruio.so'], 'pruio_gpio_Value'):
    pruio_gpio_Value = _libs['libpruio.so'].pruio_gpio_Value
    pruio_gpio_Value.argtypes = [POINTER(pruIo), uint8]
    pruio_gpio_Value.restype = uint32

# /root/libpruio-0.2/src/c_wrapper/pruio.h: 563
if hasattr(_libs['libpruio.so'], 'pruio_adc_setStep'):
    pruio_adc_setStep = _libs['libpruio.so'].pruio_adc_setStep
    pruio_adc_setStep.argtypes = [POINTER(pruIo), uint8, uint8, uint8, uint8, uint32]
    if sizeof(c_int) == sizeof(c_void_p):
        pruio_adc_setStep.restype = ReturnString
    else:
        pruio_adc_setStep.restype = String
        pruio_adc_setStep.errcheck = ReturnString

# /root/libpruio-0.2/src/c_wrapper/pruio.h: 574
if hasattr(_libs['libpruio.so'], 'pruio_adc_mm_trg_pin'):
    pruio_adc_mm_trg_pin = _libs['libpruio.so'].pruio_adc_mm_trg_pin
    pruio_adc_mm_trg_pin.argtypes = [POINTER(pruIo), uint8, uint8, uint16]
    pruio_adc_mm_trg_pin.restype = uint32

# /root/libpruio-0.2/src/c_wrapper/pruio.h: 587
if hasattr(_libs['libpruio.so'], 'pruio_adc_mm_trg_ain'):
    pruio_adc_mm_trg_ain = _libs['libpruio.so'].pruio_adc_mm_trg_ain
    pruio_adc_mm_trg_ain.argtypes = [POINTER(pruIo), uint8, int32, uint8, uint16]
    pruio_adc_mm_trg_ain.restype = uint32

# /root/libpruio-0.2/src/c_wrapper/pruio.h: 599
if hasattr(_libs['libpruio.so'], 'pruio_adc_mm_trg_pre'):
    pruio_adc_mm_trg_pre = _libs['libpruio.so'].pruio_adc_mm_trg_pre
    pruio_adc_mm_trg_pre.argtypes = [POINTER(pruIo), uint8, int32, uint16, uint8]
    pruio_adc_mm_trg_pre.restype = uint32

# /root/libpruio-0.2/src/c_wrapper/pruio.h: 610
if hasattr(_libs['libpruio.so'], 'pruio_cap_config'):
    pruio_cap_config = _libs['libpruio.so'].pruio_cap_config
    pruio_cap_config.argtypes = [POINTER(pruIo), uint8, float_t]
    if sizeof(c_int) == sizeof(c_void_p):
        pruio_cap_config.restype = ReturnString
    else:
        pruio_cap_config.restype = String
        pruio_cap_config.errcheck = ReturnString

# /root/libpruio-0.2/src/c_wrapper/pruio.h: 621
if hasattr(_libs['libpruio.so'], 'pruio_cap_Value'):
    pruio_cap_Value = _libs['libpruio.so'].pruio_cap_Value
    pruio_cap_Value.argtypes = [POINTER(pruIo), uint8, POINTER(float_t), POINTER(float_t)]
    if sizeof(c_int) == sizeof(c_void_p):
        pruio_cap_Value.restype = ReturnString
    else:
        pruio_cap_Value.restype = String
        pruio_cap_Value.errcheck = ReturnString

# /root/libpruio-0.2/src/c_wrapper/pruio.h: 633
if hasattr(_libs['libpruio.so'], 'pruio_pwm_Value'):
    pruio_pwm_Value = _libs['libpruio.so'].pruio_pwm_Value
    pruio_pwm_Value.argtypes = [POINTER(pruIo), uint8, POINTER(float_t), POINTER(float_t)]
    if sizeof(c_int) == sizeof(c_void_p):
        pruio_pwm_Value.restype = ReturnString
    else:
        pruio_pwm_Value.restype = String
        pruio_pwm_Value.errcheck = ReturnString

# /root/libpruio-0.2/src/c_wrapper/pruio.h: 644
if hasattr(_libs['libpruio.so'], 'pruio_pwm_setValue'):
    pruio_pwm_setValue = _libs['libpruio.so'].pruio_pwm_setValue
    pruio_pwm_setValue.argtypes = [POINTER(pruIo), uint8, float_t, float_t]
    if sizeof(c_int) == sizeof(c_void_p):
        pruio_pwm_setValue.restype = ReturnString
    else:
        pruio_pwm_setValue.restype = String
        pruio_pwm_setValue.errcheck = ReturnString

# /root/libpruio-0.2/src/c_wrapper/pruio.hp: 79
try:
    PRUIO_IRPT = 25
except:
    pass

# /root/libpruio-0.2/src/c_wrapper/pruio.hp: 81
try:
    PRUIO_AZ_BALL = 109
except:
    pass

# /root/libpruio-0.2/src/c_wrapper/pruio.hp: 82
try:
    PRUIO_AZ_GPIO = 3
except:
    pass

# /root/libpruio-0.2/src/c_wrapper/pruio.hp: 83
try:
    PRUIO_AZ_PWMSS = 2
except:
    pass

# /root/libpruio-0.2/src/c_wrapper/pruio.hp: 85
try:
    PRUIO_COM_GPIO_CONF = 10
except:
    pass

# /root/libpruio-0.2/src/c_wrapper/pruio.hp: 86
try:
    PRUIO_COM_GPIO_OUT = 11
except:
    pass

# /root/libpruio-0.2/src/c_wrapper/pruio.hp: 87
try:
    PRUIO_COM_PWM = 30
except:
    pass

# /root/libpruio-0.2/src/c_wrapper/pruio.hp: 88
try:
    PRUIO_COM_PWM_CAP = 31
except:
    pass

# /root/libpruio-0.2/src/c_wrapper/pruio.hp: 89
try:
    PRUIO_COM_CAP = 32
except:
    pass

# /root/libpruio-0.2/src/c_wrapper/pruio.hp: 90
try:
    PRUIO_COM_QEP = 33
except:
    pass

# /root/libpruio-0.2/src/c_wrapper/pruio.hp: 91
try:
    PRUIO_COM_ADC = 50
except:
    pass

# /root/libpruio-0.2/src/c_wrapper/pruio.hp: 93
try:
    PRUIO_DAT_GPIO = 64
except:
    pass

# /root/libpruio-0.2/src/c_wrapper/pruio.hp: 94
try:
    PRUIO_DAT_PWM = 128
except:
    pass

# /root/libpruio-0.2/src/c_wrapper/pruio.hp: 95
try:
    PRUIO_DAT_ADC = 224
except:
    pass

# /root/libpruio-0.2/src/c_wrapper/pruio.hp: 96
try:
    PRUIO_DAT_ALL = 512
except:
    pass

# /root/libpruio-0.2/src/c_wrapper/pruio.hp: 98
try:
    PRUIO_MSG_INIT_RUN = 4294967295L
except:
    pass

# /root/libpruio-0.2/src/c_wrapper/pruio.hp: 99
try:
    PRUIO_MSG_CONF_RUN = 4294967294L
except:
    pass

# /root/libpruio-0.2/src/c_wrapper/pruio.hp: 100
try:
    PRUIO_MSG_INIT_OK = 4294967293L
except:
    pass

# /root/libpruio-0.2/src/c_wrapper/pruio.hp: 101
try:
    PRUIO_MSG_CONF_OK = 4294967292L
except:
    pass

# /root/libpruio-0.2/src/c_wrapper/pruio.hp: 102
try:
    PRUIO_MSG_ADC_ERRR = 4294967291L
except:
    pass

# /root/libpruio-0.2/src/c_wrapper/pruio.hp: 103
try:
    PRUIO_MSG_MM_WAIT = 4294967290L
except:
    pass

# /root/libpruio-0.2/src/c_wrapper/pruio.hp: 104
try:
    PRUIO_MSG_MM_TRG1 = 4294967289L
except:
    pass

# /root/libpruio-0.2/src/c_wrapper/pruio.hp: 105
try:
    PRUIO_MSG_MM_TRG2 = 4294967288L
except:
    pass

# /root/libpruio-0.2/src/c_wrapper/pruio.hp: 106
try:
    PRUIO_MSG_MM_TRG3 = 4294967287L
except:
    pass

# /root/libpruio-0.2/src/c_wrapper/pruio.hp: 107
try:
    PRUIO_MSG_MM_TRG4 = 4294967286L
except:
    pass

# /root/libpruio-0.2/src/c_wrapper/pruio.hp: 108
try:
    PRUIO_MSG_IO_OK = 4294967285L
except:
    pass

# /root/libpruio-0.2/src/c_wrapper/pruio.h: 32
try:
    PRUIO_VERSION = '0.2'
except:
    pass

# /root/libpruio-0.2/src/c_wrapper/pruio.h: 50
try:
    PRUIO_DEF_AVRAGE = 4
except:
    pass

# /root/libpruio-0.2/src/c_wrapper/pruio.h: 52
try:
    PRUIO_DEF_ODELAY = 183
except:
    pass

# /root/libpruio-0.2/src/c_wrapper/pruio.h: 54
try:
    PRUIO_DEF_SDELAY = 0
except:
    pass

# /root/libpruio-0.2/src/c_wrapper/pruio.h: 56
try:
    PRUIO_DEF_SAMPLS = 1
except:
    pass

# /root/libpruio-0.2/src/c_wrapper/pruio.h: 58
try:
    PRUIO_DEF_STPMSK = 510
except:
    pass

# /root/libpruio-0.2/src/c_wrapper/pruio.h: 60
try:
    PRUIO_DEF_TIMERV = 0
except:
    pass

# /root/libpruio-0.2/src/c_wrapper/pruio.h: 62
try:
    PRUIO_DEF_LSLMOD = 4
except:
    pass

# /root/libpruio-0.2/src/c_wrapper/pruio.h: 64
try:
    PRUIO_DEF_CLKDIV = 0
except:
    pass

# /root/libpruio-0.2/src/c_wrapper/pruio_pins.h: 16
try:
    P8_03 = 6
except:
    pass

# /root/libpruio-0.2/src/c_wrapper/pruio_pins.h: 17
try:
    P8_04 = 7
except:
    pass

# /root/libpruio-0.2/src/c_wrapper/pruio_pins.h: 18
try:
    P8_05 = 2
except:
    pass

# /root/libpruio-0.2/src/c_wrapper/pruio_pins.h: 19
try:
    P8_06 = 3
except:
    pass

# /root/libpruio-0.2/src/c_wrapper/pruio_pins.h: 20
try:
    P8_07 = 36
except:
    pass

# /root/libpruio-0.2/src/c_wrapper/pruio_pins.h: 21
try:
    P8_08 = 37
except:
    pass

# /root/libpruio-0.2/src/c_wrapper/pruio_pins.h: 22
try:
    P8_09 = 39
except:
    pass

# /root/libpruio-0.2/src/c_wrapper/pruio_pins.h: 23
try:
    P8_10 = 38
except:
    pass

# /root/libpruio-0.2/src/c_wrapper/pruio_pins.h: 24
try:
    P8_11 = 13
except:
    pass

# /root/libpruio-0.2/src/c_wrapper/pruio_pins.h: 25
try:
    P8_12 = 12
except:
    pass

# /root/libpruio-0.2/src/c_wrapper/pruio_pins.h: 26
try:
    P8_13 = 9
except:
    pass

# /root/libpruio-0.2/src/c_wrapper/pruio_pins.h: 27
try:
    P8_14 = 10
except:
    pass

# /root/libpruio-0.2/src/c_wrapper/pruio_pins.h: 28
try:
    P8_15 = 15
except:
    pass

# /root/libpruio-0.2/src/c_wrapper/pruio_pins.h: 29
try:
    P8_16 = 14
except:
    pass

# /root/libpruio-0.2/src/c_wrapper/pruio_pins.h: 30
try:
    P8_17 = 11
except:
    pass

# /root/libpruio-0.2/src/c_wrapper/pruio_pins.h: 31
try:
    P8_18 = 35
except:
    pass

# /root/libpruio-0.2/src/c_wrapper/pruio_pins.h: 32
try:
    P8_19 = 8
except:
    pass

# /root/libpruio-0.2/src/c_wrapper/pruio_pins.h: 33
try:
    P8_20 = 33
except:
    pass

# /root/libpruio-0.2/src/c_wrapper/pruio_pins.h: 34
try:
    P8_21 = 32
except:
    pass

# /root/libpruio-0.2/src/c_wrapper/pruio_pins.h: 35
try:
    P8_22 = 5
except:
    pass

# /root/libpruio-0.2/src/c_wrapper/pruio_pins.h: 36
try:
    P8_23 = 4
except:
    pass

# /root/libpruio-0.2/src/c_wrapper/pruio_pins.h: 37
try:
    P8_24 = 1
except:
    pass

# /root/libpruio-0.2/src/c_wrapper/pruio_pins.h: 38
try:
    P8_25 = 0
except:
    pass

# /root/libpruio-0.2/src/c_wrapper/pruio_pins.h: 39
try:
    P8_26 = 31
except:
    pass

# /root/libpruio-0.2/src/c_wrapper/pruio_pins.h: 40
try:
    P8_27 = 56
except:
    pass

# /root/libpruio-0.2/src/c_wrapper/pruio_pins.h: 41
try:
    P8_28 = 58
except:
    pass

# /root/libpruio-0.2/src/c_wrapper/pruio_pins.h: 42
try:
    P8_29 = 57
except:
    pass

# /root/libpruio-0.2/src/c_wrapper/pruio_pins.h: 43
try:
    P8_30 = 59
except:
    pass

# /root/libpruio-0.2/src/c_wrapper/pruio_pins.h: 44
try:
    P8_31 = 54
except:
    pass

# /root/libpruio-0.2/src/c_wrapper/pruio_pins.h: 45
try:
    P8_32 = 55
except:
    pass

# /root/libpruio-0.2/src/c_wrapper/pruio_pins.h: 46
try:
    P8_33 = 53
except:
    pass

# /root/libpruio-0.2/src/c_wrapper/pruio_pins.h: 47
try:
    P8_34 = 51
except:
    pass

# /root/libpruio-0.2/src/c_wrapper/pruio_pins.h: 48
try:
    P8_35 = 52
except:
    pass

# /root/libpruio-0.2/src/c_wrapper/pruio_pins.h: 49
try:
    P8_36 = 50
except:
    pass

# /root/libpruio-0.2/src/c_wrapper/pruio_pins.h: 50
try:
    P8_37 = 48
except:
    pass

# /root/libpruio-0.2/src/c_wrapper/pruio_pins.h: 51
try:
    P8_38 = 49
except:
    pass

# /root/libpruio-0.2/src/c_wrapper/pruio_pins.h: 52
try:
    P8_39 = 46
except:
    pass

# /root/libpruio-0.2/src/c_wrapper/pruio_pins.h: 53
try:
    P8_40 = 47
except:
    pass

# /root/libpruio-0.2/src/c_wrapper/pruio_pins.h: 54
try:
    P8_41 = 44
except:
    pass

# /root/libpruio-0.2/src/c_wrapper/pruio_pins.h: 55
try:
    P8_42 = 45
except:
    pass

# /root/libpruio-0.2/src/c_wrapper/pruio_pins.h: 56
try:
    P8_43 = 42
except:
    pass

# /root/libpruio-0.2/src/c_wrapper/pruio_pins.h: 57
try:
    P8_44 = 43
except:
    pass

# /root/libpruio-0.2/src/c_wrapper/pruio_pins.h: 58
try:
    P8_45 = 40
except:
    pass

# /root/libpruio-0.2/src/c_wrapper/pruio_pins.h: 59
try:
    P8_46 = 41
except:
    pass

# /root/libpruio-0.2/src/c_wrapper/pruio_pins.h: 61
try:
    P9_11 = 28
except:
    pass

# /root/libpruio-0.2/src/c_wrapper/pruio_pins.h: 62
try:
    P9_12 = 30
except:
    pass

# /root/libpruio-0.2/src/c_wrapper/pruio_pins.h: 63
try:
    P9_13 = 29
except:
    pass

# /root/libpruio-0.2/src/c_wrapper/pruio_pins.h: 64
try:
    P9_14 = 18
except:
    pass

# /root/libpruio-0.2/src/c_wrapper/pruio_pins.h: 65
try:
    P9_15 = 16
except:
    pass

# /root/libpruio-0.2/src/c_wrapper/pruio_pins.h: 66
try:
    P9_16 = 19
except:
    pass

# /root/libpruio-0.2/src/c_wrapper/pruio_pins.h: 67
try:
    P9_17 = 87
except:
    pass

# /root/libpruio-0.2/src/c_wrapper/pruio_pins.h: 68
try:
    P9_18 = 86
except:
    pass

# /root/libpruio-0.2/src/c_wrapper/pruio_pins.h: 69
try:
    P9_19 = 95
except:
    pass

# /root/libpruio-0.2/src/c_wrapper/pruio_pins.h: 70
try:
    P9_20 = 94
except:
    pass

# /root/libpruio-0.2/src/c_wrapper/pruio_pins.h: 71
try:
    P9_21 = 85
except:
    pass

# /root/libpruio-0.2/src/c_wrapper/pruio_pins.h: 72
try:
    P9_22 = 84
except:
    pass

# /root/libpruio-0.2/src/c_wrapper/pruio_pins.h: 73
try:
    P9_23 = 17
except:
    pass

# /root/libpruio-0.2/src/c_wrapper/pruio_pins.h: 74
try:
    P9_24 = 97
except:
    pass

# /root/libpruio-0.2/src/c_wrapper/pruio_pins.h: 75
try:
    P9_25 = 107
except:
    pass

# /root/libpruio-0.2/src/c_wrapper/pruio_pins.h: 76
try:
    P9_26 = 96
except:
    pass

# /root/libpruio-0.2/src/c_wrapper/pruio_pins.h: 77
try:
    P9_27 = 105
except:
    pass

# /root/libpruio-0.2/src/c_wrapper/pruio_pins.h: 78
try:
    P9_28 = 103
except:
    pass

# /root/libpruio-0.2/src/c_wrapper/pruio_pins.h: 79
try:
    P9_29 = 101
except:
    pass

# /root/libpruio-0.2/src/c_wrapper/pruio_pins.h: 80
try:
    P9_30 = 102
except:
    pass

# /root/libpruio-0.2/src/c_wrapper/pruio_pins.h: 81
try:
    P9_31 = 100
except:
    pass

# /root/libpruio-0.2/src/c_wrapper/pruio_pins.h: 82
try:
    P9_41 = 109
except:
    pass

# /root/libpruio-0.2/src/c_wrapper/pruio_pins.h: 83
try:
    P9_42 = 89
except:
    pass

# /root/libpruio-0.2/src/c_wrapper/pruio.hp: 79
try:
    PRUIO_IRPT = 25
except:
    pass

# /root/libpruio-0.2/src/c_wrapper/pruio.hp: 81
try:
    PRUIO_AZ_BALL = 109
except:
    pass

# /root/libpruio-0.2/src/c_wrapper/pruio.hp: 82
try:
    PRUIO_AZ_GPIO = 3
except:
    pass

# /root/libpruio-0.2/src/c_wrapper/pruio.hp: 83
try:
    PRUIO_AZ_PWMSS = 2
except:
    pass

# /root/libpruio-0.2/src/c_wrapper/pruio.hp: 85
try:
    PRUIO_COM_GPIO_CONF = 10
except:
    pass

# /root/libpruio-0.2/src/c_wrapper/pruio.hp: 86
try:
    PRUIO_COM_GPIO_OUT = 11
except:
    pass

# /root/libpruio-0.2/src/c_wrapper/pruio.hp: 87
try:
    PRUIO_COM_PWM = 30
except:
    pass

# /root/libpruio-0.2/src/c_wrapper/pruio.hp: 88
try:
    PRUIO_COM_PWM_CAP = 31
except:
    pass

# /root/libpruio-0.2/src/c_wrapper/pruio.hp: 89
try:
    PRUIO_COM_CAP = 32
except:
    pass

# /root/libpruio-0.2/src/c_wrapper/pruio.hp: 90
try:
    PRUIO_COM_QEP = 33
except:
    pass

# /root/libpruio-0.2/src/c_wrapper/pruio.hp: 91
try:
    PRUIO_COM_ADC = 50
except:
    pass

# /root/libpruio-0.2/src/c_wrapper/pruio.hp: 93
try:
    PRUIO_DAT_GPIO = 64
except:
    pass

# /root/libpruio-0.2/src/c_wrapper/pruio.hp: 94
try:
    PRUIO_DAT_PWM = 128
except:
    pass

# /root/libpruio-0.2/src/c_wrapper/pruio.hp: 95
try:
    PRUIO_DAT_ADC = 224
except:
    pass

# /root/libpruio-0.2/src/c_wrapper/pruio.hp: 96
try:
    PRUIO_DAT_ALL = 512
except:
    pass

# /root/libpruio-0.2/src/c_wrapper/pruio.hp: 98
try:
    PRUIO_MSG_INIT_RUN = 4294967295L
except:
    pass

# /root/libpruio-0.2/src/c_wrapper/pruio.hp: 99
try:
    PRUIO_MSG_CONF_RUN = 4294967294L
except:
    pass

# /root/libpruio-0.2/src/c_wrapper/pruio.hp: 100
try:
    PRUIO_MSG_INIT_OK = 4294967293L
except:
    pass

# /root/libpruio-0.2/src/c_wrapper/pruio.hp: 101
try:
    PRUIO_MSG_CONF_OK = 4294967292L
except:
    pass

# /root/libpruio-0.2/src/c_wrapper/pruio.hp: 102
try:
    PRUIO_MSG_ADC_ERRR = 4294967291L
except:
    pass

# /root/libpruio-0.2/src/c_wrapper/pruio.hp: 103
try:
    PRUIO_MSG_MM_WAIT = 4294967290L
except:
    pass

# /root/libpruio-0.2/src/c_wrapper/pruio.hp: 104
try:
    PRUIO_MSG_MM_TRG1 = 4294967289L
except:
    pass

# /root/libpruio-0.2/src/c_wrapper/pruio.hp: 105
try:
    PRUIO_MSG_MM_TRG2 = 4294967288L
except:
    pass

# /root/libpruio-0.2/src/c_wrapper/pruio.hp: 106
try:
    PRUIO_MSG_MM_TRG3 = 4294967287L
except:
    pass

# /root/libpruio-0.2/src/c_wrapper/pruio.hp: 107
try:
    PRUIO_MSG_MM_TRG4 = 4294967286L
except:
    pass

# /root/libpruio-0.2/src/c_wrapper/pruio.hp: 108
try:
    PRUIO_MSG_IO_OK = 4294967285L
except:
    pass

pruIo = struct_pruIo # /root/libpruio-0.2/src/c_wrapper/pruio.h: 46

adcSteps = struct_adcSteps # /root/libpruio-0.2/src/c_wrapper/pruio.h: 70

adcSet = struct_adcSet # /root/libpruio-0.2/src/c_wrapper/pruio.h: 114

adcUdt = struct_adcUdt # /root/libpruio-0.2/src/c_wrapper/pruio.h: 134

gpioSet = struct_gpioSet # /root/libpruio-0.2/src/c_wrapper/pruio.h: 174

gpioArr = struct_gpioArr # /root/libpruio-0.2/src/c_wrapper/pruio.h: 187

gpioUdt = struct_gpioUdt # /root/libpruio-0.2/src/c_wrapper/pruio.h: 202

pwmssSet = struct_pwmssSet # /root/libpruio-0.2/src/c_wrapper/pruio.h: 309

pwmssArr = struct_pwmssArr # /root/libpruio-0.2/src/c_wrapper/pruio.h: 327

pwmssUdt = struct_pwmssUdt # /root/libpruio-0.2/src/c_wrapper/pruio.h: 344

pwmMod = struct_pwmMod # /root/libpruio-0.2/src/c_wrapper/pruio.h: 351

capMod = struct_capMod # /root/libpruio-0.2/src/c_wrapper/pruio.h: 357

qepMod = struct_qepMod # /root/libpruio-0.2/src/c_wrapper/pruio.h: 363

ballSet = struct_ballSet # /root/libpruio-0.2/src/c_wrapper/pruio.h: 409

# Begin inserted files

# Begin "pruio_include.py"

import prussdrv

struct_pruIo.__slots__ = [
    'adcUdt',
    'gpioUdt',
    'pwmssUdt',
    'pwmMod',
    'capMod',
    'Errr',
    'DRam',
    'ballSet',
    'Init',
    'Conf',
    'ERam',
    'DInit',
    'DConf',
    'MOffs',
    'BallOrg',
    'BallConf',
    'EAddr',
    'ESize',
    'DSize',
    'PruNo',
    'PruEvtOut',
    'PruIRam',
    'PruDRam',
    'ArmPruInt',
    'ParOffs',
    'DevAct',
    'IntcInit',
    'BallGpio',
]

struct_pruIo._fields_ = [
    ('adcUdt', POINTER(adcUdt)),
    ('gpioUdt', POINTER(gpioUdt)),
    ('pwmssUdt', POINTER(pwmssUdt)),
    ('pwmMod', POINTER(pwmMod)),
    ('capMod', POINTER(capMod)),
    ('Errr', String),
    ('DRam', POINTER(uint32)),
    ('Init', POINTER(ballSet)),
    ('Conf', POINTER(ballSet)),
    ('ERam', c_void_p),
    ('DInit', c_void_p),
    ('DConf', c_void_p),
    ('MOffs', c_void_p),
    ('BallOrg', POINTER(uint8)),
    ('BallConf', POINTER(uint8)),
    ('EAddr', uint32),
    ('ESize', uint32),
    ('DSize', uint32),
    ('PruNo', uint32),
    ('PruEvtOut', uint32),
    ('PruIRam', uint32),
    ('PruDRam', uint32),
    ('ArmPruInt', int16),
    ('ParOffs', int16),
    ('DevAct', int16),
    ('IntcInit', prussdrv.__pruss_intc_initdata),
    ('BallGpio', uint8 * (110)),
]

# End "pruio_include.py"

# 1 inserted files
# End inserted files

