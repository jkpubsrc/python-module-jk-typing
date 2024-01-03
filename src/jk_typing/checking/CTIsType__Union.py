

import typing

from .AbstractCTNode import AbstractCTNode





class CTIsType__Union(AbstractCTNode):

	################################################################################################################################
	## Constructor
	################################################################################################################################

	#
	# Constructor method.
	#
	def __init__(self, argName:typing.Union[str,None], sType:str, nDebug:typing.Union[bool,int], nestedAlternativeCheckFuncs:typing.Union[tuple,list]):
		if argName is not None:
			assert isinstance(argName, str)
		assert isinstance(sType, str)
		assert isinstance(nDebug, (bool, int))
		assert isinstance(nestedAlternativeCheckFuncs, (tuple,list))
		for v in nestedAlternativeCheckFuncs:
			if v is None:
				print(">>>> argName =", argName)
				print(">>>> nestedAlternativeCheckFuncs =", nestedAlternativeCheckFuncs)
				raise AssertionError("nestedAlternativeCheckFuncs contains None!")

		# ----

		self.argName = argName
		self.sType = sType
		self.__nDebug = nDebug
		self.__nestedAlternativeCheckFuncs = nestedAlternativeCheckFuncs
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
		for f in self.__nestedAlternativeCheckFuncs:
			if f.__call__(value):
				return True
		if self.__nDebug:
			self._printCodeLocation(__file__, False)
		return False
	#

	def _dump(self, prefix:str, printFunc:typing.Callable):
		printFunc(prefix + "CTIsType__Union<( argName=" + repr(self.argName) + ", sType=" + repr(self.sType))
		printFunc(prefix + "\t__nestedAlternativeCheckFuncs=[")
		for x in self.__nestedAlternativeCheckFuncs:
			x._dump(prefix + "\t\t", printFunc)
		printFunc(prefix + "\t]")
		printFunc(prefix + ")>")
	#

#







