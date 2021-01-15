# Python - Make an executable file

There's a good guide on this [here](https://realpython.com/pyinstaller-python/). We'll make a simple example for now. It won't do much other than show you a file picker on your computer, but that can be a nice feature to include in anything you build later on.

## Process
1. Make a script called `dialog.pyw`. The "w" just means that if you were to run the script by double clicking it, you would not see a shell appear. Paste the following into the script.

        import tkinter as tk
        from tkinter import filedialog

        root = tk.Tk()
        root.withdraw()

        # File picker
        file_path = filedialog.askopenfilename()

        # Folder picker
        dir_path = filedialog.askdirectory()

    Tkinter is a Python package that helps you build a graphical user interface (GUI). There are some other options, but this one is bundled with Python, and it's relatively easy to get started with. Read more [here](https://docs.python.org/3/library/tkinter.html).

2. In your environment, you need to install a package called PyInstaller. There are a few options for making Python files into standalone executables, but PyInstaller works well out of the box with dependencies that you'll probably use for scientific computing, and it's able to build apps for Windows, Mac, and Linux (although you'll need to build the executable on each respective OS).

        pip install pyinstaller

3. The next part is relatively simple. assuming you have your script/package ready, all you need to do is run following command, where the argument is the name of a python script.

        pyinstaller dialog.pyw

4. It may take a minute for your app to build, but you'll notice a few new additions to your working directory. The one of most interest (where your executable is) is `/dist`. There's a subfolder named after the script, and in that folder, a `.exe` with the same name. If you double click this, your script will run.

    There are a couple of nice things about this, aside from the convenience of not having you go into a shell, code editor, etc, once you have a system working.

    * You don't have to have Python installed to run this `.exe` file. 
    * All of the dependencies are packaged with your program
    * You can create a shortcut to this `.exe` and move it to a location of your liking, allowing you to run the program from anywhere on your computer
    * You can send this `\dist\...` folder to anyone, and they can run your program without installing Python or anything else. Disclaimer: you should confirm this for your specific case

    You can also add an option to package everything into one file, but this ends up being a little bit slower because all of the contents are extracted to a temporary directory. That won't be covered here.

    ## Outlook

    At this point, you've installed Python, you've modified someone else's code, made your own accessible, and figured out how to make an executable file and limit your time in the shell. Next up, we'll combine what we've learned here to make your own project: a standalone version of PyRaabe that you can send to other people -- even if they don't have Python.