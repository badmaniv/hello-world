# -*-coding:utf8-*-
#用来生产配置文件的脚本
import ConfigParser

def create_ini():
    file = open('test','w')
    write_config = ConfigParser.RawConfigParser()
    write_config.add_section('cases')
    write_config.add_section('case_class')
    write_config.add_section('result_path')
    write_config.add_section('case_path')
    write_config.add_section('environments')
    write_config.add_section('mail')
    write_config.set('cases', 'cases1', 'test_http')
    write_config.set('cases', 'cases2', 'test_http2')
    write_config.set('cases', 'cases3', 'test_http3')
    write_config.set('case_class', 'cases1', 'Testhttp')
    write_config.set('case_class', 'cases2', 'Testhttp')
    write_config.set('case_class', 'cases3', 'Testhttp')

    write_config.set('case_path', 'cases1', 'case')
    write_config.set('case_path', 'cases2', 'case')
    write_config.set('case_path', 'cases3', 'case')

    write_config.set('environments', 'environment', 'formal')
    write_config.set('mail', 'sender', 'kuan__xu@163.com')
    write_config.set('mail', 'sender_passowrd', 'fovg62234183')
    write_config.set('mail', 'receiver', 'lian@kmelearning.com')
    write_config.set('mail', 'stmpaddr', 'smtp.163.com')
    write_config.set('mail', 'msg', '测试报告详情请查看附件')

    write_config.set('result_path', 'debug', 'E://result.html')
    write_config.set('result_path', 'test', 'E://result.html')
    write_config.set('result_path', 'formal', 'E://result.html')
    write_config.write(file)
    file.close()

def read_ini():
    read_config = ConfigParser.RawConfigParser()
    read_config.read('test')
    print read_config.sections()
    print read_config.items('cases')
    print read_config.get('cases', 'cases1')

if __name__ == "__main__":
    create_ini()
    # read_ini()