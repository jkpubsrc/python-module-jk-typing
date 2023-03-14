#!/usr/bin/python3


from collections import deque
import os
import types
import typing
import inspect

import jk_console

from PrintToFile import PrintToFile








ALL_TYPES = [
	type(None),
	typing.Any,
	inspect._empty,
	bool,
	int,
	float,
	str,
	typing.Sequence,
	typing.Sequence[str],
	# typing.Sequence[str,int],			# THIS IS INVALID
	list,
	typing.List,
	typing.List[int],
	typing.List[float],
	typing.List[str],
	# typing.List[str,bool],			# THIS IS INVALID
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
	# typing.Set[str,bool],				# THIS IS INVALID
	frozenset,
	typing.FrozenSet[int],
	typing.FrozenSet[float],
	typing.FrozenSet[str],
	# typing.FrozenSet[str,bool],		# THIS IS INVALID
	dict,
	typing.Dict[str,int],
	typing.Dict[str,float],
	typing.Dict[str,str],
	typing.Dict[str,typing.Any],
	typing.Dict[str,typing.Union[int,float]],
	deque,
	typing.Deque,
	typing.Deque[str],
	# typing.Deque[str,bool],			# THIS IS INVALID
	typing.Union[int,float],
	typing.Union[str,bool],
]



PROPERTY_NAMES = sorted([
	"_name",
	"__origin__",
	"__args__",
	#"_inst",
	#"__parameters__",
	"_special",
])



def _addRows(typeSpecs:list, table:jk_console.SimpleTable):
	for typeSpec in typeSpecs:
		rowData = [ str(typeSpec), str(type(typeSpec)) ]
		for propertName in PROPERTY_NAMES:
			try:
				rowData.append(str(getattr(typeSpec, propertName)))
			except:
				rowData.append("-")
		table.addRow(*rowData)
#


table = jk_console.SimpleTable()
rowHeaders = [ "Type Specification", "type(~)" ]
rowHeaders.extend(PROPERTY_NAMES)
table.addRow(*rowHeaders).hlineAfterRow = True



_tempGenericAlias = []
_tempOther = []
_tempType = []

for typeSpec in ALL_TYPES:
	if type(typeSpec) == typing._GenericAlias:
		_tempGenericAlias.append(typeSpec)
		continue
	if type(typeSpec) == type:
		_tempType.append(typeSpec)
		continue
	_tempOther.append(typeSpec)

_addRows(_tempOther, table)
_addRows(_tempType, table)
_addRows(_tempGenericAlias, table)







with PrintToFile(__file__, dirPath="out", fileExt=".txt") as f:

	f.printLines(table.printToLines())

#












