# QQBot集资查询插件


## 简介
在QQ群内发送命令，查询某一用户的集资记录
![demo示意图](http://a3.qpic.cn/psb?/V13aTJbk3ppHHd/D7VLPVUwRYvWXvLli*lHaaJBgY2EqhyLB5O8Os0zcCQ!/b/dG4AAAAAAAAA&ek=1&kp=1&pt=0&bo=OATsAgAAAAAREPU!&vuin=825764773&tm=1515423600&sce=60-2-2&rf=viewer_311)

## 思路介绍
* 建立数据库，使用爬虫将微打赏或摩点的集资数据保存到数据库内
* 通过QQBot设置相关查询语句，对接收到的消息内容进行切片处理（获取用户ID）
* 通过pymysql模块对数据库进行操作，将上一步中获取到的用户ID作为参数填充到SQL语句中
* 将查询结果进行处理（排版），通过QQBot发送至指定群内

## 依赖文件介绍

`config.py`
* 配置文件，用于填写相关设置


`wds_db.py`
* 用于抓取微打赏集资数据
* 使用方法
	- 运行代码，输入微打赏pro_id
	- 重复上一步骤，直至将所有集资数据存入数据库
* 注意事项：程序运行程序过程中会警告数据库已存在，忽略即可

`modian_db.py`
* 用于抓取摩点集资数据
* 使用方法同`wds_db.py`  



`query.py`
* 使用QQBot加载的查询插件
* 需要修改的参数：
   - 查询命令（默认查询命令为“集资查询”）
   - msg中的小偶像名称
 


##  更新记录


**2018.01.08更新**：初次更新，内容包含查询插件`querry.py`和爬虫`wds_db.py`、`modian_db.py`，配置文件`config.py`

