#!/usr/bin/python3

from _common import *



DEBUGGING_ENABLED = True

print()







@jk_typing.checkFunctionSignature(bDebug=DEBUGGING_ENABLED, bDebugComp=DEBUGGING_ENABLED)
def someFunction(someArg:NONE_TYPE) -> None:
	return someArg
#








with jk_logging.wrapMain() as log:
	runTest(someFunction, [ None ], log)















