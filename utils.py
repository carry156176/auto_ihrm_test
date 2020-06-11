"""
配置文件
"""
import json

import app
import logging
import logging.handlers


def log_config():
    # 1、创建日志器对象
    logger = logging.getLogger()

    # 2、设置日志等级
    logger.setLevel(level=logging.INFO)

    # 3、创建处理器对象  输出到终端 或者文件（要有文件路径）
    # lf = logging.FileHandler("./log/test1.log")
    ls = logging.StreamHandler()
    lt = logging.handlers.TimedRotatingFileHandler(app.BASE_DIR + "/log/ihrm.log", when="midnight", interval=1,
                                                   backupCount=2)

    # 4、创建格式化对象
    fmt = logging.Formatter(
        fmt="%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s")

    # 5、设置格式化器
    lt.setFormatter(fmt)
    ls.setFormatter(fmt)

    # 6、设置处理器
    logger.addHandler(lt)
    logger.addHandler(ls)


# 封装断言方法
def assert_text(self, http_code, success, code, message, response):
    self.assertEqual(http_code, response.status_code)
    self.assertEqual(success, response.json().get("success"))
    self.assertEqual(code, response.json().get("code"))
    self.assertIn(message, response.json().get("message"))


# 读取登录模块的数据
def read_json_data(file_path):
    res_list = []
    with open(file_path, "r", encoding="utf-8") as f:
        res = json.load(f)
        for data in res:  # type:dict
            res_list.append(tuple(data.values()))
    return res_list


# 读取员工管理模块的数据
def read_emp_data(file_path, interface_name):
    res_list = []
    with open(file_path, "r", encoding="utf-8") as f:
        emp_res = json.load(f)
        data = emp_res.get(interface_name)
        res_list.append(tuple(data.values()))
    return res_list
