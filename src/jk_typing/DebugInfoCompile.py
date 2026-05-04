

import typing
import inspect

import jk_prettyprintobj

from .checking.AbstractCTNode import AbstractCTNode





class DebugInfoCompile(jk_prettyprintobj.DumpMixin):

	################################################################################################################################
	## Constants
	################################################################################################################################

	################################################################################################################################
	## Constructor
	################################################################################################################################

	#
	# Constructor method.
	#
	def __init__(self):
		self.filePath:str|None = None
		self.lineNo:int|None = None

		self.fqn:str|None = None
		self.allAnnotations:typing.Dict[str,typing.Any]|None = None
		self.signature:inspect.Signature|None = None
		self.signatureParameters:typing.Mapping[str,inspect.Parameter]|None = None
		self.signatureReturnAnnotation:type|inspect._empty|inspect._void|None = None

		self.paramCheckers:typing.Dict[str,AbstractCTNode|None] = None
		self.returnChecker:AbstractCTNode|None = None
		self.infos:list[str] = []
		self.warnings:list[str] = []
	#

	################################################################################################################################
	## Public Properties
	################################################################################################################################

	################################################################################################################################
	## Helper Methods
	################################################################################################################################

	def __debug_dumpObj(self, prefix:str, someObj, bSkipUnderscores:bool = True, names:list = None):
		#print(prefix + "| " + repr(someObj))
		if someObj is None:
			return
		if names is None:
			names = dir(someObj)
		for key in names:
			if bSkipUnderscores and key.startswith("_"):
				continue
			print(prefix + "|\t" + key + ": " + str(getattr(someObj, key)))
	#

	def _dump(self, ctx:jk_prettyprintobj.DumpCtx):
		ctx.dumpVar("fqn", self.fqn)
		ctx.dumpVar("allAnnotations", self.allAnnotations)
		ctx.dumpVar("signature", self.signature)
		ctx.dumpVar("signatureParameters", self.signatureParameters)
		ctx.dumpVar("signatureReturnAnnotation", self.signatureReturnAnnotation)
		ctx.dumpVar("paramCheckers", self.paramCheckers)
		ctx.dumpVar("returnChecker", self.returnChecker)
		ctx.dumpVar("infos", self.infos)
		ctx.dumpVar("warnings", self.warnings)
	#

	################################################################################################################################
	## Public Methods
	################################################################################################################################

	def printFunctionInfos(self):
		print()
		print("@@>> wrapping function " + self.fqn + "(..) with checkFunctionSignature() ...")
		print("\t@@>> Annotations:")
		for ak, av in self.allAnnotations.items():
			print("\t\t@@>> Annotation for " + repr(ak) + ": " + str(av))
		print("\t@@>> Signature:")
		for sk, sv in self.signatureParameters.items():
			print("\t\t@@>> Signature parameter for " + repr(sk) + ": " + repr(sv))
			self.__debug_dumpObj("\t\t\t", sv, names = ["annotation", "default", "kind"])
			# parameters are:
			#	str sv.name				-- the name of the argument
			#	any sv.annotation		-- the type annotation structure associated with this argument (or inspect._empty if not set)
			#	obj sv.default			-- the defautl value (or inspect._empty if not set)
		print("\t@@>> Return annotation: " + str(self.signatureReturnAnnotation))
		print()
	#

	################################################################################################################################
	## Public Static Methods
	################################################################################################################################

#





