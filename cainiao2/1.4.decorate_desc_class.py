'''
说明: 所有对描述器属性(比如name, shares, price)的访问会被 __get__() 、__set__() 和 __delete__() 方法捕获到.
关键点: setattr(cls, name, Typed(name, expected_type)),将这个描述器(Typed)的实例作为类(Stock)属性放到一个类的定义中
详细: https://python3-cookbook.readthedocs.io/zh_CN/latest/c08/p09_create_new_kind_of_class_or_instance_attribute.html
'''
# Descriptor for a type-checked attribute


class Typed:
    def __init__(self, name, expected_type):
        self.name = name
        self.expected_type = expected_type

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]

    def __set__(self, instance, value):
        print('===', self.__dict__)
        if not isinstance(value, self.expected_type):
            raise TypeError('Expected ' + str(self.expected_type))
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]

# Class decorator that applies it to selected attributes


def typeassert(**kwargs):
    def decorate(cls):
        for name, expected_type in kwargs.items():
            # Attach a Typed descriptor to the class
            setattr(cls, name, Typed(name, expected_type))
        return cls
    return decorate

# Example use


@typeassert(name=str, shares=int, price=float)
class Stock:
    def __init__(self, name, shares, price):
        print(f'before set name')
        self.name = name
        print(f'after set name: {self.name}')
        self.shares = shares
        self.price = price


if __name__ == '__main__':
    s = Stock('1', 2, 3.0)
    print(s.__dict__['name'])
