

import typing

from .AbstractCTNode import AbstractCTNode







class CTIsType(AbstractCTNode):

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
	def __init__(self, argName:typing.Union[str,None], sType:str, nDebug:typing.Union[bool,int], expectedType:typing.Union[type,typing.Callable]):
		if argName is not None:
			assert isinstance(argName, str)
		assert isinstance(sType, str)
		assert isinstance(nDebug, (bool, int))
		# NOTE: In python 3.9 an object of typing.Callable is not a type - for what whatever reasons
		# print("{{{{", type(expectedType), "@@", expectedType, "}}}}")
		assert isinstance(expectedType, (type,typing.Callable))

		self.argName = argName
		self.sType = sType
		self.__nDebug = nDebug
		self.__expectedType = expectedType
	#

	################################################################################################################################
	## Public Properties
	################################################################################################################################

	################################################################################################################################
	## Helper Methods
	################################################################################################################################

	# @staticmethod
	# def __getFQN(o) -> str:
	# 	klass = o.__class__
	# 	module = klass.__module__
	# 	if module == 'builtins':
	# 		return klass.__qualname__ # avoid outputs like 'builtins.str'
	# 	return module + '.' + klass.__qualname__
	# #

	################################################################################################################################
	## Public Methods
	################################################################################################################################

	def __call__(self, value) -> bool:
		if value is None:
			# return only True if self.__expectedType is None
			return self.__expectedType is type(None)

		if isinstance(value, self.__expectedType):
			return True
	
		if self.__nDebug:
			self._printCodeLocation(__file__, False)
		return False
	#

	# def __call__(self, value) -> bool:
	# 	if value is None:
	# 		# return only True if self.__expectedType is None
	# 		return self.__expectedType is type(None)

	# 	if isinstance(self.__expectedType, type):
	# 		return self.____check_expectedTypeIsType(self.__expectedType, value)

	# 	if (self.__expectedType.__module__ == "typing") and str(self.__expectedType).startswith("<function NewType."):
	# 		return self.____check_expectedTypeIsNewType(self.__expectedType, value)

	# 	raise Exception("????expectedType: " + repr(self.__expectedType))
	# #

	def _dump(self, prefix:str, printFunc:typing.Callable):
		printFunc(prefix + "CTIsType<( argName=" + repr(self.argName) + ", sType=" + repr(self.sType))
		printFunc(prefix + "\t__expectedType=" + repr(self.__expectedType))
		printFunc(prefix + ")>")
	#

#








