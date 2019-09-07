from nonebot import on_command, CommandSession
# from nonebot import on_request, RequestSession
from .dir import init
from .dir import get
import nonebot


init()


@on_command('sign', aliases=('签到', '考勤'))
async def sign(session: CommandSession):
    dir = session.current_arg
    print(dir)
    """
    1,打开数据库
    2,验证身份
        2.1正确的话就更新学生签到状态
    3,清除学生的状态
    4,关闭数据库
    """
    # 收到签到命令之后
    qq = session.ctx['user_id']
    bot = nonebot.get_bot()
    if(get().isTeacher(int(qq))):
        cid = session.get('cid', prompt='请输入需要考勤的班级:')
        lt = get().findClass(cid)  # 查看这个班级号是否在数据库中
        if(len(lt) == 0):
            await bot.send_private_msg(user_id=qq, message='请输入正确的班级号~')
        else:
            get().updateStuState(cid)  # 初始化学生状态
            await bot.send_private_msg(user_id=qq, message='等待%s班签到中~' % cid)
    else:
        # 返回身份出错
        await bot.send_private_msg(user_id=qq, message='对不起，权限不足~')
        pass


@sign.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()
    if session.is_first_run:
        if stripped_arg:
            session.state['cid'] = stripped_arg
        return
    if not stripped_arg:
        session.pause('待考勤班级编号不能为空，请重新输入:')
    session.state[session.current_key] = stripped_arg


"""
学生答到：
    更新自己的到课状态
"""
@on_command('respond', aliases=('到', '1'))
async def respond(session: CommandSession):
    qq = session.ctx['user_id']
    get().stuSign(qq)
    bot = nonebot.get_bot()
    await bot.send_private_msg(user_id=qq, message='签到成功~')
    # print('学生应答')
    # print(qq)


"""
查看命令
    ？：是否需要验证身份
    2： 查看班级是否输入正确
    3： 统计该班级没有签到的同学
"""
@on_command('show', aliases=('查看'))
async def show(session: CommandSession):
    bot = nonebot.get_bot()
    qq = session.ctx['user_id']
    cid = session.get('cid', prompt='请输入需要查看的班级:')
    ltcid = get().findClass(cid)
    print(ltcid)
    if len(ltcid) != 0:  # 班级参数输入正确
        lt = get().findAbsent(cid)  # 万一 cid 查不到也会返回空值
        if len(lt) == 0:
            await bot.send_private_msg(user_id=qq, message=cid+'全勤')
        else:
            g = ''
            for s in lt:
                id = s[0]
                name = s[1]
                f = str(id)
                f = f + " " + str(name) + " 缺勤"
                g = g + f + '\n'
            k = len(lt)
            g = g + '\n出勤率:%d/%d' % (ltcid[0][1]-k, ltcid[0][1])
            await bot.send_private_msg(user_id=qq, message=g)
    else:
        await bot.send_private_msg(user_id=qq, message='请输入正确的班级编号')


# show.args_parser 装饰器将函数声明为 show 命令的参数解析器
# 命令解析器用于将用户输入的参数解析成命令真正需要的数据
@show.args_parser
async def _(session: CommandSession):
    # 去掉消息首尾的空白符
    stripped_arg = session.current_arg_text.strip()
    if session.is_first_run:
        # 该命令第一次运行（第一次进入命令会话）
        if stripped_arg:
            # 第一次运行参数不为空，意味着用户直接将城市名跟在命令名后面，作为参数传入
            # 例如用户可能发送了：天气 南京
            session.state['cid'] = stripped_arg
        return
    if not stripped_arg:
        # 用户没有发送有效的城市名称（而是发送了空白字符），则提示重新输入
        # 这里 session.pause() 将会发送消息并暂停当前会话（该行后面的代码不会被运行）
        session.pause('班级编号不能为空，请重新输入')

    # 如果当前正在向用户询问更多信息（例如本例中的要查询的城市），且用户输入有效，则放入会话状态
    session.state[session.current_key] = stripped_arg


# # 将函数注册为群请求处理器
# @on_request('friend')
# async def _(session: RequestSession):
#     # 判断验证信息是否符合要求
#     if session.ctx['comment'] == '1':
#         # 验证信息正确，同意好友验证
#         await session.approve()
#         return
#     # 验证信息错误，拒绝添加
#     await session.reject('认证失败')
