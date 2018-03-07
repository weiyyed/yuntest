import requests,os
import yaml,re
import hashlib
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#验证session
class Getsession(object):
	
	"""使用记住密码时获取session"""
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
		# print(sessionid)
		return sessionid
	# 授权后获取jsession
	def get_sessionid(self):
		sessionid=self._get_sessionid()
		self.authorize_session(sessionid)

		return sessionid	
class GetEncryptPassword(object):
	"""使用密码登录时，获取加密的密码"""
	def __init__(self, publicExponent,modulus,password):
		self.publicExponent = publicExponent
		self.modulus=modulus
		self.password=password
		self.url_html=os.path.join(os.getcwd(),'encrypt_password.html')

	# 使用公钥和sha256密码更新html文件
	def update_html(self):
		# html_url=r'E:/py_workspaces/synchronous/yuntest/testcase/encrypt_password.html'
		# html_url=os.path.join(os.getcwd(), "encrypt_password.html")
		with open(self.url_html,encoding='utf-8') as t:
			content=t.read()
		m=r'modulus\s?=\s?"(.*)";'
		m_old=re.search(m,content).group(1)
		content=content.replace(m_old,self.modulus)
		e=r'exponent\s?=\s?"(.*)";'
		e_old=re.search(e,content).group(1)
		content=content.replace(e_old,self.publicExponent)
		p=r'pubstr\s?=\s?"(.*)";'
		p_old=re.search(p,content).group(1)
		content=content.replace(p_old,self.encryptsh256())

		# old_list=[re.search(re_expre,content).group(1) for re_expre in [m,e,p] ]
		# print(old_list,m_e_p_list)
		# replace=content.replace(m_old,m_new)
		# r_content=content.replace(old_list[0],self.modulus).replace(old_list[1],self.publicExponent).replace(old_list[2],self.encryptsh256())
		with open(self.url_html,'w+',encoding='utf-8') as man_file:
			man_file.write(content)
		# print(r_content)
	def encryptsh256(self):
		'''使用sha256加密明文密码'''
		enpass=hashlib.sha256(str(self.password).encode()).hexdigest()
		# 反转大小密文
		l=list(enpass)
		l.reverse()
		return ''.join(l).upper()
	def get_entry_password(self):
		# driver=webdriver.PhantomJS()
		self.update_html()
		chrome_options=Options()
		chrome_options.add_argument('--headless')
		chrome_options.add_argument('--disable-gpu')
		driver=webdriver.Chrome(chrome_options=chrome_options)
	
		driver.get(self.url_html)
		epass=driver.find_element_by_id('enpassword').text
		print("加密后字符串：",epass)
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
	e=get.get_entry_password()
	return e







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


