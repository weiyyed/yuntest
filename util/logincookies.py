#coding=utf-8
import requests
import json
from . import util


class LoginCookies(object):
	"""docstring for LoginCookies"""
	def __init__(self):
		super(LoginCookies, self).__init__()
		self.url_eam=util.geturl().get('eam')
		self.tenantCode=util.geturl().get('tenantcode')
		self.url_login = '{}/login'.format(util.geturl().get('passport'))
		self.url_portal=util.geturl().get("portal")
		self.headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0",
		           "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
		           "Accept-Language":"zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
		           "Accept-Encoding":"gzip, deflate",
		           "Connection":"keep-alive",
		           "Upgrade-Insecure-Requests":"1",
		           }
		self.TGC="eyJhbGciOiJIUzUxMiJ9.WlhsS2FHSkhZMmxQYVVwcllWaEphVXhEU214aWJVMXBUMmxL\
		UWsxVVNUUlJNRXBFVEZWb1ZFMXFWVEpKYmpBdUxrMHlWMVpGWVZGc1VXTTFlRVJ0ZW1WaWJqWktia0V1YTJKaVZGQTV\
		SbTVoUW5sRmRISTJOSFJ2WkZFM1ptRnJZMmh0TUVKWVYydHRaazFWY0hOVmJHOW5UbGwxVkdWT05HZ3RVVTVFYmt3eVV\
		Fc3hlWFJFZFY5bWJscDJVamRNUTFOeVNUVlJSWE52YW10U2VVaGpVVWQzTjFaMU5UWkRSVzFJWkV0V1lsVndXWE5CVFR\
		sS2MwOVZWREJqZW0wM2VURk1jMGQ1VFhSaWJFWlBjbTlQU25WcmQyZ3hjbVpSTlVadVRVOUdXRXhIWVdwaVpXWlZOakZ\
		rT0VoYVZuSlVWR0pYYW5JdFVtaFRNamczYkdGZldWQk5aWFI0UkVKNlZEWXdVV2Q1ZW5oTFVrVlRiVUptUWpOMVIxVmZ\
		hSEY0ZEhKd1UzTlZkWGQzVW5WWE56VmlaWEF5VFM1VmFtRnBlRzQwUWtreWRVbFhTV0ZuTjAweVNIQm4.2BjtqfcN2kiLMd__1Cdrnft6PVCQH4vDOV9jqNERtm2YrpIpTFUXMMPwlRfkHegJgNS3xgSpEziRiLhh_SmKmw"


	def __getJsession(self,url):
		'''
		获取产品会话session
		:arg:url
		'''
		# 访问产品，获得jsessionid
		cj = requests.cookies.RequestsCookieJar()
		cj.set("TENANTCODE", self.tenantCode)
		r = requests.get(url, headers=self.headers, cookies=cj, allow_redirects=False)
		jsessionid = r.headers["set-cookie"].split(';')[0].split('=')[1]
		return jsessionid


	def __verify(self,url,jsessionid):	
		"""验证产品session有效性"""
		# 登录获取ticket
		service="{}/cas".format(url)
		param_login = {"service": service,
		                   "tenantCode": self.tenantCode,
		                   "trial": "false"
		                   }
		cj_login = requests.cookies.RequestsCookieJar()
		cj_login.set("TGC", self.TGC)
		cj_login.set("TENANTCODE", self.tenantCode)
		print("打印1")
		print(self.url_login)
		print(cj_login)
		print(self.headers)
		print(param_login)
		r_login = requests.get(self.url_login, 
							   cookies=cj_login,
		                       headers=self.headers,
		                       params=param_login,
		                       allow_redirects=False
		                       )
		url_cas = r_login.headers.get('Location')
		print("打印")
		print(r_login.text)
		#验证session
		cj_cas = requests.cookies.RequestsCookieJar()
		cj_cas.set("TENANTCODE", self.tenantCode)
		cj_cas.set("JSESSIONID", jsessionid)
		r_cas = requests.get(url_cas, cookies=cj_cas,
		                     headers=self.headers,
		                     allow_redirects=False
		                     )


	    
	def geteamcookie(self):
		jsessionid=self.__getJsession(self.url_eam)
		cj_eam = requests.cookies.RequestsCookieJar()
		cj_eam.set("TENANTCODE", self.tenantCode)
		cj_eam.set("JSESSIONID", jsessionid)
		print("jsessionid等于"+jsessionid)
		self.__verify(self.url_eam,jsessionid)
		return cj_eam

	def getTGC():
		jsessionid=self.__getJsession(self.url_portal)
	def getrequestdict():
		pass


