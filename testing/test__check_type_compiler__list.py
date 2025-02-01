#!/usr/bin/python3



import os
import typing
import inspect

#import jk_utils
import jk_logging
import jk_json
import jk_prettyprintobj

import jk_typing
import jk_typing.checking





class TestVectorElement(jk_prettyprintobj.DumpMixin):

	def __init__(self, typeSpec, validValues, invalidValues) -> None:
		self.typeSpec = typeSpec
		self.validValues = validValues
		self.invalidValues = invalidValues
	#

	def _dumpVarNames(self):
		return [
			"typeSpec",
			"validValues",
			"invalidValues",
		]
	#

#




class Value(jk_prettyprintobj.DumpMixin):

	def __init__(self, value, typeIdentifiers:list) -> None:
		self.value = value
		if typing.Any not in typeIdentifiers:
			typeIdentifiers.append(typing.Any)
		self.typeIdentifiers = typeIdentifiers
	#

	def _dumpVarNames(self):
		return [
			"value",
			"typeIdentifiers",
		]
	#

#

class ValueCollection(object):

	def __init__(self, *args:typing.List[Value]) -> None:
		self.__values:typing.List[Value] = args
	#

	def partition(self, *typeIdentifiers):
		retFound = []
		retNotFound = []
		for v in self.__values:
			bFound = False
			for typeIdentifier in typeIdentifiers:
				if typeIdentifier in v.typeIdentifiers:
					bFound = True
					break
			if bFound:
				retFound.append(v)
			else:
				retNotFound.append(v)
		return retFound, retNotFound
	#

	def getAllValid(self, *typeIdentifiers):
		ret = []
		for v in self.__values:
			bFound = False
			for typeIdentifier in typeIdentifiers:
				if typeIdentifier in v.typeIdentifiers:
					bFound = True
					break
			if bFound:
				ret.append(v)
		return ret
	#

	def getAllInvalid(self, *typeIdentifiers):
		ret = []
		for v in self.__values:
			bFound = False
			for typeIdentifier in typeIdentifiers:
				if typeIdentifier in v.typeIdentifiers:
					bFound = True
					break
			if not bFound:
				ret.append(v)
		return ret
	#

#

valueCollection = ValueCollection(
	Value(	None,								[ type(None) ]),

	Value(	True,								[ bool, int, typing.Union[int,float], typing.Union[bool,str] ]),
	Value(	False,								[ bool, int, typing.Union[int,float], typing.Union[bool,str] ]),

	Value(	-123,								[ int, typing.Union[int,float] ]),
	Value(	-1,									[ int, typing.Union[int,float] ]),
	Value(	0,									[ int, typing.Union[int,float] ]),
	Value(	1,									[ int, typing.Union[int,float] ]),
	Value(	123,								[ int, typing.Union[int,float] ]),

	Value(	-123.4,								[ float, typing.Union[int,float] ]),
	Value(	-1.1,								[ float, typing.Union[int,float] ]),
	Value(	0.9,								[ float, typing.Union[int,float] ]),
	Value(	1.1,								[ float, typing.Union[int,float] ]),
	Value(	123.4,								[ float, typing.Union[int,float] ]),

	Value(	"",									[ str, typing.Union[bool,str], typing.Sequence, typing.Sequence[str] ]),
	Value(	"abc",								[ str, typing.Union[bool,str], typing.Sequence, typing.Sequence[str] ]),

	Value(	[],									[ list, typing.List, typing.List[int], typing.List[float], typing.List[str], typing.Sequence, typing.Sequence[str] ]),
	Value(	[ 1, 2, 3 ],						[ list, typing.List, typing.List[int], typing.Sequence ]),
	Value(	[ 1.1, 2.2, 3.3 ],					[ list, typing.List, typing.List[float], typing.Sequence ]),
	Value(	[ "a", "b", "" ],					[ list, typing.List, typing.List[str], typing.Sequence, typing.Sequence[str] ]),
	Value(	[ 1, 2.2 ],							[ list, typing.List, typing.Sequence ]),
	Value(	[ 1, "abc" ],						[ list, typing.List, typing.Sequence ]),

	Value(	tuple(),							[ tuple, typing.Tuple, typing.Tuple[int,...], typing.Tuple[float,...], typing.Tuple[str,...], typing.Sequence, typing.Sequence[str] ]),
	Value(	(1,),								[ tuple, typing.Tuple, typing.Tuple[int], typing.Tuple[int,...], typing.Sequence ]),
	Value(	(1, 2, 3),							[ tuple, typing.Tuple, typing.Tuple[int,...], typing.Sequence ]),
	Value(	(1.1, 2.2, 3.3),					[ tuple, typing.Tuple, typing.Tuple[float,...], typing.Sequence ]),
	Value(	("a", "b", ""),						[ tuple, typing.Tuple, typing.Tuple[str,...], typing.Sequence ]),
	Value(	(1, 2.2),							[ tuple, typing.Tuple, typing.Sequence ]),
	Value(	(1, "abc"),							[ tuple, typing.Tuple, typing.Sequence ]),

	Value(	("abc",False),						[ tuple, typing.Tuple, typing.Tuple[str,bool], typing.Sequence ]),
	Value(	("abc",True),						[ tuple, typing.Tuple, typing.Tuple[str,bool], typing.Sequence ]),
	Value(	("abc",0),							[ tuple, typing.Tuple, typing.Sequence ]),
	Value(	("abc",1),							[ tuple, typing.Tuple, typing.Sequence ]),
	Value(	("abc",123),						[ tuple, typing.Tuple, typing.Sequence ]),

	Value(	set(),								[ set, typing.Set, typing.Set[int], typing.Set[float], typing.Set[str] ]),
	Value(	set([ 1, 2, 3 ]),					[ set, typing.Set, typing.Set[int] ]),
	Value(	set([ 1.1, 2.2, 3.3 ]),				[ set, typing.Set, typing.Set[float] ]),
	Value(	set([ "a", "b", "" ]),				[ set, typing.Set, typing.Set[str] ]),
	Value(	set([ 1, 2.2 ]),					[ set, typing.Set ]),
	Value(	set([ 1, "abc" ]),					[ set, typing.Set ]),

	Value(	frozenset(),						[ frozenset, typing.FrozenSet, typing.FrozenSet[int], typing.FrozenSet[float], typing.FrozenSet[str] ]),
	Value(	frozenset([ 1, 2, 3 ]),				[ frozenset, typing.FrozenSet, typing.FrozenSet[int] ]),
	Value(	frozenset([ 1.1, 2.2, 3.3 ]),		[ frozenset, typing.FrozenSet, typing.FrozenSet[float] ]),
	Value(	frozenset([ "a", "b", "" ]),		[ frozenset, typing.FrozenSet, typing.FrozenSet[str] ]),
	Value(	frozenset([ 1, 2.2 ]),				[ frozenset, typing.FrozenSet ]),
	Value(	frozenset([ 1, "abc" ]),			[ frozenset, typing.FrozenSet ]),

	Value(	{},									[ dict, typing.Dict, typing.Dict[str,int], typing.Dict[str,float], typing.Dict[str,str], typing.Dict[str,typing.Any], typing.Dict[str,typing.Union[int,float]] ]),
	Value(	{ "a": 123 },						[ dict, typing.Dict, typing.Dict[str,int], typing.Dict[str,typing.Any], typing.Dict[str,typing.Union[int,float]] ]),
	Value(	{ "a": 123.4 },						[ dict, typing.Dict, typing.Dict[str,float], typing.Dict[str,typing.Any], typing.Dict[str,typing.Union[int,float]] ]),
	Value(	{ "a": "abc" },						[ dict, typing.Dict, typing.Dict[str,str], typing.Dict[str,typing.Any] ]),
	Value(	{ "a": 123, "b": 123.4 },			[ dict, typing.Dict, typing.Dict[str,typing.Any], typing.Dict[str,typing.Union[int,float]] ]),
)



