from flask import Blueprint
from flask import jsonify
import config



homepage = Blueprint('homepage', __name__)


@homepage.route("/introduce/data")  # 介绍接口
def introduce():
    return jsonify(config.introduce)


@homepage.route("/nav_links")  # 头部链接接口
def nav_links():
    return jsonify(config.nev)
