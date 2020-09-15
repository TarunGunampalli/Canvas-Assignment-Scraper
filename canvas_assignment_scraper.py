# Import the Canvas class
from canvasapi import Canvas

# Canvas API URL
API_URL = "https://utexas.instructure.com"
# Canvas API key
API_KEY = <KEY>

# Initialize a new Canvas object
canvas = Canvas(API_URL, API_KEY)

# Grab user with ID of 1
courses = canvas.get_courses()

for course in courses:
    assignments = course.get_assignments()
    for assignment in assignments:
        print(assignment)
