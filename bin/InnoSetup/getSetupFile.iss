; -- Script to create Kniffel-Installer "Kniffel_setup.exe", This script runs only within the batch "CreateSetupFile.bat" and not alone by Inno Setup!!! --

[Setup]
PrivilegesRequired=lowest
; AppId={{C5F42BAE-6BC0-44BB-8C93-56737D526E56}
AppName=Kniffel
AppVersion=0.0.1
AppPublisher=MCechgh
AppPublisherURL='https://github.com/MCechgh/Kniffel'
AppSupportURL='https://github.com/MCechgh/Kniffel'
DefaultDirName={%USERPROFILE}\Tools\Kniffel
DefaultGroupName=Kniffel
Uninstallable=yes
UninstallDisplayIcon={app}\bin\Kniffel.exe
DisableProgramGroupPage=auto
OutputDir=..\
OutputBaseFilename=Kniffel_setup
SetupIconFile=..\..\Kniffel\media\logo\Kniffel.ico
WizardImageFile="..\..\Kniffel\media\logo\Kniffel_410_797.bmp"
WizardSmallImageFile="..\..\Kniffel\media\logo\Kniffel_138_140.bmp"
Compression=lzma
SolidCompression=yes
AlwaysRestart=yes

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Files]
Source: "..\exe.win-amd64-3.9\*"; DestDir: "{app}\bin"; Flags: recursesubdirs ignoreversion
;Source: "..\..\udf\*"; DestDir: "{userappdata}\Kniffel"; Flags: recursesubdirs ignoreversion
;Source: "..\..\doc\UserManual\latex\Kniffel_UserManual.pdf"; DestDir: "{app}"; Flags: ignoreversion
;Source: "..\..\example\*"; Excludes: "..\..\example\dwi\Output\*.*"; DestDir: "{app}\example\"; Flags: recursesubdirs createallsubdirs ignoreversion
Source: "..\..\README.md"; DestDir: "{app}"; Flags: ignoreversion

[Tasks]
Name: desktopicon; Description: "Create a &desktop icon"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Icons]
Name: "{group}\Kniffel"; Filename: "{app}\bin\Kniffel.exe"
;Name: "{group}\User Manual"; Filename: "{app}\Kniffel_UserManual.pdf"
;Name: "{group}\Uninstall Kniffel"; Filename: "{app}\unins000.exe";
Name: "{userdesktop}\Kniffel"; Filename: "{app}\bin\Kniffel.exe"; Tasks: desktopicon


[InstallDelete]
;Type: files; Name: {userappdata}\Kniffel\UserFunctions\prs_rag_tank_min.py


;[Registry]
; add Kniffel-Installpath to Windows PATH Environment Variable
;Root: HKCU; Subkey: "Environment"; ValueType: expandsz; ValueName: "Path"; ValueData: "{olddata}{app}\bin"; Check: NeedsAddPath(ExpandConstant('{app}\bin'));
;Flags: uninsdeletevalue;

;Function to check if Installpath is already within the Windows PATH Environment Variable
; [Code]
; function NeedsAddPath(Param: string): boolean;
; var
  ; OrigPath: string;
; begin
  ; if not RegQueryStringValue(HKEY_CURRENT_USER,'Environment', 'Path', OrigPath)
  ; then begin
    ; Result := True;
    ; exit;
  ; end;
  ; // look for the path with leading and trailing semicolon
  ; // Pos() returns 0 if not found
  ; Result := Pos(';' + UpperCase(Param) + ';', ';' + UpperCase(OrigPath) + ';') = 0;  
  ; if Result = True then
     ; Result := Pos(';' + UpperCase(Param) + '\;', ';' + UpperCase(OrigPath) + ';') = 0; 
; end;

