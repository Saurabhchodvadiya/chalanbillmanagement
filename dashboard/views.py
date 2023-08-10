# from django.shortcuts import render
from django.shortcuts import render
from dashboard.models import Otherproducts, Surfaceproducts,Throughproducts,ChalanTable,User,Product
from .forms import surface_form
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.paginator import Paginator
# Create your views here.
from django.http import HttpResponse, JsonResponse
from .models import Surfaceproducts
from django.db.models import Q
import os
cwd=os.getcwd()
print(cwd)
def home_page(request):

    return render(request,'pages/home.html')

#  id = models.AutoField(db_column='ID', primary_key=True, blank=True, null=True)  # Field name made lowercase.
#     mrfppartno = models.TextField(db_column='MrfpPartNo', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     datasheet = models.TextField(blank=True, null=True)  # This field type is a guess.
#     ref = models.TextField(db_column='REF', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     mounting = models.TextField(db_column='Mounting', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     value = models.TextField(db_column='VALUE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     ht = models.TextField(db_column='HT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     dia = models.TextField(db_column='Dia', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     spring_dia = models.TextField(db_column='Spring_Dia', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     material = models.TextField(db_column='Material', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     pitch = models.TextField(db_column='Pitch', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     three_d_drawing = models.TextField(db_column='Three_d_drawing', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     size_of_component = models.TextField(db_column='Size_of_component', blank=True, null=True)  #
# print(Otherproducts.objects.filter(mrfppartno='ERM8-025-01-L-D-EM2-DS-TR'))
def surfaceProduct(request):
    Datao_obj=Product.objects.all()
    # page = request.GET.get('page', 1)
    # # paginator = Paginator(Datao_obj, 25) 
    # # page_number = request.GET.get('page')
    # # page_obj = paginator.get_page(page_number)
    # # print(page_obj)
    # # print(len(paginator.__dict__["object_list"]))
    # data=[]
    # paginator = Paginator(Datao_obj, 25)
    # try:
    #     page_obj = paginator.page(page)
    # except PageNotAnInteger:
    #     page_obj = paginator.page(1)
    # except EmptyPage:
    #     page_obj = paginator.page(paginator.num_pages)
 
    return render(request,'pages/surface.html')



def edit_surface_data(request):
    form = surface_form()
    id=request.GET.get("id")
    find_data=Product.objects.get(id=id)
   
    return render(request, "pages/edit_surface.html", {"find_data": find_data})


def update_surface(request):
    id=request.GET.get("id")

    name=request.GET.get("name")
    price=request.GET.get("price")
  
    data={'added':False}
    
    find_data=Product.objects.filter(id=id)
   
    if find_data.exists():
        add_industry_objet = find_data.update(
            name=name,
            price=price,
           
        )
        data["added"] = True
    return JsonResponse(data)


def update_surface(request):
    id=request.GET.get("id")

    name=request.GET.get("name")
    price=request.GET.get("price")
  
    data={'added':False}
    
    find_data=ChalanTable.objects.filter(id=id)
   
    if find_data.exists():
        add_industry_objet = find_data.update(
            name=name,
            price=price,
           
        )
        data["added"] = True
    return JsonResponse(data)


def get_surface_unique_data(request):
    id=request.GET.get("id")
    get_data=Surfaceproducts.objects.filter(id=id).first()

    data={'ht':get_data.ht,'manufacture':get_data.mrfppartno,'mounting':get_data.mounting,'dia':get_data.dia,'spring_dia':get_data.spring_dia,'material':get_data.material,'pitch':get_data.pitch,'value':get_data.value,"Datasheet":get_data.datasheet,"Ref":get_data.ref}
    return JsonResponse(data)







# -----------------------------------------------------------------------------------

def throughproducts(request):
    # Datao_obj=Throughproducts.objects.all()
    # page = request.GET.get('page', 1)
    # # paginator = Paginator(Datao_obj, 25) 
    # # page_number = request.GET.get('page')
    # # page_obj = paginator.get_page(page_number)
    # # print(page_obj)
    # # print(len(paginator.__dict__["object_list"]))
    # data=[]
    # paginator = Paginator(Datao_obj, 25)
    # try:
    #     page_obj = paginator.page(page)
    # except PageNotAnInteger:
    #     page_obj = paginator.page(1)
    # except EmptyPage:
    #     page_obj = paginator.page(paginator.num_pages)
    # print(len(data))
    return render(request,'pages/throughproducts.html')

