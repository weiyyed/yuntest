#coding=utf-8
import requests
import json
from . import util

url_eam=util.geturl().get('eam')
tenantCode=util.geturl().get('tenantcode')
url_login = '{}/login'.format(util.geturl().get('passport'))
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0",
           "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
           "Accept-Language":"zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
           "Accept-Encoding":"gzip, deflate",
           "Connection":"keep-alive",
           "Upgrade-Insecure-Requests":"1",
           }
TGC="eyJhbGciOiJIUzUxMiJ9.WlhsS2FHSkhZMmxQYVVwcllWaEphVXhEU214aWJVMXBUMmxL\
UWsxVVNUUlJNRXBFVEZWb1ZFMXFWVEpKYmpBdUxrMHlWMVpGWVZGc1VXTTFlRVJ0ZW1WaWJqWktia0V1YTJKaVZGQTV\
SbTVoUW5sRmRISTJOSFJ2WkZFM1ptRnJZMmh0TUVKWVYydHRaazFWY0hOVmJHOW5UbGwxVkdWT05HZ3RVVTVFYmt3eVV\
Fc3hlWFJFZFY5bWJscDJVamRNUTFOeVNUVlJSWE52YW10U2VVaGpVVWQzTjFaMU5UWkRSVzFJWkV0V1lsVndXWE5CVFR\
sS2MwOVZWREJqZW0wM2VURk1jMGQ1VFhSaWJFWlBjbTlQU25WcmQyZ3hjbVpSTlVadVRVOUdXRXhIWVdwaVpXWlZOakZ\
rT0VoYVZuSlVWR0pYYW5JdFVtaFRNamczYkdGZldWQk5aWFI0UkVKNlZEWXdVV2Q1ZW5oTFVrVlRiVUptUWpOMVIxVmZ\
hSEY0ZEhKd1UzTlZkWGQzVW5WWE56VmlaWEF5VFM1VmFtRnBlRzQwUWtreWRVbFhTV0ZuTjAweVNIQm4.2BjtqfcN2ki\
LMd__1Cdrnft6PVCQH4vDOV9jqNERtm2YrpIpTFUXMMPwlRfkHegJgNS3xgSpEziRiLhh_SmKmw"
'''
#访问eam，获得jsessionid
cj_eam = requests.cookies.RequestsCookieJar()
cj_eam.set("TENANTCODE",tenantCode)
r_eam=requests.get(url_eam,headers=headers,cookies=cj_eam,allow_redirects=False)
jsessionid=r_eam.headers["set-cookie"].split(';')[0].split('=')[1]
#登录获取ticket
param_eam_login={"service":"http://yfb-eam.hd-cloud.com/cas",
       "tenantCode":tenantCode,
       "trial": "false"
       }
cj_eam_login = requests.cookies.RequestsCookieJar()
cj_eam_login.set("TGC",TGC)
cj_eam_login.set("TENANTCODE",tenantCode)
r_login = requests.get(url_login,cookies=cj_eam_login,
                 headers=headers,
                 params=param_eam_login,
                 allow_redirects=False
                 )
url_cas=r_login.headers.get('Location')

cj_cas = requests.cookies.RequestsCookieJar()
cj_cas.set("TENANTCODE",tenantCode)
cj_cas.set("JSESSIONID",jsessionid)
r_cas=requests.get(url_cas,cookies=cj_cas,
                   headers=headers,
                   allow_redirects=False
                    )
# print(r_cas.headers)

#eam第二次访问
cj_eam2 = requests.cookies.RequestsCookieJar()
cj_eam2.set("TENANTCODE",tenantCode)
cj_eam2.set("JSESSIONID",jsessionid)
r_eam2=requests.get(url_eam,headers=headers,cookies=cj_eam2)
print(r_eam2.json())
'''
'''获取产品会话'''
def getJsession(url):
    # 访问产品，获得jsessionid
    cj = requests.cookies.RequestsCookieJar()
    cj.set("TENANTCODE", tenantCode)
    r = requests.get(url, headers=headers, cookies=cj, allow_redirects=False)
    jsessionid = r.headers["set-cookie"].split(';')[0].split('=')[1]
    # 登录获取ticket
    param_eam_login = {"service": "http://yfb-eam.hd-cloud.com/cas",
                       "tenantCode": tenantCode,
                       "trial": "false"
                       }
    cj_eam_login = requests.cookies.RequestsCookieJar()
    cj_eam_login.set("TGC", TGC)
    cj_eam_login.set("TENANTCODE", tenantCode)
    r_login = requests.get(url_login, cookies=cj_eam_login,
                           headers=headers,
                           params=param_eam_login,
                           allow_redirects=False
                           )
    url_cas = r_login.headers.get('Location')

    cj_cas = requests.cookies.RequestsCookieJar()
    cj_cas.set("TENANTCODE", tenantCode)
    cj_cas.set("JSESSIONID", jsessionid)
    r_cas = requests.get(url_cas, cookies=cj_cas,
                         headers=headers,
                         allow_redirects=False
                         )
    return jsessionid
def geteamcookie():
    cj_eam = requests.cookies.RequestsCookieJar()
    cj_eam.set("TENANTCODE", tenantCode)
    cj_eam.set("JSESSIONID", getJsession(url_eam))
    return cj_eam
if __name__=="__main__":
    cookie=geteamcookie()

