#!/usr/bin/python3

import sys
import typing
import inspect

from PrintToFile import PrintToFile



with PrintToFile(__file__, dirPath="out", fileExt=".txt") as f:

	f.print()
	f.print()
	f.print("Python:", sys.version)
	f.print()
	f.print()





	def someFunction(
			vIntOrFloat1:typing.Union[int,float],
			vIntOrFloat2:int|float, 
			vStr:str,
			vList:list,
			vIntList:typing.List[int],
			vDict:dict,
			vStrIntDict:typing.Dict[str,int],
			vSet:set,
			vIntSet:typing.Set[int],
			vAny1,
			vAny2:typing.Any,
			vFloatWithDefault:float = 12.345,
			*args, xStrWithDefault:str = "foo",
			xIntWithDefault:int = 123,
			**kwargs
		) -> typing.Any:
		pass
	#





	_signature = inspect.signature(someFunction)

	#pprint.pprint(dir(_signature))




	def _printAnnotation(prefix:str, a):
		f.print(prefix + f.pformat(a))
	#

	def _printParameter(prefix:str, p:inspect.Parameter):
		f.print(prefix + repr(p))
		for k2 in dir(p):
			if k2 in [ "__doc__", "__le__", "__ge__", "__lt__", "__gt__", "__eq__", "__ne__", "__dir__", "__delattr__", "__hash__", "__init__", "__init_subclass__",
				"__new__", "__reduce__", "__reduce_ex__", "__repr__", "__setattr__", "__setstate__", "__sizeof__", "__format__", "__getattribute__", "__str__",
				"__subclasshook__", "_annotation", "_default", "_kind", "_name", "__slots__", "replace",
				"__class__",				# <class 'inspect.Parameter'>
				"__module__",				# 'inspect'
				"empty",					# Constant
				"POSITIONAL_ONLY",			# Constant: <_ParameterKind.POSITIONAL_ONLY: 0>
				"POSITIONAL_OR_KEYWORD",	# Constant: <_ParameterKind.POSITIONAL_OR_KEYWORD: 1>
				"VAR_POSITIONAL",			# Constant: <_ParameterKind.VAR_POSITIONAL: 2>				-- such as: *args
				"KEYWORD_ONLY",				# Constant: <_ParameterKind.KEYWORD_ONLY: 3>
				"VAR_KEYWORD",				# Constant: <_ParameterKind.VAR_KEYWORD: 4>					-- such as: **kwargs
				]:
				continue
			f.print(prefix + "|\t{} = {}".format(k2, repr(getattr(p, k2))))
		f.print(prefix + ">> annotation:", type(p.annotation), ":", repr(p.annotation))
	#



	f.print()
	f.print()

	f.print("parameters:")
	for k, v in _signature.parameters.items():
		f.print("\t" + k + ":")
		_printParameter("\t\t", v)

	f.print()
	f.print()

	f.print("return_annotation:")
	if _signature.return_annotation is inspect._empty:
		f.print("\t_empty")
	else:
		f.print("\t", repr(_signature.return_annotation))
		if _signature.return_annotation is not None:
			try:
				for i, x in enumerate(_signature.return_annotation):
					f.print("\t", i, "\t", x)
			except TypeError as ee:
				pass

#


