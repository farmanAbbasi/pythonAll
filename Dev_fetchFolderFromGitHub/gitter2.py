from git import Repo
import shutil
import os
import stat ,re, os.path
import tempfile
import glob
from shutil import move
import requests, zipfile, io

def rmtree(top):
    for root, dirs, files in os.walk(top, topdown=False):
        for name in files:
            filename = os.path.join(root, name)
            os.chmod(filename, stat.S_IWUSR)
            os.remove(filename)
        for name in dirs:
         os.rmdir(os.path.join(root, name))

#to count variable in file            
def get_var_value(versions_wanted):
   try:
       with open( 'counter.txt', 'r+' ) as fle:
           counter = int( fle.readline() or 0) + 1
   except FileNotFoundError:
       counter = 1
   if (counter%(versions_wanted+1))==0:
       counter=versions_wanted
       mover(versions_wanted)
   with open( 'counter.txt', 'w' ) as fle:
       fle.write( str(counter) )
   return counter

#to rename folders acording to date
def mover(versions_wanted):
    dest='C:/Users/moabbasi/Desktop/gitFiles/'
    for i in range(2,versions_wanted+1):
        src=dest+"Dev_fetchFolderFromGit"+str(i)+".0"
        dst=dest+"Dev_fetchFolderFromGit"+str(i-1)+".0"
        rmtree(dst)
        move(src,dst)

        
if __name__ == "__main__":
      versions_wanted=5
      version_counter = get_var_value(versions_wanted)
      urneed='folder1/folder1.1'#keep it blank to fetch whole repository
      destFolderNameForVersioning="Dev_fetchFolderFromGit"+str(version_counter)+".0"
      dest='C:/Users/moabbasi/Desktop/gitFiles/'
      repoAddress='https://github.com/farmanAbbasi/helloWorldJenkins'
      url=repoAddress+'/archive/master.zip'
      r = requests.get(url)
      print(r.status_code)
      
      dirpath = tempfile.mkdtemp()
      print(dirpath)
      r = requests.get(url, stream=True)
      z = zipfile.ZipFile(io.BytesIO(r.content))
      z.extractall(dirpath)
      dest2=dest+destFolderNameForVersioning
      print(dest2)
      
       #create a directory if not present else delete all its content
      if not os.path.exists(dest2):
          os.makedirs(dest2)
      else:
          rmtree(dest2)
      #moving the files from temp to specified folder by user
      files = os.listdir(dirpath+'/'+'helloWorldJenkins-master'+'/'+urneed)
      for f in files:
          print(f)
          shutil.move(dirpath+'/'+'helloWorldJenkins-master'+'/'+urneed+'/'+f,dest2)

      #finally delete the temp directory
      rmtree(dirpath)#deleting contents through user defined function
      os.rmdir(dirpath)#deleting folder
      
     
  
