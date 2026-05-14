version = "0.1.4.1 pre-alpha"
isdemo = True

#Note: for the people who thought changing these values like demo or te version does stuff, it doesnt.

def buildTag():
    if isdemo:
        dtag = "DEMO "
    
    ret = dtag + "v" + version
    return ret