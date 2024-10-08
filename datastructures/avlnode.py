from abc import abstractmethod
from functools import total_ordering
from typing import Any, Callable, Protocol, TypeVar, Generic, Optional, List, Sequence, Tuple

@total_ordering
class Comparable(Protocol):
    @abstractmethod
    def __lt__(self, other: Any) -> bool: ...
        
K = TypeVar('K', bound=Comparable)  # Key type for ordering the nodes
V = TypeVar('V')  # Value type for storing associated data

class AVLNode(Generic[K, V]):
    def __init__(self, key: K, value: V, left: None = None, right: None = None): 
        self._key = key
        self._value = value
        self._left_child = left
        self._right_child = right
        self._height = 0
    
    @property 
    def key(self) -> K: 
        return self._key
    
    @key.setter
    def key(self, key: Any) -> None:
        self._key = key

    @property
    def value(self) -> V: 
        return self._value
    
    @key.setter
    def value(self, value: Any) -> None:
        self._value = value

    @property
    def left(self) -> Any: 
        return self._left_child

    @left.setter
    def left(self, left: Any) -> None: 
        self._left_child = left

    @property
    def right(self) -> Any: 
        return self._right_child

    @right.setter
    def right(self, right: Any) -> None: 
        self._right_child = right

    @property
    def height(self) -> int: 
        return self._height

    @height.setter
    def height(self, height: int) -> None: 
        self._height = height
    
    def __str__(self):
        return str(self.value)
    
    def __repr__(self):
        return str(self.value)
