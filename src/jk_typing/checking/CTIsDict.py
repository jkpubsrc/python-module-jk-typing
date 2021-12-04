

from .AbstractCTNode import AbstractCTNode





class CTIsDict(AbstractCTNode):

	################################################################################################################################
	## Constructor
	################################################################################################################################

	#
	# Constructor method.
	#
	def __init__(self, argName:str, sType:str, bDebug:bool, keyCheckFunc, valueCheckFunc):
		self.argName = argName
		self.sType = sType
		self.bDebug = bDebug
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
			if self.bDebug:
				self._printCodeLocation(__file__)
			return False
		for k, v in value.items():
			if not self.__keyCheckFunc.__call__(k):
				if self.bDebug:
					self._printCodeLocation(__file__)
				return False
			if not self.__valueCheckFunc.__call__(v):
				if self.bDebug:
					self._printCodeLocation(__file__)
				return False
		return True
	#
	def dump(self, prefix:str):
		print(prefix + "CTIsDict<( argName=" + repr(self.argName) + ", sType=" + repr(self.sType))
		print(prefix + "\t__keyCheckFunc=")
		self.__keyCheckFunc.dump(prefix + "\t\t")
		print(prefix + "\t__valueCheckFunc=")
		self.__valueCheckFunc.dump(prefix + "\t\t")
		print(prefix + ")>")
	#

#







