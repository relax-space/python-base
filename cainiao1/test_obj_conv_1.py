import json
from typing import Dict


class Person:
    def __init__(self, name: str = 'xiaomiao'):
        self.name = name

    @staticmethod
    def to_dict(obj: 'Person'):
        return obj.__dict__

    @classmethod
    def from_dict(cls, dict: Dict)->'Person':
        p = cls()
        p.__dict__ = dict
        return p


class Female(Person):
    def __init__(self, name: str = 'xiao', sex: int = 1):
        self.name = name
        self.sex = sex


def test_1():
    p = Person('xiao')
    json1 = json.dumps(p, default=Person.to_dict)
    assert '{"name": "xiao"}' == json1, 'json dump error'
    p2 = json.loads(json1, object_hook=Person.from_dict)
    assert p.__dict__ == p2.__dict__, 'json loads error'


def test_2():
    p_list = [Person('xiao1'), Person('xiao2')]
    json1 = json.dumps(p_list, default=Person.to_dict)
    assert '[{"name": "xiao1"}, {"name": "xiao2"}]' == json1, 'json dump 2 error'
    p2_list = json.loads(json1, object_hook=Person.from_dict)
    assert p_list[0].__dict__ == p2_list[0].__dict__ and p_list[1].__dict__ == p2_list[1].__dict__, 'json loads 2 error'


def test_3():
    p = Female(name='xiao1', sex=1)
    json1 = json.dumps(p, default=Female.to_dict)
    assert '{"name": "xiao1", "sex": 1}' == json1, 'json dump error'
    p2 = json.loads(json1, object_hook=Female.from_dict)
    assert p.__dict__ == p2.__dict__, 'json loads error'
