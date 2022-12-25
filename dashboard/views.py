from django.shortcuts import render
import mysql.connector as sql

# Global Variables
icod = '' 
nam = ''
priq = ''
quan = ''

# Functions
def create_rec(mycon, mycur, code, name, price, quantity):
    query = "INSERT INTO data VALUES({}, '{}', {}, {})".format(icod, nam, pri, quan)    
    mycur.execute(query)
    mycon.commit()  


# Create your views here.
def dashboardaction(request):
    global icod, nam, pri, quan
    if request.method=="POST":
        mycon=sql.connect(host="localhost",user="root",passwd="12345678",database='store')
        mycur=mycon.cursor()
        
        d=request.POST
        for key,value in d.items():
            if key=="item_code":
                icod=value
            if key=="name":
                nam=value
            if key=="price":
                pri=value
            if key=="quantity":
                quan=value
        
        create_rec(mycon,mycur,icod,nam,pri,quan)

    return render(request,'dashboard.html')
