"""
[
    {
        "HIVE": string,
        "PATH": string,
        "TYPE": string,
        "VULN_VAL": list,
        "SAFE_VAL": list
    }
]

<TYPE INFORMATION>:  
    0 REG_NONE
    1 REG_SZ
    2 REG_EXPAND_SZ
    3 REG_BINARY
    4 REG_DWORD   
    (https://ko.wikipedia.org/wiki/%EC%9C%88%EB%8F%84%EC%9A%B0_%EB%A0%88%EC%A7%80%EC%8A%A4%ED%8A%B8%EB%A6%AC)
"""

from data.REGO_data import *
from winreg import HKEY_CURRENT_USER, HKEY_LOCAL_MACHINE, HKEY_USERS

__all__ = ['REGO_data']

sec_reg = reg_scan_data()
mon_reg = reg_monitor_data()

mon_reg.add_key(HKEY_CURRENT_USER, 'Software\\Microsoft\\Windows\\CurrentVersion\\Run')
mon_reg.add_key(HKEY_CURRENT_USER, 'Software\\Microsoft\\Windows\\CurrentVersion\\RunOnce')

# 1. WEBCAM SHOULD BE TURNED OFF
sec_reg.add_reg(NAME="Webcam on/off",
                HIVE=HKEY_LOCAL_MACHINE,
                PATH="SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\CapabilityAccessManager\\ConsentStore\\webcam",
                ATTRIBUTE="Value", 
                TYPE=REG_SZ, 
                VULN_VAL=["Allow"], 
                SAFE_VAL=["Deny"],
                DESC="webcam should be turned off"
                )

# 2. FILE_EXT SHOULD BE REVEALED reveal 1, veal 0
sec_reg.add_reg(NAME="File Extension on/off",
                HIVE=HKEY_LOCAL_MACHINE,
                PATH="Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Advanced\\Folder\\HideFileExt",
                ATTRIBUTE="CheckedValue",
                TYPE=REG_DWORD,
                VULN_VAL=[0x0],
                SAFE_VAL=[0x1],
                DESC="fileExt should be revealed"
                )
                
# 3. Firewall on/off on 1, off 0
sec_reg.add_reg(NAME="Firewall on/off",
                HIVE=HKEY_LOCAL_MACHINE,
                PATH="SYSTEM\\CurrentControlSet\\Services\\SharedAccess\\Parameters\\FirewallPolicy\\StandardProfile",
                ATTRIBUTE="EnableFirewall",
                TYPE=REG_DWORD,
                VULN_VAL=[0x0],
                SAFE_VAL=[0x1],
                DESC="Firewall should be turned on"
                )

# 4. Firewall alert on/off on 0, off 1
sec_reg.add_reg(NAME="Firewall alert on/off",
                HIVE=HKEY_LOCAL_MACHINE,
                PATH="SYSTEM\\CurrentControlSet\\Services\\SharedAccess\\Parameters\\FirewallPolicy\\StandardProfile",
                ATTRIBUTE="DisableNotifications",
                TYPE=REG_DWORD,
                VULN_VAL=[0x1],
                SAFE_VAL=[0x0],
                DESC="Firewall alert recommended to be turned on"
                )

# 5. Clipboard history log on/off
sec_reg.add_reg(NAME="Clipboard History",
                HIVE=HKEY_LOCAL_MACHINE,
                PATH="software\\Policeis\\Microsoft\\Windows\\System",
                ATTRIBUTE="AllowClipboardHistory",
                TYPE=REG_DWORD,
                VULN_VAL=[0x0],
                SAFE_VAL=[0x1],
                DESC="Clipborad history log on/off"
                )

# 6. Lock Screen camera usable Enable 1, disable 0
sec_reg.add_reg(NAME="LockScreenCamera",
                HIVE=HKEY_LOCAL_MACHINE,
                PATH="Software\\Policies\\Microsoft\\Windows\\Personalization",
                ATTRIBUTE="NoLockScreenCamera",
                TYPE=REG_DWORD,
                VULN_VAL=[0x0],
                SAFE_VAL=[0x1],
                DESC="[RECOMMENDED] Prevent enabling lock screen camera"
                )

