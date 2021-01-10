# ORM方式连接 MySQL 数据库
 
import pymysql
from sqlalchemy import create_engine,Table,Column,Integer,String,MetaData,ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime 
from sqlalchemy import DateTime

Base = declarative_base()

class user_table(Base): 
    __tablename__ = 'userorm' 
    user_id = Column(Integer(), primary_key=True) 
    user_name = Column(String(50)) 
    user_age = Column(Integer())
    user_birth = Column(String(30))
    user_sex = Column(String(2))
    user_edu = Column(String(4))
    user_created = Column(DateTime(),default=datetime.now)
    updated = Column(DateTime(),default=datetime.now, onupdate=datetime.now)

# 实例一个引擎
dburl="mysql+pymysql://testuser:testpass@192.168.20.62:3306/testdb?charset=utf8mb4"
engine=create_engine(dburl, echo=True, encoding="utf-8")

Base.metadata.create_all(engine)

# pymysql 插入3条测试数据
conn = pymysql.connect(host='192.168.20.62',
                       user='testuser',
                       password='testpass',
                       database='testdb')

try:
    with conn.cursor() as cursor:
        sql = 'insert into userorm (user_id,user_name,user_age,user_birth,user_sex,user_edu) values (%s,%s,%s,%s,%s,%s)'
        values = (
            (101,'test_a',20,'19001010','男','本科'),
            (102,'小明',22,'19001010','男','本科'),
            (103,'小芳',20,'19011001','女','本科')
        )
        cursor.executemany(sql,values)
    conn.commit()
    try:
        with conn.cursor() as cursor2:
            sql = 'select * from userorm'
            cursor2.execute(sql)
            for result in cursor2.fetchall():
                print(result)
    except Exception as e:
        print(f'query error {e}')
except Exception as e:
    print(f'insert error {e}')

finally:
    conn.close()
