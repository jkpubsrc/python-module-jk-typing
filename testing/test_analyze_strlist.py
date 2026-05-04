

import os
import typing

import jk_typing
import jk_utils
import jk_logging
import jk_json
import jk_prettyprintobj

import jk_typing
import jk_typing.checking




@jk_typing.checkFunctionSignature(bDebugComp=2, bDebugRuntime=False)
def someFunction1(someArg:typing.List[str]):
	return someArg
#

@jk_typing.checkFunctionSignature(bDebugComp=2, bDebugRuntime=False)
def someFunction2(someArg:list[str]):
	return someArg
#





def _dumpFunc(func, log:jk_logging.AbstractLogger):
	log.notice("@" * 120)
	log.notice("@@ " + str(func.orgName) + str(func.orgSignature))
	log.notice("@@")
	_debugInfoCompile = func.debugInfoCompile
	assert isinstance(_debugInfoCompile, jk_typing.DebugInfoCompile)
	_debugInfoCompile.dump(prefix="@@ ", printFunc=log.notice)
	log.notice("@@")
	log.notice("@" * 120)
#



with jk_logging.wrapMain() as log:

	# ----

	print()
	_dumpFunc(someFunction1, log)

	# ----

	print()
	_dumpFunc(someFunction2, log)

	# ----

	someFunction1([ "foo", "bar", ])

	someFunction2([ "foo", "bar", ])

	# ----

	print()


