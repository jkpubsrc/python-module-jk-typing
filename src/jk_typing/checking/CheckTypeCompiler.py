

import sys
import types
import typing
import inspect
import collections
import collections.abc

from .AbstractCTNode import AbstractCTNode
from .CTAlwaysTrue import CTAlwaysTrue
from .CTIsDict import CTIsDict
from .CTIsOrderedDict import CTIsOrderedDict
from .CTIsABCMapping import CTIsABCMapping
from .CTIsNone import CTIsNone
from .CTIsType__CheckItems_AllTheSameType import CTIsType__CheckItems_AllTheSameType
from .CTIsType__Union import CTIsType__Union
from .CTIsType import CTIsType
from .CTIsSequence import CTIsSequence
from .CTIsCallable import CTIsCallable
from .CTIsType__CheckItems_ExactTypeSequence import CTIsType__CheckItems_ExactTypeSequence
from .CTIsType__Single_NewType import CTIsType__Single_NewType
from .CTIsType__Single_None import CTIsType__Single_None
from .CTIsType__TypeWithArgument import CTIsType__TypeWithArgument






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
			argName:str|None,
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

		try:
			_typeSpec_name = typeSpec._name
		except Exception as ee:
			_typeSpec_name = None

		try:
			_typeSpec__origin__ = typeSpec.__origin__
		except Exception as ee:
			_typeSpec__origin__ = None

		# ----

		if nEnableDebugging > 1:
			print("--")
			print("@@", type(typeSpec))
			print("@@", typeSpec)
			print("@@ nEnableDebugging =", nEnableDebugging)
			if typeSpec != inspect._empty:
				print("@@ _name          ", _typeSpec_name if _typeSpec_name else "n/a")
				print("@@ __origin__     ", _typeSpec__origin__ if _typeSpec__origin__ else "n/a")
				if _typeSpec__origin__:
					print("\t                    list : ", _typeSpec__origin__ == list)
					print("\t             typing.List : ", _typeSpec__origin__ == typing.List)
					print("\t                   tuple : ", _typeSpec__origin__ == tuple)
					print("\t            typing.Tuple : ", _typeSpec__origin__ == typing.Tuple)
					print("\t                     set : ", _typeSpec__origin__ == set)
					print("\t              typing.Set : ", _typeSpec__origin__ == typing.Set)
					print("\t               frozenset : ", _typeSpec__origin__ == frozenset)
					print("\t        typing.FrozenSet : ", _typeSpec__origin__ == typing.FrozenSet)
					print("\t                    dict : ", _typeSpec__origin__ == dict)
					print("\t             typing.Dict : ", _typeSpec__origin__ == typing.Dict)
					print("\t          typing.Mapping : ", _typeSpec__origin__ == typing.Mapping)
					print("\t collections.abc.Mapping : ", _typeSpec__origin__ == collections.abc.Mapping)
					print("\t collections.OrderedDict : ", _typeSpec__origin__ == collections.OrderedDict)
					print("\t      typing.OrderedDict : ", _typeSpec__origin__ == typing.OrderedDict)
					print("\t         typing.Sequence : ", _typeSpec__origin__ == typing.Sequence)
					print("\tcollections.abc.Sequence : ", _typeSpec__origin__ == collections.abc.Sequence)
				try:
					print("@@ __args__       ", typeSpec.__args__)
				except:
					print("@@ __args__       ", "n/a")
				try:
					print("@@ _inst          ", typeSpec._inst)
				except:
					print("@@ _inst          ", "n/a")
				try:
					print("@@ __parameters__ ", typeSpec.__parameters__)
				except:
					print("@@ __parameters__ ", "n/a")
				try:
					print("@@ _special       ", typeSpec._special)
				except:
					print("@@ _special       ", "n/a")
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

			if _typeSpec_name == "Callable":
				return CTIsCallable(
					argName,
					sType,
					nEnableDebugging,
				)

			if _typeSpec_name == "List":
				# typing.List[str]
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

			if _typeSpec_name == "Sequence":
				if isinstance(typeSpec.__args__[0], typing.TypeVar):
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
				else:
					return CTIsType__CheckItems_AllTheSameType(
						argName,
						sType,
						nEnableDebugging,
						typing.Sequence,
						CheckTypeCompiler._0_compile_checking(argName, sType, typeSpec.__args__[0], outWarnList, nEnableDebugging)
					)

			if _typeSpec_name == "Tuple":
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

			if _typeSpec_name == "Set":
				return CTIsType__CheckItems_AllTheSameType(
					argName,
					sType,
					nEnableDebugging,
					set,
					CheckTypeCompiler._0_compile_checking(argName, sType, typeSpec.__args__[0], outWarnList, nEnableDebugging)
				)

			if _typeSpec_name == "FrozenSet":
				return CTIsType__CheckItems_AllTheSameType(
					argName,
					sType,
					nEnableDebugging,
					frozenset,
					CheckTypeCompiler._0_compile_checking(argName, sType, typeSpec.__args__[0], outWarnList, nEnableDebugging)
				)

			if _typeSpec_name == "Deque":
				return CTIsType__CheckItems_AllTheSameType(
					argName,
					sType,
					nEnableDebugging,
					collections.deque,
					CheckTypeCompiler._0_compile_checking(argName, sType, typeSpec.__args__[0], outWarnList, nEnableDebugging)
				)

			if _typeSpec_name == "Dict":
				return CTIsDict(
					argName,
					sType,
					nEnableDebugging,
					CheckTypeCompiler._0_compile_checking(argName, sType, typeSpec.__args__[0], outWarnList, nEnableDebugging),
					CheckTypeCompiler._0_compile_checking(argName, sType, typeSpec.__args__[1], outWarnList, nEnableDebugging)
				)

			if _typeSpec_name == "OrderedDict":
				return CTIsOrderedDict(
					argName,
					sType,
					nEnableDebugging,
					CheckTypeCompiler._0_compile_checking(argName, sType, typeSpec.__args__[0], outWarnList, nEnableDebugging),
					CheckTypeCompiler._0_compile_checking(argName, sType, typeSpec.__args__[1], outWarnList, nEnableDebugging)
				)

			if (_typeSpec__origin__ == collections.abc.Mapping):
				# dict[str]
				return CTIsABCMapping(
					argName,
					sType,
					nEnableDebugging,
					CheckTypeCompiler._0_compile_checking(argName, sType, typeSpec.__args__[0], outWarnList, nEnableDebugging),
					CheckTypeCompiler._0_compile_checking(argName, sType, typeSpec.__args__[1], outWarnList, nEnableDebugging)
				)

			if (_typeSpec__origin__ == typing.Union):
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

		elif (_typeSpec__origin__ == type):
			assert len(typeSpec.__args__) == 1
			assert isinstance(typeSpec.__args__[0], type)
			return CTIsType__TypeWithArgument(
				argName,
				sType,
				nEnableDebugging,
				typeSpec.__args__[0],
			)

		elif (_typeSpec__origin__ == list):
			# list[str]
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

		elif (_typeSpec__origin__ == tuple):
			# tuple[str]
			if isinstance(typeSpec.__args__[0], typing.TypeVar):
				# NOTE: this represents: typing.Tuple
				return CTIsType(
					argName,
					sType,
					nEnableDebugging,
					tuple,
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

		elif (_typeSpec__origin__ == set):
			# set[str]
			return CTIsType__CheckItems_AllTheSameType(
				argName,
				sType,
				nEnableDebugging,
				set,
				CheckTypeCompiler._0_compile_checking(argName, sType, typeSpec.__args__[0], outWarnList, nEnableDebugging)
			)

		elif (_typeSpec__origin__ == frozenset):
			# frozenset[str]
			return CTIsType__CheckItems_AllTheSameType(
				argName,
				sType,
				nEnableDebugging,
				frozenset,
				CheckTypeCompiler._0_compile_checking(argName, sType, typeSpec.__args__[0], outWarnList, nEnableDebugging)
			)

		elif (_typeSpec__origin__ == collections.deque):
			# deque[str]
			return CTIsType__CheckItems_AllTheSameType(
				argName,
				sType,
				nEnableDebugging,
				collections.deque,
				CheckTypeCompiler._0_compile_checking(argName, sType, typeSpec.__args__[0], outWarnList, nEnableDebugging)
			)

		elif (_typeSpec__origin__ == dict):
			# dict[str]
			return CTIsDict(
				argName,
				sType,
				nEnableDebugging,
				CheckTypeCompiler._0_compile_checking(argName, sType, typeSpec.__args__[0], outWarnList, nEnableDebugging),
				CheckTypeCompiler._0_compile_checking(argName, sType, typeSpec.__args__[1], outWarnList, nEnableDebugging)
			)

		elif (_typeSpec__origin__ == collections.OrderedDict):
			# dict[str]
			return CTIsOrderedDict(
				argName,
				sType,
				nEnableDebugging,
				CheckTypeCompiler._0_compile_checking(argName, sType, typeSpec.__args__[0], outWarnList, nEnableDebugging),
				CheckTypeCompiler._0_compile_checking(argName, sType, typeSpec.__args__[1], outWarnList, nEnableDebugging)
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
	# Converts a parameter type or a type hint to string.
	#
	@staticmethod
	def paramTypeToStr(t:typing.Union[inspect.Parameter,typing.Any]) -> str:
		#print(">>", t, type(t))
		#if isinstance(t, inspect.Parameter):
		#	print(">>a", t.annotation, type(t.annotation))
		if t is None:
			#print(">>x", repr("void"))
			return "void"
		
		retExtra = ""
		if isinstance(t, inspect.Parameter):
			if t.kind == inspect._ParameterKind.VAR_POSITIONAL:
				retExtra = "*"
			elif t.kind == inspect._ParameterKind.VAR_KEYWORD:
				retExtra = "**"
			elif t.kind == inspect._ParameterKind.POSITIONAL_OR_KEYWORD:
				pass
			elif t.kind == inspect._ParameterKind.POSITIONAL_ONLY:
				pass
			elif t.kind == inspect._ParameterKind.KEYWORD_ONLY:
				pass
			else:
				# NOTE: this is quite unexpected :-/
				pass
			t = t.annotation

		if t == inspect._empty:
			#print(">>w", repr("any"))
			return "any"

		s = repr(t)
		# s should be something like this:
		#	 "<Parameter "abc">
		#	 "<Parameter "abc:int">
		#	 "<Parameter "*args">
		#if s.startswith("<Parameter \"*"):
		#	print("--1")
		#	s = s[13:-2]
		#elif s.startswith("<Parameter \""):
		#	print("--2")
		#	s = s[12:-2]
		if s.startswith("<class '"):
			#print("--3")
			s = s[8:-2]
		#else:
		#	return retExtra + "(unknown:" + s.replace(" ", "") + ")"
		s = s.replace(" ", "")

		pos = s.find(":")
		if pos > 0:
			#print(">>y", repr(retExtra + s[pos+1:]))
			return retExtra + s[pos+1:]
		else:
			#print(">>z", repr(retExtra + s))
			return retExtra + s
	#

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
			argName:str|None,
			sType:str,
			typeSpec,
			bIsArgV:bool,
			bIsKWArg:bool,
			defaultValue,
			outWarnList:list[str],
			nEnableDebugging:int|bool = 0
		) -> AbstractCTNode|None:

		if argName is not None:
			assert isinstance(argName, str)
		assert isinstance(sType, str)
		assert isinstance(bIsArgV, bool)
		assert isinstance(bIsKWArg, bool)
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

		# ----

		ret = CheckTypeCompiler._0_compile_checking(argName, sType, typeSpec, outWarnList, nEnableDebugging)

		if bIsArgV:
			# example: *argv:int
			# the tuple characteristic is implicitely defined, so wrap it here to make this characteristic explicite
			ret = CTIsType__CheckItems_AllTheSameType(
				argName,
				sType,
				nEnableDebugging,
				tuple,
				ret
			)

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






