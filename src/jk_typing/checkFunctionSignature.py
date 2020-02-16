

import typing
import inspect



def __checkType(value, typeSpec):
	if typeSpec.__class__.__name__ == "_Union":
		#print(">>", typeSpec.__origin__ is Union)
		#print(">>>", typeSpec.__args__)
		return isinstance(value, typeSpec.__args__)
	else:
		return isinstance(value, typeSpec)
#



# this is the annotation wrapper that receives arguments and returns the function that does the wrapping
def checkFunctionSignature(bDebug:bool = False):
	assert isinstance(bDebug, bool)

	if bDebug:

		# this function is executed for every function definition
		def _wrap_the_function(fn):
			annotations = typing.get_type_hints(fn)

			# this function is executed every time the function is invoked.
			def wrapped(*args, **kwargs):
				print(fn.__qualname__ + "()")

				sig = inspect.signature(fn).bind(*args, **kwargs)
				for k, v in sig.arguments.items():
					typeSpec = annotations.get(k)
					if typeSpec is not None:
						if not __checkType(v, typeSpec):
							print("\targument " + repr(k) + ": " + str(typeSpec) + "  =>  ✖")
							raise ValueError("Argument " + repr(k) + " for " + fn.__name__ + "() is of type '" + repr(type(v)) + "' which does not match '" + repr(typeSpec) + "' as expected!")
						else:
							print("\targument " + repr(k) + ": " + str(typeSpec) + "  =>  ✔")
					else:
						print("\targument " + repr(k) + ": no specification")

				ret = fn(*args, **kwargs)

				bHasReturnAnnotation = None
				if isinstance(sig.signature.return_annotation, type):
					bHasReturnAnnotation = sig.signature.return_annotation.__name__ is "_empty"
				else:
					bHasReturnAnnotation = False

				if not bHasReturnAnnotation:
					typeSpec = sig.signature.return_annotation
					if not __checkType(ret, typeSpec):
						print("\treturn value: " + str(typeSpec) + "  =>  ✖")
						raise ValueError(fn.__name__ + "() returned invalid type: " + repr(type(ret)))
					else:
						print("\treturn value: " + str(typeSpec) + "  =>  ✔")
				else:
					print("\treturn value: no specification")

				return ret
			#

			return wrapped
		#

	else:

		# this function is executed for every function definition
		def _wrap_the_function(fn):
			annotations = typing.get_type_hints(fn)

			# this function is executed every time the function is invoked.
			def wrapped(*args, **kwargs):

				sig = inspect.signature(fn).bind(*args, **kwargs)
				for k, v in sig.arguments.items():
					typeSpec = annotations.get(k)
					if typeSpec is not None:
						if not __checkType(v, typeSpec):
							raise ValueError("Argument " + repr(k) + " for " + fn.__name__ + "() is of type '" + repr(type(v)) + "' which does not match '" + repr(typeSpec) + "' as expected!")

				ret = fn(*args, **kwargs)

				bHasReturnAnnotation = None
				if isinstance(sig.signature.return_annotation, type):
					bHasReturnAnnotation = sig.signature.return_annotation.__name__ is "_empty"
				else:
					bHasReturnAnnotation = False

				if not bHasReturnAnnotation:
					typeSpec = sig.signature.return_annotation
					if not __checkType(ret, typeSpec):
						raise ValueError(fn.__name__ + "() returned invalid type: " + repr(type(ret)))

				return ret
			#

			return wrapped
		#

	return _wrap_the_function
#





