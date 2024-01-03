

import typing

from .AbstractCTNode import AbstractCTNode





class CTIsDict(AbstractCTNode):

	################################################################################################################################
	## Constructor
	################################################################################################################################

	#
	# Constructor method.
	#
	def __init__(self, argName:typing.Union[str,None], sType:str, nDebug:typing.Union[bool,int], keyCheckFunc, valueCheckFunc):
		if argName is not None:
			assert isinstance(argName, str)
		assert isinstance(sType, str)
		assert isinstance(nDebug, (bool, int))
		assert keyCheckFunc is not None
		assert valueCheckFunc is not None

		# ----

		self.argName = argName
		self.sType = sType
		self.__nDebug = nDebug
		self.__keyCheckFunc = keyCheckFunc
		self.__valueCheckFunc = valueCheckFunc
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
		if not isinstance(value, dict):
			if self.__nDebug:
				self._printCodeLocation(__file__, False)
			return False
		for k, v in value.items():
			if not self.__keyCheckFunc.__call__(k):
				if self.__nDebug:
					self._printCodeLocation(__file__, False)
				return False
			if not self.__valueCheckFunc.__call__(v):
				if self.__nDebug:
					self._printCodeLocation(__file__, False)
				return False
		return True
	#
	def _dump(self, prefix:str, printFunc:typing.Callable):
		printFunc(prefix + "CTIsDict<( argName=" + repr(self.argName) + ", sType=" + repr(self.sType))
		printFunc(prefix + "\t__keyCheckFunc=")
		self.__keyCheckFunc._dump(prefix + "\t\t", printFunc)
		printFunc(prefix + "\t__valueCheckFunc=")
		self.__valueCheckFunc._dump(prefix + "\t\t", printFunc)
		printFunc(prefix + ")>")
	#

#







