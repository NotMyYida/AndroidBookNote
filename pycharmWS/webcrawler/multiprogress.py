from multiprocessing import Process
import os

def run_proc(name):
    print("Run child process %s (%s)..."%(name,os.getpid()))

# if __name__ == '__main__':
#     print("Parent process %s."%os.getpid())
#     p = Process(target=run_proc,args=('test',))
#     print('Child process will start...')
#     p.start()
#     p.join()
#     print('Child Process End.')

# Parent process 9512.
# Child process will start...
# Run child process test (9328)...
# Child Process End.

from multiprocessing import Pool                # 线程池
import time,random

def long_time_task(name):
    print("Run task %s (%s) ..."%(name,os.getpid()))
    start = time.time()
    time.sleep(random.random()*3)
    end = time.time()
    print("Task %s run %0.2f seconds."%(name,end - start))

# if __name__ =='__main__':
#     print('Parent process %s.'%os.getpid())
#     p = Pool(4)
#     for i in range(5):
#         p.apply_async(long_time_task,args=(i,))
#     print('Waiting for all subprocess done..')
#     p.close()
#     p.join()
#     print('All the subprocess done')

# Parent process 9844.
# Waiting for all subprocess done..
# Run task 0 (8172) ...
# Run task 1 (8180) ...
# Run task 2 (9968) ...
# Run task 3 (10740) ...
# Task 3 run 1.23 seconds.
# Run task 4 (10740) ...
# Task 2 run 1.68 seconds.
# Task 0 run 2.36 seconds.
# Task 1 run 3.11 seconds.
# Task 4 run 1.72 seconds.
# All the subprocess done


import subprocess                           # 子进程
# print("$ nslookup www.python.org")
# r = subprocess.call(['nslookup','www.python.org'])
# print('Exit code : ',r)


# $ nslookup www.python.org
# ������:  ns.szptt.net.cn
# Address:  202.96.134.133
#
# ����:    python.map.fastly.net
# Addresses:  2a04:4e42:36::223
# 	  151.101.228.223
# Aliases:  www.python.org
#
# ��Ȩ��Ӧ��:
# Exit code :  0

# print("$ nslookup")
# p = subprocess.Popen(['nslookup'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
# output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
# print(output.decode('gbk'))
# print('Exit code : ',p.returncode)

# $ nslookup
# 默认服务器:  ns.szptt.net.cn
# Address:  202.96.134.133
#
# > > 服务器:  ns.szptt.net.cn
# Address:  202.96.134.133
#
# python.org	MX preference = 50, mail exchanger = mail.python.org
# >
# Exit code :  0

from multiprocessing import Queue

# 写数据
def write(q):
    print('Process to write : %s'%os.getpid())
    for value in ['A','B','C']:
        print('Put %s to queue...'%value)
        q.put(value)
        time.sleep(random.random())

# 读数据
def read(q):
    print('Process to read : %s'%os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue'%value)

if  __name__ == "__main__":
    q = Queue()
    pw = Process(target=write,args=(q,))
    pr = Process(target=read,args=(q,))
    pw.start()
    pr.start()
    pw.join()
    pr.terminate()


# Process to write : 13688
# Put A to queue...
# Process to read : 8980
# Get A from queue
# Put B to queue...
# Get B from queue
# Put C to queue...
# Get C from queue