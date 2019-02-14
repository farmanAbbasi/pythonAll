from git import Repo
import shutil
import os
import stat ,re, os.path
import tempfile
import glob

def rmtree(top):
    for root, dirs, files in os.walk(top, topdown=False):
        for name in files:
            filename = os.path.join(root, name)
            os.chmod(filename, stat.S_IWUSR)
            os.remove(filename)
        for name in dirs:
            os.rmdir(os.path.join(root, name))
    
    
if __name__ == "__main__":
    
      urneed=''#keep it blank to fetch whole repository
      destFolderNameForVersioning="farman3.0"
      dest='C:/Users/moabbasi/Desktop/gitFiles/'
      
      dirpath = tempfile.mkdtemp()
      Repo.clone_from('https://github.com/farmanAbbasi/helloWorldJenkins',dirpath, branch='master')
      dest2=dest+destFolderNameForVersioning
      print(dest2)
      #create a directory if not present else delete all its content
      if not os.path.exists(dest2):
          os.makedirs(dest2)
      else:
          rmtree(dest2)
      #moving the files from temp to specified folder by user
      files = os.listdir(dirpath+'/'+urneed)
      for f in files:
          print(f)
          shutil.move(dirpath+'/'+urneed+'/'+f,dest2)




          
      #cur_dir = os.getcwd() # current dir path
      #files = os.listdir(cur_dir+'/folder2')
     #to remove pattern match files
     #pattern = ".*\.py"
     # mypath = "folder2"
      #for root, dirs, files in os.walk(mypath):
          #for file in filter(lambda x:re.match(pattern, x),files):
              #os.remove(os.path.join(root,file))
              #print(file)
    
