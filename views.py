from django.core.files import temp
from django.shortcuts import render, redirect
from .models import *
from .myforms import *


def index(req):
    return render(req, 'index.html')


def add(req):
    # Company.objects.create(title='J7')
    # Company.objects.create(title='DOBRY')
    # p1 = Product(name='orange', price=140, volume=1, packaging='banka', is_recommended=True)
    # p2 = Product(name='multy', price=150, volume=2, packaging='korobka', is_recommended=True)
    # p3 = Product(name='apple', price=160, volume=3, packaging='bytilka', is_recommended=False)
    # c1 = Company.objects.get(title='J7')
    # c2 = Company.objects.get(title='DOBRY')
    # c2.product_set.add(p1, bulk=False)
    # c2.product_set.add(p2, bulk=False)
    # c2.product_set.add(p3, bulk=False)
    # print(c1.product_set.count())
    # print(c1.product_set.values())
    # print(c1.product_set.values_list())
    s1=Student.objects.create(name='Victor', group='g001')
    s2=Student.objects.create(name='Boris', group='g001')
    s3=Student.objects.create(name='Max', group='g001')
    s4=Student.objects.create(name='Igor', group='g002')
    s5=Student.objects.create(name='Zahar', group='g002')
    k1=Course.objects.create(title='Math')
    k2=Course.objects.create(title='Geo')
    k1.student_set.add(s1,s3,s5)
    # k1.student_set.add(s3)
    # k1.student_set.add(s5)
    k2.student_set.add(s1,s2,s3)
    # k2.student_set.add(s2)
    # k2.student_set.add(s3)
    return redirect('index')


def table1(req):
    baza = Product.objects.all()
    anketa = FormJuice()
    print(Company.objects.values_list('title', flat=False))
    bd = []
    if req.POST:      #нажали на кнопку сабмит
        # bd = []
        anketa = FormJuice(req.POST)    #форма с прошлым запросом
        a = req.POST['firma']           #собираем данные
        b = req.POST['sok']
        print(a,b)
        #формируем таблицу
        # baza = Product.objects.filter(firma_id=a, id=b)
        if a and not b:
            baza = Product.objects.filter(firma_id=a)
        elif b and not a:
            c=Product.objects.get(id=b).name
            baza = Product.objects.filter(name=c)
        elif a and b:
            c=Product.objects.get(id=b).name
            baza = Product.objects.filter(firma_id=a, name=c)
        else:
            baza=Product.objects.all()
#заполняются данные


    for i in baza:
        is_recommended = "✔" if i.is_recommended else "✘"
        bd.append((i.name, i.price, i.firma.title, i.volume, i.packaging, is_recommended))
    title = ('Название', 'Цена', 'Фирма','Объем в литрах','Упаковка','Рекомендация')
    # if req.POST:
    #     # bd = []
    #     a= req.POST['firma']
    #     baza = Product.objects.filter(firma_id=a)
    #     for i in baza:
    #         bd.append((i.name, i.price, i.firma.title, i.volume, i.packaging))

    data = {'table': bd, 'title': title, 'forma': anketa}
    return render(req, 'totable.html', context=data)

def table2(req):
    baza = Student.objects.all()
    anketa = FormStud()
    bd=[]
    if req.POST:  # нажали на кнопку сабмит
        # bd = []
        anketa = FormStud(req.POST)  # форма с прошлым запросом
        a = req.POST['kurs']  # собираем данные
        b = req.POST['nik']
        print(a, b,'#####################')
        # формируем таблицу
        # baza = Product.objects.filter(firma_id=a, id=b)
        if a and not b:
            baza = Student.objects.filter(course=a)
        elif b and not a:
            c = Student.objects.get(id=b).name
            baza = Student.objects.filter(name=c)
        elif a and b:
            c = Student.objects.get(id=b).name
            baza = Student.objects.filter(course=a, name=c)
        else:
            baza = Student.objects.all()
    for i in baza:
        temp = i.course.all()
        i.course.all()
        kursi=''
        for t in temp:
            kursi+=t.title+' '
        bd.append([i.name,i.group,kursi])
    title = ('Имя', 'Группа', 'Курсы')
    data = {'table': bd, 'title': title, 'forma': anketa}
    return render(req, 'totable.html', context=data)