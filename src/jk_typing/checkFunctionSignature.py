

from collections import deque
import sys
import typing
import inspect
import pprint



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
	(sys.version_info.major == 3) and (sys.version_info.minor < 5)):
	# older python implementation are not yet mature enough.
	raise Exception("Python versions below 3.5 are not supported!")








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




class __CheckIfNone(object):
	def __init__(self, argName:str, sType:str):
		self.argName = argName
		self.sType = sType
	#
	def __call__(self, value) -> bool:
		return value is None
	#
	def dump(self, prefix:str):
		print(prefix + "__CheckIfNone<( argName=" + repr(self.argName) + ", sType=" + repr(self.sType))
		print(prefix + ")>")
	#
#

class __CheckAlwaysTrue(object):
	def __init__(self, argName:str, sType:str):
		self.argName = argName
		self.sType = sType
	#
	def __call__(self, value) -> bool:
		return True
	#
	def dump(self, prefix:str):
		print(prefix + "__CheckAlwaysTrue<( argName=" + repr(self.argName) + ", sType=" + repr(self.sType))
		print(prefix + ")>")
	#
#

class __CheckIfType(object):
	def __init__(self, argName:str, sType:str, expectedType):
		self.argName = argName
		self.sType = sType
		self.__expectedType = expectedType
	#
	def __call__(self, value) -> bool:
		if not isinstance(value, self.__expectedType):
			return False
		return True
	#
	def dump(self, prefix:str):
		print(prefix + "__CheckIfType__CheckItems<( argName=" + repr(self.argName) + ", sType=" + repr(self.sType))
		print(prefix + "\t__expectedType=" + repr(self.__expectedType))
		print(prefix + ")>")
	#
#

class __CheckIfType__CheckItems(object):
	def __init__(self, argName:str, sType:str, expectedType, nestedCheckFunc):
		self.argName = argName
		self.sType = sType
		self.__expectedType = expectedType
		self.__nestedCheckFunc = nestedCheckFunc
	#
	def __call__(self, value) -> bool:
		if not isinstance(value, self.__expectedType):
			return False
		for v in value:
			if not self.__nestedCheckFunc.__call__(v):
				return False
		return True
	#
	def dump(self, prefix:str):
		print(prefix + "__CheckIfType__CheckItems<( argName=" + repr(self.argName) + ", sType=" + repr(self.sType))
		print(prefix + "\t__expectedType=" + repr(self.__expectedType))
		print(prefix + "\t__nestedCheckFunc=")
		self.__nestedCheckFunc.dump(prefix + "\t\t")
		print(prefix + ")>")
	#
#

class __CheckIfDict(object):
	def __init__(self, argName:str, sType:str, keyCheckFunc, valueCheckFunc):
		self.argName = argName
		self.sType = sType
		self.__keyCheckFunc = keyCheckFunc
		self.__valueCheckFunc = valueCheckFunc
	#
	def __call__(self, value) -> bool:
		if not isinstance(value, dict):
			return False
		for k, v in value.items():
			if not self.__keyCheckFunc.__call__(k):
				return False
			if not self.__valueCheckFunc.__call__(v):
				return False
		return True
	#
	def dump(self, prefix:str):
		print(prefix + "__CheckIfType__CheckItems<( argName=" + repr(self.argName) + ", sType=" + repr(self.sType))
		print(prefix + "\t__keyCheckFunc=")
		self.__keyCheckFunc.dump(prefix + "\t\t")
		print(prefix + "\t__valueCheckFunc=")
		self.__valueCheckFunc.dump(prefix + "\t\t")
		print(prefix + ")>")
	#
#

