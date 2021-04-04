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

#loop through all files present
for filename in os.listdir():
    #keep track of the files looped through
    i = i + 1
    #only run operations for JSON files
    if filename.endswith(".json"):
        fil = open(filename)
        print(filename)
        data = json.load(fil)
        print(data)
        #create dictionary used to store captured information
        add_dictionary = {}
        #capture date, should always be present so no tries here
        date = (int(float(data['userEditedTimestampUsec'])/1000000))
        date = datetime.datetime.fromtimestamp(date).isoformat()
        add_dictionary['creationDate'] = str(date)
        #try statements to catch if none is present
        #try adding text
        try:
            text = data['textContent']
            # adding the title to each note with H1 header
            text = "<h1>" + data['title'] + "</h1>" + "\n\n" + text
            add_dictionary['content'] = text
        except Exception:
            pass


        #parse lists and check checkmark status format from keep --> listContent":[{"text":"#Development #Personal","isChecked":false}]
        try:
            checklist = data['listContent']
            print(checklist)
            
            
            ####NEEDS FIXIN
            
            
            for key in checklist:
                for key1 in key:
                    print(key1)
                    if key1 == 'text':
                        liststring = checklist[key]
                        print(liststring)
                    if key1 == 'isChecked':
                        if checklist[key] == 'False':
                            liststring = "[ ]" + liststring + '\r\n'
                        if checklist[key] == 'Talse':
                            liststring = "[X]" + liststring + '\r\n'  
                    add_dictionary.append(liststring)
            #add_dictionary['content'] = liststring
        except Exception:
            pass    
        print(add_dictionary)
        #create new dictionary that needs to be appended under activenotes
        format['activeNotes'].append(add_dictionary)
        #open the format file and write to it
        os.chdir(cwd)
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