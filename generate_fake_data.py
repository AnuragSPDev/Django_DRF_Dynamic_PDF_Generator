import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Django_DRF_Dynamic_PDF_Generator.settings')

django.setup()

from pdf_generator.models import Employee
import random

from faker import Faker
fake = Faker()

def generate_fake_data(num):
    for _ in range(num):
        Employee.objects.create(
            id=random.randint(100, 1000),
            name=fake.name(),
            designation=fake.job(),
            department=fake.administrative_unit()
        )

def main():
    num = int(input('Number of employee"s you want to add: '))
    generate_fake_data(num)

if __name__ == '__main__':
    main()