# 7.a. Show recently installed list on start menu Enable 1, disable 0
sec_reg.add_reg(NAME="RecentlyInstalledList",
                HIVE=HKEY_LOCAL_MACHINE,
                PATH="Software\\Policies\\Microsoft\\Windows\\Explorer",
                ATTRIBUTE="HideRecentlyAddedApps",
                TYPE=REG_DWORD,
                VULN_VAL=[0x0],
                SAFE_VAL=[0x1],
                DESC="Delete the recently added list"
)

# 7.b. Show recently installed list on start menu Enable 1, disable 0
sec_reg.add_reg(NAME="RecentlyInstalledList",
                HIVE=HKEY_CURRENT_USER,
                PATH="Software\\Policies\\Microsoft\\Windows\\Explorer",
                ATTRIBUTE="HideRecentlyAddedApps",
                TYPE=REG_DWORD,
                VULN_VAL=[0x0],
                SAFE_VAL=[0x1],
                DESC="Delete the recently added list"
)

# Internet Explorer
# Privacy
# 8.a. Turn off tracking Protection Enable 1, disable 0
sec_reg.add_reg(NAME="TrackingProtection",
                HIVE=HKEY_LOCAL_MACHINE,
                PATH="Software\\Policies\\Microsoft\\Internet Explorer\\Safety\\PrivacIE",
                ATTRIBUTE="DisableTrackingProtection",
                TYPE=REG_DWORD,
                VULN_VAL=[0x1],
                SAFE_VAL=[0x0],
                DESC="Turn off Tracking Protection"
)

# 8.b. Turn off tracking Protection Enable 1, disable 0
sec_reg.add_reg(NAME="TrackingProtection",
                HIVE=HKEY_CURRENT_USER,
                PATH="Software\\Policies\\Microsoft\\Internet Explorer\\Safety\\PrivacIE",
                ATTRIBUTE="DisableTrackingProtection",
                TYPE=REG_DWORD,
                VULN_VAL=[0x1],
                SAFE_VAL=[0x0],
                DESC="Turn off Tracking Protection"
)

# 9.a. Disable Delete Browsing History enable 1, disable 0
sec_reg.add_reg(NAME="Browsing History",
                HIVE=HKEY_LOCAL_MACHINE,
                PATH="Software\\Policies\\Microsoft\\Internet Explorer\\Control Panel",
                ATTRIBUTE="DisableDeleteBrowsingHistory",
                TYPE=REG_DWORD,
                VULN_VAL=[0x0],
                SAFE_VAL=[0x1],
                DESC="Disable delete Browsing History"
)

# 9.b. Disable Delete Browsing History enable 1, disable 0
sec_reg.add_reg(NAME="Browsing History",
                HIVE=HKEY_CURRENT_USER,
                PATH="Software\\Policies\\Microsoft\\Internet Explorer\\Control Panel",
                ATTRIBUTE="DisableDeleteBrowsingHistory",
                TYPE=REG_DWORD,
                VULN_VAL=[0x0],
                SAFE_VAL=[0x1],
                DESC="Disable delete Browsing History"
)

# 10.a. Disable Delete Download History enable 0, disable 1
sec_reg.add_reg(NAME="Download List",
                HIVE=HKEY_LOCAL_MACHINE,
                PATH="Software\\Policies\\Microsoft\\Internet Explorer\\Privacy",
                ATTRIBUTE="CleanDownloadHistory",
                TYPE=REG_DWORD,
                VULN_VAL=[0x1],
                SAFE_VAL=[0x0],
                DESC="Disable clean download history"
)

# 10.b. Disable Delete Download History enable 0, disable 1
sec_reg.add_reg(NAME="Download List",
                HIVE=HKEY_CURRENT_USER,
                PATH="Software\\Policies\\Microsoft\\Internet Explorer\\Privacy",
                ATTRIBUTE="CleanDownloadHistory",
                TYPE=REG_DWORD,
                VULN_VAL=[0x1],
                SAFE_VAL=[0x0],
                DESC="Disable clean download history"
)

# 11.a. Disable delete web site list user visit enable 0, disable 1
sec_reg.add_reg(NAME="Website History",
                HIVE=HKEY_LOCAL_MACHINE,
                PATH="Software\\Policies\\Microsoft\\Internet Explorer\\Privacy",
                ATTRIBUTE="CleanHistory",
                TYPE=REG_DWORD,
                VULN_VAL=[0x1],
                SAFE_VAL=[0x0],
                DESC="Clean website history "
)

