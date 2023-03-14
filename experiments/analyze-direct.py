#!/usr/bin/python3

import typing

from PrintToFile import PrintToFile





def someFunction(vInt:int, vStr:str, vAny, vFloatWithDefault:float = 12.345, *args, xStrWithDefault:str = "foo", xIntWithDefault:int = 123, **kwargs):
	pass
#



with PrintToFile(__file__, dirPath="out", fileExt=".txt") as f:

	for k in dir(someFunction):
		v = getattr(someFunction, k)
		f.print(k + " :: type =", type(v))
		lines = f.pformat(v).split("\n")
		for n, line in enumerate(lines):
			if n == 0:
				f.print("\tdata =", line)
			else:
				f.print("\t", line)
		f.print()

#
