# Import the Canvas module
import requests

# Canvas API URL
API_URL = "https://utexas.instructure.com"
# Canvas API key
API_KEY = "1017~1Wi1q7dm8WaLjbrdqQsP8lpBafuw4LYVSOgi8xxjmFQSSGl9G5UHR0J5VvDfS36z"
# My User ID
USER_ID = "4345098"

headers = {"Authorization": "Bearer " + API_KEY}

courses = requests.get(API_URL + "/api/v1/courses", headers=headers)

for course in courses.json():
    assignments = requests.get(API_URL + "/api/v1/users/" + USER_ID + "/courses/" + str(course["id"]) + "/assignments", headers=headers)
    for assignment in assignments.json():
        #print(assignment)
        if not assignment["due_at"] is None:
            print(assignment["name"] + "\t\t" + assignment["due_at"])
            print(assignment["html_url"])


request = requests.get(API_URL + "/api/v1/users/" + USER_ID + "/courses/:course_id/assignments", headers=headers)
# for todo in request:
#     print(todo)
