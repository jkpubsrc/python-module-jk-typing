#!/usr/bin/python3

import typing
import pprint

from PrintToFile import PrintToFile





FooBar = typing.NewType("FooBar", object)



def someFunction(fooBar:FooBar):
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
