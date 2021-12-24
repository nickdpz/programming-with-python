# Functional programming

- Lambda functions. Infinite paramters, always return, one line and one expresión

```python
palindrome=lambda x: x==x[::-1]
```

- Filter

```python
DATA = [
{
    'name': 'Juan',
    'language': 'go',
},
{
    'name': 'Pablo',
    'language': 'python',
},
{
    'name': 'Lorena',
    'language': 'python',
},
]
pythonDevs = list(filter(lambda worker:worker["language"] == "python", DATA))
```

- Map and Merge maps

```python
DATA = [
{
    'name': 'Juan',
    'language': 'go',
},
{
    'name': 'Pablo',
    'language': 'python',
},
{
    'name': 'Lorena',
    'language': 'python',
},
]
oldPeople = list(map(lambda worker: worker | {"old": worker["age"] > 70}, DATA))
```

- Reduce

```python
from functools import reduce
SELLS = [1, 1, 1, 10]

def run():
    total = reduce(lambda a, b: a+b, SELLS)
    print(total)


if __name__ == '__main__':
    run()
```
