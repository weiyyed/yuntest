import requests,os
import yaml

#验证session
class Getsession(object):
	"""docstring for ClassName"""
	def __init__(self, productUrl,passsportUrl,cookies_dic):
		self.productUrl=productUrl
		self.passsportUrl=passsportUrl
		self.cookies_dic=cookies_dic
	# 授权session为有效
	def authorize_session(self,sessionid):
		headers=self.cookies_dic
		url="%s/login"%self.passsportUrl
		params={'service':'%s/cas'%self.productUrl}
		r_passport=requests.get(url,headers=headers,params=params,allow_redirects=False)
		#cas验证
		cas_url=r_passport.headers["Location"]
		cas_cookies = requests.cookies.RequestsCookieJar()
		cas_cookies.set('JSESSIONID',sessionid)
		r_cas=requests.get(cas_url,cookies=cas_cookies)
		return

	# 初次获取jsession
	def _get_sessionid(self):

		"""
		productName:产品名
		"""
		r=requests.get(self.productUrl,allow_redirects=False)
		sessionid=r.headers['Set-Cookie'].split(';')[0].split('=')[1]
		print(sessionid)
		return sessionid
	# 授权后获取jsession
	def get_sessionid(self):
		sessionid=self._get_sessionid()
		self.authorize_session(sessionid)

		return sessionid



def get_sessionid(productName):
	with open("conf.yml","r",encoding='utf-8') as conf:
		conf_dic=yaml.load(conf)
	# print(conf_dic.get("cookies"))
	cookies_dic=conf_dic.get("cookies")
	productUrl=conf_dic.get("url").get(productName)
	passsportUrl=conf_dic.get("url").get("passport")
	# print(conf_dic.get("url"))
	# print(productUrl,passsportUrl)
	get=Getsession(productUrl,passsportUrl,cookies_dic)
	return get.get_sessionid()


#测试

jsonid=get_sessionid("trn")
headers={
"Accept":'application/json, text/javascript, */*; q=0.01',
'Cookie':'JSESSIONID=%s'%jsonid
}
print(headers)
url="http://yfb-trn.hd-cloud.com/trn/TRN_SUBJECT/getMetaData"
r=requests.get(url,headers=headers)
rt=r.text
print(rt)


