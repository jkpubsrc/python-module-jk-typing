

import os
import typing

import jk_typing
import jk_utils
import jk_logging
import jk_json
import jk_prettyprintobj

import jk_typing
import jk_typing.checking




@jk_typing.checkFunctionSignature(bDebugComp=True, bDebugRuntime=False)
def someFunction1(someArg:tuple[str]):
	return someArg
#





with jk_logging.wrapMain() as log:

	# ----

	data = [
		"foo",
		"bar",
	]

	someFunction1(tuple(data))

