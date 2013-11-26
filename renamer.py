# -*- coding: utf-8 -*-
import csv, os, sys

CSVS = ['fields.csv','methods.csv']
CLASSES = 'classes'
UNCOMPL = 'modsrc'
DESTINN = 'unobf'


def file_get_contents(filename):
    with open(filename) as f:
        return f.read()

def all_replace(files,string):
  for file in files:
    string = str_replace(file,string)
  return string

def str_replace(filename,string):
  file = open(filename,'rb')
  reader = csv.reader(file,delimiter=',',quotechar='\'')
  for row in reader:
    string = string.replace(row[0],row[1])  
  file.close()
  return string

def scan_dir(input,output,csvs):
  return x_scan_dir(input,input,output,csvs)    
  
def x_scan_dir(main_dir,input,output,csvs):
  for f in os.listdir(input):   
    f_inp = input + '/' + f
    if os.path.isfile(f_inp):
      f_out = f_inp.replace(main_dir,output,1).replace(".class",".java",1)
      print "Original: " + f_inp
      print "Result: " + f_out
      print ""
      string = all_replace(csvs,file_get_contents(f_inp))
      with open(f_out,'w') as xf:
        xf.write(string)
    else:	
      x_dir = f_inp.replace(main_dir,output,1)
      print "List '%s' is a directory!" % x_dir
      if not os.path.exists(x_dir): os.mkdir(x_dir)
      x_scan_dir(main_dir,f_inp,output,csvs)

def decompile(input,output):
  os.system("java -jar fernflower.jar -din=0 -rbr=0 -dgs=1 -asc=1 -log=WARN " + input + " " + output)
  
def unclear(sources,result):
  size1 = len(os.listdir(sources))
  size2 = len(os.listdir(result))
  return (size1 > 0) or (size2 > 0)

  
# MAIN CODE  
 
if unclear(UNCOMPL,DESTINN):
  print "There is a files in folder '%s'  or '%s' !" % (UNCOMPL, DESTINN)
  print "If you want to continue, please launcher CLEANUP.bat!"
  sys.exit(1)
  
decompile(CLASSES,UNCOMPL)	  
scan_dir(UNCOMPL,DESTINN,CSVS)	
print "Success! Press any key to exit!"