# 11.b. Disable delete web site list user visit enable 0, disable 1
sec_reg.add_reg(NAME="Website History",
                HIVE=HKEY_CURRENT_USER,
                PATH="Software\\Policies\\Microsoft\\Internet Explorer\\Privacy",
                ATTRIBUTE="CleanHistory",
                TYPE=REG_DWORD,
                VULN_VAL=[0x1],
                SAFE_VAL=[0x0],
                DESC="Clean website history "
)

# 12.a. Disable delete passwords log enable 1, disable 0
sec_reg.add_reg(NAME="Remembered Passwords",
                HIVE=HKEY_LOCAL_MACHINE,
                PATH="Software\\Policies\\Microsoft\\Internet Explorer\\Control Panel",
                ATTRIBUTE="DisableDeletePasswords",
                TYPE=REG_DWORD,
                VULN_VAL=[0x0],
                SAFE_VAL=[0x1],
                DESC="Disable Delete Passwords"
)

# 12.b. Disable delete passwords log enable 1, disable 0
sec_reg.add_reg(NAME="Remembered Passwords",
                HIVE=HKEY_CURRENT_USER,
                PATH="Software\\Policies\\Microsoft\\Internet Explorer\\Control Panel",
                ATTRIBUTE="DisableDeletePasswords",
                TYPE=REG_DWORD,
                VULN_VAL=[0x0],
                SAFE_VAL=[0x1],
                DESC="Disable Delete Passwords"
)

# 13. Disable alert new installed app program enable 1, disable 0
sec_reg.add_reg(NAME="Alert installed app program",
                HIVE=HKEY_LOCAL_MACHINE,
                PATH="Software\\Policies\\Microsoft\\Windows\\Explorer",
                ATTRIBUTE="NoNewAppAlert",
                TYPE=REG_DWORD,
                VULN_VAL=[0x1],
                SAFE_VAL=[0x0],
                DESC="Disable alert new app"
)

# 14. Disable shell protocol protection mode enable 1, disable 0
sec_reg.add_reg(NAME="Shell protocol protection mode",
                HIVE=HKEY_LOCAL_MACHINE,
                PATH="Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\Explorer",
                ATTRIBUTE="PreXPSP2ShellProtocolBehavior",
                TYPE=REG_DWORD,
                VULN_VAL=[0x1],
                SAFE_VAL=[0x0],
                DESC="Disable shell protocol protection mode"
)

# 15. Disable Data Execution Prevention enable 1, disable 0
sec_reg.add_reg(NAME="Data execution prevention",
                HIVE=HKEY_LOCAL_MACHINE,
                PATH="Software\\Policies\\Microsoft\\Windows\\Explorer",
                ATTRIBUTE="NoDataExecutionPrevention",
                TYPE=REG_DWORD,
                VULN_VAL=[0x1],
                SAFE_VAL=[0x0],
                DESC="Disable DEP"
)

# 16. Disable file history enable 1, disable 0
sec_reg.add_reg(NAME="File history",
                HIVE=HKEY_LOCAL_MACHINE,
                PATH="Software\\Policies\\Microsoft\\Windows\\FileHistory",
                ATTRIBUTE="Disabled",
                TYPE=REG_DWORD,
                VULN_VAL=[0x1],
                SAFE_VAL=[0x0],
                DESC="Disable file history"
)


# 17. Disable user access root privilege enable 0, disable 1
sec_reg.add_reg(NAME="Access root mode",
                HIVE=HKEY_LOCAL_MACHINE,
                PATH="SOFTWARE\\Policies\\Microsoft\\Windows NT\\Terminal Services",
                ATTRIBUTE="fWritableTSCCPermTab",
                TYPE=REG_DWORD,
                VULN_VAL=[0x0],
                SAFE_VAL=[0x1],
                DESC="Disable user access root mode"
)

# 18. Ask User Authentication for remote access by network level certification enable 1, disable 0
sec_reg.add_reg(NAME="User authentication for remote access",
                HIVE=HKEY_LOCAL_MACHINE,
                PATH="SOFTWARE\\Policies\\Microsoft\\Windows NT\\Terminal Services",
                ATTRIBUTE="UserAuthentication",
                TYPE=REG_DWORD,
                VULN_VAL=[0x1],
                SAFE_VAL=[0x0],
                DESC="Ask user authentication for remote access"
)

