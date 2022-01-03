import random

"""简介配置项"""
introduce = [{'word': "kaf观测者,底层のLowb,大数据专业业余嵌入式,省赛打过一堆最高第4名,参加过国赛,菜鸡一枚。"},
             {'word': "业余爱好瞎折腾,什么东西都接触,姑且算是全栈,能拿出手的技能也就 后端开发、爬虫、运维、,其他技术水平有限，其他会的就是些大数据相关框架啊,人工智能的cnn,嵌入式等掌握很浅的技能。"},
             {'word': "写这个网站初衷是为了展示自己写过的项目,水平能力有限,网站可能有不足地方,有什么宝贵意见在本人b站私信我就ok。"},
             {'word': "本网站姑且开源,源码Github自取,仅供学习使用,使用请声明作者。"},
             {'word': "ps:要加友联的小伙伴也可以b站私信我。"}, ]
# 页头配置项
nev = [
    {'link': "/home", 'name': '首页', 'index': 1},
    {'link': "/archives", 'name': '档案馆', 'index': 1},
    {'link': "/labo", 'name': '实验室', 'index': 1},
    # {link: "/tools", name: '工具箱', index: 1},设想未实现模块等待后续开发
    {'link': "/finds", 'name': '好伙伴', 'index': 1}
]


#  随机hd图片配置项目
def get_he_img():
    img = "./static/" + str(random.randrange(1, 5)) + ".jpg"  # 修改取值范围
    return img


# 档案馆介绍
archives_what = [{'word': "1"},
                 {'word': "1"},
                 {'word': "1"},
                 {'word': "1"},
                 {'word': "1"}, ]
# 实验室介绍
labo_what = [{'word': "1"},
             {'word': "1"},
             {'word': "1"},
             {'word': "1"},
             {'word': "1"}, ]
