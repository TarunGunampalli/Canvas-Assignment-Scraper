# Import the Canvas module
from canvasapi import Canvas
import requests

# Canvas API URL
API_URL = "https://utexas.instructure.com"
# Canvas API key
API_KEY = "1017~1Wi1q7dm8WaLjbrdqQsP8lpBafuw4LYVSOgi8xxjmFQSSGl9G5UHR0J5VvDfS36z"

# Initialize a new Canvas object
canvas = Canvas(API_URL, API_KEY)

user = canvas.get_user(4345098)
courses = canvas.get_courses()

events = user.get_calendar_events_for_user(submission_types=["assignment"])

print(events)

for event in events:
    print(event)

# headers = {"Authorization": "Bearer " + API_KEY}

# for course in courses:
#     print(course.get_user_in_a_course_level_assignment_data(user))

# for course in courses:
#     assignments = requests.get("https://utexas.instructure.com//api/v1/courses/1290172/assignments")
#     print(assignments.text)

# for course in courses:
#     assignments = user.get_assignments(course)
#     print(assignments)
#     for assignment in assignments:
#         print(assignment)
