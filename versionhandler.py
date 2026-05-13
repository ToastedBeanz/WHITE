version = "0.1.3 pre-alpha"
isdemo = True

def buildTag():
    if isdemo:
        dtag = "DEMO "
    
    ret = dtag + "v" + version
    return ret