def edit_through_data(request):
    form = surface_form()
    
    id=request.GET.get("id")
    find_data=User.objects.get(id=id)
    return render(request, "pages/edit_through.html", {"find_data": find_data})



def add_data(request):
    form = surface_form()
    
    id=request.GET.get("id")
    find_data=Product.objects.all()
    return render(request, "pages/add_data.html",{"find_data": find_data})

def update_through(request):
    id=request.GET.get("id")

    name=request.GET.get("name")
    company_name=request.GET.get("company_name")
    phone_number=request.GET.get("phone_number")
 
    phone1=request.GET.get("phone1")
  
    data={'added':False}
    
    find_data=User.objects.filter(id=id)
   
    if find_data.exists():
        add_industry_objet = find_data.update(
            name=name,
            company_name=company_name,
            phone_number=phone_number,
            phone1=phone1
        )
        data["added"] = True
    return JsonResponse(data)

def get_through_unique_data(request):
    id=request.GET.get("id")
    get_data=Throughproducts.objects.filter(id=id).first()

    data={'ht':get_data.ht,'manufacture':get_data.mrfppartno,'mounting':get_data.mounting,'dia':get_data.dia,'spring_dia':get_data.spring_dia,'material':get_data.material,'pitch':get_data.pitch,'value':get_data.value,"Datasheet":get_data.datasheet,"Ref":get_data.ref}
    return JsonResponse(data)




# -----------------------------------------------------------------------------------

def otherproducts(request):
    # Datao_obj=Product.objects.all()
    # page = request.GET.get('page', 1)
    # # paginator = Paginator(Datao_obj, 25) 
    # # page_number = request.GET.get('page')
    # # page_obj = paginator.get_page(page_number)
    # # print(page_obj)
    # # print(len(paginator.__dict__["object_list"]))
    # data=[]
    # paginator = Paginator(Datao_obj, 25)
    # try:
    #     page_obj = paginator.page(page)
    # except PageNotAnInteger:
    #     page_obj = paginator.page(1)
    # except EmptyPage:
    #     page_obj = paginator.page(paginator.num_pages)
    # print(len(data))
    return render(request,'pages/other.html')

def edit_other_data(request):
    print("ffffffffdsssssssssssssssssssssssssssssssssssssssssssssssssss")
    id=request.GET.get("id")
    find_datas=Product.objects.all()
    find_data=ChalanTable.objects.filter(id=id).values_list()
    print(find_data[0][8])

    return render(request, "pages/edit_other.html",{'name':find_data[0][1],'user_id':find_data[0][2],'date':find_data[0][8],"find_data":find_datas})


def update_other(request):
    id=request.GET.get("id")

    name=request.GET.get("name")
    company_name=request.GET.get("company_name")
    phone_number=request.GET.get("phone_number")
 
    phone1=request.GET.get("phone1")
  
    data={'added':False}
    
    find_data=User.objects.filter(id=id)
   
    if find_data.exists():
        add_industry_objet = find_data.update(
            name=name,
            company_name=company_name,
            phone_number=phone_number,
            phone1=phone1
        )
        data["added"] = True
    return JsonResponse(data)

