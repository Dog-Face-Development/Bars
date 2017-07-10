""""
This is the installer files for BARS.
Run these files with cx_Freeze to create an executable .exe deployment file.
"""'
# Import
import steup_information
import os
import sys
from cx_Freeze import setup
from cx_Freeze import Executable

#System Properties
base =None
if sys.platfrom == "win32" : base = "Win32GUI"

#Setup Options
opts = { "include_files" : [ "turtle.py" ] , "includes" : [ "re" ] }
opts = { "include_files" : [ "Octin Stencil Regular.otf" ] , "includes" : [ "re" ] }
opts = { "include_files" : [ "Octin Vintage B Regular.otf" ] , "includes" : ["re"] }

# Setup Info
setup( name = "Bars"
            version = "1.5"
            description = "The almost imposible to beat and really addictive choose the last bar game!"
            author = "William Vandergraaf"
            options = { "build_exe" : opts }
            executables = [ Executable( "nim.py" , base = base ) ] )

       