# 19. Check always passwords for remote access enable 1, disable 0
sec_reg.add_reg(NAME="Ask password for remote access",
                HIVE=HKEY_LOCAL_MACHINE,
                PATH="SOFTWARE\\Policies\\Microsoft\\Windows NT\\Terminal Services",
                ATTRIBUTE="fPromptForPassword",
                TYPE=REG_DWORD,
                VULN_VAL=[0x0],
                SAFE_VAL=[0x1],
                DESC="Always ask password for remote access"
)

# 20. Allow Camera enable 1, disable 0
sec_reg.add_reg(NAME="Camera",
                HIVE=HKEY_LOCAL_MACHINE,
                PATH="software\\Policies\\Microsoft\\Camera",
                ATTRIBUTE="AllowCamera",
                TYPE=REG_DWORD,
                VULN_VAL=[0x1],
                SAFE_VAL=[0x0],
                DESC="[RECOMMENDED] Camera on/off"
)

# 21.a. Disable look password check box enable 1, disable 0
sec_reg.add_reg(NAME="Hidden look password button",
                HIVE=HKEY_LOCAL_MACHINE,
                PATH="Software\\Policies\\Microsoft\\Windows\\CredUI",
                ATTRIBUTE="DisablePasswordReveal",
                TYPE=REG_DWORD,
                VULN_VAL=[0x0],
                SAFE_VAL=[0x1],
                DESC="Disable password reveal"
)

# 21.b. Disable look password check box enable 1, disable 0
sec_reg.add_reg(NAME="Hidden look password button",
                HIVE=HKEY_CURRENT_USER,
                PATH="Software\\Policies\\Microsoft\\Windows\\CredUI",
                ATTRIBUTE="DisablePasswordReveal",
                TYPE=REG_DWORD,
                VULN_VAL=[0x0],
                SAFE_VAL=[0x1],
                DESC="Disable password reveal"
)

# 22. Disable asking authentication question to local user enable 1, disable 0
sec_reg.add_reg(NAME="Password reset question",
                HIVE=HKEY_LOCAL_MACHINE,
                PATH="Software\\Policies\\Microsoft\\Windows\\System",
                ATTRIBUTE="NoLocalPasswordResetQuestions",
                TYPE=REG_DWORD,
                VULN_VAL=[0x1],
                SAFE_VAL=[0x0],
                DESC="No Local Password reset questions"
)
# 23. Show administrators list when user have administrator privilege enable 1, disable 0
sec_reg.add_reg(NAME="Enumerate Administrators",
                HIVE=HKEY_LOCAL_MACHINE,
                PATH="Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\CredUI",
                ATTRIBUTE="EnumerateAdministrators",
                TYPE=REG_DWORD,
                VULN_VAL=[0x0],
                SAFE_VAL=[0x1],
                DESC="When local user have administrator privilege, enumerate administrators"
)

# 24. Disable Windows location provider enable 1, disable 0
sec_reg.add_reg(NAME="Windows location provider",
                HIVE=HKEY_LOCAL_MACHINE,
                PATH="Software\\Policies\\Microsoft\\Windows\\LocationAndSensors",
                ATTRIBUTE="DisableWindowsLocationProvider",
                TYPE=REG_DWORD,
                VULN_VAL=[0x0],
                SAFE_VAL=[0x1],
                DESC="Disable windows location provider"
)

# 25. Disable sensors enable 1, disable 0
sec_reg.add_reg(NAME="Sensors",
                HIVE=HKEY_LOCAL_MACHINE,
                PATH="Software\\Policies\\Microsoft\\Windows\\LocationAndSensors",
                ATTRIBUTE="DisableSensors",
                TYPE=REG_DWORD,
                VULN_VAL=[0x0],
                SAFE_VAL=[0x1],
                DESC="[OPTIONAL] disable sensors"
)

# 26. Disable Location enable 1, disable 0
sec_reg.add_reg(NAME="Location",
                HIVE=HKEY_LOCAL_MACHINE,
                PATH="Software\\Policies\\Microsoft\\Windows\\LocationAndSensors",
                ATTRIBUTE="DisableLocation",
                TYPE=REG_DWORD,
                VULN_VAL=[0x0],
                SAFE_VAL=[0x1],
                DESC="[RECOMMENDED] disable location"
)
# 27. Disable location scripting enable 1, disable 0
sec_reg.add_reg(NAME="Location Scripting",
                HIVE=HKEY_LOCAL_MACHINE,
                PATH="Software\\Policies\\Microsoft\\Windows\\LocationAndSensors",
                ATTRIBUTE="DisableLocationScripting",
                TYPE=REG_DWORD,
                VULN_VAL=[0x0],
                SAFE_VAL=[0x1],
                DESC="Disable location scripting"
)

