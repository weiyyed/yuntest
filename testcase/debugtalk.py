import requests,os
import yaml
import hashlib
from selenium import webdriver

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
class GetEncryptPassword(object):
	"""docstring for ClassName"""
	def __init__(self, publicExponent,modulus,password):
		self.publicExponent = publicExponent
		self.modulus=modulus
		self.password=password
	# 使用公钥和sha256密码更新html文件
	def update_html(m_e_p_list):
		# html_url=r'E:/py_workspaces/synchronous/yuntest/testcase/encrypt_password.html'
		# html_url=os.path.join(os.getcwd(), "encrypt_password.html")
		html="encrypt_password.html"
		with open(html,encoding='utf-8') as t:
			content=t.read()
		m=r'modulus\s?=\s?"(.*)";'
		e=r'exponent\s?=\s?"(.*)";'
		p=r'pubstr\s?=\s?"(.*)";'
		# print(content)
		# t=re.search(m,content).group(1)
		# print(t)
		old_list=[re.search(re_expre,content).group(1) for re_expre in [m,e,p] ]
		# print(old_list,m_e_p_list)
		# replace=content.replace(m_old,m_new)
		r_content=content.replace(old_list[0],self.modulus).replace(old_list[1],self.exponent).replace(old_list[2],self.encryptsh256())
		with open(html_url,'w+',encoding='utf-8') as man_file:
			man_file.write(r_content)
	def encryptsh256():
		'''使用sha256加密明文密码'''
		enpass=hashlib.sha256(self.password).hexdigest()
		# 反转大小密文
		l=list(enpass)
		l.reverse()
		return ''.join(l).upper()
	def get_entry_password():
		driver=webdriver.PhantomJs()
		driver.get("encrypt_password.html")
		epass=driver.find_element_by_id('enpassword').text
		driver.quit()
		return epass
				
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




def encrypt(publicExponent,modulus,password):
	get=GetEncryptPassword(publicExponent,modulus,password)
	return get.get_entry_password()







# #测试

# jsonid=get_sessionid("trn")
# headers={
# "Accept":'application/json, text/javascript, */*; q=0.01',
# 'Cookie':'JSESSIONID=%s'%jsonid
# }
# print(headers)
# url="http://yfb-trn.hd-cloud.com/trn/TRN_SUBJECT/getMetaData"
# r=requests.get(url,headers=headers)
# rt=r.text
# print(rt)


