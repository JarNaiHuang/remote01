import os.path

# 导入 Python 的 os.path 模块
# 这个模块提供了处理文件路径的工具函数
# 比如：获取目录名、拼接路径、判断文件是否存在等


BASE_URL = "http://192.168.40.132/"

# 项目的根目录
PATH = os.path.dirname(__file__)
print(PATH)
# os.path.dirname() - 获取目录部分（去掉文件名）
# 输出：C:\Users\Administrator\PycharmProjects\PO_practice

# 假设 config.py 的完整路径是：
# C:\Users\Administrator\PycharmProjects\PO_practice\config.py

print(__file__)
# 输出：C:\Users\Administrator\PycharmProjects\PO_practice\config.py