from queue import Queue
import threading
from sys import argv as arg

if threading.current_thread().name=='MainThread':
    a=sorted(arg[1:])

Num_of_files=len(a)
if Num_of_files==0:
    print("No files passed in argument")
    exit(0)

else:
    res_q=Queue(maxsize=Num_of_files*3)

    def read_file(name):
        filename=name
        try:
            f=open(filename,'r')
        except IOError:
            print("File name not valid")
            exit(0)
        line_count=\
            word_count=\
            character_count=0
        for l in f:
            line_count+=1
            w=l.split()
            word_count+=len(w)
            for k in w:
                character_count+=len(k)
        res_q.put(name)
        res_q.put(line_count)
        res_q.put(word_count)

    threads=[]
    for i in range(Num_of_files):
        t=threading.Thread(target=read_file(a[i]))
        threads.append(t)
        t.start()
    for i in threads:
        i.join()

    if threading.current_thread().name=='MainThread':
        print("File Name",'\t',"Number of lines",'\t',"Number of words")
        while not res_q.empty():
            print(res_q.get(),'\t',res_q.get(),'\t',res_q.get())









