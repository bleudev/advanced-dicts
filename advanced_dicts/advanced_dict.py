from typing import (
    Optional
)

class AdvancedDict:
    def __init__(self, __dict: dict) -> None:
        self.__dict = __dict
        
    def _get_list_of_tuples(self):
        keys = list(self.__dict.keys())
    
        result = [(key, self.__dict[key]) for key in keys]
    
        return result
    
    def __iter__(self):
        __list = self._get_list_of_tuples()
        return iter(__list)

    def __getitem__(self, key):
        return self.__dict[key]
    
    def __setitem__(self, key, value):
        try:
            self.__dict[key] = value
        except KeyError:
            self.__dict.setdefault(key, value)
    
    @property
    def dict(self) -> dict:
        return self.__dict
