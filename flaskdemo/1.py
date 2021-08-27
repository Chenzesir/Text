import datetime
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, UniqueConstraint, Index

Base = declarative_base()


class Users(Base):
    __tablename__ = 'users'                #表名称
    id = Column(Integer, primary_key=True) # primary_key=True设置主键
    name = Column(String(32), index=True, nullable=False) #index=True创建索引， nullable=False不为空。

def init_db(): #根据类创建数据库表
    engine = create_engine(
        "mysql+pymysql://webproject:web@192.168.1.18:3306/web?charset=utf8",
        max_overflow=0,   # 超过连接池大小外最多创建的连接
        pool_size=5,      # 连接池大小
        pool_timeout=30,  # 池中没有线程最多等待的时间，否则报错
        pool_recycle=-1   # 多久之后对线程池中的线程进行一次连接的回收（重置）
    )
    Base.metadata.create_all(engine) #这行代码很关键哦！！ 读取继承了Base类的所有表在数据库中进行创建

if __name__ == '__main__':
    init_db()