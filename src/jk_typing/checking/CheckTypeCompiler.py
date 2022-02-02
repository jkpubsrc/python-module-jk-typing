



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
from .CTIsCallable import CTIsCallable
from .CTIsType__CheckItems_ExactTypeSequence import CTIsType__CheckItems_ExactTypeSequence








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
			outWarnList:list,
			bEnableDebugging:bool,
		):

		if typeSpec is None:
			# void
			raise Exception("Can't be void ...")

		elif typeSpec == inspect._empty:
			# nothing is specified
			return CTAlwaysTrue(
				argName,
				sType,
				bEnableDebugging,
			)

		elif isinstance(typeSpec, str):
			# a string based type specified; we can't handle this as we simply don't have any information about the type;
			outWarnList.append("string based type specification notsupported: " + repr(typeSpec))
			return None

		elif isinstance(typeSpec, typing._GenericAlias):
			# generic

			if typeSpec._name == "Callable":
				return CTIsCallable(
					argName,
					sType,
					bEnableDebugging,
				)

			if typeSpec._name == "List":
				return CTIsType__CheckItems_AllTheSameType(
					argName,
					sType,
					bEnableDebugging,
					list,
					CheckTypeCompiler._0_compile_checking(argName, sType, typeSpec.__args__[0], outWarnList, bEnableDebugging)
				)

			if typeSpec._name == "Tuple":
				return CTIsType__CheckItems_ExactTypeSequence(
					argName,
					sType,
					bEnableDebugging,
					tuple,
					[
						CheckTypeCompiler._0_compile_checking(argName, sType, x, outWarnList, bEnableDebugging)
							for x in typeSpec.__args__
					]
				)

			if typeSpec._name == "Set":
				return CTIsType__CheckItems_AllTheSameType(
					argName,
					sType,
					bEnableDebugging,
					set,
					CheckTypeCompiler._0_compile_checking(argName, sType, typeSpec.__args__[0], outWarnList, bEnableDebugging)
				)

			if typeSpec._name == "FrozenSet":
				return CTIsType__CheckItems_AllTheSameType(
					argName,
					sType,
					bEnableDebugging,
					frozenset,
					CheckTypeCompiler._0_compile_checking(argName, sType, typeSpec.__args__[0], outWarnList, bEnableDebugging)
				)

			if typeSpec._name == "Deque":
				return CTIsType__CheckItems_AllTheSameType(
					argName,
					sType,
					bEnableDebugging,
					deque,
					CheckTypeCompiler._0_compile_checking(argName, sType, typeSpec.__args__[0], outWarnList, bEnableDebugging)
				)

			if typeSpec._name == "Dict":
				return CTIsDict(
					argName,
					sType,
					bEnableDebugging,
					CheckTypeCompiler._0_compile_checking(argName, sType, typeSpec.__args__[0], outWarnList, bEnableDebugging),
					CheckTypeCompiler._0_compile_checking(argName, sType, typeSpec.__args__[1], outWarnList, bEnableDebugging)
				)

			if typeSpec.__origin__ == typing.Union:
				return CTIsType__Union(
					argName,
					sType,
					bEnableDebugging,
					[ CheckTypeCompiler._0_compile_checking(argName, sType, t, outWarnList, bEnableDebugging) for t in typeSpec.__args__ ]
				)

			if outWarnList is not None:
				outWarnList.append("Can't check this type: " + repr(typeSpec))
			return CTAlwaysTrue(
				argName,
				sType,
				bEnableDebugging,
			)

		else:
			# regular type
			return CTIsType(
				argName,
				sType,
				bEnableDebugging,
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
	# @param	* typeSpec				(required) A type specification object as returned by inspect
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
			outWarnList:list,
			bEnableDebugging:bool = False
		) -> typing.Union[AbstractCTNode,None]:

		if typeSpec is None:
			# void
			return CTIsNone(
				argName,
				sType,
				bEnableDebugging,
			)

		elif typeSpec == inspect._empty:
			# nothing is specified
			return None

		elif isinstance(typeSpec, str):
			# a string based type specified; we can't handle this as we simply don't have any information about the type;
			outWarnList.append("string based type specification notsupported: " + repr(typeSpec))
			return None

		elif isinstance(typeSpec, typing._GenericAlias):
			# generic

			if typeSpec._name == "Callable":
				ret = CTIsCallable(
					argName,
					sType,
					bEnableDebugging,
				)

			elif typeSpec._name == "List":
				ret = CTIsType__CheckItems_AllTheSameType(
					argName,
					sType,
					bEnableDebugging,
					list,
					CheckTypeCompiler._0_compile_checking(argName, sType, typeSpec.__args__[0], outWarnList, bEnableDebugging)
				)

			elif typeSpec._name == "Tuple":
				ret = CTIsType__CheckItems_ExactTypeSequence(
					argName,
					sType,
					bEnableDebugging,
					tuple,
					[
						CheckTypeCompiler._0_compile_checking(argName, sType, x, outWarnList, bEnableDebugging)
							for x in typeSpec.__args__
					]
				)

			elif typeSpec._name == "Set":
				ret = CTIsType__CheckItems_AllTheSameType(
					argName,
					sType,
					bEnableDebugging,
					set,
					CheckTypeCompiler._0_compile_checking(argName, sType, typeSpec.__args__[0], outWarnList, bEnableDebugging)
				)

			elif typeSpec._name == "FrozenSet":
				ret = CTIsType__CheckItems_AllTheSameType(
					argName,
					sType,
					bEnableDebugging,
					frozenset,
					CheckTypeCompiler._0_compile_checking(argName, sType, typeSpec.__args__[0], outWarnList, bEnableDebugging)
				)

			elif typeSpec._name == "Deque":
				ret = CTIsType__CheckItems_AllTheSameType(
					argName,
					sType,
					bEnableDebugging,
					deque,
					CheckTypeCompiler._0_compile_checking(argName, sType, typeSpec.__args__[0], outWarnList, bEnableDebugging)
				)

			elif typeSpec._name == "Dict":
				ret = CTIsDict(
					argName,
					sType,
					bEnableDebugging,
					CheckTypeCompiler._0_compile_checking(argName, sType, typeSpec.__args__[0], outWarnList, bEnableDebugging),
					CheckTypeCompiler._0_compile_checking(argName, sType, typeSpec.__args__[1], outWarnList, bEnableDebugging)
				)

			elif typeSpec.__origin__ == typing.Union:
				ret = CTIsType__Union(
					argName,
					sType,
					bEnableDebugging,
					[ CheckTypeCompiler._0_compile_checking(argName, sType, t, outWarnList, bEnableDebugging) for t in typeSpec.__args__ ]
				)

			else:
				if outWarnList is not None:
					outWarnList.append("Can't check this type: " + repr(typeSpec))
				ret = CTAlwaysTrue(
					argName,
					sType,
					bEnableDebugging,
				)

			if defaultValue is None:
				ret = CTIsType__Union(
					argName,
					sType,
					bEnableDebugging,
					[ ret, CTIsNone(argName, sType, bEnableDebugging) ]
				)

			return ret

		else:
			# regular type
			ret = CTIsType(
				argName,
				sType,
				bEnableDebugging,
				typeSpec,
			)

			if defaultValue is None:
				ret = CTIsType__Union(
					argName,
					sType,
					bEnableDebugging,
					[ ret, CTIsNone(argName, sType, bEnableDebugging) ]
				)

			return ret
	#

#






