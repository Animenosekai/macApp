"""
macApp

A macOS .app information retriever\n
© Anime no Sekai — 2020
"""
from . import utils

class NotAnApp(Exception):
    """
    When the given path is not an app
    """
    def __init__(self, message):
        super().__init__(message)

class AppNameNotFound(Exception):
    """
    When the app name is not found in the App() object
    """
    def __init__(self, message) -> None:
        super().__init__(message)
        

OPTIMIZEDPATH = utils.OptimizedPath()

class App():
    """
    Returns an app details

    path: The path of the app
    """
    def __init__(self, path) -> None:
        if utils.isdir(path):
            self.path = str(path)
            self._mdls_output = utils.check_output("mdls '" + self.path + "'", shell=True).decode("utf-8").split("\n")
            
            def _getInfoFromMdls(line, string=False):
                """
                Internal Function to parse mdls output
                """
                if string:
                    return str(line).split(" = ")[1][1:-1]
                else:
                    return str(line).split(" = ")[1]

            def _getInfoListFromMdls(index):
                """
                Internal Function to parse mdls output's lists
                """
                result = []
                index += 1
                while self._mdls_output[index].replace("\n", "") != ")":
                    _temp = utils.removeSpaceBeforeAndAfter(self._mdls_output[index].replace("\n", ""))
                    if _temp[-1] == ",":
                        _temp = _temp[:-1]
                    if _temp[0] == '"' and _temp[-1] == '"':
                        _temp = _temp[1:-1]
                    result.append(_temp)
                    index += 1
                return result
                    

            ### Init attributes
            self.display_name = None
            self.alternate_names = None
            self.category = None
            self.category_type = None
            self.bundle_id = None
            self.creation_date = None
            self.modification_date = None
            self.content_type = None
            self.content_type_tree = None
            self.copyright = None
            self.added_date = None
            self.name = None
            self.document_id = None
            self.architectures = None
            self.creator_code = None
            self.finder_flags = None
            self.has_custom_icon = None
            self.is_invisible = None
            self.has_extension_hidden = None
            self.is_stationery = None
            self.filename = None
            self.node_count = None
            self.owner_group_id = None
            self.owner_user_id = None
            self._size = None
            self.size = None
            self.type_code = None
            self.interesting_date = None
            self.type = None
            self.last_used_date = None
            self._logical_size = None
            self.logical_size = None
            self._physical_size = None
            self.physical_size = None
            self.use_count = None
            self.used_dates = None
            self.version = None
            
            for index, element in enumerate(self._mdls_output):
                if "_kMDItemDisplayNameWithExtensions" in element:
                    self.display_name = _getInfoFromMdls(element, True)
                elif "kMDItemAlternateNames" in element:
                    self.alternate_names = _getInfoListFromMdls(index)
                elif "kMDItemAppStoreCategory" in element and not "kMDItemAppStoreCategoryType" in element:
                    self.category = _getInfoFromMdls(element, True)
                elif "kMDItemAppStoreCategoryType" in element:
                    self.category_type = _getInfoFromMdls(element, True)
                elif "kMDItemCFBundleIdentifier" in element:
                    self.bundle_id = BundleID(_getInfoFromMdls(element, True))
                elif "kMDItemContentCreationDate" in element:
                    self.creation_date = _getInfoFromMdls(element)
                elif "kMDItemContentModificationDate" in element:
                    self.modification_date = _getInfoFromMdls(element)
                elif "kMDItemContentType" in element and not "kMDItemContentTypeTree" in element:
                    self.content_type = _getInfoFromMdls(element, True)
                elif "kMDItemContentTypeTree" in element:
                    self.content_type_tree = _getInfoListFromMdls(index)
                elif "kMDItemCopyright" in element:
                    self.copyright = _getInfoFromMdls(element, True)
                elif "kMDItemDateAdded" in element:
                    self.added_date = _getInfoFromMdls(element)
                elif "kMDItemDisplayName" in element:
                    self.name = _getInfoFromMdls(element, True)
                elif "kMDItemDocumentIdentifier" in element:
                    self.document_id = utils.convert_to_int(_getInfoFromMdls(element))
                elif "kMDItemExecutableArchitectures" in element:
                    self.architectures = _getInfoListFromMdls(index)
                elif "kMDItemFSCreatorCode" in element:
                    self.creator_code = _getInfoFromMdls(element, True)
                elif "kMDItemFSFinderFlags" in element:
                    self.finder_flags = utils.convert_to_int(_getInfoFromMdls(element))
                elif "kMDItemFSHasCustomIcon" in element:
                    self.has_custom_icon= utils.convert_to_boolean(_getInfoFromMdls(element))
                elif "kMDItemFSInvisible" in element:
                    self.is_invisible= utils.convert_to_boolean(_getInfoFromMdls(element))
                elif "kMDItemFSIsExtensionHidden" in element:
                    self.has_extension_hidden = utils.convert_to_boolean(_getInfoFromMdls(element))
                elif "kMDItemFSIsStationery" in element:
                    self.is_stationery = utils.convert_to_boolean(_getInfoFromMdls(element))
                elif "kMDItemFSName" in element:
                    self.filename = _getInfoFromMdls(element, True)
                elif "kMDItemFSNodeCount" in element:
                    self.node_count = utils.convert_to_int(_getInfoFromMdls(element))
                elif "kMDItemFSOwnerGroupID" in element:
                    self.owner_group_id = utils.convert_to_int(_getInfoFromMdls(element))
                elif "kMDItemFSOwnerUserID" in element:
                    self.owner_user_id = utils.convert_to_int(_getInfoFromMdls(element))
                elif "kMDItemFSSize" in element:
                    self._size = utils.convert_to_int(_getInfoFromMdls(element))
                    self.size = utils.get_scaled_size(self._size)
                elif "kMDItemFSTypeCode" in element:
                    self.type_code = _getInfoFromMdls(element, True)
                elif "kMDItemInterestingDate_Ranking" in element:
                    self.interesting_date = _getInfoFromMdls(element)
                elif "kMDItemKind" in element:
                    self.type = _getInfoFromMdls(element, True)
                elif "kMDItemLastUsedDate" in element:
                    self.last_used_date = _getInfoFromMdls(element)
                elif "kMDItemLogicalSize" in element:
                    self._logical_size = utils.convert_to_int(_getInfoFromMdls(element))
                    self.logical_size = utils.get_scaled_size(self._logical_size)
                elif "kMDItemPhysicalSize" in element:
                    self._physical_size = utils.convert_to_int(_getInfoFromMdls(element))
                    self.physical_size = utils.get_scaled_size(self._physical_size)
                elif "kMDItemUseCount" in element:
                    self.use_count = utils.convert_to_int(_getInfoFromMdls(element))
                elif "kMDItemUsedDates" in element:
                    self.used_dates = _getInfoListFromMdls(index)
                elif "kMDItemVersion" in element:
                    self.version = Version(_getInfoFromMdls(element, True))
        else:
            raise NotAnApp(str(path) + " doesn't seem to be an app")

    def __repr__(self) -> str:
        return str(self.name)

    @property
    def as_dict(self):
        return {
            "displayName": self.display_name,
            "alternateNames": self.alternate_names,
            "category": self.category,
            "categoryType": self.category_type,
            "bundleID": self.bundle_id.as_dict,
            "creationDate": self.creation_date,
            "modificationDate": self.modification_date,
            "contentType": self.content_type,
            "contentTypeTree": self.content_type_tree,
            "copyright": self.copyright,
            "addedDate": self.added_date,
            "name": self.name,
            "documentID": self.document_id,
            "architectures": self.architectures,
            "creatorCode": self.creator_code,
            "finderFlags": self.finder_flags,
            "hasCustomIcon": self.has_custom_icon,
            "isInvisible": self.is_invisible,
            "hasExtensionHidden": self.has_extension_hidden,
            "isStationery": self.is_stationery,
            "filename": self.filename,
            "nodeCount": self.node_count,
            "ownerGroupId": self.owner_group_id,
            "ownerUserId": self.owner_user_id,
            "size": self.size,
            "sizeRaw": self._size,
            "type": self.type,
            "typeCode": self.type_code,
            "interestingDate": self.interesting_date,
            "lastUsedDate": self.last_used_date,
            "logicalSize": self.logical_size,
            "logicalSizeRaw": self._logical_size,
            "physicalSize": self.physical_size,
            "physicalSizeRaw": self._physical_size,
            "useCount": self.use_count,
            "usedDates": self.used_dates,
            "version": self.version.as_dict,
            "isRunning": self.is_running,
            "pid": self.pid
        }

    @property
    def as_json(self):
        return utils.dumps(self.as_dict)

    @property
    def is_running(self):
        """
        If the app is running
        """
        if self.name is not None:
            if utils.check_output("pgrep -n " + str(self.name), shell=True).decode("utf-8").replace(" ", "").lower() in [None, "null", "(null)", "none", ""]:
                return False
            else:
                return True
        else:
            return None
    
    @property
    def pid(self):
        """
        Process ID of the app if is_running is True
        """
        if self.name is not None:
            result = utils.check_output("pgrep -n " + str(self.name), shell=True).decode("utf-8").replace(" ", "").lower()
            if result in [None, "null", "(null)", "none", ""]:
                return None
            else:
                return utils.convert_to_int(result)
        else:
            return None

    def kill(self, signal=None):
        """
        Quits the app if opened (with the given signal if specified)
        """
        if self.name is not None:
            signal = utils.signal_to_name(signal)
            if signal is not None:
                utils.check_output("killall " + signal + " " + str(self.name), shell=True)
            else:
                utils.check_output("killall " + str(self.name), shell=True)
        else:
            raise AppNameNotFound("This App object has not been initialized correcly")

    def uninstall(self, starting_path=OPTIMIZEDPATH, no_warning=False):
        """
        Uninstalls the app

        Moves all of the files found by relatives() to a folder\n
        starting_path: (optional, str or <class macApp.utils.OptimizedPath>, default: OPTIMIZEDPATH) The starting point for relatives()
        no_warning: (optional, bool, default: False) Will be passed to relatives()
        """
        iteration = 0
        resultName = self.name
        if utils.exists(resultName):
            while utils.exists(resultName + " " + str(iteration)):
                iteration += 1
            resultName = self.name + " " + str(iteration)
        utils.makedirs(resultName)

        resultFile = utils.TextFile(resultName + "/__macApp_report.txt")
        resultFile.append("         macApp Report         \n")
        resultFile.append("\n")
        resultFile.append("App Information\n")
        resultFile.append("Name: " + str(self.name) + "\n")
        resultFile.append("Display Name: " + str(self.display_name) + "\n")
        resultFile.append("Alternate Names: " + ", ".join(self.alternate_names) + "\n")
        resultFile.append("Filename: " + str(self.filename) + "\n")
        resultFile.append("Version: " + str(self.version) + "\n")
        resultFile.append("Architectures: " + ", ".join(self.architectures) + "\n")
        resultFile.append("Category: " + str(self.category) + "\n")
        resultFile.append("Category Type: " + str(self.category_type) + "\n")
        resultFile.append("Copyright: " + str(self.copyright) + "\n")
        resultFile.append("Bundle ID: " + str(self.bundle_id) + "\n")
        resultFile.append("Added Date: " + str(self.added_date) + "\n")
        resultFile.append("Creation Date: " + str(self.creation_date) + "\n")
        resultFile.append("Modification Date: " + str(self.modification_date) + "\n")
        resultFile.append("Use Count: " + str(self.use_count) + "\n")
        resultFile.append("Used Dates: " + ", ".join(self.used_dates) + "\n")
        resultFile.append("Last Used Date: " + str(self.last_used_date) + "\n")
        resultFile.append("Size: " + str(self.size) + "\n")
        resultFile.append("Logical Size: " + str(self.logical_size) + "\n")
        resultFile.append("Physical Size: " + str(self.physical_size) + "\n")
        resultFile.append("Is Invisible: " + str(self.is_invisible) + "\n")
        resultFile.append("Has Custom Icon: " + str(self.has_custom_icon) + "\n")
        resultFile.append("Has Extension Hidden: " + str(self.has_extension_hidden) + "\n")
        resultFile.append("Type: " + str(self.type) + "\n")
        resultFile.append("Content Type: " + str(self.content_type) + "\n")
        resultFile.append("Document ID: " + str(self.document_id) + "\n")
        resultFile.append("Finder Flags: " + str(self.finder_flags) + "\n")
        resultFile.append("\n")
        resultFile.append("Uninstall Report\n")
        
        def addToReport(path, destination):
            """
            Adds to the final report file
            """
            resultFile.append(path + " has been moved to " + destination + "\n")

        utils.move(self.path, resultName + "/" + utils.basename(self.path))
        addToReport(self.path, resultName + "/" + utils.basename(self.path))
        for file in self.relatives(starting_path=starting_path, no_warning=no_warning):
            filename, extension = utils.splitext(file)
            if utils.exists(filename + extension):
                iteration = 0
                while utils.exists(filename + " " + str(iteration) + extension):
                    iteration += 1
                filename = filename + " " + str(iteration)
            utils.move(file, resultName + "/" + filename + extension)
            addToReport(self.path, resultName + "/" + filename + extension)
        
        resultFile.append("\n")
        resultFile.append("\n")
        resultFile.append("Credit\n")
        resultFile.append("This file has been created by the python module macApp\n")
        resultFile.append("https://github.com/Animenosekai/macApp\n")
        resultFile.append("© Anime no Sekai — 2020\n")
    


    def relatives(self, starting_path=OPTIMIZEDPATH, no_warning=False):
        """
        Searches for all of the files which might be related to the app\n

        starting_path: Specifies the folder to start the recursion (the starting point of the search) (default to OPTIMIZEDPATH)
        no_warning: Wether you want or not to display warnings
        """
        def check_files(directory):
            """
            Recursively searches for files related to the app name
            """
            registry = []
            for file in utils.listdir(directory):
                try:
                    if self.name in file or self.bundle_id.id in file or self.bundle_id.app in file or self.filename in file or self.display_name in file:
                        registry.append(directory + "/" + file)
                    elif utils.isdir(directory + "/" + file):
                        registry = registry + check_files(directory + "/" + file)
                except:
                    pass
            return registry
        if isinstance(starting_path, utils.OptimizedPath):
            results = []
            for path in ["/Applications", utils.home + "/Applications", utils.home + "/Downloads", utils.home + "/Library", utils.home + "/Documents", "/Library/LaunchAgents", "/Library/Preferences", "/Library/Application Support", "/Library/LaunchDaemons", "/Library/StartupItems"]:
                results = results + check_files(path)
            if not no_warning:
                print("[Warning] macApp: Other locations that are known to keep apps data are ignored because too sensitive: '/Library/CoreMediaIO/Plug-Ins/DAL', 'Library/Audio/Plug-Ins/HAL', '/System/Library/Extensions', '/Library/Extensions'")
            return results
        else:
            if str(starting_path)[0] == "~":
                starting_path = utils.home + str(starting_path)[1:]
            return check_files(starting_path)
        

    
