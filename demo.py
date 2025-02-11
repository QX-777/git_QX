# 将testrunner中的代码进行封装，简化自动化框架
import requests
request_data={}
res = requests.request(**request_data)

def send_http_request(request_data):
    return requests.request(**request_data)

res = send_http_request(request_data)