import urllib.request

def ifUpdate(local_version, url):
    try:
        with urllib.request.urlopen(url) as r:
            return r.read().decode().strip() != local_version
    except:
        return False
