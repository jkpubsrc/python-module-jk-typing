#!/usr/bin/python3

from _common import *



DEBUGGING_ENABLED = True





@jk_typing.checkFunctionSignature(bDebug=DEBUGGING_ENABLED, bDebugComp=DEBUGGING_ENABLED)
def someFunction(someArg:typing.Dict[str,str]) -> typing.Dict[str,str]:
	return someArg
#








with jk_logging.wrapMain() as log:
	runTest(someFunction, [ { "foo": "bar" } ], log)















