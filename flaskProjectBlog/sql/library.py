import config
from pymysql import Connect

# 创建mysql库用
coon = Connect(host=config.host, port=config.port, user=config.user, password=config.password, db='mysql')
print("ok")
with coon.cursor() as c:
    c.execute('create database MyBlog charset utf8')  # 创建库
    c.execute('show databases')
    for row in c.fetchall():  # 获取查询结果
        print(row)
