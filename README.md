# Python_POC
File cs1.py is the solution  for the following question

Implement a multithreaded solution that takes file name(s) as command-line
argument and prints the count of lines, words and characters for each line.
Spaces, tabs and newline characters are considered as word delimiters.
Each file should be analyzed by one thread. The thread must get the count of lines &
words for the file, place the results in a queue and should terminates.
The primary thread should read the queue and produce output sorted on filename.

Sample program run and output is shown below.
$ cs1.py x.dat a.txt b.dat k.txt g.txt
a.txt 123 347
b.dat 1403 712
g.txt 110897 256104
k.txt 1042 8217
x.dat 4571 10392

File cs2.py is the solution for the following question

Implement a python program that analyzes python source files in a given directory and produces class dependency list, along with the source filename in which the class definition is found, in the following format.
Class name1 [filename] 
  Derived Classname1 [filename] 
  Derived Classname2 [filename] 
  Derived Classname3 [filename] … 
Class name2 [filename] 
  Derived ClassnameA [filename] 
  Derived ClassnameB[filename] 
  Derived ClassnameC [filename] … …
For example, running the program cs2.py on the directory /usr/lib/python2.6/site-packages/virtinst, resulted in the output that is partially shown 
$ python cs2.py /usr/lib/python2.6/site-packages/virtinst
some output not shown here 
Distro [DistroInstaller.py] 
  DebianDistro [OSDistro.py] 
  GenericDistro [OSDistro.py] 
  MandrivaDistro [OSDistro.py] 
  NetWareDistro [OSDistro.py] 
  RedHatDistro [OSDistro.py] 
  SunDistro [OSDistro.py] 
  SuseDistro [OSDistro.py] 
  Guest [CapabilitiesParser.py] 
  FullVirtGuest [FullVirtGuest.py] 
  ParaVirtGuest [ParaVirtGuest.py]
