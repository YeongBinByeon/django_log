from django.shortcuts import render
import pandas as pd
from .models import *
import sqlite3
from django.http import JsonResponse

# Create your views here.
def utterance(request):
    print("hello")
    df = pd.read_excel(r'C:\code_folder\django_log\adminPage\data.xlsx')
    print(df['date'].iloc[0])
    print(df.index)
    con = sqlite3.connect("db.sqlite3")
    print(con)
    print(df)
    #df.to_sql('webApp_utterance', con)

    #print(df['date'].iloc[0])
    #print(df['tv_search_title'].iloc[0] )
    for i in df.index:
        Utterance(date=df['date'].iloc[i], language=df['language'].iloc[i], mainAction=df['mainAction'].iloc[i], utterance=df['utterance'].iloc[i]).save()
    #queryset = Utterance.objects.create(date=df['date'].iloc[0], tv_search_title=df['tv_search_title'].iloc[0], tv_unknown_search=df['tv_unknown_search'].iloc[0], tv_open_search=df['tv_open_search'].iloc[0], tv_play_title=df['tv_play_title'].iloc[0])
    return render(request, "webApp/test.html")

# Create your views here.
def utterance1(request):
    print("hello")
    df = pd.read_excel(r'C:\code_folder\django_log\adminPage\data1.xlsx')
    print(df['date'].iloc[0])
    print(df.index)
    con = sqlite3.connect("db.sqlite3")
    print(con)
    print(df)
    #df.to_sql('webApp_utterance', con)

    #print(df['date'].iloc[0])
    #print(df['tv_search_title'].iloc[0] )
    for i in df.index:
        Utterance(date=df['date'].iloc[i], language=df['language'].iloc[i], mainAction=df['mainAction'].iloc[i], utterance=df['utterance'].iloc[i]).save()
    #queryset = Utterance.objects.create(date=df['date'].iloc[0], tv_search_title=df['tv_search_title'].iloc[0], tv_unknown_search=df['tv_unknown_search'].iloc[0], tv_open_search=df['tv_open_search'].iloc[0], tv_play_title=df['tv_play_title'].iloc[0])
    return render(request, "webApp/test.html")

def saveKRMainAction(request):
    df = pd.read_excel(r'C:\code_folder\django_log\adminPage\kr_mainAction.xlsx')
    con = sqlite3.connect("db.sqlite3")
    for i in df.index:
        KR_MainAction(date=df['date'].iloc[i], language=df['language'].iloc[i], mainAction=df['mainAction'].iloc[i], count=df['count'].iloc[i], rate=df['rate'].iloc[i]).save()
    return render(request, "webApp/test.html")

def readKRMainAction(request):
    querySet = KR_MainAction.objects.all()
    print(type(list(querySet.values())))
    
    for row in querySet.values_list():
        print(row)
    
    
    return JsonResponse(data=list(querySet.values()), safe=False)

def chartjs(request):
    return render(request, "webApp/chartjs.html")
