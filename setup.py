#setup

import sys
from cx_Freeze import setup, Executable

if sys.platform == "win64":
    base = "Win64GUI"

includes = ["PySide.QtCore", "PySide.QtGui", "re"]


setup(

        name = "lombardia",
        version = "0.5",
        description = "game",
        option = {"build_exe": {"includes": includes}},
        executables = [Executable("Lombardia.py", base = base)],
        )
