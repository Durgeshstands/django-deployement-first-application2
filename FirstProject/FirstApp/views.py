from django.shortcuts import render
from django.http import HttpResponse;

# Create your views here.
def display(reqest): #view function
       ##ss ---> is html-data/code
       # print("welcome/ url is required & display() is executed");
        ss = '''
            <center>
                <h2style="color:Blue;background-color:yellow;border:2px Solid Brown;">
                    ***Hello User, Welcome to Django First-Project First-App***
                </h2>
                <hr />
            </center>
        ''';
        
        return HttpResponse(ss);
             
def hello(request):
    print("hello/ url is requested & hello() is executed");
    ss='''
	<html>
		<head>
			<title>Hello Webpage</title>
			<style>
				h1{
					color:Blue;
					width:90%;
				}
				h2{
					color:Green;
					width:80%;
				}
				h3{
					color:Red;
					width:70%;
				}
				h1,h2,h3{
					background-color:lightblue;
					border:2px Solid Brown;
				}
			</style>
		</head>
		<body>
			<center>
				<h1>Hello User..!!!</h1>
				<hr color='brown' width='80%'/>
				<h2>Welcome to Django-App</h2>
				<hr color='brown' width='60%'/>
				<h3>Have a nice day...</h3>
				<hr color='brown' width='40%'/>
			</center>
		</body>
	</html>
	''';
    return HttpResponse(ss);

