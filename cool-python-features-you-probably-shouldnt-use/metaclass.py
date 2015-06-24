import re

""" Example of solving style religion wars by converting camelCase 
variable names to lower_snake_case """

def convert_to_snake_case(camelCase):
    return re.sub('([A-Z])', r'_\1', camelCase).lower()

class SnakeCase(type):
    def __new__(cls, name, bases, attrs):
        attrs.update((convert_to_snake_case(name), value)
                     for name, value in attrs.items())
        return super(SnakeCase, cls).__new__(cls, name,
                                             bases, attrs)

class Foo(object):
    __metaclass__ = SnakeCase

    def someFunction(self):
        print "called someFunction"

x = Foo()
x.someFunction()
x.some_function()

# metaclasses are cool because they inherit to subclasses,
# unlike monkeypatching or class decorators
class SubFoo(Foo):
    def someOtherFunction(self):
        print "called someOtherFunction"

y = SubFoo()
y.some_other_function()

