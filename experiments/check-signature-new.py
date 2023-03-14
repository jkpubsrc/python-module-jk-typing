#!/usr/bin/python3

import sys
import typing
import pprint
import inspect

import jk_typing



print()
print()
print("Python:", sys.version)
print()
print()





@jk_typing.checkFunctionSignature(bDebug=True, bDebugComp=2)
def someFunction(
		vIntOrFloat1:typing.Union[int,float],
		vIntOrFloat2:int|float, 
	):
	pass
#





