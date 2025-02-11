# 测试脚本，写逻辑
# 拿到的data要进行处理
# 1.发起请求的时候，要求data参数的值为字典，但是我拿到的是字符串
# 2.expect这个字段是用来断言的，我不能直接传到发起请求的参数里面去，要把这个参数去掉
# 3.发起请求需要url，但是excel里面写的只是路径，还缺少基础地址，要拼接上
import pytest
from jinja2 import Template
from utils.allure_utils import allure_init
from utils.analyse_case import analyse_case
from utils.asserts import http_assert, jdbc_assert
from utils.excel_utils import excel_read
from utils.extracor import json_extractor, jdbc_extractor
from utils.send_request import send_http_request, send_jdbc_request


class TestRunner:

    # 读取数据源
    data=excel_read()

    # 初始化全局变量all
    all={}

    @pytest.mark.parametrize("case",data)
    def test_runner(self,case):

        all=self.all

        # 模板渲染
        case=eval(Template(str(case)).render(all))

        # 初始化allure测试报告
        allure_init(case)

        # 数据解析
        request_data = analyse_case(case)

        # 使用解析后的数据发起请求
        res=send_http_request(**request_data)

        # http响应断言
        http_assert(case, res)

        # 数据库断言：在响应断言成功下，再次验证数据库断言
        jdbc_assert(case)

        # json提取，关键在于jsonpath表达式，并将提取后的数据存入全局变量中,可以多字段提取
        json_extractor(case,all,res)

        # sql提取
        jdbc_extractor(case, all)

        # 引用全局变量，做接口关联，在测试用例中进行引用{{TOKEN}}




        # 数据解析已经完成，但还有遗留问题，
        # 接口关联怎么处理，
        # 断言的表达式写死了，需要优化，
        # 基础地址需要提取出去