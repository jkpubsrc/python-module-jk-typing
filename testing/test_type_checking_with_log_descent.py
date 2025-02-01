#!/usr/bin/python3

import datetime
import typing

from jk_typing import *

import jk_logging




DEBUGGING_ENABLED = True



# NOTE: Enabling/disabling is not yet implemented.
#print("isTypeCheckingEnabled = " + str(isTypeCheckingEnabled()))
#deactiveTypeChecking()
#print("isTypeCheckingEnabled = " + str(isTypeCheckingEnabled()))





class MyTest(object):

	@checkFunctionSignature(bDebug=DEBUGGING_ENABLED, logDescend="Descending ....")
	def someVoidMethodDescending(self, log:jk_logging.AbstractLogger) -> None:
		log.notice("--someVoidMethodDescending")
	#

	@checkFunctionSignature(bDebug=DEBUGGING_ENABLED)
	def someVoidMethodNotDescending(self, log:jk_logging.AbstractLogger) -> None:
		log.notice("--someVoidMethodNotDescending")
	#

#

@checkFunctionSignature(bDebug=DEBUGGING_ENABLED, logDescend="Descending ....")
def someVoidFunctionDescending(log:jk_logging.AbstractLogger) -> None:
	log.notice("--someVoidFunctionDescending")
#

@checkFunctionSignature(bDebug=DEBUGGING_ENABLED)
def someVoidFunctionNotDescending(log:jk_logging.AbstractLogger) -> None:
	log.notice("--someVoidFunctionNotDescending")
#

@checkFunctionSignature(bDebug=DEBUGGING_ENABLED, logDescend="Descending ....")
def someVoidFunctionDescendingWithError(log:jk_logging.AbstractLogger) -> None:
	raise Exception("--someVoidFunctionDescendingWithError")
#

@checkFunctionSignature(bDebug=DEBUGGING_ENABLED, logDescend="Descending ....")
def someFunctionWithCorrectReturnValue(log:jk_logging.AbstractLogger) -> int:
	return 123
#

@checkFunctionSignature(bDebug=DEBUGGING_ENABLED, logDescend="Descending ....")
def someFunctionWithIncorrectReturnValue(log:jk_logging.AbstractLogger) -> int:
	return "abc"
#








with jk_logging.wrapMain() as log:

	print("\n" + "@"*80)
	print("@@ someVoidFunctionNotDescending(..)")
	someVoidFunctionNotDescending(log)

	print("\n" + "@"*80)
	print("@@ someVoidFunctionDescending(..)")
	someVoidFunctionDescending(log)

	obj = MyTest()

	print("\n" + "@"*80)
	print("@@ obj.someVoidMethodNotDescending(..)")
	obj.someVoidMethodNotDescending(log)

	print("\n" + "@"*80)
	print("@@ obj.someVoidMethodDescending(..)")
	obj.someVoidMethodDescending(log)

	try:
		print("\n" + "@"*80)
		print("@@ someVoidFunctionDescendingWithError(..)")
		someVoidFunctionDescendingWithError(log)
	except:
		pass

	print("\n" + "@"*80)
	print("@@ someFunctionWithCorrectReturnValue(..)")
	someFunctionWithCorrectReturnValue(log)

	try:
		print("\n" + "@"*80)
		print("@@ someFunctionWithIncorrectReturnValue(..)")
		someFunctionWithIncorrectReturnValue(log)
	except ValueError as ee:
		log.error(ee)

	print("\n" + "@"*80)
	log.success("Success.")










