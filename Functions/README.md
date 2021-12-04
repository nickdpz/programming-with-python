## Functions Guide

- Define function dynamic type

```python
def isPrime(number):
    if number < 2:
        return False
    elif number == 2:
        return True
    elif number > 2 and number % 2 == 0:
        return False
    else:
        for i in range(3, number):
            if number % i == 0:
                return False

    return True

result= isPrime(2)
```

- Native functions

```

```

### Notes

1. Siempre deben iniciar con mayuscula
