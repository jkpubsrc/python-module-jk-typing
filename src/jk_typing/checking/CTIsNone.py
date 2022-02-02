

from .AbstractCTNode import AbstractCTNode





class CTIsNone(AbstractCTNode):

	################################################################################################################################
	## Constructor
	################################################################################################################################

	#
	# Constructor method.
	#
	def __init__(self, argName:str, sType:str, bDebug:bool):
		self.argName = argName
		self.sType = sType
		self.bDebug = bDebug
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
		if not b and self.bDebug:
			self._printCodeLocation(__file__)
		return b
	#

	def dump(self, prefix:str):
		print(prefix + "CTIsNone<( argName=" + repr(self.argName) + ", sType=" + repr(self.sType))
		print(prefix + ")>")
	#

#



