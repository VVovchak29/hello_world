from django.http import HttpResponse
# from django.http import Http404


# Create your views here.
from django.shortcuts import get_object_or_404
from polls.models import Question, Choice
from rest_framework import generics
from polls.serializers import QuestionSerializer, ChoiceSerializer



def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")



# def index(request):
#     question_list = Question.objects.all()
#     return HttpResponse(', '.join([q.question_text for q in  question_list]))


class Question_List(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer



class Question_Detail(generics.RetrieveUpdateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


    def get_object(self):
        obj = get_object_or_404(Question, pk=self.kwargs.get('question_id'))
        return obj



class Choice_List(generics.ListCreateAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer
