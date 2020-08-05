#jangan di recode pliss susah di buat cok
#MR.414N
import os,sys,time,requests,re,json,random
from time import sleep
from requests import post
os.system("clear")
os.system("print WELKOM|figlet -f banner|lolcat -a")
os.system("print cara pemakaian nya silahkan chat saya|lolcat -a")
os.system("print WA=082292838634 NO gw|lolcat -a")
print ("\033[1;97m\tLogin Data\n\t\033[93m---------")
ff=input("\033[1;97m[\033[1;97m•\033[1;97m]UserAgent: \033[1;92m")
xx=input("\033[1;97m[\033[1;97m•\033[1;97m]Cookie: \033[1;92m")
oo=input("\033[1;97m[\033[1;97m•\033[1;97m]Authorization: \033[1;92m")
pp=input("\033[1;97m[\033[1;97m•\033[1;97m]Ts:\033[1;92m")
ss=input("\033[1;97m[\033[1;97m•\033[1;97m]Index: \033[1;92m")
os.system("clear")
time.sleep(2)
os.system("print MR.414N|figlet -f banner|lolcat -a")
os.system("print LOVE|figlet -f banner|lolcat -a")
os.system("print    LIA|figlet -f banner|lolcat -a")
os.system("clear")
time.sleep(2)
os.system("print ======================================|lolcat -a")
os.system("print WA= 082292838634|lolcat -a")
os.system("print author= MR.414N|lolcat -a")
os.system("print team = CYBER CRIMINAL PUBLIC|lolcat -a")
os.system("print ======================================|lolcat -a")
def login():
    print ("\033[1;97m[\033[1;93m•\033[1;97m]Sedang Login..")
    bb={
    "Host": "ai2.caping.co.id",
    "accept-language": "in",
    "networkstate": "FouthG",
    "user-agent": ff,
    "cookie": xx,
    "market": "googleplay",
    "appid": "1",
    "content-type": "application/json",
    "accept-encoding": "gzip"
    }
    data={"city":"Jakarta"}
    a=json.dumps(data)
    r = requests.post("https://ai2.caping.co.id/v2/user/login/visitor", data=a, headers=bb)
    h=json.loads(r.text)
    if "OK" in r.text:
        print ("\033[1;97m[\033[1;92m+\033[1;97m]Login Success...\n\033[1;97m[\033[1;92m+\033[1;97m]Yourname:\033[1;92m",h["data"]["user_name"])
    else:
        print ("Login gagal")
    d=requests.get("https://ai2.caping.co.id/v2/user/ccsp/detail", headers=bb)
    g=json.loads(d.text)
    if "OK" in d.text:
        print ("\033[1;97m[\033[1;92m+\033[1;97m]id mu cok:\033[1;92m",g["data"]["uid"],"\n\033[1;97m[\033[1;92m+\033[1;97m]coin mu:\033[1;92m",g["data"]["total_coin"],"\n\033[1;97m[\033[1;92m+\033[1;97m]uangmu:\033[1;92m",g["data"]["total_money"])
    else:
        sys.exit("\033[1;97m[\033[1;91m!\033[1;97m]Login gagal\033[1;91m!")
def daili():
    login()
    time.sleep(1)
    print ("\033[1;97m[\033[1;93m•\033[1;97m]Sedang Membaca Berita... tapi boong")
    time.sleep(2)
    bb={
    "Host": "ai2.caping.co.id",
    "accept-language": "in",
    "networkstate": "FouthG",
    "user-agent": ff,
    "cookie": xx,
    "market": "googleplay",
    "appid": "1",
    "authorization": oo,
    "ts": pp,
    "index": ss,
    "content-type": "application/json",
    "accept-encoding": "gzip"
    }
    for i in range(0,50):
        pg=random.randrange(1,6)
        d=json.dumps({"articleType":1,"page":pg})
        j=requests.post("https://ai2.caping.co.id/v2/news/getNewsList2", data=d, headers=bb).text
        hh=json.loads(j)
        for x in hh["data"]["list"]:
            su=x['ArticleType']
            k=x["NewsId"]
        dat=json.dumps({"reports":[{"action":"browse_news","list":[{"articleType":su,"newsId":k,"status":1,"times":4,"totalms":40},{"articleType":su,"newsId":k,"status":1,"times":3,"totalms":33},{"articleType":su,"newsId":k,"status":1,"times":2,"totalms":31}]}]})
        time.sleep(2)
        r=requests.post("https://ai2.caping.co.id/v2/event/report",data=dat, headers=bb)
        js1=json.loads(r.text)
        if js1["data"] == 0:
           print ("\033[1;97m[\033[1;91m!\033[1;97m]gagal Claim\033[1;91m!")
        else:
           print ("\033[1;97m[\033[1;92m+\033[1;97m]Claim sukses:+\033[1;92m20")

daili()
