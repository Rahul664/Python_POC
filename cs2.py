import os
import re
import sys

files=[]
for file in os.listdir(sys.argv[1]):
    if file.endswith(".py"):
        files.append(os.path.join(sys.argv[1],file))

baseclasslist ={}
finallist= {}

for file in files:
    fname=os.path.basename(file)
    f=open(file,'r')
    for l in f:
        if (re.match("^class*", l)):
            if (re.match("^class(?:[^\(\)]*)$", l)):
                classname = l.split()[1][:-1]
                baseclasslist[classname]=classname+"["+fname+"]"
                finallist[classname+"["+fname+"]"]=[]
            else:
                classname=l.split()[1]
                split_base_derived=classname.split("(")
                derived_class=split_base_derived[0]
                base_class=split_base_derived[1][:-2]
                base_class_list=base_class.split(".")
                for i in base_class_list:
                    if i in baseclasslist:
                        finallist[baseclasslist[i]].append(derived_class+"["+fname+"]")
                        break

for i,j in finallist.items():
    print(i)
    for k in finallist[i]:
        print(" ",k)