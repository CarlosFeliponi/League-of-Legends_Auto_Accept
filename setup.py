import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == "win32":
    base = "Win32GUI"

icon = "icon.ico" 
executables = [Executable("main.py", base=base, icon=icon)]
packages = ["tkinter", "pyautogui", "os", "cv2", "numpy"]
options = {
    'build_exe': {
        'packages': packages,
        'include_files': [
            "Languages",
        ],
    },
}

setup(
    name="LOL_Auto_" \
    "Accept",
    options=options,
    version="1.0",
    description='skillz',
    executables=executables
)