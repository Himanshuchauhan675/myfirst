from django.http import HttpResponse
from django.shortcuts import render

def homePage(request):
    
    data={
        'title':'home New',
        'bdata':'wecome my collage for you',
        'clist':['php','java','django'],
        'student':[{'name':'prdeep','phone':4568899},
                   {'name':'akki','phone':4568899}
        ],
        'number':[10,20,30,50]
    }
    return render(request,"first.html",data)


def about(request):
    finalans=0
    try:
        n1=request.POST['username']
        n2=request.POST['password']
        finalans=n1+n2
        print(finalans)
    except:
        ExceptionGroup
    return render(request,'footer.html',{'output':finalans})
def calculator(request):
    c=''
    
    try:
     if request.method=="POST":
        n1=eval(request.POST.get('num1'))
        n2=eval(request.POST.get('num2'))
        opr=request.POST.get('opr')
        if opr=="+":
           c=n1+n2
        elif opr=="-":
           c=n1-n2
        elif opr=="*":
           c=n1*n2
        elif opr=="/":
           c=n1/n2
        
     
     
 
 
    except:
      c="invalid user........."
    print(c)
   

   

    return render(request,'calculator.html',{'c':c})


