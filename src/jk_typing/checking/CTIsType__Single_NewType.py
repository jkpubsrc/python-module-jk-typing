

import typing

from .AbstractCTNode import AbstractCTNode







class CTIsType__Single_NewType(AbstractCTNode):

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
	def __init__(self, argName:typing.Union[str,None], sType:str, nDebug:typing.Union[bool,int], expectedType:typing.Callable):
		if argName is not None:
			assert isinstance(argName, str)
		assert isinstance(sType, str)
		assert isinstance(nDebug, (bool, int))
		# NOTE: In python 3.9 an object of typing.Callable is not a type - for what whatever reasons
		#print("{{{{", type(expectedType), "@@", expectedType, "}}}}")
		#assert isinstance(expectedType, typing.Callable)
		assert CTIsType__Single_NewType.isSingleNewType(expectedType)

		self.argName = argName
		self.sType = sType
		self.__nDebug = nDebug
		self.__expectedTypeName = expectedType.__name__
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
	def isSingleNewType(expectedType) -> None:
		if expectedType is None:
			return False
		
		# python 3.8
		if isinstance(expectedType, typing.Callable) and (expectedType.__module__ == "typing") and str(expectedType).startswith("<function NewType."):
			return True

		# python 3.10
		if isinstance(expectedType, typing.Callable) and (expectedType.__class__ == typing.NewType):
			return True

		return False
	#

	def __call__(self, value) -> bool:
		if value is None:
			if self.__nDebug:
				self._printCodeLocation(__file__)
			return False

		presentedTypeStr = type(value).__name__
		ret = presentedTypeStr == self.__expectedTypeName
		if ret and self.__nDebug:
			self._printCodeLocation(__file__)
		return ret
	#

	def _dump(self, prefix:str, printFunc:typing.Callable):
		printFunc(prefix + "CTIsType__Single_NewType<( argName=" + repr(self.argName) + ", sType=" + repr(self.sType))
		printFunc(prefix + "\t__expectedTypeName=" + repr(self.__expectedTypeName))
		printFunc(prefix + ")>")
	#

#








