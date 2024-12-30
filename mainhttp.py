from xml.dom import minidom
from MainModuleADM.Encryption.aes import i_decrypt

dbUser = ""
dbPassword = ""
dbName = ""
token = ""
host = ""
dbUrl = ""
dbClass = ""
google = ""
port = 6543



def loadXml():
    global dbUser, dbPassword, dbName, port, token, host, google, dbUrl, dbClass
    eElement = minidom.parse('confighttp.xml')

    if getTagValue("dbUser", eElement) != '':
        key = 'WKbWo%Grj)C6YhAq'[:16]
        try:
            dbUser = str(i_decrypt(key, getTagValue('dbUser', eElement)))
            # print(dbUser)
        except Exception as ex:
            dbUser = ""
    
    if getTagValue("dbUrl", eElement) != '':
        key = 'WKbWo%Grj)C6YhAq'[:16]
        try:
            dbUrl = str(i_decrypt(key, getTagValue('dbUrl', eElement)))
            # print(dbUser)
        except Exception as ex:
            dbUrl = ""

    if getTagValue("dbPassword", eElement) != "":
        key = 'WKbWo%Grj)C6YhAq'[:16]
        try:
            dbPassword = str(i_decrypt(key, getTagValue("dbPassword", eElement)))
            # print(dbPassword)
        except Exception as ex:
            dbPassword = ""

    if getTagValue("dbName", eElement) != "":
        key = 'WKbWo%Grj)C6YhAq'[:16]
        try:
            dbName = str(i_decrypt(key, getTagValue("dbName", eElement)))
            # print(dbName)
        except Exception as ex:
            dbName = ""


    if getTagValue("token", eElement) != "":
        key = 'WKbWo%Grj)C6YhAq'[:16]
        try:
            token = str(i_decrypt(key, getTagValue("token", eElement)))
            # print(token)
        except Exception as ex:
            token = ""
    
    if getTagValue("host", eElement) != "":
        key = 'WKbWo%Grj)C6YhAq'[:16]
        try:
            host = str(i_decrypt(key, getTagValue("host", eElement)))
            # print(host)
        except Exception as ex:
            host = ""
    
    if getTagValue("google", eElement) != "":
        key = 'WKbWo%Grj)C6YhAq'[:16]
        try:
            google = str(i_decrypt(key, getTagValue("google", eElement)))
            # print(host)
        except Exception as ex:
            google = ""


    if getTagValue("port", eElement) != "":
        port = int(getTagValue("port", eElement))
    
    if getTagValue("dbClass", eElement) != "":
        dbClass = str(getTagValue("dbClass", eElement))
    

def getTagValue(sTag, element):
    x = ''
    for nodes in element.getElementsByTagName(sTag):
        node = nodes.childNodes
        if (len(node) > 0):
            x = node[0].data
    return x

loadXml()