# 28. Disable sound recoder enable 1, disable 0
sec_reg.add_reg(NAME="Sound rec",
                HIVE=HKEY_LOCAL_MACHINE,
                PATH="SOFTWARE\\Policies\\Microsoft\\SoundRecorder",
                ATTRIBUTE="Soundrec",
                TYPE=REG_DWORD,
                VULN_VAL=[0x0],
                SAFE_VAL=[0x1],
                DESC="[RECOMMENDED] Disable sound recoder"
)

# 29. Hide user protection area section enable 1, disable 0
sec_reg.add_reg(NAME="User protection area section",
                HIVE=HKEY_LOCAL_MACHINE,
                PATH="SOFTWARE\\Policies\\Microsoft\\Windows Defender Security Center\\Account protection",
                ATTRIBUTE="UILockdown",
                TYPE=REG_DWORD,
                VULN_VAL=[0x0],
                SAFE_VAL=[0x1],
                DESC="Hidden user protection section"
)

# 30. Hide ransomware recovery enable 1, disalbe 0
sec_reg.add_reg(NAME="RansomwareRecovery",
                HIVE=HKEY_LOCAL_MACHINE,
                PATH="SOFTWARE\\Policies\\Microsoft\\Windows Defender Security Center\\Virus and threat protection",
                ATTRIBUTE="HideRansomwareRecovery",
                TYPE=REG_DWORD,
                VULN_VAL=[0x0],
                SAFE_VAL=[0x1],
                DESC="Hide Ransomware recovery"
)

# 31. Hide virus and vul UI enable 1, disable 0
sec_reg.add_reg(NAME="Virus and danger section",
                HIVE=HKEY_LOCAL_MACHINE,
                PATH="SOFTWARE\\Policies\\Microsoft\\Windows Defender Security Center\\Virus and threat protection",
                ATTRIBUTE="UILockdown",
                TYPE=REG_DWORD,
                VULN_VAL=[0x1],
                SAFE_VAL=[0x0],
                DESC="Hide virus and danger section"
)

# 32. Hide firewall and network protection section enable 1, disable 0
sec_reg.add_reg(NAME="Firewall and network protection section",
                HIVE=HKEY_LOCAL_MACHINE,
                PATH="SOFTWARE\\Policies\\Microsoft\\Windows Defender Security Center\\Firewall and network protection",
                ATTRIBUTE="UILockdown",
                TYPE=REG_DWORD,
                VULN_VAL=[0x1],
                SAFE_VAL=[0x0],
                DESC="Hide firewall and network protection section"
)

# 33. Disable all notifications enable 1, disable 0
sec_reg.add_reg(NAME="AllNotifications",
                HIVE=HKEY_LOCAL_MACHINE,
                PATH="SOFTWARE\\Policies\\Microsoft\\Windows Defender Security Center\\Notifications",
                ATTRIBUTE="DisableNotifications",
                TYPE=REG_DWORD,
                VULN_VAL=[0x1],
                SAFE_VAL=[0x0],
                DESC="Disable all notifications"
)

# 34. Disable enhanced notifications enable 1, disable 0
sec_reg.add_reg(NAME="EnhancedNotifications",
                HIVE=HKEY_LOCAL_MACHINE,
                PATH="SOFTWARE\\Policies\\Microsoft\\Windows Defender Security Center\\Notifications",
                ATTRIBUTE="DisableEnhancedNotifications",
                TYPE=REG_DWORD,
                VULN_VAL=[0x1],
                SAFE_VAL=[0x0],
                DESC="Disable enhanced notifications"
)

# 35. Disallow exploit protection override enable 1, disable 0
sec_reg.add_reg(NAME="Exploit protection override",
                HIVE=HKEY_LOCAL_MACHINE,
                PATH="SOFTWARE\\Policies\\Microsoft\\Windows Defender Security Center\\App and Browser protection",
                ATTRIBUTE="DisallowExploitProtectionOverride",
                TYPE=REG_DWORD,
                VULN_VAL=[0x0],
                SAFE_VAL=[0x1],
                DESC="Disallow Exploit Protection Override"
)

