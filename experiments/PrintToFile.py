


import os
import typing
import sys
import pprint

import jk_typing
import jk_utils
import jk_logging
import jk_json
import jk_prettyprintobj








class PrintToFile(object):

	################################################################################################################################
	## Constructor
	################################################################################################################################

	#
	# Constructor method.
	#
	@jk_typing.checkFunctionSignature()
	def __init__(self, filePath:str, *args, dirPath:typing.Union[str,None] = None, fileExt:typing.Union[str,None] = None):
		assert not args

		# ----

		_dirPath, _fileName = os.path.split(filePath)
		assert _fileName
		_fileBaseName, _fileExt = os.path.splitext(_fileName)
		assert _fileBaseName
		assert _fileExt
		assert _fileExt.startswith(".")
		assert len(_fileExt) > 1

		if dirPath:
			while dirPath[1:].endswith(os.sep):
				dirPath = dirPath[:-1]
			_dirPath = dirPath

		if fileExt:
			if not fileExt.startswith("."):
				fileExt = "." + fileExt
			_fileExt = fileExt
		
		_fileName = "{}---python-{}.{}.{}{}".format(_fileBaseName, sys.version_info.major, sys.version_info.minor, sys.version_info.micro, _fileExt)
		if _dirPath:
			filePath = os.path.join(_dirPath, _fileName)
		else:
			filePath = _fileName

		self.__filePath = filePath
		self.__f = None

		self.__pprinterArgs = (1, 160, None, False, True)
		self.__pprinter = pprint.PrettyPrinter(
			indent=self.__pprinterArgs[0],
			width=self.__pprinterArgs[1],
			depth=self.__pprinterArgs[2],
			compact=self.__pprinterArgs[3],
			sort_dicts=self.__pprinterArgs[4]
		)

		print("Writing output to file: " + filePath)
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

	def __enter__(self):
		self.__f = open(self.__filePath, "w", encoding="utf-8", newline="\n")
		return self
	#

	def __exit__(self, exc_type, exc_value, exc_tb):
		self.__f.close()
		self.__f = None
	#

	def pformat(self, object, indent=1, width=160, depth=None, *, compact=False, sort_dicts=True) -> str:
		a = (indent, width, depth, compact, sort_dicts)
		if a == self.__pprinterArgs:
			printer = self.__pprinter
		else:
			printer = pprint.PrettyPrinter(
				indent=indent,
				width=width,
				depth=depth,
				compact=compact,
				sort_dicts=sort_dicts
			)
		return printer.pformat(object)
	#

	def pprint(self, object, indent=1, width=160, depth=None, *, compact=False, sort_dicts=True):
		a = (indent, width, depth, compact, sort_dicts)
		if a == self.__pprinterArgs:
			printer = self.__pprinter
		else:
			printer = pprint.PrettyPrinter(
				indent=indent,
				width=width,
				depth=depth,
				compact=compact,
				sort_dicts=sort_dicts
			)
		self.print(printer.pformat(object))
	#

	def printLines(self,
			lines,
		):
		for arg in lines:
			self.print(arg)
	#

	def print(self,
			*args,
			sep:typing.Union[str,None] = " ",
			end:typing.Union[str,None] = "\n",
			flush:bool = False,
		):
		if args:
			if sep is not None:
				textToWrite = sep.join([ str(a) for a in args ])
			else:
				textToWrite = "".join([ str(a) for a in args ])
		else:
			textToWrite = ""
		if end is not None:
			textToWrite += end
		self.__f.write(textToWrite)
		if flush:
			self.__f.flush()
	#

#





