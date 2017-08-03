# Imports in Python

## Prerequisites

### Namespace

For example, you might be writing some code that has a function called `fun()` and there is another module available, which also has a function with the name `fun()`. Now the interpreter has no way of knowing which version of `fun()` function you are referring within your code.

**Namespace** is designed to overcome this difficulty and is used to differentiate functions, classes, variables etc. with the same name, available in different modules.

### Module vs. Package

A Python **module** is simply a Python source file, which can expose classes, functions and global variables. When imported from another Python source file, the file name is sometimes treated as a namespace.

A Python **package** is simply a directory of Python module(s).

### `__init__.py`

The `__init__.py` file is the first thing that gets executed when a package is loaded.

More on the `__init__.py` file in the **Packages (with the `__init__.py` file) and Relative Imports** section.

### Relative vs. Absolute Imports

**Relative imports** - specific location of the modules to be imported are relative to the current package.

**Absolute imports** - an import where you fully specify the location of the entities being imported.


## Regular Imports

Assume the following file structure.

```sh
someDir/
	main.py
	siblingModule.py
```

The following shows different ways to import the module `siblingModule.py` into `main.py`.

```python
# siblingModule.py

def siblingModuleFun():
	print('Hello from siblingModuleFun')
	
def siblingModuleFunTwo():
	print('Hello from siblingModuleFunTwo')
```

```python
# main.py

# Provides access to all exposed functions, global variables, classes, etc.
# We need to specify the namespace explicitly, hence we always have to prepend the module name.
# Since we are not using the current files namespace, it allows us to have multiple function with the same name, from different modules.
import siblingModule

siblingModule.siblingModuleFun() # Hello from siblingModuleFun
siblingModule.siblingModuleFunTwo() # Hello from siblingModuleFunTwo

# If siblingModule is already defined in current namespace, we can use the 'as' keyword to give the module a different namespace identifier.
import siblingModule as sibMod

sibMod.siblingModuleFun() # Hello from siblingModuleFun
sibMod.siblingModuleFunTwo() # Hello from siblingModuleFunTwo

# Only imports specific entities from a module.
# Allows to access the entity without prepending module name.
# But the downside is that we are allowed to overwrite (not override) the function name and we cannot use the module name to help as reach the function.
from siblingModule import siblingModuleFun

siblingModuleFun() # Hello from siblingModuleFun

siblingModuleFunTwo() # Error
siblingModule.siblingModuleFunTwo() # Error

# Both 'from siblingModule import *' and 'import siblingModule' import all entities from the module.
# With 'import siblingModule' you are allowed to have multiple function with the same name, from different modules.
# With 'from siblingModule import *' the functions with the same name will overwrite any function from the imported module(s).
from siblingModule import *

siblingModuleFun() # Hello from siblingModuleFun
siblingModuleFunTwo() # Hello from siblingModuleFunTwo
```

## Local Imports

Importing modules at the top of the script, is importing the module into the global scope, which means that any functions will be able to use it. 

A **local import** is when you import a module into local scope, which means that it exists only within the block that it was loaded in.

```python
import globalModule  # Global scope
 
def funOne(a):

    # Local scope
    import localModule
    
    globalModule.someFunction()
    return localModule.someFunction()

def funTwo():

	globalModule.someFunction()
	return localModule.someFunction() # Error

globalModule.someFunction()
```

## Optional Imports

**Optional imports** are used when you have a preferred module or package that you want to use, but you also want a fallback in case it something goes wrong.

You might use **optional imports** to support multiple operating system, resolve issues between different versions,  etc.

```python
try:
    # Import 'someModuleA' that is only available in Windows
    import someModuleA
except ImportError:
    try:
	    # Import 'someModuleB' that is only available in Linux
        import someModuleB
    except ImportError:
```

## Circular Imports

**Circular imports** happen when you create two modules that import each other.

```python
# A.py

import B
 
def Afun():
	print('Hello from Afun')
	
B.Bfun()
Afun()
```
```sh
# B.py

import A
 
def Bfun():
	print('Hello from Bfun')
	
A.Afun()
Bfun()
```

If you run either of these modules, you should receive an `AttributeError`. This happens because both modules are attempting to import each other. Basically what’s happening here is that `A.py` is trying to import `B.py`, but it can’t do that because `B.py` is attempting to import `A.py`, which is already being executed. To prevent this kind of thing from happening, refactor your code.

## Shadowed imports

**Shadow imports** happen when the programmer creates a module with the same name as a standard Python module.

In this case, create a file named `math.py` and put the following code inside it:

```python
import math

def square_root(number):
	return math.sqrt(number)
	
square_root(72)
```

When you run a Python script, the first place Python looks for a module called `math` is in the currently running script’s directory. In this case, it finds the module we’re running and tries to use that. But our module doesn’t have a function or attribute called `sqrt`, so an `AttributeError` is raised.

## Packages (without the `__init__.py` file)

Assume the following file structure.
```sh
someDir/
	main.py
	subModules/
		subA.py
		subSubModules/
			subSubA.py
```

```python
# subA.py

def subAFun():
	print('Hello from subAFun')
	
def subAFunTwo():
	print('Hello from subAFunTwo')
```

```python
# subSubA.py

def subSubAFun():
	print('Hello from subSubAFun')
	
def subSubAFunTwo():
	print('Hello from subSubAFunTwo')
```

