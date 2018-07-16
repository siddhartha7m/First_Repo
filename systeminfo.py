def get_registry_value(key, subkey, value):
    import _winreg
    key = getattr(_winreg, key)
    handle = _winreg.OpenKey(key, subkey)
    (value, type) = _winreg.QueryValueEx(handle, value)
    return value
 
def os_version():
    def get(key):
        return get_registry_value(
            "HKEY_LOCAL_MACHINE", 
            "SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion",
            key)
    os = get("ProductName")
    sp = get("CSDVersion")
    build = get("CurrentBuildNumber")
    return "%s %s (build %s)" % (os, sp, build)