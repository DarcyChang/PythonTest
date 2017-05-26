#codinf=utf-8
import requests
import json
import os

#Step flow#
#1. get all_docs
#2. get idName
#3. change / to %2
#4. get all idName json snd save


hosturl = 'https://4fa75cd1-58c9-40f8-b564-f0ea711bd506-bluemix.cloudant.com'
user = '4fa75cd1-58c9-40f8-b564-f0ea711bd506-bluemix'
password = '9490c5b340b894b4db5f02b357cf59bf1a6fec84543e2080bcb1049cd2d4a4f5'


def change_char_for_url(doc_id='null'):
    if doc_id != '_design/library':
        doc_id_change = doc_id.replace('/','%2F')
        return doc_id_change
    else:
        return doc_id
        
def get_json_from_couchdb(idName='null'):
    idName_api_url = hosturl+'/nodered/'+idName
    r=requests.get(idName_api_url,auth=(user, password))        
    output=r.text
    return output
    
def save_json(json = 'null',filename='null'):
    if filename == '_design/library':
        filename = filename.replace('/','%2F')
    F2 = 'CouchDB_json/'+filename+'.json'
    print F2
    file=open(F2,'w')
    file.write(json.strip().encode('utf-8'))
    file.close()
    

#1. get all_docs
all_docs = get_json_from_couchdb('_all_docs')

#2. get idName
# get number
json_obj_of_all_docs = json.loads(all_docs)
all_doc_number = json_obj_of_all_docs['total_rows']
print json_obj_of_all_docs

while all_doc_number > 0:
    doc_number_id = json_obj_of_all_docs['rows'][all_doc_number-1]['id']
    idName_for_url = change_char_for_url(doc_number_id) #3. change / to %2F except nodered >> _design/library
    idName_json = get_json_from_couchdb(idName_for_url)
    save_json(idName_json,idName_for_url)#4. get all idName json snd save
    all_doc_number -= 1 

#note. no need to change %2F: 
#   1. humix >>_design/module 
#   2. nodered >> _design/library
