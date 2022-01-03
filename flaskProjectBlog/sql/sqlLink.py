from pymysql import Connect
import sql_config 

try:
    coon = Connect(host=sql_config.host,
                   port=sql_config.port,
                   user=sql_config.user,
                   password=sql_config.password,
                   db=sql_config.db,
                   charset='utf8')
except:
    print("链接错误")


def getMysqlData(tableName: str, dataname: str):  # 查询函数 接受参数表明和字段名
    try:
        data = []
        with coon.cursor() as c:
            sql = 'select ' + dataname + ' from ' + tableName
            c.execute(sql)
            for row in c.fetchall():
                data.append(row)
        return data
    except:
        return []
print(getMysqlData('archives', 'name,imglink,words,links'))