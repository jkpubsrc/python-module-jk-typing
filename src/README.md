jk_typing
==========

Introduction
------------

This module provides capabilities for type checking function arguments.

Please note that a full type check with this module is not possible, since this is fundamentally not possible due to limitiations of Python itself.

Information about this module can be found here:

* [github.org](https://github.com/jkpubsrc/python-module-jk-typing)
	* [Documentation](https://github.com/jkpubsrc/python-module-jk-typing/tree/master/documentation)
* [pypi.python.org](https://pypi.python.org/pypi/jk_typing)

Why this module?
----------------

Python nowadays is capable of managing type hints for function arguments and return values. Unfortunately Python does not perform type checking automatically. This module provides capabilities of performing type checking automatically.

For more details have a look at the [documentation](https://github.com/jkpubsrc/python-module-jk-typing/tree/master/documentation).

Requirements
------------

This module requires Python 3.7 or later. It can not be used on older releases of Python because of limitations of module `typing`.

Limitations of this module
--------------------------

Type checking is not implemented in pure Python. Therefore it is slower as if the Python interpreter would perform type checking itself. Additionally this module has not yet a complete implementation of all kinds of types. (This will change in the future, maybe with your help.)

For more details have a look at the [documentation](https://github.com/jkpubsrc/python-module-jk-typing/tree/master/documentation).

How to use this module
----------------------

### Import this module

Please include this module into your application using the following code:

```python
import jk_typing
```

### Define a function

Example:

```python
@checkFunctionSignature(bDebug = True)
def someFunction(a:int, b:str) -> bool:
	return str(a) == b
```

### Invoke the function (and perform type checking)

```python
result = someFunction(123, "123")
print(result)
```

Contact Information
-------------------

This work is Open Source. This enables you to use this work for free.

Please have in mind this also enables you to contribute. We, the subspecies of software developers, can create great things. But the more collaborate, the more fantastic these things can become. Therefore Feel free to contact the author(s) listed below, either for giving feedback, providing comments, hints, indicate possible collaborations, ideas, improvements. Or maybe for "only" reporting some bugs:

* Jürgen Knauth: jknauth@uni-goettingen.de, pubsrc@binary-overflow.de

License
-------

This software is provided under the following license:

* Apache Software License 2.0



