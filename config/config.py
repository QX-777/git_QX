# 测试环境基准地址
BASE_URL= "http://192.168.130.10/v1"

# 测试用例配置
FILE_PATH= "./data/测试用例.xlsx"
SHEET_NAME= "Sheet1"

# 数据库配置
DB_HOST="127.0.0.1"
DB_PORT=3306
DB_NAME="mydb",
DB_USER="root",
DB_PASSWORD="123456",
DB_CHARSET="utf8"

# mysql资源销毁
SQL1="delete from sp_goods where goods_name = '牛仔裤'"
SQL2="delete from sp_attribute where attr_name = '大码衣服'"
SQL3="delete from sp_category where category_name = '牛仔裤+'"