

import sys
import types
import typing
import inspect
from collections import deque

from .AbstractCTNode import AbstractCTNode
from .CTAlwaysTrue import CTAlwaysTrue
from .CTIsDict import CTIsDict
from .CTIsNone import CTIsNone
from .CTIsType__CheckItems_AllTheSameType import CTIsType__CheckItems_AllTheSameType
from .CTIsType__Union import CTIsType__Union
from .CTIsType import CTIsType
from .CTIsSequence import CTIsSequence
from .CTIsCallable import CTIsCallable
from .CTIsType__CheckItems_ExactTypeSequence import CTIsType__CheckItems_ExactTypeSequence
from .CTIsType__Single_NewType import CTIsType__Single_NewType
from .CTIsType__Single_None import CTIsType__Single_None






_HAS_PIPE_UNIONS = (sys.version_info.major, sys.version_info.minor) >= (3, 10)

# print("@@@@ _HAS_PIPE_UNIONS =", _HAS_PIPE_UNIONS)





class CheckTypeCompiler(object):

	################################################################################################################################
	## Constructor
	################################################################################################################################

	################################################################################################################################
	## Public Properties
	################################################################################################################################

	################################################################################################################################
	## Helper Methods
	################################################################################################################################

	@staticmethod
	def _0_compile_checking(
			argName:typing.Union[str,None],
			sType:str,
			typeSpec,
			outWarnList:typing.List[str],
			nEnableDebugging:int,
		) -> AbstractCTNode:

		if argName is not None:
			assert isinstance(argName, str)
		assert isinstance(sType, str)
		assert isinstance(outWarnList, list)
		assert isinstance(nEnableDebugging, int)

		# ----

		if nEnableDebugging > 1:
			print("--")
			print("@@", type(typeSpec))
			print("@@", typeSpec)
			print("@@ nEnableDebugging =", nEnableDebugging)
			if typeSpec != inspect._empty:
				try:
					print("@@ _name          ", typeSpec._name)
				except:
					pass
				try:
					print("@@ __origin__     ", typeSpec.__origin__)
				except:
					pass
				try:
					print("@@ __args__       ", typeSpec.__args__)
				except:
					pass
				try:
					print("@@ _inst          ", typeSpec._inst)
				except:
					pass
				try:
					print("@@ __parameters__ ", typeSpec.__parameters__)
				except:
					pass
				try:
					print("@@ _special       ", typeSpec._special)
				except:
					pass
			# print(dir(typeSpec))

		if typeSpec is None:
			# void
			raise Exception("Can't be void ...")

		elif CTIsType__Single_None.isSingleNone(typeSpec):
			# None is specified
			return CTIsType__Single_None(
				argName,
				sType,
				nEnableDebugging
			)

		elif typeSpec == inspect._empty:
			# nothing is specified
			return CTAlwaysTrue(
				argName,
				sType,
				nEnableDebugging,
			)

		elif typeSpec == typing.Any:
			# nothing is specified
			return CTAlwaysTrue(
				argName,
				sType,
				nEnableDebugging,
			)

		elif isinstance(typeSpec, str):
			# a string based type specified; we can't handle this as we simply don't have any information about the type;
			outWarnList.append("string based type specification not supported: " + repr(typeSpec))
			return CTAlwaysTrue(
				argName,
				sType,
				nEnableDebugging,
			)

		elif _HAS_PIPE_UNIONS and isinstance(typeSpec, types.UnionType):
			return CTIsType__Union(
				argName,
				sType,
				nEnableDebugging,
				[ CheckTypeCompiler._0_compile_checking(argName, sType, t, outWarnList, nEnableDebugging) for t in typeSpec.__args__ ]
			)

		elif isinstance(typeSpec, typing._GenericAlias):			# matches against typing._UnionGenericAlias as well
			# generic

			if typeSpec._name == "Callable":
				return CTIsCallable(
					argName,
					sType,
					nEnableDebugging,
				)

			if typeSpec._name == "List":
				if isinstance(typeSpec.__args__[0], typing.TypeVar):
					# NOTE: this represents: typing.List
					return CTIsType(
						argName,
						sType,
						nEnableDebugging,
						list,
					)
				else:
					return CTIsType__CheckItems_AllTheSameType(
						argName,
						sType,
						nEnableDebugging,
						list,
						CheckTypeCompiler._0_compile_checking(argName, sType, typeSpec.__args__[0], outWarnList, nEnableDebugging)
					)

			if typeSpec._name == "Sequence":
				if outWarnList is not None:
					outWarnList.append("Can't check members of sequence.")
				# CTIsSequence
				#print("=->")
				return CTIsType(
					argName,
					sType,
					nEnableDebugging,
					typing.Sequence,
				)

			if typeSpec._name == "Tuple":
				if len(typeSpec.__args__) == 0:
					return CTIsType(
						argName,
						sType,
						nEnableDebugging,
						typing.Tuple,
					)
				elif (len(typeSpec.__args__) > 0) and (typeSpec.__args__[-1] == Ellipsis):
					if len(typeSpec.__args__) == 2:
						# something like: typing.Tuple[int,...]
						return CTIsType__CheckItems_AllTheSameType(
							argName,
							sType,
							nEnableDebugging,
							tuple,
							CheckTypeCompiler._0_compile_checking(argName, sType, typeSpec.__args__[0], outWarnList, nEnableDebugging)
						)
					else:
						if outWarnList is not None:
							outWarnList.append("Probably wrong type specification encountered: " + repr(typeSpec))
						return CTIsType(
							argName,
							sType,
							nEnableDebugging,
							tuple,
						)
				else:
					return CTIsType__CheckItems_ExactTypeSequence(
						argName,
						sType,
						nEnableDebugging,
						tuple,
						[
							CheckTypeCompiler._0_compile_checking(argName, sType, x, outWarnList, nEnableDebugging)
								for x in typeSpec.__args__
						]
					)

			if typeSpec._name == "Set":
				return CTIsType__CheckItems_AllTheSameType(
					argName,
					sType,
					nEnableDebugging,
					set,
					CheckTypeCompiler._0_compile_checking(argName, sType, typeSpec.__args__[0], outWarnList, nEnableDebugging)
				)

			if typeSpec._name == "FrozenSet":
				return CTIsType__CheckItems_AllTheSameType(
					argName,
					sType,
					nEnableDebugging,
					frozenset,
					CheckTypeCompiler._0_compile_checking(argName, sType, typeSpec.__args__[0], outWarnList, nEnableDebugging)
				)

			if typeSpec._name == "Deque":
				return CTIsType__CheckItems_AllTheSameType(
					argName,
					sType,
					nEnableDebugging,
					deque,
					CheckTypeCompiler._0_compile_checking(argName, sType, typeSpec.__args__[0], outWarnList, nEnableDebugging)
				)

			if typeSpec._name == "Dict":
				return CTIsDict(
					argName,
					sType,
					nEnableDebugging,
					CheckTypeCompiler._0_compile_checking(argName, sType, typeSpec.__args__[0], outWarnList, nEnableDebugging),
					CheckTypeCompiler._0_compile_checking(argName, sType, typeSpec.__args__[1], outWarnList, nEnableDebugging)
				)

			if typeSpec.__origin__ == typing.Union:
				return CTIsType__Union(
					argName,
					sType,
					nEnableDebugging,
					[ CheckTypeCompiler._0_compile_checking(argName, sType, t, outWarnList, nEnableDebugging) for t in typeSpec.__args__ ]
				)

			if outWarnList is not None:
				outWarnList.append("Can't check this type: " + repr(typeSpec))

			return CTAlwaysTrue(
				argName,
				sType,
				nEnableDebugging,
			)

		elif (typeSpec == tuple) or (typeSpec == typing.Tuple):
			return CTIsType(
				argName,
				"tuple",
				nEnableDebugging,
				typeSpec,
			)

		elif (typeSpec == list) or (typeSpec == typing.List):
			return CTIsType(
				argName,
				"list",
				nEnableDebugging,
				typeSpec,
			)

		elif (typeSpec == set) or (typeSpec == typing.Set):
			return CTIsType(
				argName,
				"set",
				nEnableDebugging,
				typeSpec,
			)

		elif (typeSpec == frozenset) or (typeSpec == typing.FrozenSet):
			return CTIsType(
				argName,
				"frozenset",
				nEnableDebugging,
				typeSpec,
			)

		else:
			# regular type
			if CTIsType__Single_NewType.isSingleNewType(typeSpec):
				return CTIsType__Single_NewType(
					argName,
					sType,
					nEnableDebugging,
					typeSpec
				)
			else:
				return CTIsType(
					argName,
					sType,
					nEnableDebugging,
					typeSpec
				)
	#

	################################################################################################################################
	## Public Methods
	################################################################################################################################

	#
	# Compile to value checking logic and return it.
	#
	# @param	str argName				(optional) Argument name. If none is specified, this should be a return value.
	# @param	str sType				(required) A string representation of the return type (for output).
	# @param	* typeSpec				(required) A type specification object as returned by inspect. This is the content of the <c>Parameter.annotation</c> field.
	# @param	any defaultValue		(required) The default value. If it is (null) an additional check for empty data is added. Specify `inspect._empty` if not defined.
	# @param	str[] outWarnList		(required) A list that receives warning messages.
	#
	# @param	AbstractCTNode|null		Returns a callable (based on a hierarchical object model) that performs the type checking
	#									or (null) if no type checking should be performed
	#
	@staticmethod
	def compile(
			argName:typing.Union[str,None],
			sType:str,
			typeSpec,
			defaultValue,
			outWarnList:typing.List[str],
			nEnableDebugging:typing.Union[int,bool] = 0
		) -> typing.Union[AbstractCTNode,None]:

		if argName is not None:
			assert isinstance(argName, str)
		assert isinstance(sType, str)
		assert isinstance(outWarnList, list)
		if isinstance(nEnableDebugging, bool):
			nEnableDebugging = int(nEnableDebugging)
		else:
			assert isinstance(nEnableDebugging, int)

		# ----

		if typeSpec is None:
			# void
			return CTIsNone(
				argName,
				sType,
				nEnableDebugging,
			)

		ret = CheckTypeCompiler._0_compile_checking(argName, sType, typeSpec, outWarnList, nEnableDebugging)

		if defaultValue is None:
			ret = CTIsType__Union(
				argName,
				sType,
				nEnableDebugging,
				[ ret, CTIsNone(argName, sType, nEnableDebugging) ]
			)

		return ret
	#

#






