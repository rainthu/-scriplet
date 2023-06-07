
import xlrd
import  os

#读取excel对象
file_path=input("请输入文件路径：")
sheets=xlrd.open_workbook(file_path)

#获取第一个工作表
table=sheets.sheets()[0]

#获取总列数
col=table.ncols
#获取当前py文件路径下是否有save目录，若没有就创建一个用于存放生成的文件夹
dir_list=os.listdir()
if 'save' not in dir_list:
    os.mkdir("save")
path=os.path.join(os.getcwd(),"save")


for i in range(col):
    #读取第一行的每一列，作为文件夹/目录名称
    name=str(table.col_values(i)[0])
    try:
        file_path=os.path.join(path,name)
        os.mkdir(file_path)
    except FileExistsError as e:
        print(e)
print("end")



