from msilib.schema import tables
from django.shortcuts import render, redirect
from grapeapp.forms import UsersForm
from grapeapp.models import Usuario

# Create your views here.
#a= 0

def home(request):
    tabela = Usuario.objects.all()
    return render(request,'home2.html',{'usuario':tabela})   


#def home(request):
    #return render(request,'cafe.html',{})

def cadastro(request):
    data = {}
    data['form'] = UsersForm()
    return render(request,'cadastro.html',data)


def docad(request):
    tabela = Usuario.objects.all()
    form = UsersForm(request.POST or None)
    erro = ''
    for c in tabela:        
        if form['usuario'].data == c.usuario:
            erro = "Mensagem de erro"
        
    if form.is_valid() and erro == '':
        form.save()
    #if form.is_valid():
        #form.save()
    return redirect('home')
