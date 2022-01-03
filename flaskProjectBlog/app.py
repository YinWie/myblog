from flask import Flask
from flask import redirect
from labo import labo
from homepage import homepage
from links import links
from archives import archives
from tools import tools
from flask_cors import CORS
import time

app = Flask(__name__)
CORS(app)
app.register_blueprint(homepage, url_prefix='/v1/api/home')
app.register_blueprint(labo, url_prefix='/v1/api/labo')
app.register_blueprint(links, url_prefix='/v1/api/links')
app.register_blueprint(archives, url_prefix='/v1/api/archives')
app.register_blueprint(tools, url_prefix='/v1/api/toolsarchives')


@app.errorhandler(404)
def page_not_found(error):
    return redirect('https://baike.baidu.com/',code=301)


if __name__ == '__main__':
	app.run(host="0.0.0.0",port=5000, debug=True,ssl_context=(
        "static/www.yinwei.icu.pem"
        ,"static/www.yinwei.icu.key"))
