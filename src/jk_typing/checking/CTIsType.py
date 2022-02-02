

import typing

from .AbstractCTNode import AbstractCTNode







class CTIsType(AbstractCTNode):

	################################################################################################################################
	## Constructor
	################################################################################################################################

	#
	# Constructor method.
	#
	def __init__(self, argName:typing.Union[str,None], sType:str, bDebug:bool, expectedType):
		if argName is not None:
			assert isinstance(argName, str)
		assert isinstance(sType, str)
		assert isinstance(bDebug, bool)
		assert isinstance(expectedType, type) or isinstance(expectedType, tuple)

		self.argName = argName
		self.sType = sType
		self.bDebug = bDebug
		self.__expectedType = expectedType
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
		if not isinstance(value, self.__expectedType):
			if self.bDebug:
				self._printCodeLocation(__file__)
			return False
		return True
	#
	def dump(self, prefix:str):
		print(prefix + "CTIsType<( argName=" + repr(self.argName) + ", sType=" + repr(self.sType))
		print(prefix + "\t__expectedType=" + repr(self.__expectedType))
		print(prefix + ")>")
	#

#








