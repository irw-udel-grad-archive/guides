# Python - Quickstart

## Personal musing
For a while, I resisted learning or using Python. It seemed more wild and free than other languages, and unlike MATLAB or R, I didn't know where Python *lived*. But if you're doing any kind of scientific computing, especially using open source tools, it's hard to resist for long. So here's something to make the transition easier.

Let's get started. I'm going to assume that you're here because you actually want to run Python, so there are a couple of things to go over before you run any code.


## Setup
1. Install [Anaconda](https://www.anaconda.com/products/individual).  
    * It says data science, but think of it more broadly as scientific computing.
2. If you haven't already, install a code/text editor like VS Code, which I'll be using here.
3. Install a VS Code Python extension (ms-python.python, for example)
    * See the quickstart for a visual reference [here](https://code.visualstudio.com/docs/python/python-tutorial#_prerequisites)
4. Add the Python folder to your system's Path.  
    In the Anaconda prompt, type `where python` and copy the path before `python.exe`. Add this path to the Path environment variable.  
    * On windows, this can be accomplished by pressing the Windows key, typing "path", and going through the menu to edit the environment variables, adding something like `C:\ProgramData\Anaconda`. Don't forget to keep the slash direction consistent with the other paths here. If you run into problems later, you should also add the `Scripts` folder to the path (e.g., `C:\ProgramData\Anaconda3\Scripts`).
5. Still in Anaconda prompt, run the `init` command to allow Anaconda to work properly in the shell your system uses  

        conda init

    It's important that if on Windows, you're using the cmd Anaconda prompt, not Powershell. Powershell and Anaconda working appropriately requires permission to run scripts, which might have security implications. Since we're not trying to be security experts here, it's easier to run the cmd version. This also requires an extra step in VS Code.

    Open VS Code and use the keyboard shortcut Ctrl + Shift + P to open the command palette. Then in the input bar that pops up, type Terminal: Select Default Shell. You can type any combo of those and get there, but the important part is to select Command Prompt.

    Note: this allows the shell to use the `activate` script from conda, which allows you to load libraries, packages, modules, etc.

6. Go ahead and complete the quickstart linked in step 3, just to make sure everything runs smoothly. Because you're using Anaconda, you don't have to worry about installing packages or the virtualenv section. You can just copy-paste the code and run it. Without doing step 5, I previously had some trouble running the matplotlib example from a script. If you can run that example, everything up to here has worked, and you're all set.

Unlike R, which downloads all of your packages in one place and loads them when you call them from any script, Python works by installing outside libraries/packages/etc in just one environment. If you have conflicting dependencies, this can be a good thing, but it also introduces a new level of complexity: the virtual environment. When you work with Python, you need to tell it what _interpreter_ to use and where these files live. This is normally accomplished with `virtualenv` or `conda` environments. 

When you install Anaconda and run the Anaconda prompt, you'll be using the `base` environment. To see a list of environments on your computer and which is active, use
    
    conda env list

The active environment is denoted with an asterisk, and other environments and their paths are listed in this output. To see which packages/libraries you have installed in this environment, use

    conda list

To update any packages

    conda udpate packagename


While you _can_ run Python from the Anaconda prompt, I find it more comfortable to run from an editor like VS Code. With Python, VS Code, and the extension installed, let's go through a few examples.

## What's a module? What's a package?
You might be used to running scripts in Matlab, R, or another language. Python is interesting because you can easily break up a script into different pieces to be reused in that project or others. (That's also one thing I found challenging about reading source code in Python.) This is done by importing code from a module, package, or library. [Here's an overview of the difference.](https://www.geeksforgeeks.org/what-is-the-difference-between-p.ythons-module-package-and-library/). From the Python documentation:

> A module is a file containing Python definitions and statements.

The quickest way to understand is to do it. Create a new folder to use for your project and open it in VS Code. Mine is called get_started. Within VS Code's file explorer, add a new file via the icon or File > New File (Ctrl + N).

Taking from the Python documentation on [modules](https://docs.python.org/3/tutorial/modules.html), paste the following into the new file and save it as `fibonacci.py`

```
def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end = ' ')
        a, b = b, a+b # personal note: this defines a and b simultaneously
    print()

def fib2(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result
```

Here two functions are defined, fib and fib2. This allows you to call these functions in any other file in the same directory by adding an `import` statement to the top of your script.  

Open a blank script, and at the top, type `import fibonacci`. You can call either of the functions by adding the fibonacci prefix. Here is an example:

```
import fibonacci

fibonacci.fib(10)

```

You can also import specific definitions (recommended over importing all or `*`) and modify the names of imports for the purposes of your script.

```
from fibonacci import fib2 as fi

print(fi(10))

```

Next up, we'll look at how to make more useful things with Python, and by the end of this series, you should have a good idea of how to get started using it for your own projects.