# 36. Hide app and browser protection section enable 1, disable 0
sec_reg.add_reg(NAME="AppBrowserProtectionsection",
                HIVE=HKEY_LOCAL_MACHINE,
                PATH="SOFTWARE\\Policies\\Microsoft\\Windows Defender Security Center\\App and Browser protection",
                ATTRIBUTE="UILockdown",
                TYPE=REG_DWORD,
                VULN_VAL=[0x1],
                SAFE_VAL=[0x0],
                DESC="Hide app and browser protection section"
)

# 37. Hide secure boot section enable 1, disable 0
sec_reg.add_reg(NAME="Secure Boot",
                HIVE=HKEY_LOCAL_MACHINE,
                PATH="SOFTWARE\\Policies\\Microsoft\\Windows Defender Security Center\\Device security",
                ATTRIBUTE="HideSecureBoot",
                TYPE=REG_DWORD,
                VULN_VAL=[0x1],
                SAFE_VAL=[0x0],
                DESC="Hide Secure boot"
)

# 38. Hide device security section enable 1, disable 0
sec_reg.add_reg(NAME="Device Security section",
                HIVE=HKEY_LOCAL_MACHINE,
                PATH="SOFTWARE\\Policies\\Microsoft\\Windows Defender Security Center\\Device security",
                ATTRIBUTE="UILockdown",
                TYPE=REG_DWORD,
                VULN_VAL=[0x1],
                SAFE_VAL=[0x0],
                DESC="Hide device security section"
)

# 39. Hide the device performance & health section enable 1, disable 0
sec_reg.add_reg(NAME="Device performance and health section",
                HIVE=HKEY_LOCAL_MACHINE,
                PATH="SOFTWARE\\Policies\\Microsoft\\Windows Defender Security Center\\Device performance and health",
                ATTRIBUTE="UILockdown",
                TYPE=REG_DWORD,
                VULN_VAL=[0x1],
                SAFE_VAL=[0x0],
                DESC="Hide the device performance and health section"
)

# 40. User Account Control: Detect application installations and prompt for elevation default 1 home, 0 enterprise
sec_reg.add_reg(NAME="UAC",
                HIVE=HKEY_LOCAL_MACHINE,
                PATH="SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System",
                ATTRIBUTE="EnableInstallerDetection",
                TYPE=REG_DWORD,
                VULN_VAL=[0x0],
                SAFE_VAL=[0x1],
                DESC="[RECOMMENDED] 1 for Home, 0 for enterprise"
)

# 41. Display Last Log on info enable 1, disable 0
sec_reg.add_reg(NAME="LogOnInfo",
                HIVE=HKEY_LOCAL_MACHINE,
                PATH="Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System",
                ATTRIBUTE="DisplayLastLogonInfo",
                TYPE=REG_DWORD,
                VULN_VAL=[0x0],
                SAFE_VAL=[0x1],
                DESC="Display last log on info"
)

# 42. User Account Control: Behavior of the elevation prompt for standard users
# 0 = Automatically deny elevation requests
# 1 = Prompt for credentials on the secure desktop
# 3 (Default) = Prompt for credentials
sec_reg.add_reg(NAME="UAC:ElevationPromt",
                HIVE=HKEY_LOCAL_MACHINE,
                PATH="SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System",
                ATTRIBUTE="ConsentPromptBehaviorUser",
                TYPE=REG_DWORD,
                VULN_VAL=[0x0],
                SAFE_VAL=[0x3],
                DESC="User Account Control: Behavior of the elevation prompt for standard users"
)

# 43. Always install with elevated privileges enable 1, disable 0
sec_reg.add_reg(NAME="FreeInstall",
                HIVE=HKEY_LOCAL_MACHINE,
                PATH="software\\policies\\microsoft\\windows\\installer",
                ATTRIBUTE="AlwaysInstallElevated",
                TYPE=REG_DWORD,
                VULN_VAL=[0x1],
                SAFE_VAL=[0x0],
                DESC="Always install with elevated privileges"
)

# 44. No start windows security center 2 auto, 3 manual, 4 not use
sec_reg.add_reg(NAME="StartSecurityCenter",
                HIVE=HKEY_LOCAL_MACHINE,
                PATH="HKEY_LOCAL_MACHINE\\SYSTEM\\ControlSet001\\Services\\wscsvc",
                ATTRIBUTE="start",
                TYPE=REG_DWORD,
                VULN_VAL=[0x4],
                SAFE_VAL=[0x3],
                DESC="No start windows security center"
)


#####################################################################################################################s