import urllib.request
from version import KavaVersion

def hasUpdate():
    VERSION_URL = "https://raw.githubusercontent.com/SantiagoCalebe/Kava/refs/heads/main/gitVersion.txt"
    try:
        with urllib.request.urlopen(VERSION_URL) as r:
            remote_version = r.read().decode("utf-8").strip()
            return remote_version != str(KavaVersion)
    except:
        return False
