

import collections
import sys
import typing
import inspect

from .checking.AbstractCTNode import AbstractCTNode
from .checking.CheckTypeCompiler import CheckTypeCompiler
from .DebugInfoCompile import DebugInfoCompile
from ._PySrcHelper import _PySrcHelper





"""
def __checkUnion(value, typeSpecs:list):
	for typeSpec in typeSpecs:
		if _checkType(value, typeSpec):
			return True
	return False
#
"""



#_type_checking_enabled = True

if (sys.version_info.major < 3) or (
	(sys.version_info.major == 3) and (sys.version_info.minor <= 6)):
	# older Python implementation are not yet mature enough.
	raise Exception("Python versions below 3.6 are not supported!")








"""
def deactiveTypeChecking():
	global _type_checking_enabled
	_type_checking_enabled = False
#

def isTypeCheckingEnabled() -> bool:
	global _type_checking_enabled
	return _type_checking_enabled
#
"""








#
# Do the type check.
# This function is the heart of the type checking implementation.
#
# @param		any value			The value to check
# @param		various typeSpec	The type specification such as `None`, `int`, `typing.List[int]`, etc.
# @param		int indent			The current indentation level to use for debugging ouptut. A negative indent disables output.
#
def _checkType(value, typeSpec, indent:int):
	if indent >= 0:
		print("\t"*indent + ">> checking value " + repr(value) + " against: " + repr(typeSpec))

	if typeSpec is None:
		return value is None

	elif isinstance(typeSpec, typing._GenericAlias):
		if indent >= 0:
			print("\t"*indent + ">> (the condition type is generc (_name={}, __origin__={}))".format(
				repr(typeSpec._name),
				repr(typeSpec.__origin__)
			))

		if typeSpec._name == "List":
			if not isinstance(value, list):
				return False
			for v in value:
				if not _checkType(v, typeSpec.__args__[0], indent+1):
					return False
			return True

		elif typeSpec._name == "Tuple":
			if not isinstance(value, tuple):
				return False
			for v in value:
				if not _checkType(v, typeSpec.__args__[0], indent+1):
					return False
			return True

		elif typeSpec._name == "Set":
			if not isinstance(value, set):
				return False
			for v in value:
				if not _checkType(v, typeSpec.__args__[0], indent+1):
					return False
			return True

		elif typeSpec._name == "FrozenSet":
			if not isinstance(value, frozenset):
				return False
			for v in value:
				if not _checkType(v, typeSpec.__args__[0], indent+1):
					return False
			return True

		elif typeSpec._name == "Deque":
			if not isinstance(value, collections.deque):
				return False
			for v in value:
				if not _checkType(v, typeSpec.__args__[0], indent+1):
					return False
			return True

		elif typeSpec._name == "Dict":
			if not isinstance(value, dict):
				return False
			for k, v in value.items():
				if not _checkType(k, typeSpec.__args__[0], indent+1):
					return False
				if not _checkType(v, typeSpec.__args__[1], indent+1):
					return False
			return True

		elif typeSpec.__origin__ == typing.Union:
			for t in typeSpec.__args__:
				if _checkType(value, t, indent+1):
					return True
			return False

		else:
			if indent >= 0:
				print("\t"*indent + "WARN: Can't check this type: " + repr(typeSpec))
			return True

	else:
		if indent >= 0:
			print("\t"*indent + ">> (the condition type is primitive)")
		return isinstance(value, typeSpec)
#



