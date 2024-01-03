

import typing

from .AbstractCTNode import AbstractCTNode





class CTIsNone(AbstractCTNode):

	################################################################################################################################
	## Constructor
	################################################################################################################################

	#
	# Constructor method.
	#
	def __init__(self, argName:typing.Union[str,None], sType:str, nDebug:typing.Union[bool,int]):
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

	################################################################################################################################
	## Public Methods
	################################################################################################################################

	def __call__(self, value) -> bool:
		b = value is None
		if not b and self.__nDebug:
			self._printCodeLocation(__file__, b)
		return b
	#

	def _dump(self, prefix:str, printFunc:typing.Callable):
		printFunc(prefix + "CTIsNone<( argName=" + repr(self.argName) + ", sType=" + repr(self.sType))
		printFunc(prefix + ")>")
	#

#




