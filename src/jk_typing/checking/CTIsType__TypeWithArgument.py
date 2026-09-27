

import typing

import jk_prettyprintobj

from .AbstractCTNode import AbstractCTNode







class CTIsType__TypeWithArgument(AbstractCTNode):

	################################################################################################################################
	## Constructor
	################################################################################################################################

	#
	# Constructor method.
	#
	# @param		str argName					(optional) The name of the argument. This information is used if an error occurs.
	# @param		str sType					(required) A string representation of the return type (for output).
	# @param		bool bDebug					(required) ???
	# @param		type expectedSubclassType	(required) The class the argument value must be a subclass of.
	# 											This is a type specification object as returned by inspect.
	#
	def __init__(self, argName:str|None, sType:str, nDebug:bool|int, expectedSubclassType:type):
		if argName is not None:
			assert isinstance(argName, str)
		assert isinstance(sType, str)
		assert isinstance(nDebug, (bool, int))
		assert isinstance(expectedSubclassType, type)

		self.argName = argName
		self.sType = sType
		self.__nDebug = nDebug
		self.__expectedSubclassType = expectedSubclassType
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
		ctx.dumpVar("__expectedSubclassType", self.__expectedSubclassType)
	#

	################################################################################################################################
	## Public Methods
	################################################################################################################################

	def __call__(self, value) -> bool:
		if not isinstance(value, type):
			if self.__nDebug:
				self._printCodeLocation(__file__, False)
			return False

		if issubclass(value, self.__expectedSubclassType):
			return True

		if self.__nDebug:
			self._printCodeLocation(__file__, False)
		return False
	#

#








