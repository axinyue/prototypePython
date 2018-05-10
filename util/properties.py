'''
流程：
1.读文件: 读文件行read()，转换为对象analysis()
2.更新配置项
3.把对象转换为str
4.写入文件 write()
'''

import os

class Properties(object):
    def __init__(self,filePath,**kwargs):

        if not (os.path.exists(filePath)and os.path.isfile(filePath)):
            raise FileNotFoundError("the file(%s)  not found"%filePath)
        else:
            self.filePath = filePath
        self.encoding = kwargs.get("encoding",'gbk')

    def read(self):
        try:
            with open(self.filePath,'r',encoding=self.encoding) as f:
                lines = f.readlines()

            return lines
        except:
            print("warning.now file is not encoding:%s"%self.encoding)
            try:
                with open(self.filePath,'r',encoding='utf-8') as f:
                    lines = f.readlines()
                    self.encoding = 'utf-8'
                return lines
            except:
                try:
                    with open(self.filePath, 'r', encoding='gbk') as f:
                        lines = f.readlines()
                        self.encoding = 'gbk'
                    return lines
                except:
                    raise Exception('File Encode Error,Use utf8 or gbk,please check file encoding')

    def analysis(self,line):
        '''
        flag:
            1  注释
            2  空行
            3  键值
        '''
        line = line.strip()
        if len(line)>0:
            if line[0] =='#':
                return (1,line)
            else:
                index = line.find('=')
                if index==-1:
                    raise Exception("Invalid configuration in %s"%line)
                else:
                    return (3,{line[0:index]:line[index+1:]})       # 返回一个键值
        else:
            # print(len(line))
            return (2,'')

    def test(self):
        lines = self.read()
        data_ls = []
        for i in lines:
            result = self.analysis(i)
            data_ls.append(result)
            print(result)
        return data_ls

    def convert(self,obj):
        '''
        1  注释
        2  空行
        3  键值
        '''
        if obj[0]<=2:
            return obj[1]
        elif obj[1]==3:
            return [x for x in obj[1].items()]
        return str
    def write(self,iter_str):
        with open("server2.properties",encoding=self.encoding) as f:
            for i in iter:
                f.write(i[1])



a = Properties(r'E:\GMAUTO\config\server.properties')
b = a.test()


for i in b:
    print(i)

# a.write(b)
