from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import TEAM_Register, TEAM_Login, clues
import datetime
import time
# Create your views here.

WORD_LIST = ["Liquid_Cooling","Shell_Scripting","Cloud_Storage","Cache","RAM","Algorithms","Android","Inbuilt_function","Java","PHP",
"Linux","Recycle_Bin","Data_Analysis","Protocols","Virtual_Reality","Firewall","GitHub","Bitcoin","Mac_Address","Pandas",
"AI","Command_Prompt","Automation","Compiler","Machine_Learning","Processor","Anaconda","Antivirus","Kali","Topology","timepass","Operating_System","Encapsulation"]

count = 0
team_name1 = ""
seq = [1,]
timer = []
def login(request):
    return render(request,"login.html",{})

def register(request):
    global team_name1
    context = {}
    if request.method=="POST":
        print("in here")
        data = request.POST
        team_name1 = data['team_name']
        obj = TEAM_Register(team_name = data['team_name'], stu1_name = data['s1'], stu2_name = data['s2'])
        obj.save()
        context = {'status':'Successful'}
        return redirect("/rules/")
    return render(request,"register.html",context)

def rules(request):
    return render(request,"rules.html",{})

def home(request):
    global WORD_LIST
    global seq
    global timer
    global count
    count = 0
    seq = [1,]
    t0 = time.time()
    timer.append(t0)
    print(t0)
    obj2 = clues.objects.filter(clue_seq=1)
    print(obj2)
    
    clue_des = obj2[0].clue_desc
    clue_no = len(seq)
    context = {'words' : WORD_LIST,'clue_desc':clue_des,'clue_no':clue_no}
    return render(request,"talash_home_page.html",context)

def checkclue(request, id):
    global WORD_LIST
    global count
    global team_name1
    global seq
    global timer
    stat = {}
    context = {'words' : WORD_LIST}
    obj = clues.objects.filter(clue_ans=id)
    l = len(seq)
    print(obj)
    if(len(seq)>=4):
        t1 = time.time()
        total_time = t1-timer[0]
        print(total_time)
        count=count+1
        stat = {'title':'Congratulations','team_name':team_name1,'total_clues':count,'total_time':total_time}
        return render(request,'final_page.html',stat)
    if len(obj)>0:
        print("found")
        if ((obj[0].clue_ans==id) and (str(count+1)==obj[0].clue_seq)):
            count = count + 1
            seq.append(count+1)
            print(seq)
            return redirect('/nextclue/')
        else:
            t1 = time.time()
            total_time = t1-timer[0]
            stat = {'title':'Dead End','team_name':team_name1,'total_clues':count,'total_time':total_time}
            return render(request,'final_page.html',stat)

    else:
        t1 = time.time()
        total_time = t1-timer[0]
        stat = {'title':'Dead End','team_name':team_name1,'total_clues':count,'total_time':total_time}
        return render(request,'final_page.html',stat)
    return redirect('/nextclue/')

def nextclue(request):
    global WORD_LIST
    global count
    global seq
    l = len(seq)
    obj2 = clues.objects.filter(clue_seq=l)
    print(obj2)
    
    clue_des = obj2[0].clue_desc
    clue_no = len(seq)
    context = {'words' : WORD_LIST,'clue_desc':clue_des,'clue_no':clue_no}
    return render(request,"talash_home_page.html",context)