import json
def add_menu_data(request):
    try:
        if request.method == "POST":
            is_private = False
            print(request.POST.get('data'),"Fffffffffffffffffffffffffffffffffffffffffff")
            # print(json.dumps(request.POST.get('data')),"Fffffffffffffffffffffffffffffffffffffffffff")
            data = request.POST.get('data')
            chalanno = request.POST.get('chalanno')
            user_id = request.POST.get('user_id')
            date = request.POST.get('date')  
            print(date,"Ddddddddddddddddddddddddddddddddddddd")
            url=None
            merged_products = []
            merged_prices = []
            merged_qty = []
            merged_rate = []
            merged_amount = []
            data = json.loads(data)
            for inner_dict in data.values():
                print(inner_dict)
                merged_products.append(inner_dict["products"])
                merged_prices.append(inner_dict["prices"])
                merged_qty.append(inner_dict["qty"])
                merged_rate.append(inner_dict["rate"])
                merged_amount.append(inner_dict["amount"])
            merged_data = {
                "products": ",".join(merged_products),
                "prices": ",".join(merged_prices),
                "qty": ",".join(merged_qty),
                "rate": ",".join(merged_rate),
                "amount": ",".join(merged_amount)
            }

            merged_json = json.dumps(merged_data, indent=4)
            print(merged_json)
            try:
                file=request.FILES['file']
                
                if file:
                    
                    
                    if "pdf" not  in file.name:
                        
                        data["flag"] =False
                        data["msg"]="Only Pdf formate is allowed"
                        return JsonResponse(data)
                    with open('media/'+file.name, 'wb+') as destination:  
                        for chunk in file.chunks():  
                            destination.write(chunk)
                    url= '/media/'+file.name
            except:
                pass 
            
            Pitch = request.POST.get('Pitch')
            Material = request.POST.get('Material')
            data={'added':False}
            data["flag"] =True
        
                

            
            
            
            find_data=User.objects.filter(id=user_id)
            if not find_data.exists():
                data["flag"] =False
                data["msg"]="વપરાશકર્તા ID(user_id) ઉપલબ્ધ નથી પહેલા વપરાશકર્તાની નોંધણી કરો"
                return JsonResponse(data)
            else  :


                add_industry_objet = ChalanTable(
                    chalanno=chalanno,
                    user_id=user_id,
                    products=merged_data['products'],
                    prices=merged_data['prices'],
                    qty=merged_data['qty'],
                    rate=merged_data['rate'],
                    amount=merged_data['amount'],
                    date=date,
                    url=url
                    
                )
                add_industry_objet.save()
                data["flag"] =True
                data["msg"]="Data Added Successfully"
                

                print(data)
            
                return JsonResponse(data)
            
        else:
            data["flag"] = False
            return JsonResponse(data)
    except Exception as e:
        print(str(e))
        return HttpResponse(str(e))
    
def edit_menu_data(request):
    try:
        if request.method == "POST":
            is_private = False
            print(request.POST.get('data'),"Fffffffffffffffffffffffffffffffffffffffffff")
            # print(json.dumps(request.POST.get('data')),"Fffffffffffffffffffffffffffffffffffffffffff")
            id=request.POST.get('id')
            data = request.POST.get('data')
            chalanno = request.POST.get('chalanno')
            user_id = request.POST.get('user_id')
            date = request.POST.get('date')  
            print(date,"Ddddddddddddddddddddddddddddddddddddd")
            url=None
            merged_products = []
            merged_prices = []
            merged_qty = []
            merged_rate = []
            merged_amount = []
            data = json.loads(data)
            for inner_dict in data.values():
                print(inner_dict)
                merged_products.append(inner_dict["products"])
                merged_prices.append(inner_dict["prices"])
                merged_qty.append(inner_dict["qty"])
                merged_rate.append(inner_dict["rate"])
                merged_amount.append(inner_dict["amount"])
            merged_data = {
                "products": ",".join(merged_products),
                "prices": ",".join(merged_prices),
                "qty": ",".join(merged_qty),
                "rate": ",".join(merged_rate),
                "amount": ",".join(merged_amount)
            }

            merged_json = json.dumps(merged_data, indent=4)
            print(merged_json)
            try:
                file=request.FILES['file']
                
                if file:
                    
                    
                    if "pdf" not  in file.name:
                        
                        data["flag"] =False
                        data["msg"]="Only Pdf formate is allowed"
                        return JsonResponse(data)
                    with open('media/'+file.name, 'wb+') as destination:  
                        for chunk in file.chunks():  
                            destination.write(chunk)
                    url= '/media/'+file.name
            except:
                pass 
            
            Pitch = request.POST.get('Pitch')
            Material = request.POST.get('Material')
            data={'added':False}
            data["flag"] =True
        
                

            
            user_date=ChalanTable.objects.filter(id=id)
            
            find_data=User.objects.filter(id=user_id)
            if  find_data.exists():
                


                add_industry_objet = user_date.update(
                    chalanno=chalanno,
                    user_id=user_id,
                    products=merged_data['products'],
                    prices=merged_data['prices'],
                    qty=merged_data['qty'],
                    rate=merged_data['rate'],
                    amount=merged_data['amount'],
                    date=date,
                    url=url
                    
                )

                data["flag"] =True
                data["msg"]="Data updated Successfully"
                

                print(data)
            
                return JsonResponse(data)
            else:
                data["flag"] =False
                data["msg"]="વપરાશકર્તા ID(user_id) ઉપલબ્ધ નથી પહેલા વપરાશકર્તાની નોંધણી કરો"
                return JsonResponse(data)
            
            
        else:
            data["flag"] = False
            return JsonResponse(data)
    except Exception as e:
        print(str(e))
        return HttpResponse(str(e))
