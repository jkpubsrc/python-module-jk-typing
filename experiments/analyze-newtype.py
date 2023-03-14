#!/usr/bin/python3

import typing

from PrintToFile import PrintToFile




with PrintToFile(__file__, dirPath="out", fileExt=".txt") as f:

	FooBar = typing.NewType("FooBar", object)

	f.print(repr(FooBar))

	f.print()
	f.print()
	f.print()

	for k in dir(FooBar):
		v = getattr(FooBar, k)
		f.print(k + " :: type =", type(v))
		lines = f.pformat(v).split("\n")
		for n, line in enumerate(lines):
			if n == 0:
				f.print("\tdata =", line)
			else:
				f.print("\t", line)
		f.print()

#
