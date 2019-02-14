'''from github import Github
import pygit2

# using username and password establish connection to github
g = Github(userName, password)
org = g.get_organization('yourOrgName')

#create the new repository
repo = org.create_repo(projectName, description = projectDescription )

#create some new files in the repo
repo.create_file("/README.md", "init commit", readmeText)

#Clone the newly created repo
repoClone = pygit2.clone_repository(repo.git_url, '/path/to/clone/to')

#put the files in the repository here

#Commit it
repoClone.remotes.set_url("origin", repo.clone_url)
index = repoClone.index
index.add_all()
index.write()
author = pygit2.Signature("your name", "your email")
commiter = pygit2.Signature("your name", "your email")
tree = index.write_tree()
oid = repoClone.create_commit('refs/heads/master', author, commiter, "init commit",tree,[repoClone.head.get_object().hex])
remote = repoClone.remotes["origin"]
credentials = pygit2.UserPass(userName, password)
remote.credentials = credentials

callbacks=pygit2.RemoteCallbacks(credentials=credentials)
'''
# this is user defined function to clear the directory
def rmtree(top):
    for root, dirs, files in os.walk(top, topdown=False):
        for name in files:
            filename = os.path.join(root, name)
            os.chmod(filename, stat.S_IWUSR)
            os.remove(filename)
        for name in dirs:
         os.rmdir(os.path.join(root, name))
   



from git import Repo
import os
import stat
repo_dir = 'C:/Users/moabbasi/Desktop/pyProject/'
subdir='testFolder'
path=repo_dir+subdir
filename = "testfile3.txt"

try:  
    os.mkdir(path)
except OSError:
    rmtree(path)#deleting contents through user defined function
    #os.rmdir(path)#deleting folder
    #os.mkdir(path)
    print ("Already existing directory %s" % path)
else:  
    print ("Successfully created the directory %s " % path)

    
filepath = repo_dir+subdir+'/'+filename   
print(filepath)
with open(filepath, "w") as f:
    f.write("dsdsdsds")



repo = Repo(repo_dir)
file_list = [subdir]
commit_message = 'Added '+filename
repo.index.add(file_list)
repo.index.commit(commit_message)
origin = repo.remote('origin')
origin.push()