def add_product(request):
    try:
        if request.method == "POST":
            is_private = False
            print("Fffffffffffffffffffffffffffffffffffffffffff")
            # print(json.dumps(request.POST.get('data')),"Fffffffffffffffffffffffffffffffffffffffffff")
            name = request.POST.get('name')
            price = request.POST.get('price')
            
            data={'added':False}
            data["flag"] =True
        
                

            
            
            
            # find_data=User.objects.filter(id=user_id)
            # if not find_data.exists():
            #     data["flag"] =False
            #     data["msg"]="વપરાશકર્તા ID(user_id) ઉપલબ્ધ નથી પહેલા વપરાશકર્તાની નોંધણી કરો"
            #     return JsonResponse(data)
            # if   find_data.exists():


        add_industry_objet = Product(
            name=name,
            price=price,
            
            
        )
        add_industry_objet.save()
        data["flag"] =True
        data["msg"]="Data Added Successfully"
        

        print(data)
    
        return JsonResponse(data)
    
            # data["added"] = True
        return JsonResponse(data)
    except Exception as e:
        print(str(e))



def add_user(request):
    try:
        if request.method == "POST":
            is_private = False
            
            # print(json.dumps(request.POST.get('data')),"Fffffffffffffffffffffffffffffffffffffffffff")
            name = request.POST.get('name')
            company_name = request.POST.get('company_name')
            phone_number = request.POST.get('phone_number')
            phone1 = request.POST.get('phone1')
            data={'added':False}
            data["flag"] =True


        add_industry_objet = User(
            name=name,
            company_name=company_name,
             phone_number=phone_number,
              phone1=phone1,
               
            
        )
        add_industry_objet.save()
        data["flag"] =True
        data["msg"]="Data Added Successfully"
        

        print(data)
    
    
        return JsonResponse(data)
    
            # data["added"] = True
        return JsonResponse(data)
    except Exception as e:
        print(str(e))

def get_other_unique_data(request):
    id=request.GET.get("id")
    get_data=Otherproducts.objects.filter(id=id).first()

    data={'ht':get_data.ht,'manufacture':get_data.mrfppartno,'mounting':get_data.mounting,'dia':get_data.dia,'spring_dia':get_data.spring_dia,'material':get_data.material,'pitch':get_data.pitch,'value':get_data.value,"Datasheet":get_data.datasheet,"Ref":get_data.ref}
    return JsonResponse(data)

# def find_record(request):
#     return render(request,'pages/search.html')
def get_price(request):
    print("Ddddddds            c222222222222      ccaaaaaaaaaaaaaaaaaaaaaaaacs")
    id=request.GET.get("product")
    get_data=Product.objects.filter(name=id).first()

    data={'name':get_data.price}
    return JsonResponse(data)