def generateTestElement(typeSpec:type, valueCollection:ValueCollection):
	_ok, _notOk = valueCollection.partition(typeSpec)
	return TestVectorElement(
		typeSpec = typeSpec,
		validValues = _ok,
		invalidValues = _notOk,
	)
#









ALL_TYPES = [
	type(None),
	typing.Any,
	bool,
	int,
	float,
	str,
	list,
	typing.List,
	typing.List[int],
	typing.List[float],
	typing.List[str],
	tuple,
	typing.Tuple,
	typing.Tuple[int],
	typing.Tuple[int,...],
	typing.Tuple[float],
	typing.Tuple[float,...],
	typing.Tuple[str],
	typing.Tuple[str,...],
	typing.Tuple[str,bool],
	set,
	typing.Set[int],
	typing.Set[float],
	typing.Set[str],
	frozenset,
	typing.FrozenSet[int],
	typing.FrozenSet[float],
	typing.FrozenSet[str],
	dict,
	typing.Dict[str,int],
	typing.Dict[str,float],
	typing.Dict[str,str],
	typing.Dict[str,typing.Any],
	typing.Dict[str,typing.Union[int,float]],
	typing.Union[int,float],
	typing.Union[bool,str],
]

ALL_TYPES = [
	##typing.Tuple,
	typing.Sequence,
	#typing.Sequence[str],
]

TEST_VECTOR = [	generateTestElement(t, valueCollection) for t in ALL_TYPES	]






with jk_logging.wrapMain() as log:

	nErrors = 0
	nTotal = 0

	for testVectorElement in TEST_VECTOR:
		print(repr(testVectorElement))
		assert isinstance(testVectorElement, TestVectorElement)

		log.info("#" * 160)
		log2 = log.descend(("#### " + str(testVectorElement.typeSpec) + " ").ljust(160, "#"))

		outWarnList = []
		ctnode = jk_typing.checking.CheckTypeCompiler.compile(
			argName = "argName",
			sType = "sType",
			typeSpec = testVectorElement.typeSpec,
			bIsArgV = False,
			bIsKWArg = False,
			defaultValue = inspect._empty,
			outWarnList = outWarnList,
			# bEnableDebugging = True,
			nEnableDebugging = False,
		)
		for line in outWarnList:
			log2.warn("WARNING: " + line)
		ctnode.dump("", log2.notice)

		for validValue in testVectorElement.validValues:
			assert isinstance(validValue, Value)
			bResult = ctnode(validValue.value)
			s = "Testing valid value: " + repr(validValue.value) + " ===> " + repr(bResult)
			if bResult:
				log2.info(s)
			else:
				log2.error(s)
				nErrors += 1
			nTotal += 1

		for invalidValue in testVectorElement.invalidValues:
			assert isinstance(invalidValue, Value)
			bResult = ctnode(invalidValue.value)
			s = "Testing invalid value: " + repr(invalidValue.value) + " ===> " + repr(bResult)
			if not bResult:
				log2.info(s)
			else:
				log2.error(s)
				nErrors += 1
			nTotal += 1

	log.info("#" * 160)

	log.info("{} tests performed.".format(nTotal))
	if nErrors:
		log.error("There were {} error(s).".format(nErrors))
	else:
		log.success("There were no error(s).")
	print()














