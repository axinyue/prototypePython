
import time
import datetime
from network.task import Task

# 配置
WAIT_TIME = 3  # 单位s

class DS(object):
    def __init__(self):
        '''
        task = (task_id,time)   # 任务id ,执行的时间
        '''
        task_ls = [1,]
        pass
    def inTime(self,year=1,month=1,day=1,hour=0,minute=0,second=0):
        sysTime = datetime.datetime.now()
        if year<sysTime.year and month<sysTime.month:
            return False    # "年月，必须大于系统当前年月"

        end_time = datetime.datetime(year=year,month=month,day=day,hour=hour,minute=minute,second=second)
        print(end_time)
        t = end_time.strftime("%Y:%m:%d %H %M %S")
        print(t)
        print(type(end_time))
        print(str(end_time.timestamp()))
        return end_time

    def someTimeAfter(self,days=0,hours=0,minutes=0,seconds=0):  # 一段时间后 几(天，小时，分钟，秒)
        end_time = datetime.timedelta(days=days,hours=hours,minutes=minutes,seconds=seconds)+datetime.datetime.now()
        t = datetime.datetime.now().strftime("%Y:%m:%d %H %M %S")
        print(t)
        return end_time

    def isOverdue(self,overdueTime):
        if datetime.datetime.now().timestamp()>overdueTime.timestamp():         # 过期后返回真，执行某些命令
            return True
        else:
            return False                                                        # 继续等待


class Listen(object):
    def __init__(self):
        self.ds = DS()
        self.taskQueue = [(1,"")]            # 录入task 时保证格式正确（int,datetime()对象）
        self.task = Task()
    def loop(self):
        while True:
            for i in self.taskQueue:
                if self.ds.isOverdue(i[1]):
                    r = self.task.runTask(i[0])
                    self.taskQueue.remove(i)
                    # TODO 写个日志

            time.sleep(WAIT_TIME)


