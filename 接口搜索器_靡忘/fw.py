# @author:九世
# @time:2019/6/5
# @file:fw.py


from gevent import monkey;monkey.patch_all()
import requests
import os
import gevent
from multiprocessing import Process
from configparser import ConfigParser
import re

banner='''

 _______         __ ________                    
|    ___|.-----.|__|  |  |  |.---.-.-----.-----.
|    ___||  -__||  |  |  |  ||  _  |     |  _  |
|___|    |_____||__|________||___._|__|__|___  |
                                         |_____|
'''
print(banner)

black_list=[]
bai_list=[]
dept=[]
js=[]
hei=[]
guol=[]
config={}

class Fw:
    def __init__(self,path,path2,path3,PATTERN_URl):
        self.path=path
        self.path2=path2
        self.path3=path3
        self.PATTERN_URl=PATTERN_URl

    def file_pd(self):
        if os.path.exists(path=self.path) and os.path.exists(path=self.path2) and os.path.exists(path=self.path3):
            print('[+] 找到配置文件:{}'.format(self.path))
            print('[+] 找到黑名单文件:{}'.format(self.path2))
            print('[+] 找到ini配置文件:{}'.format(self.path3))
            dk=open(self.path,'r',encoding='utf-8')
            for d in dk.readlines():
                qc="".join(d.split('\n'))
                bai_list.append(qc)

            dk2=open(self.path2,'r',encoding='utf-8')
            for d in dk2.readlines():
                qc="".join(d.split('\n'))
                black_list.append(qc)

            cf=ConfigParser()
            cf.read(self.path3)
            config['xc_size']=cf.get('config','calc_xc')
            config['search_filter']=cf.get('config','gol')
            config['search']=cf.get('config','search')
            config['id']=cf.get('config','id')
            try:
                self.respone(config['search'])
            except Exception as r:
                print(r)
        else:
            print('[-] 配置文件找不到或黑名单或ini配置文件找不到....')
            exit()

    def respone(self,url):
        headers={'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
        try:
            rqt=requests.get(url=url,headers=headers)
            if rqt.status_code==200 and rqt.text!='':
                if rqt.url not in hei:
                    for g in black_list:
                        if g in rqt.text:
                            print('黑名单匹配:{} url:{}'.format(g, rqt.url))
                            print('黑名单匹配:{} url:{}'.format(g,rqt.url),file=open('save/save.txt','a',encoding='utf-8'))
                            hei.append(rqt.url)

                if rqt.url not in hei and rqt.url not in guol:
                    print('存活url:{}'.format(rqt.url))
                    print('存活url:{}'.format(rqt.url),file=open('save/save.txt','a',encoding='utf-8'))
                    guol.append(rqt.url)

                    for b in bai_list:
                        if b in rqt.text:
                            print('白名单匹配:{} url:{}'.format(b,rqt.url))
                            print('白名单匹配:{} url:{}'.format(b, rqt.url),file=open('save/save.txt','a',encoding='utf-8'))


                    zz=re.findall(self.PATTERN_URl,rqt.text)
                    for z in zz:
                        if config['search_filter'] in z:
                            if z not in dept:
                                dept.append(z)


                    if int(config['id'])==1:
                        reg=[]
                        calc=0
                        for d in dept:
                            if calc==int(config['xc_size']):
                                p=Process(target=self.xc,args=(reg,))
                                p.start()
                                reg.clear()
                                calc=0
                            reg.append(d)
                            calc+=1

                        if len(reg)>0:
                            p = Process(target=self.xc, args=(reg,))
                            p.start()
                    else:
                        for d in dept:
                            self.respone(d)
        except Exception as r:
            print(r)

    def xc(self,rg):
        rb=[]
        for r in rg:
            rb.append(gevent.spawn(self.respone,r))

        gevent.joinall(rb)

if __name__ == '__main__':
    path='conf/config.txt'
    path2='conf/black.txt'
    path3='conf/config.ini'
    PATTERN_URl='<a.*href=\"(https?://.*?)[\"|\'].*'
    obj=Fw(path=path,path2=path2,path3=path3,PATTERN_URl=PATTERN_URl)
    obj.file_pd()