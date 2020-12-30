# macApp
 A macOS .app information retriever for Python 3

# Installation
`pip install macApp --upgrade`

Works for Python >=3.1

# Usage
```python
>>> import macApp
>>> macApp.App(<path>)
'App Name'
# Example:
>>> VSCode = macApp.App("/Applications/Visual Studio Code - Insiders.app")
>>> VSCode.architectures
['arm64']
>>> VSCode.used_dates
['2020-12-24 08:00:00 +0000', '2020-12-24 23:00:00 +0000', '2020-12-25 23:00:00 +0000', '2020-12-26 23:00:00 +0000', '2020-12-27 23:00:00 +0000', '2020-12-28 23:00:00 +0000', '2020-12-29 23:00:00 +0000']
>>> VSCode.size
'276.41MB'
>>> VSCode.copyright
'Copyright (C) 2019 Microsoft. All rights reserved'
>>> VSCode.creation_date
'2020-12-16 00:00:00 +0000'
>>> VSCode.bundle_id
'com.microsoft.VSCodeInsiders'
>>> VSCode.bundle_id.vendor
'microsoft'
>>> VSCode.bundle_id.app
'VSCodeInsiders'
>>> VSCode.bundle_id.version
'1.53.0-insider'
>>> VSCode.bundle_id.version.major
1
>>> VSCode.as_dict
{'displayName': 'Visual Studio Code - Insiders.app', 'alternateNames': ['Visual Studio Code - Insiders.app'], 'category': 'public.app-category.developer-tools', 'categoryType': None, 'bundleID': {'id': 'com.microsoft.VSCodeInsiders', [...] 'minor': 53, 'patch': 0, 'other': None}}
```

# Methods
- kill(signal=None)
> Closes the app if running (is_running == True)  
>> The 'signal' parameter is used specify a special signal used with `killall`

- relatives(starting_path=OPTIMIZEDPATH, no_warning=False)
> Searches for all of the files which might be related to the app    
>> The 'starting_path' parameter is used specify which directory (folder) to start searching from  
>> The 'no_warning' parameter is used specify if macApp should display warnings or not  
>>> OPTIMIZEDPATH or macApp.utils.OptimizedPath() is a variable used to indicate relatives() that we want to search through predefined paths which are more likely to have files related to the app

- uninstall(starting_path=OPTIMIZEDPATH, no_warning=False)
> Moves all of the files found by relatives() to a folder and creates a report  
>> 'starting_path' is the same as the one on relatives()  
>> 'no_warning' is the same as the one on relatives()

# How does it work
macApp parses the result from the shell macOS built-in shell command `mdls` to retrieve information about the app

# Dependencies
This module uses one dependency to ensure that created reports are safely written to
- safeIO

# Credit
```
macApp by Anime no Sekai

© Anime no Sekai — 2020
```