class __CheckIfType__Union(object):
	def __init__(self, argName:str, sType:str, nestedCheckFuncs):
		self.argName = argName
		self.sType = sType
		self.__nestedCheckFuncs = nestedCheckFuncs
	#
	def __call__(self, value) -> bool:
		for f in self.__nestedCheckFuncs:
			if f.__call__(value):
				return True
		return False
	#
	def dump(self, prefix:str):
		print(prefix + "__CheckIfType__CheckItems<( argName=" + repr(self.argName) + ", sType=" + repr(self.sType))
		print(prefix + "\t__nestedCheckFuncs=[")
		for x in self.__nestedCheckFuncs:
			x.dump(prefix + "\t\t")
		print(prefix + "\t]")
		print(prefix + ")>")
	#
#





def _0_compile_checking(argName:typing.Union[str,None], sType:str, typeSpec, outWarnList:list):
	if typeSpec is None:
		# void
		raise Exception("Can't be void ...")

	elif typeSpec == inspect._empty:
		# nothing is specified
		return __CheckAlwaysTrue(argName, sType)

	elif isinstance(typeSpec, typing._GenericAlias):
		# generic

		if typeSpec._name == "List":
			return __CheckIfType__CheckItems(argName, sType, list, _0_compile_checking(argName, sType, typeSpec.__args__[0], outWarnList))

		elif typeSpec._name == "Tuple":
			return __CheckIfType__CheckItems(argName, sType, tuple, _0_compile_checking(argName, sType, typeSpec.__args__[0], outWarnList))

		elif typeSpec._name == "Set":
			return __CheckIfType__CheckItems(argName, sType, set, _0_compile_checking(argName, sType, typeSpec.__args__[0], outWarnList))

		elif typeSpec._name == "FrozenSet":
			return __CheckIfType__CheckItems(argName, sType, frozenset, _0_compile_checking(argName, sType, typeSpec.__args__[0], outWarnList))

		elif typeSpec._name == "Deque":
			return __CheckIfType__CheckItems(argName, sType, deque, _0_compile_checking(argName, sType, typeSpec.__args__[0], outWarnList))

		elif typeSpec._name == "Dict":
			return __CheckIfDict(argName, sType, _0_compile_checking(argName, sType, typeSpec.__args__[0], outWarnList), _0_compile_checking(argName, sType, typeSpec.__args__[1], outWarnList))

		elif typeSpec.__origin__ == typing.Union:
			return __CheckIfType__Union(argName, sType, [ _0_compile_checking(argName, sType, t, outWarnList) for t in typeSpec.__args__ ])

		else:
			if outWarnList is not None:
				outWarnList.append("Can't check this type: " + repr(typeSpec))
			return __CheckAlwaysTrue(argName, sType)

	else:
		# regular type
		return __CheckIfType(argName, sType, typeSpec)
#



