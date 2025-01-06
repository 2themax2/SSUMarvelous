from django.core.management.base import BaseCommand, CommandError
from projects.models import RoleTest


class Command(BaseCommand):
    help = "Load RoleTest Questions"
    def handle(self, *args, **options):
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