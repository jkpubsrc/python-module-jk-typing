

import typing

import jk_prettyprintobj

from .AbstractCTNode import AbstractCTNode




class CTAlwaysTrue(AbstractCTNode):

	################################################################################################################################
	## Constructor
	################################################################################################################################

	#
	# Constructor method.
	#
	def __init__(self, argName:str|None, sType:str, nDebug:bool|int):
		if argName is not None:
			assert isinstance(argName, str)
		assert isinstance(sType, str)
		assert isinstance(nDebug, (bool, int))

		# ----

		self.argName = argName
		self.sType = sType
		self.__nDebug = nDebug
	#

	################################################################################################################################
	## Public Properties
	################################################################################################################################

	################################################################################################################################
	## Helper Methods
	################################################################################################################################

	def _dump(self, ctx:jk_prettyprintobj.DumpCtx):
		ctx.dumpVar("argName", self.argName)
		ctx.dumpVar("sType", self.sType)
	#

	################################################################################################################################
	## Public Methods
	################################################################################################################################

	def __call__(self, value) -> bool:
		return True
	#

	# def _dump(self, prefix:str, printFunc:typing.Callable):
	# 	printFunc(prefix + "CTAlwaysTrue<( argName=" + repr(self.argName) + ", sType=" + repr(self.sType))
	# 	printFunc(prefix + ")>")
	# #

#







