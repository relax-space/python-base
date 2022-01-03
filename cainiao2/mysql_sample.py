'''
说明：创建数据库，创建表，添加列，增删改查
'''

from mysql.connector import connect


def conn():
    # mydb = connect(host='localhost',
    #                port='3306',
    #                user='root',
    #                passwd='1234')
    # mycursor = mydb.cursor()
    # # mycursor.execute('create database test1;')
    # mycursor.execute('show databases;')
    # for i in mycursor:
    #     print(i)
    # print('==========')
    # mycursor.close()
    # mydb.close()
    mydb = connect(host='localhost',
                   port='3306',
                   user='root',
                   passwd='1234',
                   database='test1')
    # mycursor.execute('create table book(name varchar(255),price int);')
    # mycursor.execute('show tables;')
    # for i in mycursor:
    #     print(i)
    # mycursor.execute('alter table book add column id int auto_increment primary key')
    return mydb


def add(mydb):
    mycursor = mydb.cursor()
    mycursor.executemany(
        'insert into book(name,price) values(%s,%s)', [('python', 100), ('python', 200)])
    mydb.commit()
    print(f'插入时影响的行数：{mycursor.rowcount}')
    mycursor.close()
    pass


def delete(mydb):
    mycursor = mydb.cursor()
    mycursor.execute('delete from book where price = %s', (200,))
    mydb.commit()
    print(f'删除：受影响的行：{mycursor.rowcount}')
    mycursor.close()
    
    pass


def update(mydb):
    cur = mydb.cursor()
    cur.execute('update book set price = %s where price = %s', (101, 100))
    mydb.commit()
    print(f'更新：受影响的行{cur.rowcount}')
    cur.close()
    
    pass


def select(mydb):
    mycursor = mydb.cursor()
    mycursor.execute('select * from book')
    res = mycursor.fetchall()
    print(f'查询结果：{res}')
    mycursor.close()
    
    pass


def truncate(mydb):
    cur = mydb.cursor()
    cur.execute('truncate table book;')
    mydb.commit()
    print(f'清空表：受影响的行{cur.rowcount}')
    cur.close()
    


def main():
    mydb = conn()
    truncate(mydb)
    select(mydb)
    add(mydb)
    select(mydb)
    delete(mydb)
    select(mydb)
    update(mydb)
    select(mydb)


if __name__ == '__main__':
    main()
