import sqlite3


class ConnDb:
    def __init__(self):
        self.conn = sqlite3.connect("F:\VSCoding\Code\python\\bot-2\db\sign.db")  # 链接数据库
        self.curs = self.conn.cursor()  # 创建命令对象

    def addStu(self, cid, name, qq, id, state):  # 插入数据
        cid = '\''+cid+'\''
        name = '\''+name+'\''  # 字符型要加引号
        v = "%s,%s,%d,%d,%d" % (cid, name, qq, id, 0)  # 默认的状态设置为0
        self.curs.execute('insert into stu values(%s)' % v)
        self.conn.commit()  # 事件提交
        return self.conn.total_changes

    def addTeacher(self, tm, name, qq, state=0):
        """ create table teacher(
                tm int,
                name text,
                qq int,
                state int
            )
        """
        name = '\''+name+'\''  # 字符型要加引号
        v = '%d,%s,%d,%d' % (tm, name, qq, 0)  # 默认的状态设置为0
        self.curs.execute('insert into teacher values(%s)' % v)
        self.conn.commit()
        print('教师添加成功！')

    def selectStu(self, qq):  # 按照qq号来查询学生
        self.curs.execute('''
        select *
        from stu
        where qq=%d
        ''' % qq)
        results = self.curs.fetchall()
        return results

    def selectTeacher(self, qq):  # 按照qq号来查询学生
        self.curs.execute('''
        select tm, qq, name, state
        from teacher
        where qq=%d
        ''' % qq)
        results = self.curs.fetchall()
        return results

    def close(self):
        self.conn.close()  # 关闭数据库

    def deleteStu(self, id):
        self.curs.execute("DELETE from stu WHERE id=%d" % (id))  # 自己的只能删除自己的
        self.conn.commit()
        print('删除成功')
        return self.conn.total_changes  # 删除了多少数据，成功删除返回 1， 失败返回 0

    def findClass(self, cid):
        cid = '\''+cid+'\''
        self.curs.execute('''
        select *
        from cla
        where cid=%s
        ''' % cid)
        results = self.curs.fetchall()
        return results

    def execsqldir(self, sqldir):
        self.curs.execute(sqldir)
        self.conn.commit()
        print("执行成功")

    def updateStuState(self, cid):
        cid = '\''+cid+'\''
        self.curs.execute("""
        update stu
        set state=0
        where cid=%s
        """ % cid)
        self.conn.commit()
        print("状态更新成功")

    def selectAllStu(self):  # 查询所有的学生
        self.curs.execute("""
        select *
        from stu
        """)
        return self.curs.fetchall()

    def selectAllTeacher(self):  # 查询所有的老师
        self.curs.execute("""
        select *
        from teacher
        """)
        return self.curs.fetchall()

    def isTeacher(self, qq):
        self.curs.execute(
            """
            select *
            from teacher
            where qq=%d
            """ % qq
            )
        s = self.curs.fetchall()
        if(len(s)):
            return True
        else:
            return False

    def stuSign(self, qq):  # 学生签到
        self.curs.execute("""
        update stu
        set state=1
        where qq=%d
        """ % qq)  # 万一签到不成功咋办？？？？？？？？？？？？？
        self.conn.commit()
        pass

    def findAbsent(self, cid):  # 查看不在的学生
        cid = '\''+cid+'\''
        self.curs.execute("""
        select id, name
        from stu
        where state=0 and cid=%s
        """ % cid)
        return self.curs.fetchall()

    def clearTable(self, tableName):
        self.curs.execute("""
        delete
        from %s
        where name not null
        """ % tableName)
        self.conn.commit()
        print(tableName + ' 清除成功！')


def init():
    global cn
    cn = ConnDb()
    print('数据库打开成功')


def get():
    return cn


init()
cn.execsqldir("""
update stu
set times=10
""")
s = cn.selectAllStu()
print(s)
