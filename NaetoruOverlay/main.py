from cx_Freeze import setup, Executable

setup(
    name="SmashPros Overlay",
    version="1.0",
    description="SmashPros Overlay", 
    executables=[Executable("naeStats.py")]
)
