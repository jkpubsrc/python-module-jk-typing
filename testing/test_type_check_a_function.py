#!/usr/bin/python3




from jk_typing import *




@checkFunctionSignature(bDebug = True)
def someFunction(a:int, b:str) -> bool:
	return str(a) == b
#




result = someFunction(123, "123")
print(result)














