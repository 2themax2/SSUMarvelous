from operator import inv
from django.core.management.base import BaseCommand
from projects.models import RoleTest, Role, Student, Teacher, Project, ProjectStudents


class Command(BaseCommand):
    help = "Load test data into the database"
    def handle(self, *args, **options):
        # Clear the current data
        Role.objects.all().delete()

        # Prepare a list of roles with template (role, description)
        roles = [
        ("Plant", "You are a Plant, meaning you’re probably a creative, imaginative thinker. You might sometimes get lost in your own ideas, but your originality can spark innovative solutions."),
        ("Investigator", "You are an Investigator, meaning you probably enjoy exploring new opportunities and connecting with different people. Your enthusiasm can energize the team, though you might lose interest if the novelty wears off."),
        ("Coordinator", "You are a Coordinator, meaning you probably excel at bringing people together and clarifying goals. You help everyone stay aligned, but be mindful of seeming too direct at times."),
        ("Shaper", "You are a Shaper, meaning you probably push the team forward and enjoy tackling challenges head-on. Your drive can be inspiring, though it may come across as overly forceful under stress."),
        ("Monitor", "You are a Monitor, meaning you probably look at all angles and analyze situations carefully. This logical approach helps the team make sound decisions, but others might see you as detached or too critical."),
        ("Teamworker", "You are a Teamworker, meaning you probably excel at fostering harmony and maintaining good relationships. While your diplomacy keeps the group cohesive, you might hold back when strong decisions are needed."),
        ("Implementer", "You are an Implementer, meaning you probably prefer structured plans and practical action. Your reliability helps keep projects on track, but you might need to stay open-minded about new ideas."),
        ("Finisher", "You are a Finisher, meaning you probably pay close attention to details and deliver high-quality results. This diligence is valuable, but be cautious about over-focusing on minor flaws or bottlenecks."),
        ("Specialist", "You are a Specialist, meaning you probably have in-depth expertise in a particular area. You bring valuable knowledge to the team, though it’s helpful to stay connected to broader team goals."),
        ]

        # Add each role to the model
        for role, description in roles:
            object = Role(role=role, description=description)
            object.save()
        print("Added roles to database.")

        # Clear the current data
        RoleTest.objects.all().delete()

        # Prepare a list of questions with template (role, question)
        question_list = [
        ("Plant", "I enjoy coming up with unconventional solutions that often surprise others."),
        ("Plant", "I get inspired by brainstorming sessions and prefer creating something new over repeating existing ideas."),
        ("Investigator", "I easily make connections and see potential collaboration partners everywhere."),
        ("Investigator", "I enjoy connecting people and love exploring new opportunities."),
        ("Coordinator", "I have a good overview and ensure everyone knows what needs to be done."),
        ("Coordinator", "I logically divide tasks and monitor the team's progress."),
        ("Shaper", "I like motivating others to take action and make quick decisions."),
        ("Shaper", "I perform well under time pressure and enjoy a fast work pace."),
        ("Monitor", "I love delving into problems and asking critical questions when needed."),
        ("Monitor", "Before making a decision, I like to consider all sides of the matter."),
        ("Teamworker", "I find it important that everyone feels comfortable and can truly collaborate."),
        ("Teamworker", "I quickly notice tensions or irritations in the group and try to resolve them."),
        ("Implementer", "I enjoy translating great plans into a concrete action plan."),
        ("Implementer", "I work in a structured manner and like to complete tasks efficiently."),
        ("Finisher", "I am a perfectionist and check that everything is correct down to the last detail."),
        ("Finisher", "I derive satisfaction from completing a project meticulously."),
        ("Specialist", "I enjoy diving deep into a subject and mastering the finer details of the craft."),
        ("Specialist", "I like sharing my expertise with others and continuously learning."),
        ]

        # Add each question to the model
        for role, question in question_list:
            object = RoleTest(role=role, question=question)
            object.save()
        print("Added questions to database.")
        
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
        teachers = [("SPNI", "Nienke", "van der Spek"),
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
        print(f"{count} new users created. {len(students)+len(teachers)-count} users already existed.")

        # Clear the current data
        Project.objects.all().delete()

        nienke = Teacher.objects.get(teacher_code="SPNI")
        arjan = Teacher.objects.get(teacher_code="LOAA")
        martijn = Teacher.objects.get(teacher_code="RIMJ")

        # Prepare a list of projects
        projects = [
        (1, "Klimaat bescherming", "Het klimaat moet beschermd. Laten we daar samen aan werken!", nienke),
        (2, "Motor rijles", "Iedereen moet leren motor rijden!", arjan),
        (3, "Software Startup", "Bedenk je eigen Software Startup en werk deze uit.", martijn),
        ]

        # Add each project to the model
        for project_nr, name, description, teacher in projects:
            object = Project(project_nr=project_nr, name=name, description=description, teacher=teacher)
            object.save()
        print("Added projects to database.")

        # Clear the current data
        ProjectStudents.objects.all().delete()

        proj1 = Project.objects.get(project_nr=1)
        proj2 = Project.objects.get(project_nr=3)

        # Add each project student coupling to the model
        for student in Student.objects.all():
            object = ProjectStudents(project=proj1, student=student)
            object.save()
            object = ProjectStudents(project=proj2, student=student)
            object.save()
        print("Added project student coupling to database.")