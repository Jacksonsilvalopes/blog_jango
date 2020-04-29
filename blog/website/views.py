from django.shortcuts import render



# Create your views here.
def hello_blog(request):
    lista = ['Djang', 'Python', 'Git', 'Html', 'banco de dados',
     'linux', 'Nginx', 'Uwsgi', 'Systemactl']
    data = {'name': 'Curso de Django 3', 'lista_tecnologia': lista}
    return render(request, 'indexgeral.html', data)