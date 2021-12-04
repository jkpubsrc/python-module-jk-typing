#!/usr/bin/python3

from _common import *



DEBUGGING_ENABLED = True

print()







@jk_typing.checkFunctionSignature(bDebug=DEBUGGING_ENABLED, bDebugComp=DEBUGGING_ENABLED)
def someFunction(someArg:int) -> int:
	return someArg
#








with jk_logging.wrapMain() as log:
	runTest(someFunction, [ 123 ], log)















