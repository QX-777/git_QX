import allure


def allure_init(case):
    allure.dynamic.feature(case["feature"])
    allure.dynamic.story(case["story"])
    allure.dynamic.title("ID:{}--{}".format(case["id"], case["title"]))