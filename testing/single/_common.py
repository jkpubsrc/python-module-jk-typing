


import sys
import os
import typing

import jk_logging
import jk_typing

print("jk_typing version: " + jk_typing.__version__)
print()





NONE_TYPE = type(None)






def runTest(someFunction, testArgs, log:jk_logging.AbstractLogger):
	print("\n" + "#" * 80)

	bSuccess = False
	print("#### " + str(someFunction.orgName) + "()")
	try:
		result = someFunction(*testArgs)
		#print("result=" + str(result))
		bSuccess = True
	except Exception as ee:
		log.exception(ee)

	print("#" * 80 + "\n")

	if not bSuccess:
		sys.exit(1)
#












