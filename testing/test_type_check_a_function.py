#!/usr/bin/python3



from typing import *
from jk_typing import *



print(isTypeCheckingEnabled())
deactiveTypeChecking()
print(isTypeCheckingEnabled())








@checkFunctionSignature(bDebug = True)
def someFunction(a:int, b:str) -> bool:
	return str(a) == b
#

@checkFunctionSignature(bDebug = True)
def someFunction2(a:List[int], b:str) -> bool:
	return str(a) == b
#




result = someFunction(123, "123")
print(result)

result = someFunction2([123], "[123]")
print(result)