def find_record(request):
    print(request.GET.get('idDropdown'),"ffffffffxxxxxxxxxxxxxwqfffffffffffffffffffffffffffff")
    type =request.GET.get('Type')
    data=Product.objects.all()
    if str(type) =="0":
         objects=   Product.objects.filter(id=request.GET.get('idDropdown'))
    elif str(type)=="1":
        objects=   User.objects.filter(id=request.GET.get('id'))
    else:

        objects=   ChalanTable.objects.filter(chalanno=request.GET.get('id'))
    # Manufacturer = request.GET.get('Manufacturer')
    # Mounting = request.GET.get('Mounting')
    # productvalue = request.GET.get('productvalue')
    # ht = request.GET.get('HT')      
    # Dia = request.GET.get('Dia')
    # Spring = request.GET.get('Spring')
    # Spring = request.GET.get('Spring')
    # Pitch = request.GET.get('Pitch')
    # Material = request.GET.get('Material')
    # print(Manufacturer,Mounting,productvalue,ht,Dia,Spring)

    # query = Q()
    # if Manufacturer:
    #     query &= Q(mrfppartno__icontains =Manufacturer)
    # # if Mounting:
    # #     query &= Q(mrfppartno__icontains =Mounting)
    # if productvalue:
    #     query &= Q(value__icontains =productvalue)
    # if ht:
    #     query &= Q(ht__icontains =ht)
    # if Dia:
    #     query &= Q(dia__icontains =Dia)
    # if Spring:
    #     query &= Q(spring_dia__icontains =Spring)
    # if Material:
    #     query &= Q(material__icontains =Material)
    # if Pitch:
    #     query &= Q(pitch__icontains =Pitch)
    # product_type=2
    # # objects=Otherproducts.objects.filter(query).values('id','mrfppartno','datasheet','ref','mounting' ,'value','ht','dia','spring_dia' ,'material','pitch','three_d_drawing' ,'size_of_component')
    # if Mounting=="0" or Mounting==None:
    #     product_type="0"
    #     objects=Surfaceproducts.objects.filter(query).values('id','mrfppartno','datasheet','ref','mounting' ,'value','ht','dia','spring_dia' ,'material','pitch','three_d_drawing' ,'size_of_component')
    # elif Mounting=="1":
    #     product_type="1"
    #     objects=Throughproducts.objects.filter(query).values('id','mrfppartno','datasheet','ref','mounting' ,'value','ht','dia','spring_dia' ,'material','pitch','three_d_drawing' ,'size_of_component')
    # elif Mounting=="2":
    #     product_type="2"
    #     objects=Otherproducts.objects.filter(query).values('id','mrfppartno','datasheet','ref','mounting' ,'value','ht','dia','spring_dia' ,'material','pitch','three_d_drawing' ,'size_of_component')
   
    paginator = Paginator(objects, 25)
    page = request.GET.get('page', 1)
    print(page,'dddddddddddddaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    url="/find_record/?"
    if str(type) =="0":

        url+="id="+request.GET.get('id')

    
        url+="&Type="+type
   
    # ,{'page_obj':page_obj,'url':url,'type':product_type}
    print(page_obj)
    return  render(request,'pages/search.html',{'page_obj':page_obj,'url':url,'type':type,"data":data})


def find_records_for_user(request):
    print("jjjjjjjiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii")
    print(request.GET,"ffffffffxxxxxxxxxxxxxwqfffffffffffffffffffffffffffff")
   
    type =request.GET.get('type')

    data=Product.objects.all()
    if request.GET.get('id')!='' and  request.GET.get('starting_date')!="" and  request.GET.get('ending_date')!=None:
        objects=   ChalanTable.objects.filter(user_id=str(request.GET.get('id')),date__gte=request.GET.get('starting_date'),date__lte=request.GET.get('ending_date'))
    
    # Manufacturer = request.GET.get('Manufacturer')
    # Mounting = request.GET.get('Mounting')
    # productvalue = request.GET.get('productvalue')
    # ht = request.GET.get('HT')      
    # Dia = request.GET.get('Dia')
    # Spring = request.GET.get('Spring')
    # Spring = request.GET.get('Spring')
    # Pitch = request.GET.get('Pitch')
    # Material = request.GET.get('Material')
    # print(Manufacturer,Mounting,productvalue,ht,Dia,Spring)

    # query = Q()
    # if Manufacturer:
    #     query &= Q(mrfppartno__icontains =Manufacturer)
    # # if Mounting:
    # #     query &= Q(mrfppartno__icontains =Mounting)
    # if productvalue:
    #     query &= Q(value__icontains =productvalue)
    # if ht:
    #     query &= Q(ht__icontains =ht)
    # if Dia:
    #     query &= Q(dia__icontains =Dia)
    # if Spring:
    #     query &= Q(spring_dia__icontains =Spring)
    # if Material:
    #     query &= Q(material__icontains =Material)
    # if Pitch:
    #     query &= Q(pitch__icontains =Pitch)
    # product_type=2
    # # objects=Otherproducts.objects.filter(query).values('id','mrfppartno','datasheet','ref','mounting' ,'value','ht','dia','spring_dia' ,'material','pitch','three_d_drawing' ,'size_of_component')
    # if Mounting=="0" or Mounting==None:
    #     product_type="0"
    #     objects=Surfaceproducts.objects.filter(query).values('id','mrfppartno','datasheet','ref','mounting' ,'value','ht','dia','spring_dia' ,'material','pitch','three_d_drawing' ,'size_of_component')
    # elif Mounting=="1":
    #     product_type="1"
    #     objects=Throughproducts.objects.filter(query).values('id','mrfppartno','datasheet','ref','mounting' ,'value','ht','dia','spring_dia' ,'material','pitch','three_d_drawing' ,'size_of_component')
    # elif Mounting=="2":
    #     product_type="2"
    #     objects=Otherproducts.objects.filter(query).values('id','mrfppartno','datasheet','ref','mounting' ,'value','ht','dia','spring_dia' ,'material','pitch','three_d_drawing' ,'size_of_component')
        print(objects.all(),"44444444444444444444444444444444444444444444444444444444444444444444444444")
        # paginator = Paginator(objects, 25)
        # page = request.GET.get('page', 1)
        # try:
        #     page_obj = paginator.page(page)
        # except PageNotAnInteger:
        #     page_obj = paginator.page(1)
        # except EmptyPage:
        #     page_obj = paginator.page(paginator.num_pages)
        url="/find_records_for_user/?"
        if str(type) =="0":

            url+="id="+request.GET.get('id')
            url+="&starting_date="+request.GET.get('starting_date')
        
            url+="&ending_date="+request.GET.get('ending_date')
    
        # ,{'page_obj':page_obj,'url':url,'type':product_type}
        return  render(request,'pages/other.html',{'page_obj':objects.all(),'url':url,'type':'2',"data":data})
    return  render(request,'pages/other.html',{'type':'2',"data":data})
# from openpyxl import Workbook
import csv
def download_excel(request):
    # Fetch data from the model

    data=   ChalanTable.objects.filter(chalanno=request.GET.get('id')).all()
    count_item=len(str(data[0].amount).split(','))
    
    l=["id","chalanno","user_id","products","prices","qty","rate","meter","date","totalqty","totalrate","totalmeter"]
   
    print(l[0:9])
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="data.csv"'
    writer = csv.writer(response)
    
    # Write headers
    writer.writerow(l)
    for item in data:
        row = []
        for field_name in l[0:9]:
            row.append(getattr(item, field_name, ""))
        row[7]=item.amount
        # Perform operation on age and add result as new column
        totalqty = getattr(item, "qty", 0)  # Default to 0 if age is missing
        totalqty = str(totalqty).replace(",","+")   # Example: Adding 5 to the age
        totalqty=eval(str(totalqty))
        row.append(totalqty)
        

        totalqty = getattr(item, "rate", 0)  # Default to 0 if age is missing
        totalqty = str(totalqty).replace(",","+")   # Example: Adding 5 to the age
        rate=eval(str(totalqty))
        row.append(rate)


        totalqty = getattr(item, "amount", 0)  # Default to 0 if age is missing
        print(totalqty)
        totalqty = str(totalqty).replace(",","+")   # Example: Adding 5 to the age
        amount=eval(str(totalqty))
        row.append(amount)


       

        writer.writerow(row)
   
     

    return response 


def download_excels(request):
    # Fetch data from the model
    print("ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc")
    data=  ChalanTable.objects.filter(user_id=str(request.GET.get('id')),date__gte=request.GET.get('starting_date'),date__lte=request.GET.get('ending_date')).all()
    
    
    l=["id","chalanno","user_id","products","prices","qty","rate","meter","date","totalqty","totalrate","totalmeter"]
   
    print(l[0:9],"cddddefwegwefwergewrceqcdeqecq")
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="data.csv"'
    writer = csv.writer(response)
    
    # Write headers
    writer.writerow(l)
    for item in data:
        row = []
        for field_name in l[0:9]:
            row.append(getattr(item, field_name, ""))
        row[7]=item.amount
        # Perform operation on age and add result as new column
        totalqty = getattr(item, "qty", 0) 
        print(totalqty,"dvvvvvvvvvvvvvvsdvssdddddddsvsvsvvvvvvvvv",row)
        if totalqty!=None:
            totalqty="0"
         # Default to 0 if age is missing
        totalqty = str(totalqty).replace(",","+")   # Example: Adding 5 to the age
        
        totalqty=eval(str(totalqty))
        row.append(totalqty)
        

        totalqty = getattr(item, "rate", 0)  # Default to 0 if age is missing
        if totalqty!=None:
            totalqty="0"
        totalqty = str(totalqty).replace(",","+")   # Example: Adding 5 to the age
        rate=eval(str(totalqty))
        row.append(rate)


        totalqty = getattr(item, "amount", 0)  # Default to 0 if age is missing
        if totalqty!=None:
            totalqty="0"
        totalqty = str(totalqty).replace(",","+")   # Example: Adding 5 to the age
        amount=eval(str(totalqty))
        row.append(amount)


        print(row,"nnnnnnnnnnnnnnnnnnnnnnnnnnnnn")

        writer.writerow(row)
   
     
    print("ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff")
    return response 



def delete_user(request):
    # Fetch data from the model
    print("ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc")
    data={'added':False}
    
    if request.GET.get('Type')=="0":
        datas=  Product.objects.filter(id=str(request.GET.get('id')))
    elif  request.GET.get('Type')=="1":
        datas=  User.objects.filter(id=str(request.GET.get('id')))
    else:
        datas=  ChalanTable.objects.filter(id=str(request.GET.get('id')))
    datas.delete()
    print("ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff")
    data["added"] = True
    return  render(request,'pages/search.html',{"data":data})
