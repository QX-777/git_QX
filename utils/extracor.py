import logging

import allure
import jsonpath

from utils.send_request import send_jdbc_request


def json_extractor(case,all,res):
    if case["jsonExData"]:
        with allure.step("4.JSON提取"):
            for key, value in eval(case["jsonExData"]):
                value = jsonpath.jsonpath(res.json(), value)[0]
                all[key] = value
            logging.info(f"经过JSON提取后的全局变量为 {all}")
            allure.attach(f"{all}", name="JSON提取数据")


def jdbc_extractor(case,all):
    if case["sqlExData"]:
        with allure.step("4.JDBC提取"):
            for key, value in eval(case["jsonExData"]):
                value = send_jdbc_request(value)
                # 存进全局变量all
                all[key] = value
            logging.info(f"经过JDBC提取后的全局变量为 {all}")
            allure.attach(f"{all}", name="JDBC提取数据")