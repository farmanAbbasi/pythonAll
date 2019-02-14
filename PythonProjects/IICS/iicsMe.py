#apse1
import requests
import json
import zipfile
import io
import os

def putjson(filename,data):
    with open(filename, 'w') as f:
        json.dump(data, f)

def getjson(filepath):
    with open((filepath),'r') as fp:
        return json.load(fp)
#login--------------------------------------------------------------------------------------------------------------------------------
values = {"username":"farmanshaikh2009@gmail.com","password":"Qwerty@123"}
headers={'content-type':'application/json','accept':'application/json'}
url1='https://dm-ap.informaticacloud.com/saas/public/core/v3/login'
r = requests.post(url1,data=json.dumps(values),headers=headers)
print(r.status_code)

#convert r into json format
data = r.json()
#formatting d json in beautified form
d=json.dumps(data,indent=2)
#print(d)

#putting in *.json file
putjson('1)loginData.json',data)
#retrieving data from that file
myobj=getjson('./1)loginData.json')

ics=myobj['userInfo']['sessionId']#NOTE WE ARE SENDING AND THEN RECEIVING THEN PRINTING WE CAN DIRECTLY PRINT ALSO
#as ics=data['userInfo']['sessionId']
print(ics)


#lookup----------------------------------------------------------------------------------------------------------------------------------
values={
	"objects": [ {'path' : "Default/farmanMapping",
                      "type" : "Mapping"    },
                     
                     {"path" : "testFarmanProject",
                      "type" : "Project"   
                     },
                     
                     {"path" : "testFarmanProject/insideTestFarmanFolder",
                      "type" : "Folder"   
                     }
]}
headers={'content-type':'application/json','INFA-SESSION-ID':ics}
r=requests.post('https://apse1.dm-ap.informaticacloud.com/saas/public/core/v3/lookup',data=json.dumps(values),headers=headers)
print(r.status_code)

data=r.json()
d=json.dumps(data,indent=2)
print(d)

#putting in *.json file
putjson('2)lookup.json',data)
#retrieving data from that file
myobj=getjson('./2)lookup.json')


#export of all ids-------------------------------------------------------------------------------------------------------------------------------------
#getting all the ids of objects dynamically
numberOfObjects=len(myobj['objects'])
#just for printing ids if will reomove then also no problem

ids=[]
idsArray=[]
for i in range(numberOfObjects):
    key=["id"]
    ids.append(myobj['objects'][i]['id'])
    value=[myobj['objects'][i]['id']]
    idsArray.append(dict(zip(key,value)))
print(ids)
print(idsArray)

#idsArray is storing a dict od key : value pairs of id : ids
values={
    "objects": idsArray
    }
headers={'content-type':'application/json','accept':'application/json','INFA-SESSION-ID':ics}
r=requests.post('https://apse1.dm-ap.informaticacloud.com/saas/public/core/v3/export',data=json.dumps(values),headers=headers)
print(r.status_code)

data= r.json()
#putting in *.json file
putjson('3)export.json',data)
#retrieving data from that file
myobj=getjson('./3)export.json')
print(json.dumps(myobj,indent=2))
exportId=myobj["id"]
print(exportId)

#get status of export with id (note: its exported id)---------------------------------------------------------------------------------------------------------
headers={'content-type':'application/json','accept':'application/json','INFA-SESSION-ID':ics}
r=requests.get('https://apse1.dm-ap.informaticacloud.com/saas/public/core/v3/export/'+exportId,headers=headers)
print(r.status_code)
data=r.json()
putjson('4)export_status.json',data)
myobj=getjson('./4)export_status.json')
print(json.dumps(myobj,indent=2))

#download export package----------------------------------------------------------------------------------------------------------------------------------
r=requests.get('https://apse1.dm-ap.informaticacloud.com/saas/public/core/v3/export/'+exportId+'/package',headers=headers)
print(r.status_code)

z = zipfile.ZipFile(io.BytesIO(r.content))
z.extractall('./export_file')

fzip = zipfile.ZipFile('C:\\Users\\moabbasi\\Desktop\\PythonProjects\\export_file.zip','w')
 
for folder, subfolders, files in os.walk('C:\\Users\\moabbasi\\Desktop\\PythonProjects\\export_file'):
 
    for file in files:
        
            fzip.write(os.path.join(folder, file), os.path.relpath(os.path.join(folder,file),'C:\\Users\\moabbasi\\Desktop\\PythonProjects\\export_file'),compress_type = zipfile.ZIP_DEFLATED)
 
fzip.close()



#logout-----------------------------------------------------------------------------------------------------------------------------------------------
headers={'content-type':'application/json','INFA-SESSION-ID':ics}
r=requests.post('https://dm-ap.informaticacloud.com/saas/public/core/v3/logout',headers)
print(r.status_code)



