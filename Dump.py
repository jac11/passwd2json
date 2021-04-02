#!/usr/bin/env python3

import json

try:
    with open ("milestone_00.txt", "r") as dump:
         Dump_list = []
         Dump_Users = {
         "User_acconut": "", 
         "User_ID": "", 
         "Environment_var": "", 
         "Interpreter": "", 
         "Normal_User": ""}
         for line in dump:
            info = line.strip().split(":")
            Dump_Users["User_acconut"] = info[0]
            Dump_Users["User_ID"] = info[2]
            Dump_Users["Environment_var"] = info[5]
            Dump_Users["Interpreter"] = info[6]
            if int(info[2]) >= 1000 :
                Dump_Users["Normal_User"] = True
                Dump_list.append(Dump_Users.copy())
            else:
                Dump_Users["Normal_User"] = False
                Dump_list.append(Dump_Users.copy())
    json_format = json.dumps(Dump_list,indent=4)
    with open('data_format.json','w') as json :
          json.write(json_format)
    print("script create file data_format.json contain all data information at same dir ")
   except Exception :
        print("Error Exit code 1")
    
