@ECHO OFF
@ECHO.
REM  Batch-File to create a BEES-Executable and create a setup.exe for the Installer


REM  Set up Install Path, You will probably have to change to your q-Nummer.
@SET InnoCompiler="C:\Users\marce\Tools\Inno Setup 6\ISCC.exe"
REM @SET MiKTeX="C:\Users\%qNumber%\Tools\MIKTexPortable\texmfs\install\MIKTeX\bin\"
@SET Python="C:\Users\marce\Tools\anaconda3\envs\python4ui\python.exe"

	
REM run cx_freeze to generate BEES
@ECHO. 
@ECHO.
@ECHO        ************************************************ 
@ECHO        **             Running cx_Freeze              ** 
@ECHO        ************************************************ 
@ECHO. 
@ECHO.

chdir ../Kniffel/
%Python% setup_cx_freeze.py build -b ..\bin\


REM REM run MiKTeX to generate BEES User Manual
REM @ECHO. 
REM @ECHO.
REM @ECHO        ************************************************ 
REM @ECHO        **             Running MiKTeX                 ** 
REM @ECHO        ************************************************ 
REM @ECHO. 
REM @ECHO.
REM chdir ../doc/UserManual/latex/
REM %MiKTeX%pdflatex.exe BEES_UserManual.tex
REM %MiKTeX%pdflatex.exe BEES_UserManual.tex
REM chdir ../../../src/



REM run InnoSetup to create setup.exe
@ECHO. 
@ECHO.
@ECHO        ************************************************ 
@ECHO        **             Running InnoSetup              ** 
@ECHO        ************************************************ 
@ECHO. 
@ECHO.


REM clean up example folder bevor packing to installer
if exist "../example/Output" rmdir /s /q "../example/Output"

%InnoCompiler% "../bin/InnoSetup/getSetupFile.iss"


REM clean up cx_Freeze
@ECHO. 
@ECHO.
@ECHO        ************************************************ 
@ECHO        **          Cleaning up cx_Freeze Data        ** 
@ECHO        ************************************************ 
@ECHO. 
@ECHO.

if exist "../bin/exe.win-amd64-3.9" rmdir /s /q "../bin/exe.win-amd64-3.9"

PAUSE
