

import typing
import inspect
import warnings




class _PySrcHelper(object):

	################################################################################################################################
	## Constants
	################################################################################################################################

	################################################################################################################################
	## Constructor
	################################################################################################################################

	################################################################################################################################
	## Public Properties
	################################################################################################################################

	################################################################################################################################
	## Helper Methods
	################################################################################################################################

	#
	# Find a sublist in a given list 
	#
	@staticmethod
	def __subListFinder(needle:list[str], haystack:list[str]) -> int:
		lenMyList = len(haystack)
		lenPattern = len(needle)
		if lenPattern > lenMyList:
			return -1

		for i in range(0, lenMyList - lenPattern):
			if haystack[i] == needle[0] and haystack[i:i+lenPattern] == needle:
				return i

		return -1
	#

	################################################################################################################################
	## Public Methods
	################################################################################################################################

	################################################################################################################################
	## Public Static Methods
	################################################################################################################################

	@staticmethod
	def getFirstCodeLine(fn) -> str:
		return inspect.getsource(fn).split("\n")[0].rstrip()
	#

	@staticmethod
	def getLineNo(fn) -> int:
		fnLines = [
			x.rstrip() for x in inspect.getsource(fn).split("\n")
		]

		while fnLines and not(fnLines[-1].rstrip()):
			fnLines = fnLines[:-1]

		filePath = inspect.getabsfile(fn)
		with open(filePath, "r", newline="\n", encoding="utf-8") as fin:
			sourceLines = [
				x.rstrip() for x in fin.read().split("\n")
			]

		return _PySrcHelper.__subListFinder(fnLines, sourceLines)
	#

	@staticmethod
	def warn(fn, msg:str):
		warnings.warn_explicit(
			message=f"{fn.__qualname__}(): " + msg,
			category=Warning,
			filename=inspect.getabsfile(fn),
			lineno=_PySrcHelper.getLineNo(fn),
			module=inspect.getmodule(fn).__name__,
		)
	#

#











