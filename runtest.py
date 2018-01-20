#coding=utf-8
import unittest,os
import sys

import stringTest
sys.path.append('E:\\selenium_class\\chapter7-7\\testcase')
sys.path.append('/testcase/2')
import test_2
def creatsuite():
    testunit=unittest.TestSuite()
    #定义测试文件查找的目录
    test_dir=os.getcwd()+'/testcase'
    #定义 discover 方法的参数
    discover=unittest.defaultTestLoader.discover(test_dir,
                                                 pattern ='test*.py',
                                                 top_level_dir=None)
    #discover 方法筛选出来的用例，循环添加到测试套件中
    for test_suite in discover:
        for test_case in test_suite:
            testunit.addTests(test_case)
            #print (testunit)
    return testunit
if __name__ == '__main__':
    alltestnames=creatsuite()
    runner =unittest.TextTestRunner()
    runner.run(alltestnames)

