# Virtual Enviroments

- Create virtual enviroment

```sh
$ python3 -m venv venv
```

- Activate virtual enviroment
- 
```sh
source venv/bin/activate 
```

- List dependencies

```python
$ pip freeze > requirements.txt && cat requirements.txt
```

- Install dependecies

```python
$ pip install -r requirements.txt
```

- Install new dependecy

```python
$ pip install pandas
```

- Update dependencies

```sh
pip list --outdated --format=freeze | grep -v '^\-e' | cut -d = -f 1  | xargs -n1 pip install -U
```
