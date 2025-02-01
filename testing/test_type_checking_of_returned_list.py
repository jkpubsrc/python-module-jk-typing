#!/usr/bin/python3



import os
import typing

import jk_typing
#import jk_utils
import jk_logging
import jk_json
import jk_prettyprintobj




class MyClass(object):

	pass

#



"""
class Foo:

	jk_typing.checkFunctionSignature(bDebug=True, bDebugComp=True)
	def do_return_list(self) -> typing.List[MyClass]:
		print("foo")
		ret = []
		ret.append(MyClass())
		return ret
	#

#
"""


class Bar(object):

	@jk_typing.checkFunctionSignature(bDebug=True, bDebugComp=True)
	def do_return_list(self) -> typing.List[str]:
		ret = []
		ret.append(MyClass())
		ret.append(123)
		return ret
	#

#



#foo = Foo()
bar = Bar()
x = bar.do_return_list()
print(x)


