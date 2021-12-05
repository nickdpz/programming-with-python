## Cycles Guide

### While

- Defined cycle functions

```python
count=1
while(count):
    count+=1
    print(count)
```

- Undefined end cycle

```python
LIMIT=10
while (power <= LIMIT):
    result = numero ** power
    print('Power of {} raised to the {} is {}'.format(numero, power, result))
    power += 1
```

### For

- For with map

```python
values = {'A': 4, 'E': 3, 'I': 1, 'O': 0}
for k in values:
    print(k)
```

- For with a range or a list

```python
for i in range(10):
    print(11 * i)
```

- For with string
```python
def run ():
    name = input("Type you name: ")
    for i in name:
        print(i)
if __name__ == '__main__':
    run()
```

## Break

- Break end cycle. Duty for searching
```python
numbers = [1, 2, 3, 4, 5, 8, 6]
for n in numbers:
    if n == 3:
        break
```


- For with break

```python
numbers = [1, 2, 3, 4, 5, 8, 6]
for n in numbers:
    if n == 3:
        break
else:
    print('Print if dont break in one moment')
```

### Continue

- Continue skip and code in and cycle. Print pair numbers
```python
for count in range(1000):
    if count % 2 != 0:
        continue
    print(count
```