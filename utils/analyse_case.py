import logging

import allure
from config.config import BASE_URL


@allure.step("1.解析测试数据")
def analyse_case(case):
    method = case["method"]
    url = BASE_URL + case["path"]
    headers = eval(case["headers"]) if isinstance(case["headers"], str) else None
    params = eval(case["params"]) if isinstance(case["params"], str) else None
    data = eval(case["data"]) if isinstance(case["data"], str) else None
    json = eval(case["json"]) if isinstance(case["json"], str) else None
    files = eval(case["files"]) if isinstance(case["files"], str) else None

    # 将解析后的数据重新组装
    request_data = {
        "method": method,
        "url": url,
        "headers": headers,
        "params": params,
        "data": data,
        "json": json,
        "files": files,
    }

    logging.info(f"解析后的数据为：{request_data}")
    allure.attach(f"{request_data}",name="解析数据结果")

    return request_data