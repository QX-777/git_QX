import logging

import allure
import jsonpath

from utils.send_request import send_jdbc_request


@allure.step("3.HTTP响应断言")
def http_assert(case,res):
    if case["check"]:  # 如果有给出校验字段的值，说明是想要进行精确断言，则使用jsonpath表达式提取实际结果
        actual=jsonpath.jsonpath(res.json(), case["check"])[0]
        logging.info(f"http响应断言的结果为：{actual}={case["expect"]}")
        allure.attach(f"{actual}={case["expect"]}", name="HTTP断言结果")
        assert actual == case["expect"]

    else:  # 如果没有给出校验字段的值，说明是模糊断言，只要实际结果中包含预期结果即可（jmeter中的响应断言原理）
        logging.info(f"http响应断言的结果为：{case["expect"]} in {res.text}")
        allure.attach(f"{case["expect"]} in {res.text}", name="HTTP断言结果")
        assert case["expect"] in res.text


def jdbc_assert(case):
    if case["sql_check"] and case["sql_expect"]:
        with allure.step("3.JDBC响应断言"):
            jdbc_actual=send_jdbc_request(case["sql_check"])
            logging.info(f"jdbc响应断言的结果为：{jdbc_actual} = {case["sql_expect"]}")
            allure.attach(f"{jdbc_actual}={case["sql_expect"]}", name="JDBC断言结果")
            assert jdbc_actual == case["sql_expect"]

# 这里不使用@allure.step("步骤描述")是因为使用了之后，
# 只要调用jdbc_assert(),测试报告中就一定有jdbc响应断言这个步骤，
# 但却不一定会真的去断言，而是要在函数内部判断成功才会真正去断言
# 如果没有断言，但是测试报告却出现了这个步骤，就不合适
# 用了这个方法，在测试报告中不会显示参数，仅此而已
# 为什么http_assert可以用@allure.step()，因为它用的是if else，是一定会执行断言的