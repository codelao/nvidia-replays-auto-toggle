#define MyAppName "nvidia replays auto toggle"
#define MyAppVersion "1.0.0"
#define MyAppPublisher "CodeLao"
#define MyAppExeName "nvidia replays auto toggle.exe"

[Setup]
AppId={{9E06367C-81A5-402F-9464-5FC179111A66}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
AppPublisher={#MyAppPublisher}
DefaultDirName={autopf}\{#MyAppName}
UninstallDisplayIcon={app}\{#MyAppExeName}
ArchitecturesAllowed=x64compatible
ArchitecturesInstallIn64BitMode=x64compatible
DefaultGroupName={#MyAppName}
DisableProgramGroupPage=yes
PrivilegesRequiredOverridesAllowed=dialog
OutputBaseFilename=install_nvidia_replays_auto_toggle_x64
SolidCompression=yes
WizardStyle=modern
DisableWelcomePage=no
LicenseFile=LICENSE.txt
WizardImageFile=qr.bmp
WizardSmallImageFile=wizard-icon.bmp

#include "customization.iss"



