#!/usr/bin/python3

from _common import *



DEBUGGING_ENABLED = True

print()







def foo():
	pass
#

@jk_typing.checkFunctionSignature(bDebug=DEBUGGING_ENABLED, bDebugComp=DEBUGGING_ENABLED)
def someFunction(someArg:typing.Callable) -> typing.Callable:
	return someArg
#








with jk_logging.wrapMain() as log:
	runTest(someFunction, [ foo ], log)















