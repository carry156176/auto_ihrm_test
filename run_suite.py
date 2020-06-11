import time
import unittest
import app
import HTMLTestRunner_PY3

suit = unittest.TestLoader().discover(app.BASE_DIR + "/script", pattern="test*.py")

# 定义存放测试报告的文件名
report_path = app.BASE_DIR + "/report/time{}.html".format(time.strftime("%Y%m%d%H%M%S"))

# 2、使用HTMLTestRunner生成测试报告
with open(report_path, "wb") as f:
    runner = HTMLTestRunner_PY3.HTMLTestRunner(f, verbosity=1, title="登录接口测试", description="登录接口测试报告")
    runner.run(suit)
