import sys
from cx_freeze import setup, Executable

#Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os"], "includes": ["PyQt5"] + ["pytube"] + ["music_main"] + ["vid_main"]}

# GUI applications require a different base on Windows (the default is for
# a console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="Downloader",
    version="0.1",
    description="Baixe músicas e vídeos de forma grátis do YouTube.",
    options={"build_exe": build_exe_options},
    executables=[Executable("main.py", base=base)]
)