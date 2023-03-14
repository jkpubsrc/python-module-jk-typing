

import typing

from .AbstractCTNode import AbstractCTNode







class CTIsType__Single_None(AbstractCTNode):

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
	def __init__(self, argName:typing.Union[str,None], sType:str, nDebug:typing.Union[bool,int]):
		if argName is not None:
			assert isinstance(argName, str)
		assert isinstance(sType, str)
		assert isinstance(nDebug, (bool, int))
		# NOTE: In python 3.9 an object of typing.Callable is not a type - for what whatever reasons
		#print("{{{{", type(expectedType), "@@", expectedType, "}}}}")

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

	@staticmethod
	def isSingleNone(expectedType) -> None:
		return expectedType is type(None)
	#

	def __call__(self, value) -> bool:
		if value is None:
			return True

		if self.__nDebug:
			self._printCodeLocation(__file__)
		return False
	#

	def _dump(self, prefix:str, printFunc:typing.Callable):
		printFunc(prefix + "CTIsType__Single_None<( argName=" + repr(self.argName) + ", sType=" + repr(self.sType))
		printFunc(prefix + ")>")
	#

#








