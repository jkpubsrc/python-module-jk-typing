

import typing

from .AbstractCTNode import AbstractCTNode





class CTIsType__CheckItems_ExactTypeSequence(AbstractCTNode):

	################################################################################################################################
	## Constructor
	################################################################################################################################

	#
	# Constructor method.
	#
	# @param		str argName				(optional) The name of the argument. This information is used if an error occurs.
	# @param		str sType				(required) A string representation of the return type (for output).
	# @param		bool bDebug				(required) ???
	# @param		* expectedType			(required) A type specification object as returned by inspect
	#
	def __init__(self, argName:typing.Union[str,None], sType:str, nDebug:typing.Union[bool,int], expectedType:type, nestedCheckFuncList:typing.List[AbstractCTNode]):
		if argName is not None:
			assert isinstance(argName, str)
		assert isinstance(sType, str)
		assert isinstance(nDebug, (bool, int))
		# NOTE: In python 3.9 an object of typing.Callable is not a type - for what whatever reasons
		assert isinstance(expectedType, type) or isinstance(expectedType, tuple) or isinstance(expectedType, typing.Callable)

		# ----

		self.argName = argName
		self.sType = sType
		self.__nDebug = nDebug
		self.__expectedType = expectedType
		self.__nestedCheckFuncList = nestedCheckFuncList
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
			# not the right type
			if self.__nDebug:
				self._printCodeLocation(__file__)
			return False

		if len(value) != len(self.__nestedCheckFuncList):
			# sequence specified has invalid length
			if self.__nDebug:
				self._printCodeLocation(__file__)
			return False

		for v, nestedCheckFunc in zip(value, self.__nestedCheckFuncList):
			if not nestedCheckFunc.__call__(v):
				if self.__nDebug:
					self._printCodeLocation(__file__)
				return False

		return True
	#

	def _dump(self, prefix:str, printFunc:typing.Callable):
		printFunc(prefix + "CTIsType__CheckItems_ExactTypeSequence<( argName=" + repr(self.argName) + ", sType=" + repr(self.sType))
		printFunc(prefix + "\t__expectedType=" + repr(self.__expectedType))
		printFunc(prefix + "\t__nestedCheckFuncList=[")
		for nestedCheckFunc in self.__nestedCheckFuncList:
			nestedCheckFunc._dump(prefix + "\t\t", printFunc)
		printFunc(prefix + "\t]")
		printFunc(prefix + ")>")
	#

#










