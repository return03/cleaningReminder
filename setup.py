import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os", "selenium"], "excludes": ["tkinter"], "include_files": ["last_ts.txt"]}

# GUI applications require a different base on Windows (the default is for
# a console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "biC_Analysis",
        version = "0.1",
        description = "Your cleaning reminder!",
        options = {"build_exe": build_exe_options},
        executables = [Executable("bigC_Analysis.py", base=base)])