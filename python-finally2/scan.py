import os
import importlib.util


# 定义python文件加载模块
def connect(ip_address, poc_path):
    try:
        # 通过importlib动态导入模块
        spec = importlib.util.spec_from_file_location("poc", poc_path) #函数创建一个指定路径的模块规范对象，该对象指定了模块的名称和路径
        poc_module = importlib.util.module_from_spec(spec)  #函数创建一个空的模块对象，并将模块规范对象与之关联
        spec.loader.exec_module(poc_module)  #方法执行模块代码，并将执行结果存储在模块对象中

        # 执行poc中的connnet函数并返回结果
        result = poc_module.connect(ip_address) #最后返回该模块对象，即可在执行代码时使用该模块中的函数
        print("##############################################\n")
        #return result
    except Exception as e:
        #print(f"An error occurred while connecting to {ip_address}: {e}")a
        return 0


# 定义扫描和爆破模块
def scan_moduls(module_name):
    module_path = os.path.join(path, module_name)
    if not os.path.isdir(module_path):
        print(f"{module_path} is not a valid directory.")
        return None

    submodules = [sub for sub in os.listdir(module_path) if sub.endswith(".py")]#列表推导式
    if not submodules:
        print(f"No submodule found in {module_path}.")
        return None

    # 打印出来供用户选择
    print("请选择要扫描的模块：")
    for i, content in enumerate(submodules):
        print(f"{i}. {content}")

    # 获取用户选择的子模块
    try:
        submodule_index = input("请输入子模块编号：")
        if submodule_index == "q" or submodule_index == "Q" or submodule_index == "exit":
            return 0
        submodule_index=int(submodule_index)
        if submodule_index < 0 or submodule_index >= len(submodules):
            raise ValueError("Invalid submodule index.")
    except ValueError as e:
        print(f"Invalid input: {e}")
        return None

    submodule_name = submodules[submodule_index]
    ip_addr = input("请输入ip/网段：")
    print("##############################################\n")
    result = connect(ip_addr, os.path.join(module_path, submodule_name))#将IP地址和路径传参connect函数
    if result is not None:
        print(f"{os.path.join(module_path, submodule_name)} 扫描结果为：{result}")


# 定义cve模块
def cve_scan(module_name):
    # 获取该模块下的所有文件夹，并过滤掉__pycache__文件夹
    module_path = os.path.join(path, module_name)
    submodules = [sub for sub in os.listdir(module_path) if
                  os.path.isdir(os.path.join(module_path, sub)) and sub != '__pycache__']#列表推导式

    # 打印出来供用户选择
    print("请选择要扫描的子模块：")
    for i, submodule in enumerate(submodules):#遍历了一个子模块列表，并打印出每个子模块以及它在列表中的索引
        print(f"{i}. {submodule}")

    # 获取用户选择的子模块
    submodule_index = input("请输入子模块编号：")
    if submodule_index == "q" or submodule_index == "Q" or submodule_index == "exit":
        return 0
    submodule_name = submodules[int(submodule_index)]

    ip_address = input("请输入URL地址! 地址格式：http://[ip/other]:[port]:  ")
    print("##############################################\n")
    # 执行该子模块下的所有.py文件，并过滤掉__pycache__文件夹
    submodule_path = os.path.join(module_path, submodule_name)
    for file in os.listdir(submodule_path):
        if file.endswith(".py"):
            poc_path = os.path.join(submodule_path, file)
            result = connect(ip_address, poc_path)
            #print(f"{poc_path} 扫描结果为：{result}")


if __name__ == '__main__':
    while True:
        # 获取当前工作目录（即scan.py所在的目录）
        path = os.getcwd()

        # 获取根目录下的所有文件夹，并过滤掉__pycache__文件夹
        contents = [content for content in os.listdir(path) if
                    os.path.isdir(os.path.join(path, content)) and content != '__pycache__']#列表推导式

        # 打印出来供用户选择
        print("请选择要扫描的模块：")
        for i, content in enumerate(contents):#遍历了一个子模块列表，并打印出每个子模块以及它在列表中的索引
            print(f"{i}. {content}")

        # 获取用户选择的模块
        module_index = input("请输入模块编号：")
        if module_index == "q" or module_index == "Q" or module_index == "exit":
            exit()

        else:
            module_name = contents[int(module_index)]
            # 判断用户输入的内容，进入相应的模块
            if module_name == "basic_scan":
                scan_moduls(module_name)
            elif module_name == "cve_scan":
                cve_scan(module_name)
