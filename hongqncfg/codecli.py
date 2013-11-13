from occupy import File

CONF = """\
[user]
        email = hongqn@douban.com
        name = Qiangning Hong
"""


def apply():
    yield File("~hongqn/.codecli.conf", content=CONF)
