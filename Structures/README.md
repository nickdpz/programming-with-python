## Structures Guide

Save many values in a one variable.

### List

A list is a data structure that store repeating values

- List Operators

```python
a=[1,2]
b=[3,4]
c=a + b #[1,2,3,4]


a=[1,2]
c= a * 2 # [1,2,1,2]
```

- Add elements to end of list

```python
a=[1]
a.append(2) #[1,2]
```

- Delete last element of list

```python
a=[1,2]
b=a.pop() # [1,2,1,2]
```

- Delete and element of list

```python
a=[1,2]
b=a.pop(1)#a=[1],b=2
```

- Sort list modified list

```python
a=[3,8,1]
a.sort()# a=[1,3,8]
```

- Sort list Without modified list

```python
a=[3,8,1]
a.sorted()# [1,3,8]
```

- Delete elements of list

```python
a=[1,2,3]
del a[0]# a[2,3]
```

- Delete elements of list with a value

```python
a=[0, 2, 4, 6, 8]
a.remove(6)#a=[0, 2, 4, 8]
```

- Create list with a range

```python
a=(list(range(0,10,2)))# a=[0,2,4,6,8]
```

- Get length of the list

```python
a=[0,2,4,6,8]
b=len(a)#5
```

### Tuple

- Change values of a tuple

```python
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
```

### Maps

- Iterate map

```python
countries = {
    "Argentina": 44938712,
    "Bolivia": 11510225,
    "Brasil": 210147125,
    "Colombia": 50372424,
}

for keys, values in countries.items():
    print(f'county {keys} has {values} population')
```

- List with dictionaries

```python
superList = [
    {
        "name": "value"
    }
]
```

- List comprehensions (List and Map merge)

```python
multiplesFourSixNine = [item for item in range(0, 100)if item % 4 == 0 and item % 6 == 0 and item % 9 == 0]
```

- Dictionary comprehensions

```python
squareMulTwo={item: item**(1/2) for item in range(0, 10) if item % 2 == 0}
```
