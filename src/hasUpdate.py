def _parse(v):
    return tuple(map(int, v.split(".")))

def hasUpdate():
    VERSION_URL = "https://raw.githubusercontent.com/SantiagoCalebe/Kava/refs/heads/main/gitVersion.txt"

    try:
        with urllib.request.urlopen(VERSION_URL) as r:
            remote = r.read().decode().strip()
            return _parse(remote) > _parse(KavaVersion.VERSION)
    except:
        return False
