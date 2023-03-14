

import typing

from .AbstractCTNode import AbstractCTNode





class CTIsType__CheckItems_AllTheSameType(AbstractCTNode):

	################################################################################################################################
	## Constructor
	################################################################################################################################

	#
	# Constructor method.
	#
	def __init__(self, argName:typing.Union[str,None], sType:str, nDebug:typing.Union[bool,int], expectedType, nestedCheckFunc):
		if argName is not None:
			assert isinstance(argName, str)
		assert isinstance(sType, str)
		assert isinstance(nDebug, (bool, int))
		assert expectedType is not None
		assert nestedCheckFunc is not None

		# ----

		self.argName = argName
		self.sType = sType
		self.__nDebug = nDebug
		self.__expectedType = expectedType
		self.__nestedCheckFunc = nestedCheckFunc
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
			if self.__nDebug:
				self._printCodeLocation(__file__)
			return False
		for v in value:
			if not self.__nestedCheckFunc.__call__(v):
				if self.__nDebug:
					self._printCodeLocation(__file__)
				return False
		return True
	#

	def _dump(self, prefix:str, printFunc:typing.Callable):
		printFunc(prefix + "CTIsType__CheckItems_AllTheSameType<( argName=" + repr(self.argName) + ", sType=" + repr(self.sType))
		printFunc(prefix + "\t__expectedType=" + repr(self.__expectedType))
		printFunc(prefix + "\t__nestedCheckFunc=")
		self.__nestedCheckFunc._dump(prefix + "\t\t", printFunc)
		printFunc(prefix + ")>")
	#

#










