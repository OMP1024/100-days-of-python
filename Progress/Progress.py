import os

pid = os.fork()

# 子进程复制父进程所有资源信息，子进程返回0，父进程返回的是子进程的id
# fork函数调用一次，返回两次，因为子进程复制了父进程，并都做了返回
if pid == 0:
    print('子进程')
else:
    print('父进程')


