import time

class MyTime:
    year=None
    month=None
    day=None
    weekday=None
    time_stamp=None
    def __new__(cls):
        if not hasattr(cls,"_instance"):
            cls._instance=object.__new__(cls)
        return cls._instance

    def __init__(self):
        if self.year==None:
            self.time_stump=time.time()
            struct_time=time.localtime(self.time_stamp)
            self.year=struct_time.tm_year
            self.month=struct_time.tm_mon
            self.day=struct_time.tm_mday
            self.weekday=struct_time.tm_wday+1
            if self.weekday==7:
                self.weekday="日"

    @staticmethod
    def toDict():
        m_time=MyTime()

        def toStr(time):
            if time<10:
                return "0"+str(time)
            else:
                return str(time)

        return {"year":toStr(m_time.year)
                ,"month":toStr(m_time.month)
                ,"day":toStr(m_time.day)
                ,"weekday":str(m_time.weekday)}

    @staticmethod
    def dump(m_str):
        _ans=MyTime.toDict()
        for each in _ans:
            m_str=m_str.replace("${"+each+"}",_ans[each])

        return m_str

    @staticmethod
    def toString():
        return MyTime.dump("${year}-${month}-${day}")

    @staticmethod
    def toTimeStamp(time_str):
        timeArray = time.strptime(time_str, "%Y-%m-%d")
        return int(time.mktime(timeArray))

