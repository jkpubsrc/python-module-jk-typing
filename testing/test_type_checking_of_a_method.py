#!/usr/bin/python3

import datetime
import typing

from jk_typing import *

import jk_logging



DEBUGGING_ENABLED = False



# NOTE: Enabling/disabling is not yet implemented.
#print("isTypeCheckingEnabled = " + str(isTypeCheckingEnabled()))
#deactiveTypeChecking()
#print("isTypeCheckingEnabled = " + str(isTypeCheckingEnabled()))





class MyTest(object):

	@checkFunctionSignature(bDebug = DEBUGGING_ENABLED, bDebugComp = DEBUGGING_ENABLED)
	def someFunction(self, a:bool, b:int, c:str) -> bool:
		return False
	#

	@checkFunctionSignature(bDebug = DEBUGGING_ENABLED, bDebugComp = DEBUGGING_ENABLED)
	def someFunc_crazy(self, a, b:int, c:datetime.date, *args, **kwargs) -> None:
		pass
	#

	@checkFunctionSignature(bDebug = DEBUGGING_ENABLED, bDebugComp = DEBUGGING_ENABLED)
	def someFunc_list(self, a:typing.List[int]) -> bool:
		return True
	#

	@checkFunctionSignature(bDebug = DEBUGGING_ENABLED, bDebugComp = DEBUGGING_ENABLED)
	def someFunc_tuple(self, a:typing.Tuple[int]) -> bool:
		return True
	#

	@checkFunctionSignature(bDebug = DEBUGGING_ENABLED, bDebugComp = DEBUGGING_ENABLED)
	def someFunc_set(self, a:typing.Set[int]) -> bool:
		return True
	#

	@checkFunctionSignature(bDebug = DEBUGGING_ENABLED, bDebugComp = DEBUGGING_ENABLED)
	def someFunc_frozenset(self, a:typing.FrozenSet[int]) -> bool:
		return True
	#

	@checkFunctionSignature(bDebug = DEBUGGING_ENABLED, bDebugComp = DEBUGGING_ENABLED)
	def someFunc_dict(self, a:typing.Dict[str,int]) -> bool:
		return True
	#

	@checkFunctionSignature(bDebug = DEBUGGING_ENABLED, bDebugComp = DEBUGGING_ENABLED)
	def someFunc_union(self, a:typing.Union[str,int]) -> bool:
		return True
	#

	@checkFunctionSignature(bDebug = DEBUGGING_ENABLED, bDebugComp = DEBUGGING_ENABLED)
	def someVoidFunction(self, a:str) -> None:
		b = a + "something"
	#

	@checkFunctionSignature(bDebug = DEBUGGING_ENABLED, bDebugComp = DEBUGGING_ENABLED)
	def someVoidFunctionErr(self, a:str) -> None:
		b = a + "something"
		return "foobar"
	#

	@checkFunctionSignature(bDebug = DEBUGGING_ENABLED, bDebugComp = DEBUGGING_ENABLED)
	def someVoidFunctionX(self) -> None:
		pass
	#

#







def runTest(someFunction, testArgs, log:jk_logging.AbstractLogger):
	print("\n" + "#" * 80)

	print("#### " + str(someFunction.orgQualName) + "()")
	try:
		result = someFunction(*testArgs)
		#print("result=" + str(result))
	except Exception as ee:
		log.exception(ee)

	print("#" * 80 + "\n")
#



with jk_logging.wrapMain() as log:
	obj = MyTest()

	#obj.someVoidFunctionX()
	runTest(obj.someVoidFunctionX, [], log)

	runTest(obj.someFunction, [ True, 123, "123" ], log)

	#runTest(obj.someFunc_crazy, [ True, 123, "123" ], log)
	runTest(obj.someFunction, [ True, True, "123" ], log)
	runTest(obj.someFunc_list, [ [123] ], log)
	runTest(obj.someFunc_tuple, [ (123,) ], log)
	runTest(obj.someFunc_set, [ set((123,)) ], log)
	runTest(obj.someFunc_frozenset, [ frozenset((123,)) ], log)
	runTest(obj.someFunc_dict, [ {"x": 123 } ], log)
	runTest(obj.someFunc_union, [ 123 ], log)

	#runTest(obj.someVoidFunction, [ "foo" ], log)
	#runTest(obj.someVoidFunction, [ 123 ], log)
	#runTest(obj.someVoidFunctionErr, [ "foo" ], log)













