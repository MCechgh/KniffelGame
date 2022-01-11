# -*- coding: utf-8 -*-

# A setup script to create a single executable of 
#
# Run the build process by running the command 'python setup.py build -b ..\bin\'


from cx_Freeze import *
from Info import version as __version__

company_name = "homemade"
product_name = 'Kniffel'
description = 'Kniffel as simple PC-game.'
url = 'https://github.com/MCechgh/KniffelGame'
author = 'MCechgh'
author_email = 'marcel.cech@t-online.de'

#packages = ['numpy','pkg_resources','idna','scipy']
packages = []
path = []
includes = []
include_files = []
#excludes = ['tkinter', 'scipy.spatial.cKDTree'] #exclude notwendig, damit mat export klappt

excludes = []

Kniffel_Target = Executable(
    script = "..\example\main.py",
    base = "Win32GUI",
    icon = r"media\logo\Kniffel.ico",
    shortcut_name="Kniffel", # former shortcutName
    target_name = "Kniffel.exe" # former targetName
    )

build_exe_options  = {
    "packages": packages,
    "path":path,
    "includes":includes,
    "include_files":include_files,
	"excludes":excludes,
    }    

setup(name='Kniffel',
      version=__version__,
      #company_name=company_name, # no matching cx_freeze variable
      #product_name=product_name, # no matching cx_freeze variable
      description=description,
      author=author,
      author_email=author_email,
      url=url,
      options = {"build_exe": build_exe_options
                },
      executables=[Kniffel_Target]
      )
