from typing import overload
import Boost.Python

@overload
def Deprotect(RDKit) -> Any: ...
@overload
def Deprotect(RDKit, boost) -> Any: ...
def GetDeprotections(*args, **kwargs) -> Any: ...

class DeprotectData(Boost.Python.instance):
    __instance_size__: Any = ...
    @classmethod
    def __init__(self, *args, **kwargs) -> None: ...
    @classmethod
    def isValid(RDKit) -> Any: ...
    @classmethod
    def __reduce__(self) -> Any: ...
    @property
    def abbreviation(self) -> Any: ...
    @property
    def deprotection_class(self) -> Any: ...
    @property
    def example(self) -> Any: ...
    @property
    def full_name(self) -> Any: ...
    @property
    def reaction_smarts(self) -> Any: ...

class DeprotectDataVect(Boost.Python.instance):
    __instance_size__: Any = ...
    @classmethod
    def __init__(self, *args, **kwargs) -> None: ...
    @classmethod
    def append(self, *args, **kwargs) -> Any: ...
    @classmethod
    def extend(self, *args, **kwargs) -> Any: ...
    @classmethod
    def __contains__(self, other) -> Any: ...
    @classmethod
    def __delitem__(self, other) -> Any: ...
    @classmethod
    def __getitem__(self, index) -> Any: ...
    @classmethod
    def __iter__(boost, std) -> Any: ...
    @classmethod
    def __len__(self) -> Any: ...
    @classmethod
    def __reduce__(self) -> Any: ...
    @classmethod
    def __setitem__(self, index, object) -> Any: ...