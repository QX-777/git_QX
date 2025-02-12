import os

import pytest

# --alluredir ./report/json_report 指定一个目录，生成中间结果
# --clean-alluredir 每次运行前会清空历史数据
# 生成最终结果 allure generate 中间结果的路径 -o 最终结果的路径 --clean

if __name__ == '__main__':
    pytest.main(["-vs","./testcases/test_runner.py","--alluredir","./report/json_report","--clean-alluredir"])
    os.system("allure generate ./report/json_report -o ./report/html_report --clean")