#
# Compile to value checking logic and return it.
#
# @param	str argName			(optional) Argument name. If none is specified, this should be a return value.
# @param	str sType			(required) A string representation of the return type (for output).
# @param	* typeSpec			(required) A type specification object as returned by inspect
# @param	any defaultValue	(required) The default value. If it is (null) an additional check for empty data is added. Specify `inspect._empty` if not defined.
# @param	str[] outWarnList	(required) A list that receives warning messages.
# @param	Returns a callable (based on a hierarchical object model) that performs the type checking or (null) if no type checking should be performed
#
def _compile_checking(argName:typing.Union[str,None], sType:str, typeSpec, defaultValue, outWarnList:list):
	if typeSpec is None:
		# void
		return __CheckIfNone(argName, sType)

	elif typeSpec == inspect._empty:
		# nothing is specified
		return None

	elif isinstance(typeSpec, typing._GenericAlias):
		# generic

		if typeSpec._name == "List":
			ret = __CheckIfType__CheckItems(argName, sType, list, _0_compile_checking(argName, sType, typeSpec.__args__[0], outWarnList))

		elif typeSpec._name == "Tuple":
			ret = __CheckIfType__CheckItems(argName, sType, tuple, _0_compile_checking(argName, sType, typeSpec.__args__[0], outWarnList))

		elif typeSpec._name == "Set":
			ret = __CheckIfType__CheckItems(argName, sType, set, _0_compile_checking(argName, sType, typeSpec.__args__[0], outWarnList))

		elif typeSpec._name == "FrozenSet":
			ret = __CheckIfType__CheckItems(argName, sType, frozenset, _0_compile_checking(argName, sType, typeSpec.__args__[0], outWarnList))

		elif typeSpec._name == "Deque":
			ret = __CheckIfType__CheckItems(argName, sType, deque, _0_compile_checking(argName, sType, typeSpec.__args__[0], outWarnList))

		elif typeSpec._name == "Dict":
			ret = __CheckIfDict(argName, sType, _0_compile_checking(argName, sType, typeSpec.__args__[0], outWarnList), _0_compile_checking(argName, sType, typeSpec.__args__[1], outWarnList))

		elif typeSpec.__origin__ == typing.Union:
			ret = __CheckIfType__Union(argName, sType, [ _0_compile_checking(argName, sType, t, outWarnList) for t in typeSpec.__args__ ])

		else:
			if outWarnList is not None:
				outWarnList.append("Can't check this type: " + repr(typeSpec))
			ret = __CheckAlwaysTrue(argName, sType)

		if defaultValue is None:
			ret = __CheckIfType__Union(argName, sType, [ ret, __CheckIfNone(argName, sType) ])

		return ret

	else:
		# regular type
		ret = __CheckIfType(argName, sType, typeSpec)

		if defaultValue is None:
			ret = __CheckIfType__Union(argName, sType, [ ret, __CheckIfNone(argName, sType) ])

		return ret
#







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
			if not isinstance(value, deque):
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



def _getTypeDescr(t) -> str:
	if t is None:
		return "void"

	s = repr(t)
	# s should be something like this:
	#	 "<Parameter "abc">
	#	 "<Parameter "abc:int">
	#	 "<Parameter "*args">
	if s.startswith("<Parameter \"*"):
		s = s[13:-2]
	elif s.startswith("<Parameter \""):
		s = s[12:-2]
	elif s.startswith("<class '"):
		s = s[8:-2]
	else:
		return "(unknown:" + s + ")"

	pos = s.find(":")
	if pos > 0:
		return s[pos+1:].strip()
	else:
		return "?"
#


def _debug_dumpObj(prefix:str, someObj, bSkipUnderscores:bool = True, names:list = None):
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