class BundleID():
    """
    Returns a BundleID object representation of the given Apple Bundle ID string
    """
    def __init__(self, bundle_id) -> None:
        self.id = str(bundle_id)
        self._id_parts = self.id.split(".")
        self.vendor_type = self._id_parts[0]
        self.vendor = self._id_parts[1]
        self.app = self._id_parts[2]

    def __repr__(self) -> str:
        return str(self.id)

    @property
    def as_dict(self):
        return {
            "id": self.id,
            "vendor": self.vendor,
            "vendorType": self.vendor_type,
            "app": self.app,
        }
    
    @property
    def as_json(self):
        return utils.dumps(self.as_dict)

class Version():
    """
    Returns a Version object representation of the given Apple application version string
    """
    def __init__(self, version) -> None:
        self.version = str(version)
        self._version_parts = self.version.split(".")
        self.major = utils.convert_to_int(self._version_parts[0])
        self.minor = utils.convert_to_int(self._version_parts[1])
        self.patch = utils.convert_to_int(self._version_parts[2])
        if len(self._version_parts) == 4:
            self.other = utils.convert_to_int(self._version_parts[3])
        elif len(self._version_parts) > 4:
            self.other = "".join(self._version_parts[2:])
        else:
            self.other = None

    def __repr__(self) -> str:
        return str(self.version)

    @property
    def as_dict(self):
        return {
            "version": self.version,
            "major": self.major,
            "minor": self.minor,
            "patch": self.patch,
            "other": self.other
        }

    @property
    def as_json(self):
        return utils.dumps(self.as_dict)