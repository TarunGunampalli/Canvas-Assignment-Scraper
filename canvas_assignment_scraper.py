import requests
import json
import pickle
import os.path
from googleapiclient.discovery import build

# Canvas API URL
API_URL = "https://utexas.instructure.com"
# Canvas Auth key
AUTH_KEY = <Authentication Key>
# My User ID
USER_ID = <User_ID>

homeworklist_code = <code for "Homework" tasklist>
testlist_code = <code for "Test" tasklist>

headers = {"Authorization": "Bearer " + AUTH_KEY}

if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)

service = build('tasks', 'v1', credentials=creds)

current_tasks = service.tasks().list(tasklist=testlist_code, maxResults=100).execute()
courses = requests.get(API_URL + "/api/v1/courses", headers=headers)

for course in courses.json():
    assignments = requests.get(API_URL + "/api/v1/users/" + USER_ID + "/courses/" + str(course["id"]) + "/assignments", headers=headers)
    for assignment in assignments.json():
        alreadyInTasks = False
        if assignment["due_at"] is not None:
            
            if "items" in current_tasks.keys():
                # while True:
                for current_task in current_tasks["items"]:
                    if current_task["title"] == assignment["name"]: # and current_task["due"] == assignment["due_at"]
                        # print(current_task["title"] + ", " + assignment["name"])
                        alreadyInTasks = True
                        print(assignment["name"] + " is already in the tasklist")
                    
                    # if ()
            
            if not alreadyInTasks:
                parameters={ "title":assignment["name"], "notes":assignment["html_url"], "due":assignment["due_at"], "status":"needsAction" }
                task = service.tasks().insert(tasklist=testlist_code, body=parameters, x__xgafv='1').execute()

                print(task["title"] + " successfully added")

current_tasks = service.tasks().list(tasklist=testlist_code, maxResults=100).execute()
if "items" in current_tasks.keys():
    for task1 in current_tasks["items"]:
        for task2 in current_tasks["items"]:
            if task1["title"] == task2["title"] and task1["due"] == task2["due"]:
                if task1["id"] != task2["id"]:
                    service.tasks().delete(tasklist=testlist_code, task=task2["id"], x__xgafv='1').execute()
                    print(task2["title"] + " deleted")
