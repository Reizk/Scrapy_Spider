import  sqlite3
import  os
class sqlite:
    def get_conn( self,path):
        '''获取到数据库的连接对象，参数为数据库文件的绝对路径
        如果传递的参数是存在，并且是文件，那么就返回硬盘上面改
        路径下的数据库文件的连接对象；否则，返回内存中的数据接
        连接对象'''
        conn = sqlite3.connect(path)
        if os.path.exists(path) and os.path.isfile(path):
            print('硬盘上面:[{}]'.format(path))
            return conn
        else:
            conn = None
            print('内存上面:[:memory:]')
            return sqlite3.connect(':memory:')

    def get_cursor(self,conn):
        '''该方法是获取数据库的游标对象，参数为数据库的连接对象
        如果数据库的连接对象不为None，则返回数据库连接对象所创
        建的游标对象；否则返回一个游标对象，该对象是内存中数据
        库连接对象所创建的游标对象'''
        if conn is not None:
            return conn.cursor()
        else:
            return self.get_conn('').cursor()

    ###############################################################
    ####            创建|删除表操作     START
    ###############################################################
    def drop_table(self,conn, table):
        '''如果表存在,则删除表，如果表中存在数据的时候，使用该
        方法的时候要慎用！'''
        if table is not None and table != '':
            sql = 'DROP TABLE IF EXISTS ' + table
            cu = self.get_cursor(conn)
            cu.execute(sql)
            conn.commit()
            print('删除数据库表[{}]成功!'.format(table))
            self.close_all(conn, cu)
        else:
            print('the [{}] is empty or equal None!'.format(sql))

    def create_table(self,conn, sql):
        '''创建数据库表：student'''
        if sql is not None and sql != '':
            cu = self.get_cursor(conn)

            cu.execute(sql)
            conn.commit()
            print('创建数据库表[]成功!')
            self.close_all(conn, cu)
        else:
            print('the [{}] is empty or equal None!'.format(sql))

    def close_all(self,conn, cu):
        '''关闭数据库游标对象和数据库连接对象'''
        try:
            if cu is not None:
                cu.close()
        finally:
            if cu is not None:
                cu.close()

    def save(self,conn, sql, data):
        '''插入数据'''
        if sql is not None and sql != '':
            if data is not None:
                cu = self.get_cursor(conn)
                for d in data:

                    cu.execute(sql, d)
                    conn.commit()
                self.close_all(conn, cu)
        else:
            print('the [{}] is empty or equal None!'.format(sql))

    def fetchall(self,conn, sql):
        '''查询所有数据'''
        if sql is not None and sql != '':
            cu = self.get_cursor(conn)
            cu.execute(sql)
            r = cu.fetchall()
            if len(r) > 0:
                for e in range(len(r)):
                    print(r[e])
            return  r
        else:
            print('the [{}] is empty or equal None!'.format(sql))

    def fetchone(self,conn, sql, data):
        '''查询一条数据'''
        if sql is not None and sql != '':
            if data is not None:
                # Do this instead
                d = (data,)
                cu =self.get_cursor(conn)
                cu.execute(sql, d)
                r = cu.fetchall()
                if len(r) > 0:
                    for e in range(len(r)):
                        print(r[e])
            else:
                print('the [{}] equal None!'.format(data))
        else:
            print('the [{}] is empty or equal None!'.format(sql))

    def update(self,conn, sql, data):
        '''更新数据'''
        if sql is not None and sql != '':
            if data is not None:
                cu = self.get_cursor(conn)
                for d in data:

                    cu.execute(sql, d)
                    conn.commit()
                self.close_all(conn, cu)
        else:
            print('the [{}] is empty or equal None!'.format(sql))

    def delete(self,conn, sql, data):
        '''删除数据'''
        if sql is not None and sql != '':
            if data is not None:
                cu = self.get_cursor(conn)
                for d in data:
                    cu.execute(sql, d)
                    conn.commit()
                self.close_all(conn, cu)
        else:
            print('the [{}] is empty or equal None!'.format(sql))

