#   实验室
from flask import Blueprint
from sql import sqlLink
from flask import jsonify
import config

labo = Blueprint('api', __name__)


def get_mysql_data():  # 数据库处理函数
    # 'labo', 'name,imglink,words,links' 数据库数据
    mysql_data = sqlLink.getMysqlData('labo', 'name,imglink,words,links')
    data = []
    for i in mysql_data:
        data.append({'name': i[0], 'img': i[1], 'datas': i[2], 'link': i[3]})
    return data


@labo.route("/labo_content/data")
def labo_content():
    data = [get_mysql_data(), config.labo_what, config.get_he_img()]
    return jsonify(data)
