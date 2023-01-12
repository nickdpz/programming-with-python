# Static Typing With Python

## Primitive types

```python
a: int = 5
print(a)

b: str = "hello"
print(b)

c: bool = True
print(c)
```

## Functions

```python
def sum(a: int, b: int) -> int :
	return a + b

print(sum(1,2))
```

```python

def scale(scalar: float, vector: list[float]) -> list[float]:
    return [scalar * num for num in vector]

new_vector = scale(2.0, [1.0, -4.2, 5.4])
```


## Lists / Dictionaries

- List of primitives
```python
from typing import List

positives: List [int] = [1,2,3,4,5]
```

- Dictionaries of primitives 

```python
from typing import List

users: Dict [str, int] = {
	"argentina": 1.
	"mexico": 34,
	"colombia": 45,
}
```

- List of dictionaries of primitives

```python
from typing import Dict, List

countries: List[Dict[str, str]] = [
	{
		"name" : "Argentina",
		"people" : "45000",
	},
	{
		"name" : "México",
		"people" : "9000000",
	},
	{
		"name" : "Colombia",
		"people" : "99999999999",
	}
]
```

## Wildcard type
- NoReturn (Unreturned)
```python
def broadcast_message(
        message: str,
        servers: list[int]) -> NoReturn:
```

- Any

```python
from typing import Any

a: Any = None

def foo(item: Any) -> int:
    item.bar()
```

- Never

```python 
from typing import Never

def never_call_me(arg: Never) -> None:
    pass
```

## Create types

```python
Vector = list[float]
def scale(scalar: float, vector: Vector) -> Vector:
    return [scalar * num for num in vector]

new_vector = scale(2.0, [1.0, -4.2, 5.4])
```

## Type of function

```python
from collections.abc import Callable

def async_query(on_success: Callable[[int], None],
                on_error: Callable[[int, Exception], None]) -> None:
```

## Interfaces
- The interface in python is not exist, however one interface is emulate with abstract class. The abstract class can not attributes
```python
from abc import ABC, abstractmethod

class Shape(ABC):

    _name = ""

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value

    @abstractmethod
    def area(self) -> float:
        pass

class Circle(Shape):
    def __init__(self, radius: float):
        self._radius = radius
        self.name = "circle"

    def area(self) -> float:
        return 3.14 * (self._radius ** 2)
```

(More Info)[https://docs.python.org/es/3/library/typing.html]
