

from .AbstractCTNode import AbstractCTNode





class CTIsType__CheckItems_ExactTypeSequence(AbstractCTNode):

	################################################################################################################################
	## Constructor
	################################################################################################################################

	#
	# Constructor method.
	#
	def __init__(self, argName:str, sType:str, bDebug:bool, expectedType, nestedCheckFuncList):
		self.argName = argName
		self.sType = sType
		self.bDebug = bDebug
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
			if self.bDebug:
				self._printCodeLocation(__file__)
			return False

		if len(value) != len(self.__nestedCheckFuncList):
			# sequence specified has invalid length
			if self.bDebug:
				self._printCodeLocation(__file__)
			return False

		for v, nestedCheckFunc in zip(value, self.__nestedCheckFuncList):
			if not nestedCheckFunc.__call__(v):
				if self.bDebug:
					self._printCodeLocation(__file__)
				return False

		return True
	#

	def dump(self, prefix:str):
		print(prefix + "CTIsType__CheckItems_ExactTypeSequence<( argName=" + repr(self.argName) + ", sType=" + repr(self.sType))
		print(prefix + "\t__expectedType=" + repr(self.__expectedType))
		print(prefix + "\t__nestedCheckFuncList=[")
		for nestedCheckFunc in self.__nestedCheckFuncList:
			nestedCheckFunc.dump(prefix + "\t\t\t")
		print(prefix + "\t]")
		print(prefix + ")>")
	#

#










