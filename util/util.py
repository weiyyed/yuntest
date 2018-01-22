import json
import configparser
import os
import projroot

def readjson(filename):
    path=r"..\..\testdata\\"
    file='{}{}.json'.format(path,filename)
    with open(file, 'r', encoding='utf-8') as es:
        return json.load(es)


def geturl():
    """
    得到配置文件中url的字典
    :return:字典
    """
    path=os.path.join(projroot.PROJECT_ROOT,r'conf\testconf.conf')
    cf=configparser.ConfigParser()
    cf.read(path)
    # print(cf.sections())
    item=dict(cf.items("url"))
    return item
# geturl()
