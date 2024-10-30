import os
import sys

import django
from faker import Faker
#from datetime from datetime

# Add the project directory to the sys.path
sys.path.append("D://my_django_project//myDjangoProject")


# Set up Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myDjangoProject.settings')
django.setup()


# Import the model
from myDjangoSecond_app2.models import Student

# Initialize Faker
fake = Faker()

# Populate script
def create_students(n=50):
    for _ in range(n):
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = fake.unique.email()
        enrollment_date = fake.date_between(start_date='-30d', end_date='today')

        Student.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            course_name = "Django Training",
            enrollment_date=enrollment_date
        )
if __name__ == 'main':
    print("Populating the database with student data...")
    create_students(50)
    print("Database populated successfully...")
