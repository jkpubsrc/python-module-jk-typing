

import os
import typing

#import jk_logging
import jk_testing2 as t

import jk_typing







DEBUGGING_ENABLED_RUNTIME = False



# --------------------------------------------------------------------------------------------------------------------------------

@jk_typing.checkFunctionSignature(bDebug=DEBUGGING_ENABLED_RUNTIME, bDebugComp=True)
def someFunction_any1(someArg):
	return someArg
#

@jk_typing.checkFunctionSignature(bDebug=DEBUGGING_ENABLED_RUNTIME, bDebugComp=True)
def someFunction_any2(someArg:typing.Any):
	return someArg
#

@jk_typing.checkFunctionSignature(bDebug=DEBUGGING_ENABLED_RUNTIME, bDebugComp=True)
def someFunction_any3(someArg:typing.Any) -> typing.Any:
	return someArg
#

# --------------------------------------------------------------------------------------------------------------------------------

@jk_typing.checkFunctionSignature(bDebug=DEBUGGING_ENABLED_RUNTIME, bDebugComp=True)
def someFunction_bool(someArg:bool) -> bool:
	return someArg
#

@jk_typing.checkFunctionSignature(bDebug=DEBUGGING_ENABLED_RUNTIME, bDebugComp=True)
def someFunction_boolOrStrRet(someArg:bool) -> bool|str:
	return someArg
#

@jk_typing.checkFunctionSignature(bDebug=DEBUGGING_ENABLED_RUNTIME, bDebugComp=True)
def someFunction_boolOrStrArg(someArg:bool|str) -> bool|str:
	return someArg
#

@jk_typing.checkFunctionSignature(bDebug=DEBUGGING_ENABLED_RUNTIME, bDebugComp=True)
def someFunction_boolOpt1(someArg:typing.Union[bool,None]) -> bool:
	return someArg
#

@jk_typing.checkFunctionSignature(bDebug=DEBUGGING_ENABLED_RUNTIME, bDebugComp=True)
def someFunction_boolOpt2(someArg:bool|None) -> bool:
	return someArg
#

@jk_typing.checkFunctionSignature(bDebug=DEBUGGING_ENABLED_RUNTIME, bDebugComp=True)
def someFunction_boolOpt3(someArg:typing.Optional[bool]) -> bool:
	return someArg
#

@jk_typing.checkFunctionSignature(bDebug=DEBUGGING_ENABLED_RUNTIME, bDebugComp=True)
def someFunction_boolOpt4(someArg:bool|None = None) -> bool:
	return someArg
#

# --------------------------------------------------------------------------------------------------------------------------------

@jk_typing.checkFunctionSignature(bDebug=DEBUGGING_ENABLED_RUNTIME, bDebugComp=True)
def someFunction_int(someArg:int) -> int:
	return someArg
#

@jk_typing.checkFunctionSignature(bDebug=DEBUGGING_ENABLED_RUNTIME, bDebugComp=True)
def someFunction_intOrStrRet(someArg:int) -> int|str:
	return someArg
#

@jk_typing.checkFunctionSignature(bDebug=DEBUGGING_ENABLED_RUNTIME, bDebugComp=True)
def someFunction_intOrStrArg(someArg:int|str) -> int|str:
	return someArg
#

@jk_typing.checkFunctionSignature(bDebug=DEBUGGING_ENABLED_RUNTIME, bDebugComp=True)
def someFunction_intOpt1(someArg:typing.Union[int,None]) -> int:
	return someArg
#

@jk_typing.checkFunctionSignature(bDebug=DEBUGGING_ENABLED_RUNTIME, bDebugComp=True)
def someFunction_intOpt2(someArg:int|None) -> int:
	return someArg
#

@jk_typing.checkFunctionSignature(bDebug=DEBUGGING_ENABLED_RUNTIME, bDebugComp=True)
def someFunction_intOpt3(someArg:typing.Optional[int]) -> int:
	return someArg
#

# --------------------------------------------------------------------------------------------------------------------------------

@jk_typing.checkFunctionSignature(bDebug=DEBUGGING_ENABLED_RUNTIME, bDebugComp=True)
def someFunction_strIntDict1a(someArg:dict[str,int]) -> dict[str,int]:
	return someArg
#

@jk_typing.checkFunctionSignature(bDebug=DEBUGGING_ENABLED_RUNTIME, bDebugComp=True)
def someFunction_strIntDict1b(someArg:typing.Dict[str,int]) -> dict[str,int]:
	return someArg
