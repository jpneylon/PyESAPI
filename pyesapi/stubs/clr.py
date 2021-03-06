# encoding: utf-8
# module clr
# from (built-in)
# by generator 1.145
# type: ()
""" module() """
# no imports

# Variables with simple values

IsDebug = False
IsMacOS = False
IsMono = False
IsNetCoreApp = False

TargetFramework = '.NETFramework,Version=v4.5'

# functions

def accepts(*types, p_object=None): # real signature unknown; restored from __doc__
    # type: (*types: Array[object]) -> object
    """ accepts(*types: Array[object]) -> object """
    return object()

def AddReference(*args, **kwargs): # real signature unknown
    """
    Adds a reference to a .NET assembly.  Parameters can be an already loaded
    Assembly object, a full assembly name, or a partial assembly name. After the
    load the assemblies namespaces and top-level types will be available via 
    import Namespace.
    """
    pass

def AddReferenceByName(*args, **kwargs): # real signature unknown
    """
    Adds a reference to a .NET assembly.  Parameters are an assembly name. 
    After the load the assemblies namespaces and top-level types will be available via 
    import Namespace.
    """
    pass

def AddReferenceByPartialName(*args, **kwargs): # real signature unknown
    """
    Adds a reference to a .NET assembly.  Parameters are a partial assembly name. 
    After the load the assemblies namespaces and top-level types will be available via 
    import Namespace.
    """
    pass

def AddReferenceToFile(*args, **kwargs): # real signature unknown
    """
    Adds a reference to a .NET assembly.  One or more assembly names can
    be provided.  The assembly is searched for in the directories specified in 
    sys.path and dependencies will be loaded from sys.path as well.  The assembly 
    name should be the filename on disk without a directory specifier and 
    optionally including the .EXE or .DLL extension. After the load the assemblies 
    namespaces and top-level types will be available via import Namespace.
    """
    pass

def AddReferenceToFileAndPath(*args, **kwargs): # real signature unknown
    """
    Adds a reference to a .NET assembly.  One or more assembly names can
    be provided which are fully qualified names to the file on disk.  The 
    directory is added to sys.path and AddReferenceToFile is then called. After the 
    load the assemblies namespaces and top-level types will be available via 
    import Namespace.
    """
    pass

def AddReferenceToTypeLibrary(rcw): # real signature unknown; restored from __doc__
    # type: (rcw: object)AddReferenceToTypeLibrary(typeLibGuid: Guid)
    """ AddReferenceToTypeLibrary(rcw: object)AddReferenceToTypeLibrary(typeLibGuid: Guid) """
    pass

def ClearProfilerData(): # real signature unknown; restored from __doc__
    # type: ()
    """ ClearProfilerData() """
    pass

def CompileModules(assemblyName, **kwArgs, p_str=None, p_object=None, *args): # real signature unknown; NOTE: unreliably restored from __doc__ 
    # type: (assemblyName: str, **kwArgs: IDictionary[str, object], *filenames: Array[str])
    """ CompileModules(assemblyName: str, **kwArgs: IDictionary[str, object], *filenames: Array[str]) """
    pass

def CompileSubclassTypes(assemblyName, *newTypes, p_object=None): # real signature unknown; restored from __doc__
    # type: (assemblyName: str, *newTypes: Array[object])
    """ CompileSubclassTypes(assemblyName: str, *newTypes: Array[object]) """
    pass

def Convert(o, toType): # real signature unknown; restored from __doc__
    # type: (o: object, toType: Type) -> object
    """ Convert(o: object, toType: Type) -> object """
    return object()

def Deserialize(serializationFormat, data): # real signature unknown; restored from __doc__
    # type: (serializationFormat: str, data: str) -> object
    """ Deserialize(serializationFormat: str, data: str) -> object """
    return object()

def Dir(o): # real signature unknown; restored from __doc__
    # type: (o: object) -> list
    """ Dir(o: object) -> list """
    return []

def DirClr(o): # real signature unknown; restored from __doc__
    # type: (o: object) -> list
    """ DirClr(o: object) -> list """
    return []

def EnableProfiler(enable): # real signature unknown; restored from __doc__
    # type: (enable: bool)
    """ EnableProfiler(enable: bool) """
    pass

def GetBytes(*args, **kwargs): # real signature unknown
    """ Converts a string to an array of bytesConverts maxCount of a string to an array of bytes """
    pass

def GetClrType(type): # real signature unknown; restored from __doc__
    # type: (type: Type) -> Type
    """ GetClrType(type: Type) -> Type """
    pass

def GetCurrentRuntime(): # real signature unknown; restored from __doc__
    # type: () -> ScriptDomainManager
    """ GetCurrentRuntime() -> ScriptDomainManager """
    pass

def GetDynamicType(t): # real signature unknown; restored from __doc__
    # type: (t: Type) -> type
    """ GetDynamicType(t: Type) -> type """
    return type(*(), **{})

def GetProfilerData(includeUnused): # real signature unknown; restored from __doc__
    # type: (includeUnused: bool) -> tuple
    """ GetProfilerData(includeUnused: bool) -> tuple """
    return ()

def GetPythonType(t): # real signature unknown; restored from __doc__
    # type: (t: Type) -> type
    """ GetPythonType(t: Type) -> type """
    return type(*(), **{})

def GetString(*args, **kwargs): # real signature unknown
    """ Converts an array of bytes to a string.Converts maxCount of an array of bytes to a string """
    pass

