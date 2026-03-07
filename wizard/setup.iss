#define MyAppName "nvidia replays auto-enable"
#define MyAppVersion "1.0.2-beta"
#define MyAppPublisher "CodeLao"
#define MyAppExeName "nvidia replays auto-enable.exe"

[Setup]
AppId={{6623B84F-6630-48EC-94EE-81503759B4A6}
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
OutputBaseFilename=x64_nvidia_replays_auto-enable_{#MyAppVersion}
SolidCompression=yes
WizardStyle=modern
DisableWelcomePage=no
LicenseFile=LICENSE.txt
WizardImageFile=qr.bmp
WizardSmallImageFile=wizard-small.bmp

#include "customization.iss"