#
# this is the annotation wrapper that receives arguments and returns the function that does the wrapping
#
# @param		bool bDebug							(optional) Enable debugging output at runtime.
# @param		int|bool bDebugComp					(optional) Enable debugging output at compile time.
#													If enabled this case the wrapped function or method will contain a 'debugInfoCompile' variable containing an instance of DebugInfoCompile.
# @param		str logDescend						(optional) Log descend message.
# @param		jk_logging.EnumLoglevel logLevel	(optional) Modify the standard descend log level.
# @param		bool bLogWithhold					(optional) Only log if a minimum log level of warning occurs.
#
def checkFunctionSignature(
		*,
		logDescend:str = None,
		logLevel = None,
		bLogWithhold:bool = False,
		bDebugComp:typing.Union[bool,int] = False,
		bDebugCompPrint:typing.Union[bool,int] = False,
		bDebugRuntime:typing.Union[bool,int] = False,
		bDebug:typing.Union[bool,int] = False,				# DEPRECATED
	):

	assert isinstance(bDebug, (bool, int))
	assert isinstance(bDebugComp, (bool, int))
	assert isinstance(bDebugCompPrint, (bool, int))
	assert isinstance(bDebugRuntime, (bool, int))
	assert isinstance(bLogWithhold, bool)
	if bDebug:
		bDebugRuntime = bDebug

	# ----

	debugInfoComp:DebugInfoCompile|None = None
	if bDebugComp:
		debugInfoComp = DebugInfoCompile()

	# ----

	# NOTE: This function is executed once for every function or method definition.
	def _wrap_the_function(fn):
		allAnnotations:typing.Dict[str,typing.Any] = typing.get_type_hints(fn)									# receives a normal dictionary
		_signature = inspect.signature(fn)
		_signature_parameters:typing.Mapping[str,inspect.Parameter] = _signature._parameters					# receives an ordered dictionary
		_signature_return_annotation:type|inspect._empty|inspect._void|None = _signature._return_annotation		# receives a type annotation structure

		if debugInfoComp:
			debugInfoComp.filePath = inspect.getabsfile(fn)
			debugInfoComp.lineNo = _PySrcHelper.getLineNo(fn)
			debugInfoComp.fqn = fn.__qualname__
			debugInfoComp.allAnnotations = allAnnotations
			debugInfoComp.signature = _signature
			debugInfoComp.signatureParameters = _signature_parameters
			debugInfoComp.signatureReturnAnnotation = _signature_return_annotation

		# variables to fill during compile phase
		_paramCheckers:typing.Dict[str,AbstractCTNode|None] = {}
		_returnChecker:AbstractCTNode|None = None

		# ----------------------------------------------------------------
		# ---- compile

		outWarnList = []			# NOTE: we reuse this list for performance reasons

		for k, p in _signature_parameters.items():
			outWarnList.clear()
			assert isinstance(p, inspect.Parameter)
			_bIsArgV = p.kind == inspect._ParameterKind.VAR_POSITIONAL
			_bIsKWArgs = p.kind == inspect._ParameterKind.VAR_KEYWORD
			_sType = CheckTypeCompiler.paramTypeToStr(p)
			c = CheckTypeCompiler.compile(
				k,												# argName
				_sType,											# sType
				p.annotation,									# typeSpec
				_bIsArgV,										# bKindIsArgV
				_bIsKWArgs,										# bKindIsKWArg
				p.default,										# defaultValue
				outWarnList,									# outWarnList
				bDebugComp,										# nEnableDebugging
			)
			if bDebugComp:
				#if c is not None:
				#	print("\t@@>> Signature parameter compilation for " + repr(k) + ":")
				#	c.dump("\t\t|\t")
				if outWarnList:
					for warnEntry in outWarnList:
						if debugInfoComp:
							debugInfoComp.warnings.append(f"Parameter {p!r}: {warnEntry}")
						_PySrcHelper.warn(fn, f"Parameter {p!r}: {warnEntry}")
			if c is not None:
				_paramCheckers[k] = c

		if _signature_return_annotation != inspect._empty:
			outWarnList.clear()
			_sType = CheckTypeCompiler.paramTypeToStr(_signature_return_annotation)
			_returnChecker = CheckTypeCompiler.compile(
				None,											# argName
				_sType,											# sType
				_signature_return_annotation,					# typeSpec
				False,											# bKindIsArgV
				False,											# bKindIsKWArg
				inspect._empty,									# defaultValue
				outWarnList,									# outWarnList
				bDebugComp,										# nEnableDebugging
			)
			if bDebugComp:
				#if _returnChecker is not None:
				#	print("\t@@>> Signature parameter compilation for returned values:")
				#	_returnChecker.dump("\t\t|\t")
				if outWarnList:
					for warnEntry in outWarnList:
						if debugInfoComp:
							debugInfoComp.warnings.append(f"Return data: {warnEntry}")
						_PySrcHelper.warn(fn, f"Return data: {warnEntry}")

		_bIsMethod = "self" in _paramCheckers

		if debugInfoComp:
			debugInfoComp.paramCheckers = _paramCheckers
			debugInfoComp.returnChecker = _returnChecker

		# ----------------------------------------------------------------

		_logDescend = None
		if logDescend:
			_pcLog = _paramCheckers["log"]
			if _pcLog:
				#_tmp = _pcLog.sType.split(".")
				#if (_tmp[0] == "jk_logging") and (_tmp[-1].endswith("Logger")):
				#	_logDescend = logDescend
				_logDescend = logDescend

			if debugInfoComp:
				if _logDescend is None:
					debugInfoComp.warnings.append("No suitable parameter 'log' for log descent!")
				else:
					debugInfoComp.infos.append("Using log descend.")
			else:
				if _logDescend is None:
					_PySrcHelper.warn(fn, "No suitable parameter 'log' for log descent!")

		else:
			if debugInfoComp:
				debugInfoComp.infos.append("Not using log descend.")

		# ----------------------------------------------------------------

		if debugInfoComp and bDebugCompPrint:
			print()
			print("@" * 120)
			debugInfoComp.dump(prefix="@@@ ")
			print("@" * 120)
			print()

		# ----------------------------------------------------------------

		def _wrapper(*args, **kwargs):
			# bind arguments

			boundedArgs = _signature.bind(*args, **kwargs)
			#_pLog = _signature.parameters.get("log")
			#print("@@", _pLog)
			#print(dir(_pLog))

			#print("\t>> " + pprint.pformat(boundedArgs))

			# ----------------------------------------------------------------
			# check arguments. delay raising of errors to print all error messages before raising an exception.

			if bDebugRuntime:
				print("@@>> Invoking function/method: " + fn.__qualname__ + "(..)")

				err = None
				for k, v in boundedArgs.arguments.items():
					# k is the argument name
					# v is the argument value
					c = _paramCheckers.get(k)
					if c:
						if not c.__call__(v):
							print("\targument " + repr(k) + ": " + c.sType + "  =>  ✖")
							if not err:
								err = ValueError("Argument " + repr(k) + " for " + fn.__name__ + "() of type '" + repr(type(v)) + "' does not match '" + c.sType + "' as expected!")
						else:
							print("\targument " + repr(k) + ": " + c.sType + "  =>  ✔")
					else:
						print("\targument " + repr(k) + ": no constraint specified")
				if err:
					raise err

			else:
				for k, v in boundedArgs.arguments.items():
					# k is the argument name
					# v is the argument value
					c = _paramCheckers.get(k)
					if c:
						if not c.__call__(v):
							# c.dump()
							raise ValueError("Argument " + repr(k) + " for " + fn.__name__ + "() of type '" + repr(type(v)) + "' does not match '" + c.sType + "' as expected!")

			# ----------------------------------------------------------------
			# invoke the function

			if _logDescend:
				_baLogger = boundedArgs.arguments.get("log")
				if _baLogger is not None:
					# a 'log' argument is a) expected and b) has been specified; this is the normal situation => descent

					_baVerbose = boundedArgs.arguments.get("bVerbose")
					bWithholdVerbose = _baVerbose if isinstance(_baVerbose, bool) else False

					with _baLogger.descend(_logDescend.format(**boundedArgs.arguments), logLevel=logLevel, bWithhold=bLogWithhold, bWithholdVerbose=bWithholdVerbose) as log2:
						boundedArgs.arguments["log"] = log2
						ret = fn(*boundedArgs.args, **boundedArgs.kwargs)

				else:
					# a 'log' argument is a) expected and b) but has been specified; this will now result in an exception raise (= programming error by the caller)
					ret = fn(*args, **kwargs)
			else:
				# no 'log' argument is expected => no descent
				ret = fn(*args, **kwargs)

			# ----------------------------------------------------------------
			# check the return value.

			if bDebugRuntime:
				if _returnChecker:
					if not _returnChecker.__call__(ret):
						print("\treturn value: " + _returnChecker.sType + "  =>  ✖")
						raise ValueError("Return value for " + fn.__name__ + "() of type '" + repr(type(ret)) + "' does not match '" + _returnChecker.sType + "' as expected!")
					else:
						print("\treturn value: " + _returnChecker.sType + "  =>  ✔")
				else:
					print("\treturn value: no constraint specified")

			else:
				if _returnChecker:
					if not _returnChecker.__call__(ret):
						raise ValueError("Return value for " + fn.__name__ + "() of type '" + repr(type(ret)) + "' does not match '" + _returnChecker.sType + "' as expected!")

			# ----------------------------------------------------------------

			return ret
		#

		# we return a new instance of _wrapper for each annotated function
		_wrapper.orgName = fn.__name__
		_wrapper.orgQualName = fn.__qualname__			# the full qualified name
		_wrapper.orgSignature = _signature
		if bDebugComp:
			_wrapper.debugInfoCompile = debugInfoComp

		return _wrapper
	#

	# we return a new instance of _wrap_the_function for each annotated function
	return _wrap_the_function
#