# this is the annotation wrapper that receives arguments and returns the function that does the wrapping
def checkFunctionSignature(bDebug:bool = False, bDebugComp:bool = False, logDescend:str = None):
	assert isinstance(bDebug, bool)
	assert isinstance(bDebugComp, bool)

	# this function is executed for every function definition
	def _wrap_the_function(fn):
		#print(fn)
		annotations = typing.get_type_hints(fn)								# receives a normal dictionary
		_signature = inspect.signature(fn)
		_signature_parameters = _signature.parameters						# receives an ordered dictionary
		_signature_return_annotation = _signature.return_annotation			# receives a type annotation structure

		if bDebugComp:
			print("@@>> wrapping function " + fn.__qualname__ + "(..) with checkFunctionSignature() ...")
			for ak, av in annotations.items():
				print("\t@@>> Annotation for " + repr(ak) + ": " + str(av))
			for sk, sv in _signature_parameters.items():
				print("\t@@>> Signature parameter for " + repr(sk) + ": " + repr(sv))
				_debug_dumpObj("\t\t", sv, names = ["annotation", "default", "kind"])
				# parameters are:
				#	str sv.name				-- the name of the argument
				#	any sv.annotation		-- the type annotation structure associated with this argument (or inspect._empty if not set)
				#	obj sv.default			-- the defautl value (or inspect._empty if not set)
			print("\t@@>> Return annotation: " + str(_signature_return_annotation))

		# variables to fill during compile phase
		_paramCheckers = {}
		_returnChecker = None

		# compile

		outWarnList = []			# NOTE: we reuse this object for performance reasons
		for k, t in _signature._parameters.items():
			c = _compile_checking(k, _getTypeDescr(t), t.annotation, t.default, outWarnList)
			if bDebugComp:
				if c is not None:
					print("\t@@>> Signature parameter compilation for " + repr(k) + ":")
					c.dump("\t\t|\t")
			if bDebug:
				if outWarnList:
					for entry in outWarnList:
						print("WARNING: " + fn.__qualname__ + "(), param " + repr(t.name) + " : " + entry)
					outWarnList.clear()
			if c is not None:
				_paramCheckers[k] = c
			#print("paramCheckers[" + k + "] =", c)

		if _signature._return_annotation != inspect._empty:
			outWarnList = []
			_returnChecker = _compile_checking(None, _getTypeDescr(_signature._return_annotation), _signature._return_annotation, inspect._empty, outWarnList)
			if bDebugComp:
				if _returnChecker is not None:
					print("\t@@>> Signature parameter compilation for returned values:")
					_returnChecker.dump("\t\t|\t")
		#print("returnChecker =", repr(returnChecker.sType))
		_bIsMethod = "self" in _paramCheckers

		# ----

		_logDescend = None
		if logDescend:
			_pcLog = _paramCheckers["log"]
			if _pcLog:
				_tmp = _pcLog.sType.split(".")
				if (_tmp[0] == "jk_logging") and (_tmp[-1].endswith("Logger")):
					_logDescend = logDescend
			if bDebug and (_logDescend is None):
				print("WARNING: " + fn.__qualname__ + "() has no suitable parameter 'log' for log descent!")

		# ----

		def _wrapper(*args, **kwargs):
			# bind arguments

			boundedArgs = _signature.bind(*args, **kwargs)
			#_pLog = _signature.parameters.get("log")
			#print("@@", _pLog)
			#print(dir(_pLog))

			#print("\t>> " + pprint.pformat(boundedArgs))

			# ----------------------------------------------------------------
			# check arguments. delay raising of errors to print all error messages before raising an exception.

			if bDebug:
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
								err = ValueError("Argument " + repr(k) + " for " + fn.__name__ + "() is of type '" + repr(type(v)) + "' which does not match '" + c.sType + "' as expected!")
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
							raise ValueError("Argument " + repr(k) + " for " + fn.__name__ + "() is of type '" + repr(type(v)) + "' which does not match '" + c.sType + "' as expected!")

			# ----------------------------------------------------------------
			# invoke the function

			if _logDescend:
				_baLog = boundedArgs.arguments.get("log")
				if _baLog is not None:
					# a 'log' argument is a) expected and b) has been specified; this is the normal situation => descent
					with _baLog.descend(_logDescend.format(**boundedArgs.arguments)) as log2:
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

			if bDebug:
				if _returnChecker:
					if not _returnChecker.__call__(ret):
						print("\treturn value: " + _returnChecker.sType + "  =>  ✖")
						raise ValueError("Return value for " + fn.__name__ + "() is of type '" + repr(type(ret)) + "' which does not match '" + _returnChecker.sType + "' as expected!")
					else:
						print("\treturn value: " + _returnChecker.sType + "  =>  ✔")
				else:
					print("\treturn value: no constraint specified")

			else:
				if _returnChecker:
					if not _returnChecker.__call__(ret):
						raise ValueError("Return value for " + fn.__name__ + "() is of type '" + repr(type(ret)) + "' which does not match '" + _returnChecker.sType + "' as expected!")

			# ----------------------------------------------------------------

			return ret
		#

		_wrapper.orgName = fn.__name__
		_wrapper.orgQualName = fn.__qualname__
		return _wrapper
		#return _FunctionWrapper(fn, signature, paramCheckers, returnChecker, bDebug)
	#

	return _wrap_the_function
#