```python
# main.py

# Provides access to all exposed functions, global variables, public classes, etc. in a module 'subA'.
# We need to specify the namespace explicitly, hence we have to prepend the package name and/or module name.
# Since we are not using the current files namespace, it allows us to have multiple function with the same name, from different modules/packages.
import subModules.subA

subModules.subA.subAFun() # Hello from subAFun
subModules.subA.subAFunTwo() # Hello from subAFunTwo

# Only imports specific entities from a module.
# Allows to access the entity without prepending module name.
# But the downside is that we are allowed to overwrite (not override) the function name and we cannot use the module/package name to help as reach the function.
from subModules.subA import subAFun

subAFun() # Hello from subAFun
subAFunTwo() # Error

# To me, this is the most clear way of import modules from subdirectories, and it allows to differentiate between namespaces.
from subModules import subA

subA.subAFun() # Hello from subAFun
subA.subAFunTwo() # Hello from subAFunTwo
```
```python
# Importing all entities from a sub-submodule.
import subModules.subSubModules.subSubA

subModules.subSubModules.subSubA.subSubAFun() # Hello from subSubAFun
subModules.subSubModules.subSubA.subSubAFunTwo() # Hello from subSubAFunTwo

# Importing a specific entity from a sub-submodule.
from subModules.subSubModules.subSubA import subSubAFun

subSubAFun() # Hello from subSubAFun
subSubAFunTwo() # Error

# Imports all entities.
# Allows to differentiate between namespaces.
from subModules.subSubModules import subSubA

subSubA.subSubAFun() # Hello from subSubAFun
subSubA.subSubAFunTwo() # Hello from subSubAFunTwo
```

## Packages (with the `__init__.py` file) and Relative Imports

### `__init__.py`

There are two main reasons for using the `__init__.py` file.

1. For convenience,  other users will not need to know your module's exact location in the package hierarchy.

    ```sh
    someDir/
    	__init__.py
    	A.py
    	B.py
    	...
    	Z.py
    ```
    ```python
    # A.py

    def add(x, y):
    	return x + y
    ```

    ```python
    # __init__.py

    from A import *
    from B import *
    ...
    from Z import *
    ```

    Then others can call `add(x, y)` , without knowing `A.py` exists

    ```python
    from someDir import add
    ```

    Without `__init__.py`

    ```python
    from someDir.A import add
    ```

2. If you want something to be initialized as soon as the package gets executed.

### Relative Imports

Note that relative imports are not specific to `__init__.py` files.

`'__main__'` is the name of the scope in which top-level code executes. A module’s` __name__` variable is set to `'__main__'` when read from standard input, a script, or from an interactive prompt.

Relative imports use the module's ` __name__` variable to determine where it is in a package.  When you use a relative import, such as `from ..someDir import someModule`, the two dots indicate to step up a level in the package hierarchy.  For instance, if your current module is `moduleA`, then it's `__name__` variable is `someDir.subDir.moduleA`. Then, writing `from ..moduleB import *` in `moduleA` means, go up a directory, and import everything from `moduleB`. `moduleB` would be found on the same level as the `subDir` directory.

However, if your module's name is `__main__`,  you cannot use `from ..somePath import moduleName` statements.

### Loading Modules with the Help of the `init.py` File

Assume the following file structure.
```sh
someDir/
	main.py
	subModules/
		__init__.py
		subA.py
		subSubModules/
			__init__.py
			subSubA.py
```

```python
# subA.py

def subAFun():
	print('Hello from subAFun')
	
def subAFunTwo():
	print('Hello from subAFunTwo')
```

```python
# subSubA.py

def subSubAFun():
	print('Hello from subSubAFun')
	
def subSubAFunTwo():
	print('Hello from subSubAFunTwo')
```

```python
# __init__.py from subDir

# Adds 'subAFun()' and 'subAFunTwo()' to the 'subDir' namespace 
from .subA import *

# The following two import statement do the same thing, they add 'subSubAFun()' and 'subSubAFunTwo()' to the 'subDir' namespace. The first one assumes '__init__.py' is empty in 'subSubDir', and the second one, assumes '__init__.py' in 'subSubDir' contains 'from .subSubA import *'.

# Assumes '__init__.py' is empty in 'subSubDir'
# Adds 'subSubAFun()' and 'subSubAFunTwo()' to the 'subDir' namespace
from .subSubDir.subSubA import *

# Assumes '__init__.py' in 'subSubDir' has 'from .subSubA import *'
# Adds 'subSubAFun()' and 'subSubAFunTwo()' to the 'subDir' namespace
from .subSubDir import *
```

```python
# __init__.py from subSubDir

# Adds 'subSubAFun()' and 'subSubAFunTwo()' to the 'subSubDir' namespace
from .subSubA import *
```

```python
# main.py

import subDir

subDir.subAFun() # Hello from subAFun
subDir.subAFunTwo() # Hello from subAFunTwo
subDir.subSubAFun() # Hello from subSubAFun
subDir.subSubAFunTwo() # Hello from subSubAFunTwo
```

From the above, we can observe that it's almost as though `__init__.py` converts a package into a module, or more correctly makes a package behave like a module.

To access functions of `subA.py` in `subSubA.py`.
Only works if the `__name__` variable of `subSubA.py` is not `'__main__'`

```python
# subSubA.py

from ..subA import *

subAFun() # Hello from subAFun
subAFunTwo() # Hello from subAFunTwo
```
