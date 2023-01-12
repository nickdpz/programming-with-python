from cerberus import Validator

person_schema = {
    'name': {'required': True, 'type': 'string'},
    'age': {'required': True, 'type': 'integer', 'min': 18},
}
v = Validator(person_schema)

person = {"name": "Alice", "age": 30}
print(v.validate(person)) # True

person = {"name": "Alice", "age": 15}
print(v.validate(person)) # False

person = {"age": 30}
print(v.validate(person)) # False