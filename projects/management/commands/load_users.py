from operator import inv
from django.core.management.base import BaseCommand, CommandError
from projects.models import Student, Teacher


class Command(BaseCommand):
    help = "Load some data into Student and Teacher"
    def handle(self, *args, **options):
        # Prepare data
        students = [(440536, "Matthias", "Nijman", "HBO-ICT Software Engineering", 2, 2, 2, 2, 2, 2, 2, 2, 2),
        (357531, "Max", "Reneman", "HBO-ICT Software Engineering", 2, 2, 2, 2, 2, 2, 2, 2, 12),
        (440330, "Kyra", "Noordhof", "HBO-ICT Software Engineering", 2, 2, 2, 2, 12, 2, 2, 2, 2),
        (430315, "Bas", "Mellens", "HBO-ICT Software Engineering", 2, 12, 2, 2, 2, 2, 2, 2, 2),
        (444444, "Jos", "Joszoon", "Rechten", 12, 2, 2, 2, 2, 2, 2, 2, 2),
        (444445, "Lies", "Bakker", "Medische Diagnostiek", 12, 2, 2, 2, 2, 2, 2, 2, 2),
        (444446, "Femke", "Prins", "Medische Diagnostiek", 2, 12, 2, 2, 2, 2, 2, 2, 2),
        (444447, "Willem", "de Vries", "Medische Diagnostiek", 2, 2, 12, 2, 2, 2, 2, 2, 2),
        (444448, "Selim", "Kirbiyik", "Dans", 2, 2, 2, 12, 2, 2, 2, 2, 2),
        (444449, "José", "Uniloop", "Acteur", 2, 2, 2, 2, 12, 2, 2, 2, 2),
        (444450, "David", "Sabelis", "Acteur", 2, 2, 2, 2, 2, 12, 2, 2, 2),
        (444451, "Jarno", "Robbe", "Rechten", 2, 2, 2, 2, 2, 2, 12, 2, 2),
        (444452, "Rob", "Robinson", "Rechten", 2, 2, 2, 2, 2, 2, 2, 12, 2),
        (444453, "Sophie", "Blom", "Geschiedenis", 2, 2, 2, 2, 2, 2, 2, 2, 12),
        (444454, "Asllan", "Ibrahimi", "Geschiedenis", 12, 2, 2, 2, 2, 2, 2, 2, 2),
        (444455, "Sem", "van der Vlugt", "Geschiedenis", 2, 12, 2, 2, 2, 2, 2, 2, 2),
        (444456, "Astrid", "Bolt", "Acteur", 2, 12, 2, 2, 2, 2, 2, 2, 2),
        (444457, "Linda", "Noordhuis", "Pabo", 2, 2, 12, 2, 2, 2, 2, 2, 2),
        (444458, "Pepijn", "Douwma", "Pabo", 2, 2, 2, 12, 2, 2, 2, 2, 2),
        (444459, "Wessel", "Berends", "Bewegingswetenschappen", 2, 2, 2, 2, 12, 2, 2, 2, 2),
        (444460, "Bart", "Bernard", "Geoloog", 2, 12, 2, 2, 2, 2, 2, 2, 2),
        (444461, "Erik", "Roos", "Geoloog", 2, 2, 2, 2, 2, 12, 2, 2, 2),
        (444462, "Sacha", "Veenstra", "Natuurkunde", 2, 2, 2, 2, 2, 2, 12, 2, 2),
        (444463, "Koen", "Hendrikse", "Natuurkunde", 2, 2, 2, 2, 2, 2, 2, 12, 2),
        (444464, "Koen", "Kooij", "Natuurkunde", 2, 2, 2, 2, 2, 2, 2, 2, 12),
        (444465, "Bas", "Holtman", "Natuurkunde", 2, 2, 2, 2, 2, 2, 12, 2, 2),
        (444466, "Joeke", "Schaafsma", "Natuurkunde", 12, 2, 2, 2, 2, 2, 2, 2, 2),]
        teachers = [("SPNI", "Nieke", "van der Spek"),
        ("LOAA", "Arjan", "Loermans"),
        ("RIMJ", "Martijn", "Riemersma")]

        # Load data into correct model
        count = 0
        for student in students:
            obj, created = Student.objects.get_or_create(student_nr=student[0],first_name=student[1],last_name=student[2], mayor=student[3], plant=student[4],investigator=student[5],coordinator=student[6],shaper=student[7],monitor=student[8],teamworker=student[9],implementer=student[10],finisher=student[11],specialist=student[12])
            if created:
                count += 1
        for teacher_code, first_name, last_name in teachers:
            obj, created = Teacher.objects.get_or_create(teacher_code=teacher_code,first_name=first_name,last_name=last_name)
            if created:
                count += 1
        print(f"{count} new objects created. {len(students)+len(teachers)-count} object already existed.")