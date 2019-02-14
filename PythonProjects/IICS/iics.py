import requests
import json
import zipfile
import io
import os

values = {"username":"phaniveerk@gmail.com","password":"Ruthvik@12"}
headers={'content-type':'application/json','accept':'application/json'}
r = requests.post(' https://dm-us.informaticacloud.com/saas/public/core/v3/login',data=json.dumps(values),headers=headers)
print(r.status_code)


data = r.json()
with open('data.json', 'w') as f:
    json.dump(data, f)

def getjson(filepath):
    with open((filepath),'r') as fp:
        return(json.load(fp))

myobj=getjson('./data.json')
ics=myobj['userInfo']['sessionId']
print(ics)

values={
	"objects": [{ 
	"path":"My_Project/My_Folder/Mapping1",
	"type":"Mapping"
	},
	{
	"path" : "My_Project", 
	"type" : "Project"
	},
	{
	"path": "My_Project/My_Folder", 
	"type": "Folder"
	},
	{
	"path": "HSC-342Z6BS", 
	"type": "Agent"
	},
	{
	"path": "File_conn", 
	"type": "Connection"
	}]
}
headers={'content-type':'application/json','INFA-SESSION-ID':ics}
r=requests.post('https://na1.dm-us.informaticacloud.com/saas/public/core/v3/lookup',data=json.dumps(values),headers=headers)
print(r.status_code)
d=r.json()
print(json.dumps(d,indent=2))

data = r.json()
with open('lookup.json', 'w') as f:
    json.dump(data, f)

def getjson(filepath):
    with open((filepath),'r') as fp:
        return(json.load(fp))


myobj=getjson('./lookup.json')
idd=myobj['objects'][0]['id']
idd1=myobj['objects'][1]['id']
idd2=myobj['objects'][2]['id']
idd3=myobj['objects'][3]['id']
idd4=myobj['objects'][4]['id']

values={
"objects" : [
{
"id": idd
},
{
"id": idd1
},
{
"id": idd2
},
{
"id": idd3
},
{
"id": idd4
}
]
}

r=requests.post('https://na1.dm-us.informaticacloud.com/saas/public/core/v3/export',data=json.dumps(values),headers=headers)
print(r.status_code)

data = r.json()
with open('export.json', 'w') as f:
    json.dump(data, f)

def getjson(filepath):
    with open((filepath),'r') as fp:
        return(json.load(fp))
    
myobj=getjson('./export.json')
#idd=myobj["id"]

r=requests.get('https://na1.dm-us.informaticacloud.com/saas/public/core/v3/export/'+idd+'',headers=headers)
print(r.status_code)

data = r.json()
with open('export_status.json', 'w') as f:
    json.dump(data, f)

def getjson(filepath):
    with open((filepath),'r') as fp:
        return(json.load(fp))
myobj=getjson('./export_status.json')

r=requests.get('https://na1.dm-us.informaticacloud.com/saas/public/core/v3/export/'+idd+'/package',headers=headers)
print(r.status_code)
z = zipfile.ZipFile(io.BytesIO(r.content))
z.extractall('./export_file')

fzip = zipfile.ZipFile('C:\\Users\\vkundum\\Desktop\\export_file.zip','w')
 
for folder, subfolders, files in os.walk('C:\\Users\\vkundum\\Desktop\\export_file'):
 
    for file in files:
        
            fzip.write(os.path.join(folder, file), os.path.relpath(os.path.join(folder,file),'C:\\Users\\vkundum\\Desktop\\export_file'),compress_type = zipfile.ZIP_DEFLATED)
 
fzip.close()
