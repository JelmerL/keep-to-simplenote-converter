#This simple converter iterates through all google keep JSON files in a directory, extracts the note and builds a SimpleNote accepted JSON for importing into SimpleNote

import json
import os
import datetime

#Setting the correct directory and entering the Keep Files folder you should create containing the JSON files
cwd = os.getcwd()
path = os.path.join(cwd, 'Keep Files')
os.chdir(path)
print("Working directory changed to:     ",path)

for filename in os.listdir():
    if filename.endswith(".json"):
        fil = open(filename)
        data = json.load(fil)
        text = data['textContent']
        date = (int(float(data['userEditedTimestampUsec'])/1000000))
        date = datetime.datetime.fromtimestamp(date).isoformat()
        #change the directory to where the standard file is
        os.chdir(cwd)
        #open the JSON file
        content = json.load(open('simplenote.json'))
        print(content)
        add_dictionary = {}
        add_dictionary['content'] = text
        add_dictionary['creationDate'] = str(date)
        #create new dictionary that needs to be appended under activenotes
        content['activeNotes'].append(add_dictionary)
        print(content)
        #open the format file and write to it
        with open('simplenote.json', 'w') as json_file:
            json.dump(content, json_file, indent = 3)
        #change the directory back to where the Keep files are before going through to the next file
        os.chdir(path)
    else:
        #just in case there are no JSON files in the directory
        print("No JSON files found or you are in the wrong directory")