#

@jk_typing.checkFunctionSignature(bDebug=DEBUGGING_ENABLED_RUNTIME, bDebugComp=True)
def someFunction_strIntDictOpt1a(someArg:typing.Union[dict[str,int],None]) -> dict[str,int]:
	return someArg
#

@jk_typing.checkFunctionSignature(bDebug=DEBUGGING_ENABLED_RUNTIME, bDebugComp=True)
def someFunction_strIntDictOpt1b(someArg:typing.Union[typing.Dict[str,int],None]) -> dict[str,int]:
	return someArg
#

@jk_typing.checkFunctionSignature(bDebug=DEBUGGING_ENABLED_RUNTIME, bDebugComp=True)
def someFunction_strIntDictOpt2a(someArg:dict[str,int]|None) -> dict[str,int]:
	return someArg
#

@jk_typing.checkFunctionSignature(bDebug=DEBUGGING_ENABLED_RUNTIME, bDebugComp=True)
def someFunction_strIntDictOpt2b(someArg:typing.Dict[str,int]|None) -> dict[str,int]:
	return someArg
#

@jk_typing.checkFunctionSignature(bDebug=DEBUGGING_ENABLED_RUNTIME, bDebugComp=True)
def someFunction_strIntDictOpt3a(someArg:typing.Optional[dict[str,int]]) -> dict[str,int]:
	return someArg
#

@jk_typing.checkFunctionSignature(bDebug=DEBUGGING_ENABLED_RUNTIME, bDebugComp=True)
def someFunction_strIntDictOpt3b(someArg:typing.Optional[typing.Dict[str,int]]) -> dict[str,int]:
	return someArg
#

# --------------------------------------------------------------------------------------------------------------------------------









TEST_VECTOR_PARSING:typing.List[t.VectorData] = [

	t.VectorData( (someFunction_any1, True), True, None ),
	t.VectorData( (someFunction_any2, True), True, None ),
	t.VectorData( (someFunction_any3, True), True, None ),

	t.VectorData( (someFunction_bool, True), True, None ),
	t.VectorData( (someFunction_boolOrStrRet, True), True, None ),
	t.VectorData( (someFunction_boolOrStrArg, True), True, None ),
	t.VectorData( (someFunction_boolOpt1, True), True, None ),
	t.VectorData( (someFunction_boolOpt2, True), True, None ),
	t.VectorData( (someFunction_boolOpt3, True), True, None ),
	t.VectorData( (someFunction_boolOpt4, True), True, None ),				# TODO: here a superfluous alternative is added!
	
	t.VectorData( (someFunction_int, 123), 123, None ),
	t.VectorData( (someFunction_intOrStrRet, 123), 123, None ),
	t.VectorData( (someFunction_intOrStrArg, 123), 123, None ),
	t.VectorData( (someFunction_intOpt1, 123), 123, None ),
	t.VectorData( (someFunction_intOpt2, 123), 123, None ),
	t.VectorData( (someFunction_intOpt3, 123), 123, None ),
	
	t.VectorData( (someFunction_strIntDict1a, {}), {}, None ),
	t.VectorData( (someFunction_strIntDict1b, {}), {}, None ),
	t.VectorData( (someFunction_strIntDictOpt1a, {}), {}, None ),
	t.VectorData( (someFunction_strIntDictOpt1b, {}), {}, None ),
	t.VectorData( (someFunction_strIntDictOpt2a, {}), {}, None ),
	t.VectorData( (someFunction_strIntDictOpt2b, {}), {}, None ),
	t.VectorData( (someFunction_strIntDictOpt3a, {}), {}, None ),
	t.VectorData( (someFunction_strIntDictOpt3b, {}), {}, None ),

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

	# @t.TestCase()
	# def test_1(self, ctx:t.TestContext):
	# 	#io2 = jk_simpleexec.SimpleIOStd()
	# 	#t.Assert.isTrue(self.__io == io2)
	# 	pass
	# #

	@t.VectorTestCase(
		dataProvider=TEST_VECTOR_PARSING,
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

		return someFunction(*testArgs)
	#

	################################################################################################################################
	## Test Deinit
	################################################################################################################################

	# @t.DeinitializeTests()
	# def deinit(self, ctx:t.TestContext):
	# 	pass
	# #

#


