## 接口搜索器_靡忘 ##
conf文件夹下的
```
config.ini #配置文件
config.txt #白名单文件（要匹配的关键字放在里面）
black.txt #黑名单文件（要过滤的关键字放在里面）
```

config.ini详解
```
[config]
calc_xc=500 #当任务满多少个时开始多进程+协程 （注意：不要设置太低，否则本机或目标会死掉）
gol=baidu.com #无限爬虫时过滤关键字
search=http://baidu.com #无限爬的域名
id=0 #id为0是单线程，id为1是多进程+协程
```

本程序思路图：
![](https://s2.ax1x.com/2019/06/05/VUs9Ug.md.png)


测试图：

![](https://s2.ax1x.com/2019/06/05/VUrOgI.png)