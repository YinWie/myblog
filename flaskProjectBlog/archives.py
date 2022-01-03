#  档案馆
from flask import Blueprint
from flask import jsonify
from sql import sqlLink
import config
archives = Blueprint('archives', __name__)
data = sqlLink.getMysqlData('archives', 'name,imglink,words,links')


# 'archives', 'name,imglink,words,links'
def get_mysql_data():# 数据库处理函数
    mysql_data = sqlLink.getMysqlData('archives', 'name,imglink,words,links')
    data = []
    for i in mysql_data:
        data.append({'name': i[0], 'img': i[1], 'datas': i[2], 'link': i[3]})
    return data


@archives.route("/project_data")
def project_data():
    data = [get_mysql_data(), config.archives_what, config.get_he_img()]
    return jsonify(data)
