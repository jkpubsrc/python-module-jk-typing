

import os
import typing

#import jk_logging
import jk_testing2 as t

import jk_typing





DEBUGGING_ENABLED_RUNTIME = False
DEBUGGING_ENABLED_COMPILE_TIME = True

@jk_typing.checkFunctionSignature(bDebug=DEBUGGING_ENABLED_RUNTIME, bDebugComp=DEBUGGING_ENABLED_COMPILE_TIME)
def someFunction_bool(someArg:bool) -> bool:
	return someArg
#

@jk_typing.checkFunctionSignature(bDebug=DEBUGGING_ENABLED_RUNTIME, bDebugComp=DEBUGGING_ENABLED_COMPILE_TIME)
def someFunction_boolOrStr(someArg:bool) -> bool|str:
	return someArg
#



TEST_VECTOR:typing.List[t.VectorData] = [
	t.VectorData( (someFunction_bool, True), None, None ),
	t.VectorData( (someFunction_boolOrStr, True), None, None ),
]





@t.TestGroup(
	testCaseOrder=t.EnumTestCaseOrder.AS_DEFINED
)
class testcase_single_bool(object):

	################################################################################################################################
	## Constants
	################################################################################################################################

	################################################################################################################################
	## Constructor
	################################################################################################################################

	def __init__(self) -> None:
		pass
	#

	################################################################################################################################
	## Helper Methods
	################################################################################################################################

	################################################################################################################################
	## Test Init
	################################################################################################################################

	@t.InitializeTests()
	def init(self, ctx:t.TestContext):
		pass
	#

	################################################################################################################################
	## Test Methods
	################################################################################################################################

	@t.TestCase()
	def test_1(self, ctx:t.TestContext):
		#io2 = jk_simpleexec.SimpleIOStd()
		#t.Assert.isTrue(self.__io == io2)
		pass
	#

	@t.VectorTestCase(
		dataProvider=TEST_VECTOR,
		description="This is test"
	)
	def vtest_1(self, ctx:t.TestContext, testInput:tuple):
		someFunction, *testArgs = testInput
		assert callable(someFunction)

		# ----

		ctx.log.notice("@" * 120)
		ctx.log.notice("@@ " + str(someFunction.orgName) + str(someFunction.orgSignature))
		ctx.log.notice("@@")
		_debugInfoCompile = someFunction.debugInfoCompile
		assert isinstance(_debugInfoCompile, jk_typing.DebugInfoCompile)
		_debugInfoCompile.dump(prefix="@@ ", printFunc=ctx.log.notice)
		ctx.log.notice("@@")
		ctx.log.notice("@" * 120)

		# ----

		if _debugInfoCompile.warnings:
			t.Assert.fail("There were compile errors or warnings!")

		bSuccess = False
		try:
			result = someFunction(*testArgs)
			#print("result=" + str(result))
			bSuccess = True
		except Exception as ee:
			ctx.log.exception(ee)

		if not bSuccess:
			t.Assert.fail()

		# ----
	#

	################################################################################################################################
	## Test Deinit
	################################################################################################################################

	# @t.DeinitializeTests()
	# def deinit(self, ctx:t.TestContext):
	# 	pass
	# #

#


