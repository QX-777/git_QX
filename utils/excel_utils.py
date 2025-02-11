# 用于读取excel
import openpyxl

from config.config import FILE_PATH, SHEET_NAME


def excel_read(file_path=FILE_PATH,sheet_name=SHEET_NAME):

    # 打开文件
    workbook=openpyxl.load_workbook(file_path)   # 如果用pytest框架的main文件来运行，这里的路径要改成让main文件能找到
    # 选择表
    worksheet=workbook[sheet_name]

    # 读取，组装数据
    #定义一个空列表，因为我们最后组装的数据data要返回到测试脚本中，作为数据驱动的数据源，数据源要求是可迭代对象，我们一般都喜欢传入列表
    data=[]

    # 关键函数 dict(zip(keys,value))，keys和value是可迭代对象，zip可以将他们形成具有对应关系的元组，
    # 再用dict转换为字典格式，再将得到的数据放入data列表中
    # 然后通过数据驱动一个个提取出来，再通过**解包，就能实现发起请求。

    # 怎么得到keys，keys就是excel文件的第二行数据,还要将keys转为可迭代对象
    keys=[cell.value for cell in worksheet[2]]   # cell.value才是单元格中具体的数据，cell不是

    # 怎么得到values，这个不太一样，因为keys永远是第二行，而从第三行开始的所有数据都属于values，所以要遍历存入
    for row in worksheet.iter_rows(min_row=3,values_only=True):
        #values_only=True才是单元格中具体的数据，和cell.value一个意思
        # 得到的row刚好是元组，符合可迭代对象
        dict_data=dict(zip(keys,row))
        if dict_data["is_true"]:
            data.append(dict_data)  # 最后将数据组装进data


     # 关闭文件
    workbook.close()
    # 返回数据
    return data







# data=excel_read()
#
# print(data)