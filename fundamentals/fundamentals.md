#### method in python:

1) instanace method
2) class method
3) static method

#### self keyword --> represent instance/object from a class

_________________________________________________________________________________________________


How to call method:

1)className.methodName(...) --> methodName(params .....) --> without "self" param

--> if has "self" param it will display type error: "missing 1 required positional argument: 'self'"

2)use self or object from that class, but your method must contain "self" parameter. Otherwise your first parameter
will contain reference object/instance from this class. or it will display "takes 0 positional arguments but 1 was given"
