# -*-coding:utf8-*-
import unittest
import HTMLTestRunner
import ConfigParser
import importlib
import time

class Suites():
    def casesuite(self):
        cases = unittest.TestSuite()
        read_config = ConfigParser.RawConfigParser()
        read_config.read('test')
        caselist = read_config.items('cases')
        casecllist = read_config.items('case_class')
        casenamelist = []
        caseclasslist = []
        classlist =[]
        #动态导入测试用例文件
        stringmodule = importlib.import_module('case')
        #
        for i in range(0, len(caselist)):
            casenamelist.append(caselist[i][1])
            caseclasslist.append(casecllist[i][1])
            classlist.append(getattr(stringmodule, caseclasslist[i]))
        for i in range(0, len(casenamelist)):
            # print type(caseclasslist[i])
            cases.addTest(classlist[i](casenamelist[i]))
        timeStamp = time.time()
        timeArray = time.localtime(timeStamp)
        timenow = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
        filepath='/Users/xukuan/Desktop/result'+timenow+'.html'
        with open(filepath, 'wb')as fp:
            runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Result'+str(time.time()), description='Test_Report')
            runner.run(cases)
        return filepath


if __name__ == '__main__':
    suite_obj = Suites()
    print suite_obj.casesuite()