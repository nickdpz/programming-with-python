# Advance

```sh
$ source venv/bin/activate 
```

### Installation

- Dependencias de producción

```sh
$ pip install -r requirements.txt
```

- Dependencias de desarrollo

```sh
$ pip install -r requirements-dev.txt
```

- Ver dependencias desactualizadas

```sh
$ pip list --outdated
```

- Verificar tipos

```sh
$ mypy staticType.py --check-untyped-defs
```

### Test

```sh
$ pytest
```

### Run with jobs

```sh
python main.py --job=dummy
```

## Code Style & Quality Checker

```sh
$ flake8 .

$ black . --exclude=venv

$ pylint $module_folder

$ pylint --generate-rcfile > .pylintrc
```

## Unit Test Coverage

```sh
$ pytest tests/
```
