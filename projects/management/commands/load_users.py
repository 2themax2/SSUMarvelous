from django.core.management.base import BaseCommand, CommandError
from projects.models import Student, Teacher


class Command(BaseCommand):
    help = "Load some data into Student and Teacher"
    def handle(self, *args, **options):
        # Prepare data
        students = [(440536, "Matthias", "Nijman"),
        (357531, "Max", "Reneman"),
        (440330, "Kyra", "Noordhof"),
        (444444, "Bas", "Mellens")]
        teachers = [("SPNI", "Nieke", "van der Spek"),
        ("LOAA", "Arjan", "Loermans"),
        ("RIMJ", "Martijn", "Riemersma")]

        # Load data into correct model
        count = 0
        for student_nr, first_name, last_name in students:
            obj, created = Student.objects.get_or_create(student_nr=student_nr,first_name=first_name,last_name=last_name)
            if created:
                count += 1
        for teacher_code, first_name, last_name in teachers:
            obj, created = Teacher.objects.get_or_create(teacher_code=teacher_code,first_name=first_name,last_name=last_name)
            if created:
                count += 1
        print(f"{count} new objects created. {len(students)+len(teachers)-count} object already existed.")