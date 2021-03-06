#This simple converter iterates through all google keep JSON files in a directory, extracts the note and builds a SimpleNote accepted JSON for importing into SimpleNote

import json
import os
import datetime

#some standard string and dictionary formats used later on 

format = {"activeNotes": [],"trashedNotes": [{"content": "","creationDate": "2021-04-01T14:59:47.875Z","lastModified": "2021-04-01T16:32:53.898Z"}]}
checked = "- [X] "
unchecked = "- [ ] "
errors = 0
#Setting the correct directory and entering the Keep Files folder you should create containing the JSON files
cwd = os.getcwd()
path = os.path.join(cwd, 'Keep Files')
os.chdir(path)
print("Working directory changed to:     ",path, "\n")
i = 0

#loop through all files present
for filename in os.listdir():
    #only run operations for JSON files
    if filename.endswith(".json"):
        #keep track of the files looped through
        i = i +1
        add_dictionary = {"content": ""}
        fil = open(filename)
        print(filename)
        data = json.load(fil)
        #capture date, should always be present so no tries here
        date = (int(float(data['userEditedTimestampUsec'])/1000000))
        date = datetime.datetime.fromtimestamp(date).isoformat()
        add_dictionary['creationDate'] = str(date)
        #try adding text
        try:
            text = data['textContent']
            # adding the title to each note with H1 header
            text = data['title'] + "\n\n" + text
            add_dictionary['content'] = add_dictionary['content'] + text
        except Exception as e: 
            print(e)

        #parse lists and check checkmark status format from keep --> listContent":[{"text":"#Development #Personal","isChecked":false}]
        try:
            checklist = data['listContent']
            #parse the checklist items in the correct format
            for key in checklist:
                checklistcontents = ""
                for keys in key:
                    if keys == 'isChecked':
                        if key[keys] == True:
                            checklistcontents = checked + checklistcontents + "\r\n"
                        if key[keys] == False:
                            checklistcontents = unchecked + checklistcontents + "\r\n"
                    add_dictionary['content'] = add_dictionary['content'] + checklistcontents
                    if keys == 'text':
                        checklistcontents = key[keys] + checklistcontents
            #add the title to the file
            add_dictionary['content'] = data['title'] + '\n' + add_dictionary['content']
        except Exception as e: 
            print(e)

        #create new dictionary that needs to be appended under activenotes
        format['activeNotes'].append(add_dictionary)
        #change the directory to where the JSON export file is located and write to it
        os.chdir(cwd)
        with open('simplenote.json', 'w') as json_file:
            json.dump(format, json_file, indent = 3)
            print(i,": Added", filename, "to JSON")
        #change the directory back to where the Keep files are before going through to the next file
        os.chdir(path)
        
    else:
        #just in case there are no JSON files in the directory
        print("Skipping File, not JSON")
        pass

print("\n","Number of notes converted:",i, "\n")
print("Hit Enter to exit")
input()