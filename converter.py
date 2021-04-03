#This simple converter iterates through all google keep JSON files in a directory, extracts the note and builds a SimpleNote accepted JSON for importing into SimpleNote

import json
import os
import datetime

format = {"activeNotes": [],"trashedNotes": [{"content": "","creationDate": "2021-04-01T14:59:47.875Z","lastModified": "2021-04-01T16:32:53.898Z"}]}

#Setting the correct directory and entering the Keep Files folder you should create containing the JSON files
cwd = os.getcwd()
path = os.path.join(cwd, 'Keep Files')
os.chdir(path)
print("Working directory changed to:     ",path, "\n")
i = 0
for filename in os.listdir():
    i = i + 1
    print(filename)
    if filename.endswith(".json"):
        fil = open(filename)
        data = json.load(fil)
        text = data['textContent']
        # adding the title to each note with H1 header
        text = "<h1>" + data['title'] + "</h1>" + "\n\n" + text
        date = (int(float(data['userEditedTimestampUsec'])/1000000))
        print(date)
        date = datetime.datetime.fromtimestamp(date).isoformat()
        #change the directory to where the standard file is
        os.chdir(cwd)
        #open the JSON file
        add_dictionary = {}
        add_dictionary['content'] = text
        add_dictionary['creationDate'] = str(date)
        #create new dictionary that needs to be appended under activenotes
        format['activeNotes'].append(add_dictionary)
        #open the format file and write to it
        with open('simplenote.json', 'w') as json_file:
            json.dump(format, json_file, indent = 3)
            print(i,": Added", filename, "to JSON")
        #change the directory back to where the Keep files are before going through to the next file
        os.chdir(path)
    else:
        #just in case there are no JSON files in the directory
        print("No JSON files found or you are in the wrong directory")

print("\n","Number of notes converted:",i, "\n")
print("Hit Enter to exit")
input()