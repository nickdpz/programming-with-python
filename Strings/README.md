## String guide

- Manejo de cadenas de más de una linea

```python
name = """
I am string with line jump
Look that me
"""
```

- Concatenar variables en una misma caneda

```python
print('{} is a subcategory of {}'.format(subcategory, category))# Cars is a subcategory of Toys
```

- Multiplicar o sumar textos

```python
line="Toys"
line="Toys"+"Cars" # ToysCars
lines=line*3 # ToysToysToys
```

### Metodos de la clase String

- Covertir en mayuscula

```python
name="toys"
name=name.upper()#TOYS
```

- Covertir en minúscula

```python
name="TOYS"
name=name.lower()#toys
```

- Covertir primera letra en mayuscula

```python
name="toys"
name=name.capitalize()#Toys
```

- Eliminar espacios basura

```python
name="Nicolas "
name=name.strip()# Nicolas
```

- Reemplazar caracteres

```python
name="Camilo"
name=name.replace('o','a')# Camila
```

- Operaciones De arreglo

```python
name="Nicolas"
initial=name[1]#i
nameLen=len(name)#7
```

- División de string (slice)

```python
name="nicolas-pastran"
name13=name[0:8:2]#nclsp
name13=name[::-1]#nartsap-salocin
```
