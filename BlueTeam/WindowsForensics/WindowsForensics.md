## Windows Forensics

## Windows Registry

### Windows Registry Overview
Five main keys:
- HKEY_CURRENT_USER (HKCU)
- HKEY_USERS (HKU)
- HKEY_LOCAL_MACHINE (HKLM)
- HKEY_CLASSES_ROOT (HKCR)
- HKEY_CURRENT_CONFIG (HKCC)

Majority of the registry hives are stored in the `C:\Windows\System32\config` directory.
* DEFAULT (mounted on HKEY_USERS\DEFAULT)
* SAM (Security Accounts Manager, mounted on HKEY_LOCAL_MACHINE\SAM)
* SECURITY (mounted on HKEY_LOCAL_MACHINE\SECURITY)
* SOFTWARE (mounted on HKEY_LOCAL_MACHINE\SOFTWARE)
* SYSTEM (mounted on HKEY_LOCAL_MACHINE\SYSTEM)

### System Information

OS Version:
- `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\CurrentVersion`

Computer Name:
- `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\ComputerName\ComputerName`

Timezone:
- `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\TimeZoneInformation`

Network Information:
- `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters\Interfaces`

Past Network Information:
- `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\NetworkList\Signatures\Unmanaged`
- `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\NetworkList\Signatures\Managed`

Auto-Start Programs:
- `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run`
- `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\RunOnce`

Services:
- `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services`

SAM hive contains the user account information, including the password hashes.
- `HKEY_LOCAL_MACHINE\SAM\SAM\Domains\Account\Users`

### Usage or knowledge of files 

Recent Files:
- `HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\RecentDocs`

Office Recent Files:
- `HKEY_CURRENT_USER\Software\Microsoft\Office\15.0\Word`

Windows Explorer Address / Search Bar:
- `HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\TypedPaths`
- `NTUSER.DAT\Software\Microsoft\Windows\CurrentVersion\Explorer\WordWheelQuery`