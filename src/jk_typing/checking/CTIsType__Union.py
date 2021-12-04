

from .AbstractCTNode import AbstractCTNode





class CTIsType__Union(AbstractCTNode):

	################################################################################################################################
	## Constructor
	################################################################################################################################

	#
	# Constructor method.
	#
	def __init__(self, argName:str, sType:str, bDebug:bool, nestedCheckFuncs):
		self.argName = argName
		self.sType = sType
		self.bDebug = bDebug
		self.__nestedCheckFuncs = nestedCheckFuncs
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
		for f in self.__nestedCheckFuncs:
			if f.__call__(value):
				return True
		if self.bDebug:
			self._printCodeLocation(__file__)
		return False
	#

	def dump(self, prefix:str):
		print(prefix + "CTIsType__Union<( argName=" + repr(self.argName) + ", sType=" + repr(self.sType))
		print(prefix + "\t__nestedCheckFuncs=[")
		for x in self.__nestedCheckFuncs:
			x.dump(prefix + "\t\t")
		print(prefix + "\t]")
		print(prefix + ")>")
	#

#







