

import typing

from .AbstractCTNode import AbstractCTNode





class CTAlwaysTrue(AbstractCTNode):

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
		return True
	#

	def _dump(self, prefix:str, printFunc:typing.Callable):
		printFunc(prefix + "CTAlwaysTrue<( argName=" + repr(self.argName) + ", sType=" + repr(self.sType))
		printFunc(prefix + ")>")
	#

#







