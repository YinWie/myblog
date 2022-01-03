#  友链
from flask import Blueprint
from sql import sqlLink
from flask import jsonify
import config

links = Blueprint('links', __name__)


def get_mysql_data():  # 数据库处理函数
    # 'labo', 'name,imglink,words,links' 数据库数据
    mysql_data = sqlLink.getMysqlData('finds', 'imglink,name,links')
    data, data_phon, _data, num = [], [], [], 0
    for i in mysql_data:
        num += 1
        data.append({'imgSrc': i[0], 'name': i[1], 'lk': i[2]})
        _data.append({'imgSrc': i[0], 'name': i[1], 'lk': i[2]})
        if num == 2:
            data_phon.append(_data)
            num = 0
            _data = []
    else:
        data_phon.append(_data)
    return [data, data_phon]


# imglink,name,links
@links.route("/finds_links/data")
def finds_links():
    pc, phon = get_mysql_data()
    texts = [pc, phon, config.get_he_img()
             ]

    return jsonify(texts)
