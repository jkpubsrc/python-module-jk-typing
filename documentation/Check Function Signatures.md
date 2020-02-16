Check Function Signatures
=========================

## Python Type Hints

Python nowadays provides capabilities to define the data types of values passed to functions and methods as well as the returned types. This is implemented by having so called "type hints" that possibly provide this information for a Python intepreter.

This feature has a great benefit: Similar to real programming languages this would allow interpreters to detect erroneous method calls quite early. If the wrong data types are passed to a function the interpreter could use these type hints to detect these errors (and in consequence: complain). Unfortunately this feature is not used by Python interpreters nowadays.

And there is a reason for that. It would break with the concept of "duck typing" used in Python. Duck typing is the idea that Python code should not check details about the data objects it processes but rather use the data objects in the way necessary for the implementation. The caller is responsible for passing data suitable for processing. This allows great flexibility: For example if a text string is ment to be processed character by character a function will have the greates flexibility if it just assumes it will receive a sequence of something that "feels" like a text string if processed, regardless of what it is by nature.

This flexibility has a drawback: As the caller of a function does often not know about the exact requirements, nor is there any automatic type checking involved at design time, this approach is very error prone. It results in the disadvantage that programmers can easily make mistakes that go unnoticed. The consequence of this approach is that extensive testing of software would be required in order to compensate for this disadvantage. Which is often not performed. Furthermore it seems to be unrealistic in general to assume that extensive testing would be done in Python programs.

## Best Practice

Duck typing is a nice feature. Interestingly most of the time functions will process floats, integers, matrices or similar data where clear semantics are expected that will almost always not be delivered by other data objects. Additionally most of the time there will never be a need to make use of duck typing and pass in other data types. Duck typing is interesting, but in practice it is rarely needed.

Is it worth to abandon type checking just to allow a feature that is not used very much? In practice we could benefit greatly from type checking as it improves the process of developing software by early detection of programming errors. In Python we would profit of such type checking. Therefore the author of these lines believes that a compromise should be made here: Use type checking where possible and use duck typing where necessary. This seems to be a good approach even if sometimes decisions between both approaches can't be made easily and sometimes can't even be taken.

## Function Decorator "checkFunctionSignature"

To use type checking this module provides a function decoration: `@checkFunctionSignature()`. Example:

```python
@checkFunctionSignature()
def intToStr(someInt:int) -> str:
	s = str(someInt)
	return s
```

If a function is decorated with `@checkFunctionSignature()` the function is wrapped with another function that performs type checking automatically whenever the wrapped function is called. In order to check types the wrapper will analyse the signature of the function invoked and complain if some errors are detected by raising an exception.

This approach allows programmers to selectively make use of type checking whereever they think it might be necessary.

This selective approach makes very much sense as this feature comes with a drawback: Type checking takes a bit of time as it is not implemented within the Python interpreter itself (where it would be implemented in fast machine code). While performance typically is not a real issue in some special cases this might impose a delay that is unwanted. Therefore it is good practice for developers to choose on their own when such a type checking should be performed. It might even be a good approach to first implement everything with type checking and then later on removing it from some areas of the code in the final software product.

## Capabilities of "checkFunctionSignature"

Currently `@checkFunctionSignature()` will perform type checking for all primitive data types as well as for unions. As there is not a uniform API for implementing this type checking in python, the current implementation is still a bit limited (which in consequence makes `jk_utils` "alpha", not "stable").

Please use this decorator nevertheless. If you run into any kinds of problems please contact the author of this software to have a look into it and extend the functionality.

## Future Work

In the future the type checking capabilities will be completed and extended. As this is quite a self-contained feature `@checkFunctionSignature()` might be factured out into an own module in the future. For now this decorator will reside here in module `jk_utils`.

































