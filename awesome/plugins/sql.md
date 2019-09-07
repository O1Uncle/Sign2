create table teacher(
    tm int,
    name text,
    qq int,
    state int
)

"""
select *
from teacher
where qq=%d
""" % qq

# 建表
create table cla(  #创建班级表
cid text,
num int,
insTqq int,
Tqq int
)
create table stu(
    cid text,
    name text,
    qq int,
    id int,
    state int
)

<!-- 
[
(计科1703,'刘洋',2050503109, 201606030311, 0),
(计科1703,'袁军建',2752876977, 201606030336, 0),
(计科1703,'朱文奎',2521949301, 201606030339, 0)
]
-->

 
 

 
 
 
 
[(0, '段华斌老师', 1825868, 0),
(0, '顾思思老师', 57652261, 0),
(0, '韩国栋老师', 253524343, 0),
(0, '游珍珍老师', 18242464, 0),
(0, '张彬老师', 108484617, 0),
(0, '周华先老师', 33346893, 0),
(0, '扈乐华老师', 547587735, 0)]

init()
# s = cn.execsqldir("""
# insert into cla 
# values('计科1703', 40, 2607623712, 727260009)
# """)
cn.execsqldir("""
select *
from cla
""")
s=cn.curs.fetchall()
print(s)
# s=cn.selectAllTeacher()
# print(s)


# # print(cn.selectAllStu())

# s=[(0, '段华斌老师', 1825868, 0),
# (0, '顾思思老师', 57652261, 0),
# (0, '韩国栋老师', 253524343, 0),
# (0, '游珍珍老师', 18242464, 0),
# (0, '张彬老师', 108484617, 0),
# (0, '周华先老师', 33346893, 0),
# (0, '扈乐华老师', 547587735, 0)]
# for i in s:
#     cn.addTeacher(i[0], i[1], i[2], 0)


# s=[
# ('计科1703','刘洋',2050503109, 201606030311, 0),
# ('计科1703','袁军建',2752876977, 201606030336, 0),
# ('计科1703','朱文奎',2521949301, 201606030339, 0)
# ]
# init()

# for t in s:
#     cn.addStu(str(t[0]), str(s[1]), t[2], t[3], t[4])

# print('yes')

SQLite 的缺陷之一是它的写入操作。这个数据库同一时间只允许一个写操作，因此吞吐量有限。
cn.execsqldir("""
alter table stu
add column times int
""")

