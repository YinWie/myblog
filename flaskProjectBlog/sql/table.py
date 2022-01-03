from pymysql import Connect
import config
# 创建mysql表用
coon = Connect(host=config.host,
               port=config.port,
               user=config.user,
               password=config.password,
               db=config.db,
               charset='utf8')
print("ok")
with coon.cursor() as  c:
    c.execute('drop table if exists archives')
    c.execute('drop table if exists labo')
    c.execute('drop table if exists finds')
    sql = """
       create table archives(
       id char(32) primary key,
       name varchar(50)unique,
       imglink varchar(100),
       words text,
       links varchar(100) 
       )
       """
    labo_sql = """
       create table labo(
       id char(32) primary key ,
       name varchar(50),
       imglink varchar(100),
       words text,
       links varchar(100) 
       )"""
    links_finds = """
         create table finds(
         id char(32) primary key ,
         imglink varchar(100),
         name varchar(50),
         links varchar(100) 
         )"""

    c.execute(sql)  # 创建表
    c.execute(labo_sql)  # 创建实验室表
    c.execute(links_finds)
    c.execute('show tables')
    for row in c.fetchall():  # 获取查询结果
        print(row)
