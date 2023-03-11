import sys
from cx_Freeze import setup, Executable

files = ['../compiled_files/backend.pyc', 'gui.qml']
packages = ["sys", "PySide6.QtGui", "PySide6.QtQml", "PySide6.QtCore", "random", "array"]
exclude = ["tkinter", "asyncio", "concurrent", "ctypes", "distutils", "email", "html", "http", "lib2to3",
           "multiprocessing", "pydoc_data", "test", "unittest", "xml", "xmlrpc"]
output_dir = "..\\build"

build_exe_options = {
    "packages": packages,
    "include_files": files,
    "excludes": exclude,
    'build_exe': output_dir,
    "build-base": output_dir
}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

target = Executable(
    script="main.py",
    base=base,
    icon="icon.ico"
)

setup(
    name="PassGen",
    version="1",
    description="Simple app for generating strong passwords",
    options={"build_exe": build_exe_options},
    executables=[target]
)
