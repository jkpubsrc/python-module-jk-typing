#!/usr/bin/python3

import datetime
import typing

from jk_typing import *

import jk_logging

import jk_typing


DEBUGGING_ENABLED = False



# NOTE: Enabling/disabling is not yet implemented.
#print("isTypeCheckingEnabled = " + str(isTypeCheckingEnabled()))
#deactiveTypeChecking()
#print("isTypeCheckingEnabled = " + str(isTypeCheckingEnabled()))







@checkFunctionSignature(bDebug = DEBUGGING_ENABLED)
def someFunction(a:bool, b:int, c:str) -> bool:
	return False
#

@checkFunctionSignature(bDebug = DEBUGGING_ENABLED)
def someFunc_crazy(a, b:int, c:datetime.date, *args, **kwargs) -> None:
	pass
#

@checkFunctionSignature(bDebug = DEBUGGING_ENABLED)
def someFunc_list(a:typing.List[int]) -> bool:
	return True
#

@checkFunctionSignature(bDebug = DEBUGGING_ENABLED)
def someFunc_tuple(a:typing.Tuple[int]) -> bool:
	return True
#

@checkFunctionSignature(bDebug = DEBUGGING_ENABLED)
def someFunc_set(a:typing.Set[int]) -> bool:
	return True
#

@checkFunctionSignature(bDebug = DEBUGGING_ENABLED)
def someFunc_frozenset(a:typing.FrozenSet[int]) -> bool:
	return True
#

@checkFunctionSignature(bDebug = DEBUGGING_ENABLED)
def someFunc_dict(a:typing.Dict[str,int]) -> bool:
	return True
#

@checkFunctionSignature(bDebug = DEBUGGING_ENABLED)
def someFunc_union(a:typing.Union[str,int]) -> bool:
	return True
#

@checkFunctionSignature(bDebug = DEBUGGING_ENABLED)
def someVoidFunction(a:str) -> None:
	b = a + "something"
#

@checkFunctionSignature(bDebug = DEBUGGING_ENABLED)
def someVoidFunctionErr(a:str) -> None:
	b = a + "something"
	return "foobar"
#









def runTest(someFunction, testArgs, log:jk_logging.AbstractLogger):
	print("\n" + "#" * 80)

	print("#### " + str(someFunction.orgName) + "()")
	try:
		result = someFunction(*testArgs)
		#print("result=" + str(result))
	except Exception as ee:
		log.exception(ee)

	print("#" * 80 + "\n")
#



with jk_logging.wrapMain() as log:
	runTest(someFunction, [ True, 123, "123" ], log)
	#runTest(someFunc_crazy, [ True, 123, "123" ], log)
	runTest(someFunction, [ True, True, "123" ], log)
	runTest(someFunc_list, [ [123] ], log)
	runTest(someFunc_tuple, [ (123,) ], log)
	runTest(someFunc_set, [ set((123,)) ], log)
	runTest(someFunc_frozenset, [ frozenset((123,)) ], log)
	runTest(someFunc_dict, [ {"x": 123 } ], log)
	runTest(someFunc_union, [ 123 ], log)

	#runTest(someVoidFunction, [ "foo" ], log)
	#runTest(someVoidFunction, [ 123 ], log)
	#runTest(someVoidFunctionErr, [ "foo" ], log)













