

import subprocess

# 获取所有安装包的名称
result=subprocess.check_output(['pip','list']).decode('utf-8').split('\n')[2:-1]
packages=[package.split()[0] for package in result]

# 升级所有包
for package in packages:
    subprocess.call(['pip','install','--upgrade',package])






