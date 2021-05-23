import graphene
from graphene_django import DjangoObjectType

from polls.models import Choice,Question

class QuestionType(DjangoObjectType):
    class Meta:
        model = Question
        fields = "__all__"

class ChoiceType(DjangoObjectType):
    class Meta:
        model = Choice
        fields = "__all__"

class Query(graphene.ObjectType):
    all_questions = graphene.List(QuestionType)
    all_choices = graphene.List(ChoiceType)

    def resolve_all_questions(root, info):
        return Question.objects.all()
    def resolve_all_choices(root, info):
        return Choice.objects.all()

schema = graphene.Schema(query=Query)