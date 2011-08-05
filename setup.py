from distutils.core import setup

#This is a list of files to install, and where
#(relative to the 'root' dir, where setup.py is)
#You could be more specific.
files = ["*.py", "*.pyd", "_psycopg.pyd",]

setup(name = "win32-py26-psycopg2",
    version = "1.0",
    description = "This contains psycopg2 compiled for Windows Python 2.6",
    author = "Ed Menendez",
    author_email = "ed@menendez.com",
    url = "http://menendez.com",
    #Name the folder where your packages live:
    #(If you have other packages (dirs) or modules (py files) then
    #put them into the package directory - they will be found 
    #recursively.)
    packages = ['psycopg2'],
    #'package' package must contain files (see list above)
    #I called the package 'package' thus cleverly confusing the whole issue...
    #This dict maps the package name =to=> directories
    #It says, package *needs* these files.
    package_data = {'package' : files },
    #'runner' is in the root.
    scripts = ["runner"],
    long_description = """This will work with virtualenv on Windows.""" 
    #
    #This next part it for the Cheese Shop, look a little down the page.
    #classifiers = []     
) 
