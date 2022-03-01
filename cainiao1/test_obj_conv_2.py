import importlib
import json
from typing import Dict


class Person1:
    def __init__(self, name: str = 'xiao'):
        self.name = name


class Person:
    def __init__(self, name: str = 'good'):
        self.name = name
        self.p1:Person1 = None

    @staticmethod
    def to_dict_pure(obj: 'Person'):
        return obj.__dict__

    @staticmethod
    def to_dict(obj: 'Person'):
        obj.__dict__.update(
            {'fullname': f'{obj.__module__}.{obj.__class__.__name__}'})
        return obj.__dict__

    @staticmethod
    def from_dict(dict: Dict)->'Person':
        module, classname = dict['fullname'].rsplit('.', 1)
        p = getattr(importlib.import_module(module), classname)()
        p.__dict__ = dict
        return p


def test_1():
    p = Person('xiao')
    p.p1 = Person1('xinmiao')
    json1 = json.dumps(p, default=Person.to_dict)
    assert '{"name": "xiao", "p1": {"name": "xinmiao", "fullname": "test_obj_conv_2.Person1"}, ' +\
        '"fullname": "test_obj_conv_2.Person"}' == json1, 'json dumps error'
    p2 = json.loads(json1, object_hook=Person.from_dict)
    assert p.__dict__['name'] == p2.__dict__['name'] \
        and p.__dict__['p1'].__dict__ == p2.__dict__['p1'].__dict__, 'json loads error'


def test_2():
    p1 = Person('xiao1')
    p1.p1 = Person1('xin1')
    p2 = Person('xiao2')
    p2.p1 = Person1('xin2')
    p_list = [p1, p2]
    json1 = json.dumps(p_list, default=Person.to_dict)
    assert '[{"name": "xiao1", "p1": {"name": "xin1", "fullname": "test_obj_conv_2.Person1"},' +\
        ' "fullname": "test_obj_conv_2.Person"}, {"name": "xiao2", "p1": {"name": "xin2", ' +\
        '"fullname": "test_obj_conv_2.Person1"}, "fullname": "test_obj_conv_2.Person"}]', 'json dumps 2 error'
    p2_list = json.loads(json1, object_hook=Person.from_dict)
    assert p_list[0].__dict__['name'] == p2_list[0].__dict__['name'] \
        and p_list[0].__dict__['p1'].__dict__ == p2_list[0].__dict__['p1'].__dict__ \
        and p_list[1].__dict__['name'] == p2_list[1].__dict__['name'] \
        and p_list[1].__dict__['p1'].__dict__ == p2_list[1].__dict__['p1'].__dict__, 'json loads 2 error'
