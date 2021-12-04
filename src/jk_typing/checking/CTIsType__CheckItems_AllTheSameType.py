

from .AbstractCTNode import AbstractCTNode





class CTIsType__CheckItems_AllTheSameType(AbstractCTNode):

	################################################################################################################################
	## Constructor
	################################################################################################################################

	#
	# Constructor method.
	#
	def __init__(self, argName:str, sType:str, bDebug:bool, expectedType, nestedCheckFunc):
		self.argName = argName
		self.sType = sType
		self.bDebug = bDebug
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
			if self.bDebug:
				self._printCodeLocation(__file__)
			return False
		for v in value:
			if not self.__nestedCheckFunc.__call__(v):
				if self.bDebug:
					self._printCodeLocation(__file__)
				return False
		return True
	#
	def dump(self, prefix:str):
		print(prefix + "CTIsType__CheckItems_AllTheSameType<( argName=" + repr(self.argName) + ", sType=" + repr(self.sType))
		print(prefix + "\t__expectedType=" + repr(self.__expectedType))
		print(prefix + "\t__nestedCheckFunc=")
		self.__nestedCheckFunc.dump(prefix + "\t\t")
		print(prefix + ")>")
	#

#










