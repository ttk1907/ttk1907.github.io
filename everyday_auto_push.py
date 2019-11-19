import os
# 调用os的system方法
os.system('git add .')
# 这里的参数就相当于在终端中输入的命令
os.system('git commit -m\"python auto push\"')
# 你可以自己定义自己的 commit 说明内容
os.system('git push origin master')
# 最后push到对应的远程库中的某个分之中,就成了