def GetSubclassedTypes(): # real signature unknown; restored from __doc__
    # type: () -> tuple
    """ GetSubclassedTypes() -> tuple """
    return ()

def ImportExtensions(type): # real signature unknown; restored from __doc__
    # type: (type: type)ImportExtensions(namespace: namespace#)
    """ ImportExtensions(type: type)ImportExtensions(namespace: namespace#) """
    pass

def LoadAssemblyByName(*args, **kwargs): # real signature unknown
    """
    Loads an assembly from the specified assembly name and returns the assembly
    object.  Namespaces or types in the assembly can be accessed directly from 
    the assembly object.
    """
    pass

def LoadAssemblyByPartialName(*args, **kwargs): # real signature unknown
    """
    Loads an assembly from the specified partial assembly name and returns the 
    assembly object.  Namespaces or types in the assembly can be accessed directly 
    from the assembly object.
    """
    pass

def LoadAssemblyFromFile(*args, **kwargs): # real signature unknown
    """
    Loads an assembly from the specified filename and returns the assembly
    object.  Namespaces or types in the assembly can be accessed directly from 
    the assembly object.
    """
    pass

def LoadAssemblyFromFileWithPath(*args, **kwargs): # real signature unknown
    """
    Adds a reference to a .NET assembly.  Parameters are a full path to an. 
    assembly on disk. After the load the assemblies namespaces and top-level types 
    will be available via import Namespace.
    """
    pass

def LoadTypeLibrary(rcw): # real signature unknown; restored from __doc__
    # type: (rcw: object) -> ComTypeLibInfo
    """
    LoadTypeLibrary(rcw: object) -> ComTypeLibInfo
    LoadTypeLibrary(typeLibGuid: Guid) -> ComTypeLibInfo
    """
    pass

def returns(type): # real signature unknown; restored from __doc__
    # type: (type: object) -> object
    """ returns(type: object) -> object """
    return object()

def Self(): # real signature unknown; restored from __doc__
    # type: () -> object
    """ Self() -> object """
    return object()

def Serialize(self): # real signature unknown; restored from __doc__
    # type: (self: object) -> tuple
    """ Serialize(self: object) -> tuple """
    return ()

def SetCommandDispatcher(dispatcher, Action=None): # real signature unknown; restored from __doc__
    # type: (dispatcher: Action[Action]) -> Action[Action]
    """ SetCommandDispatcher(dispatcher: Action[Action]) -> Action[Action] """
    pass

def Use(name): # real signature unknown; restored from __doc__
    # type: (name: str) -> object
    """
    Use(name: str) -> object
    Use(path: str, language: str) -> object
    """
    return object()

# classes

class ArgChecker(object):
    # type: (prms: Array[object])
    """ ArgChecker(prms: Array[object]) """
    def __call__(self, *args): #cannot find CLR method
        """ x.__call__(...) <==> x(...) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, prms):
        """ __new__(cls: type, prms: Array[object]) """
        pass


class StrongBox(object, IStrongBox):
    # type: ()
    """
    StrongBox[T]()
    StrongBox[T](value: T)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, value=None):
        """
        __new__(cls: type)
        __new__(cls: type, value: T)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Value = None


Reference = StrongBox


class ReferencesList(List[Assembly], IList[Assembly], ICollection[Assembly], IEnumerable[Assembly], IEnumerable, IList, ICollection, IReadOnlyList[Assembly], IReadOnlyCollection[Assembly], ICodeFormattable):
    # type: ()
    """ ReferencesList() """
    def Add(self, *__args):
        # type: (self: ReferencesList, other: Assembly)
        """ Add(self: ReferencesList, other: Assembly) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __repr__(self, context):
        """ __repr__(self: ReferencesList) -> str """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass


class ReturnChecker(object):
    # type: (returnType: object)
    """ ReturnChecker(returnType: object) """
    def __call__(self, *args): #cannot find CLR method
        """ x.__call__(...) <==> x(...) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, returnType):
        """ __new__(cls: type, returnType: object) """
        pass

    retType = None


class RuntimeArgChecker(PythonTypeSlot):
    # type: (function: object, expectedArgs: Array[object])
    """
    RuntimeArgChecker(function: object, expectedArgs: Array[object])
    RuntimeArgChecker(instance: object, function: object, expectedArgs: Array[object])
    """
    def __call__(self, *args): #cannot find CLR method
        """ x.__call__(...) <==> x(...)x.__call__(...) <==> x(...) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, function: object, expectedArgs: Array[object])
        __new__(cls: type, instance: object, function: object, expectedArgs: Array[object])
        """
        pass


class RuntimeReturnChecker(PythonTypeSlot):
    # type: (function: object, expectedReturn: object)
    """
    RuntimeReturnChecker(function: object, expectedReturn: object)
    RuntimeReturnChecker(instance: object, function: object, expectedReturn: object)
    """
    def GetAttribute(self, instance, owner):
        # type: (self: RuntimeReturnChecker, instance: object, owner: object) -> object
        """ GetAttribute(self: RuntimeReturnChecker, instance: object, owner: object) -> object """
        pass

    def __call__(self, *args): #cannot find CLR method
        """ x.__call__(...) <==> x(...)x.__call__(...) <==> x(...) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, function: object, expectedReturn: object)
        __new__(cls: type, instance: object, function: object, expectedReturn: object)
        """
        pass


# variables with complex values

References = None

