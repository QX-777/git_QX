import logging

import allure
import pymysql
import requests

from config.config import *


@allure.step("2.发送HTTP请求")
def send_http_request(**request_data):
    res=requests.request(**request_data)
    logging.info(f"得到的响应结果为：{res.text}")
    allure.attach(f"{res.text}", name="得到响应结果")
    # allure.attach()将附件添加到测试报告中，在UI自动化用的多，因为可以添加截图附件
    return res



def send_jdbc_request(sql,index=0):
    conn = pymysql.connect(
        host=DB_HOST,
        port=DB_PORT,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        charset=DB_CHARSET
    )
    cur = conn.cursor()
    cur.execute(sql)
    result = cur.fetchone()
    cur.close()
    conn.close()
    return result[index]


# 这里踩了一个坑，留个笔记
# 一开始封装send_http_request的时候是这样写的
# def send_http_request(request_data):
#     return requests.request(**request_data)
# 调用的时候是这样的，res=send_http_request(request_data)
# 这种方式是没有问题的，很简洁直白，但是如果是别人看到我这样调用
# 别人就不知道我传入的request_data是什么类型的
#
# 所以我采用了第二种方式：
# def send_http_request(**request_data):
#     return requests.request(**request_data)
# 这样的话，我在调用这个函数的时候就必须这样调用
# res=send_http_request(**request_data)
# 别人看到我这么调用，就知道我这里的request_data是字典了
#
# 这个时候我产生了疑问，为什么我是传入**request_data而不是request_data?
# 我难道不是传入一个字典，然后这个字典经过一系列传递，最终到达requests.request(**request_data)进行解包就行了吗？
# 我意识到我在解包这个过程有不理解的地方，于是我去查资料
# 最后才知道，我在定义send_http_request的时候就意味着我这个函数需要传入【关键字参数】，也就是这样的类型a=1，b=2，而不是传入字典
# def send_http_request(**request_data):
#     return requests.request(**request_data)
#
# 字典和关键字参数直接，需要一个关键的操作，那就是解包
# 字典request_data经过解包**request_data，才会变成关键字参数，才是这个函数真正想接收的数据
# 最后重新梳理了解包的过程
# 调用send_http_request(**request_data)的时候，会将字典解包成关键字参数进入函数内部
# 在函数内部进行一一对应，也会形成一个集合request_data
# 然后在调用requests.request()的时候，由于request函数内部也需要关键字参数，所以再次对刚刚那个集合进行解包
# requests.request(**request_data)
# 这个解包/集合/解包的过程有点繁琐，用第一种方法就很简洁直白，但是第一种方法别人在看到我的代码的时候不知道我传入的类型
# 只能说有利有弊吧，看场景来选择
# 第一种方法简洁直白
# 第二种方法更加灵活，只是我不知道灵活在哪