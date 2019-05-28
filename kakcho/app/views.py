from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.core.files import File

from .serializers import UploadFileSerializer
from rest_framework.response import Response
from .forms import UploadFileForm
from .models import UploadFileModel, FirstTaskModel, SecondTaskModel, RoundOffModel

import pandas
import numpy
import os


class LoginView(View):
    def get(self,request):
        return render(request, 'login.html')

class UploadView(View):
    def post(self, request):
        if request.user.is_authenticated:
            model = UploadFileModel(file= request.FILES['file'], user= request.user)
            model.save()

            return redirect("task1", str(model.id))
        else:
            return HttpResponse("You need to authenticate")

    def get(self, request):
        form = UploadFileForm()
        return render(request, "form.html", {'form': form})

class FirstTaskView(View):
    def get(self, request, pk):
        if request.user.is_authenticated:
            file_set = UploadFileModel.objects.filter(pk= pk)
            file = file_set.values()[0]
            file_set = file_set[0]
            filename = file['file'].split("/")[-1].split(".")[0]
            df = pandas.read_csv(file['file'])
            df_free = df.loc[df['Type'] == 'Free']
            df_paid = df.loc[df['Type'] == 'Paid']
            if not os.path.exists("temp/" + filename):
                os.makedirs("temp/" + filename)
            df_free.to_csv("temp/"+filename + "/free.csv")
            df_paid.to_csv("temp/"+filename + "/paid.csv")

            f =  open("temp/" + filename +"/free.csv", "rb") 
            django_file = File(f)
            model = FirstTaskModel(uploadfile= file_set)
            model.file.save(filename + "/free.csv", django_file, save=True)
            f = open("temp/" + filename + "/paid.csv", "rb")
            model = FirstTaskModel(uploadfile= file_set)
            model.file.save(filename + "/paid.csv", django_file, save=True)
            return redirect("task2", pk )
            

class SecondTaskView(View):
    def get(self, request, pk):
        if request.user.is_authenticated:
            file = UploadFileModel.objects.filter(pk=pk)[0]
            query_set_values = FirstTaskModel.objects.filter(uploadfile= file.pk)
            for first_task in query_set_values.values():
                file = first_task['file']
                print(file)
                filename = file.split("/")[-2]
                df = pandas.read_csv(file)
                for rating in df['Content Rating'].unique():
                    df_temp = df.loc[df['Content Rating'] == rating ]
                    df_temp.to_csv("temp/"+ filename + "/" + rating + ".csv")

                    print(type(query_set_values.filter(file=file)))

                    f = open("temp/" + filename + "/" + rating + ".csv", "rb")
                    django_file = File(f)
                    model = SecondTaskModel(firsttask= query_set_values.get(file= file))
                    model.file.save(filename + "/" + rating +".csv", django_file, save=True)

            return redirect("roundoff", pk)

class RoundOffView(View):
    def get(self, request, pk):
        if request.user.is_authenticated:
            file_set = UploadFileModel.objects.filter(pk= pk)
            file = file_set.values()[0]
            filename = file['file'].split("/")[-1].split(".")[0]
            df = pandas.read_csv(file['file'])
            df_new = df.copy()
            df_new['Rating Roundoff'] = numpy.around(df['Rating'])
            df_new.to_csv("temp/" + filename + "/round.csv")
            
            f =  open("temp/" + filename + "/round.csv")
            django_file = File(f)
            model = RoundOffModel(uploadfile= file_set[0])
            model.file.save(filename + "/round.csv", django_file, save=True)

            return HttpResponse("Completed!")
