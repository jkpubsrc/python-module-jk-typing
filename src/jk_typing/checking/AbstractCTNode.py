

import typing
import inspect





class AbstractCTNode(object):

	################################################################################################################################
	## Constructor
	################################################################################################################################

	################################################################################################################################
	## Public Properties
	################################################################################################################################

	################################################################################################################################
	## Helper Methods
	################################################################################################################################

	def _printCodeLocation(self, codeFileName:str, bValue:bool):
		lineNo = inspect.currentframe().f_back.f_lineno
		print(f">> Returns **{bValue}** here: {codeFileName}:{lineNo}")
	#

	################################################################################################################################
	## Public Methods
	################################################################################################################################

	def __call__(self, value) -> bool:
		raise NotImplementedError()
	#

	def dump(self, prefix:str = None, printFunc:typing.Callable = None):
		if prefix is None:
			prefix = ""
		if printFunc is None:
			printFunc = print

		self._dump(prefix, printFunc)
	#

	def _dump(self, prefix:str, printFunc:typing.Callable):
		raise NotImplementedError()
	#

#





