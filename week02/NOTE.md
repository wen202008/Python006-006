学习笔记

爬虫：
应对反爬虫，构建headers，用cookie模拟用户密码登录，user-agent模拟浏览器
使用第3方库requests来处理http相关的功能
使用第3方库lxml来处理html数据，xpath提取数据


异常处理：
try：
except：#如果不知道会产生什么异常，可以把“Exception”放在except关键字后来捕获所有异常
finally：
    #不管有无异常，这里的语句都会执行，清理收尾语句可以放这里
