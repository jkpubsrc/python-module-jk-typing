#!/usr/bin/python3

from _common import *



DEBUGGING_ENABLED = True





@jk_typing.checkFunctionSignature(bDebug=DEBUGGING_ENABLED, bDebugComp=DEBUGGING_ENABLED)
def someFunction(*someArg:int) -> typing.Tuple[int,str]:
	return 123, "abc"
#








with jk_logging.wrapMain() as log:
	runTest(someFunction, [ 123, 123 ], log)















