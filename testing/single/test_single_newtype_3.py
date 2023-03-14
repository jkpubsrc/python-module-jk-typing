#!/usr/bin/python3

import typing

from _common import *



DEBUGGING_ENABLED = True

print()





FooBar = typing.NewType("FooBar", object)

class FooBar(object):
	def __init__(self) -> None:
		pass
	#
#

@jk_typing.checkFunctionSignature(bDebug=DEBUGGING_ENABLED, bDebugComp=DEBUGGING_ENABLED)
def someFunction(appName:str, log:jk_logging.AbstractLogger, userDBFilePath:str = None) -> FooBar:
	return FooBar()
#










with jk_logging.wrapMain() as log:
	runTest(someFunction, [ "foo", log ], log)















