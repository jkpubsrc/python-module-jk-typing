

import typing

from .AbstractCTNode import AbstractCTNode







class CTIsSequence(AbstractCTNode):

	################################################################################################################################
	## Constructor
	################################################################################################################################

	#
	# Constructor method.
	#
	# @param		str argName				(optional) The name of the argument. This information is used if an error occurs.
	# @param		str sType				(required) A string representation of the return type (for output).
	# @param		bool bDebug				(required) ???
	#
	def __init__(self, argName:typing.Union[str,None], sType:str, nDebug:typing.Union[bool,int]):
		if argName is not None:
			assert isinstance(argName, str)
		assert isinstance(sType, str)
		assert isinstance(nDebug, (bool, int))
		# NOTE: In python 3.9 an object of typing.Callable is not a type - for what whatever reasons

		# ----

		self.argName = argName
		self.sType = sType
		self.__nDebug = nDebug
		self.__expectedTypes = (tuple, list, range, dict, str, bytes, bytearray, set, frozenset)
	#

	################################################################################################################################
	## Public Properties
	################################################################################################################################

	################################################################################################################################
	## Helper Methods
	################################################################################################################################

	################################################################################################################################
	## Public Methods
	################################################################################################################################

	def __call__(self, value) -> bool:
		if isinstance(value, typing.Sequence):
			return True
		if self.__nDebug:
			self._printCodeLocation(__file__, False)
		return False
	#

	def _dump(self, prefix:str, printFunc:typing.Callable):
		printFunc(prefix + "CTIsSequence<( argName=" + repr(self.argName) + ", sType=" + repr(self.sType))
		printFunc(prefix + "\t__expectedTypes=" + repr(self.__expectedTypes))
		printFunc(prefix + ")>")
	#

#








