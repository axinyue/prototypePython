# 存放全局配置
import os
# 数据表数据库配置

DB_USERNAME = "name"
DB_PORT = "3306"
DB_IP = "192.168.0.2"
DB_NAME = "xktestdb"
DB_PASSWORD = "password"

# 配置数据库 sqlalchemy的连接
DB_CONNECT_URL = "mysql+pymysql://%s:%s@%s:%s/%s?charset=utf8"%(DB_USERNAME,DB_PASSWORD,DB_IP,DB_PORT,DB_NAME)


# redis 配置
REDIS_CONFIG = {
    "host":"192.168.0.2",
    "port":6379,
    "password": "597fcdbd-fb51-47e0-b7e0-458531553076"
}

# server
SVRVER_PORT = 80


CURRENT_PATH  = os.path.dirname(__file__)