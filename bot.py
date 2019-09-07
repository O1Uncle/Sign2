import nonebot
import config
from os import path


# 小心端口被占用


if __name__ == '__main__':
    nonebot.init(config)  # 必须在使用NoneBot的任何功能之前调用 （必须要有）
    # nonebot.load_builtin_plugins()  # 加载了NoneBot的内置插件，不是必须的
    nonebot.load_plugins(
        path.join(path.dirname(__file__), 'awesome', 'plugins'),
        'awesome.plugins'
    )
    nonebot.run()  # host='127.0.0.1', port='8080'
