#codinf=utf-8
import requests
import json
import os

def newOpen(filename='null'):
    str1 = os.popen('hostname').read()
    hostName = str1[0:-1]
    url = "http://127.0.0.1:5984/nodered/"+hostName+"%2F"+filename
    r=requests.get(url)        
    output=r.text
    F2 = 'CouchDB_json/'+filename+'.json'
    file=open(F2,'w')
    file.write(output.strip().encode('utf-8'))
    file.close()

def newOpen_designLibrary(dbname='null',modulename='null',filename='null'):
    url = "http://127.0.0.1:5984/"+dbname+'/'+modulename
    r=requests.get(url)        
    output=r.text
    F2 = 'CouchDB_json/'+dbname+filename+'.json'
    file=open(F2,'w')
    file.write(output.strip().encode('utf-8'))
    file.close()


newOpen('flow')
newOpen('settings')
newOpen('credential')
newOpen_designLibrary('humix','_design/module','designModule')
newOpen_designLibrary('nodered','/_design/library','designLibrary')



