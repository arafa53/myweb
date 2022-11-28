from django.shortcuts import redirect, render
from .models import Main_Category, Product,Sub_Category,Orders,OrderItem
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.

def contact(request):
    
    return render (request,"shop/contact.html")


def catview(request):
    allproduct=Product.objects.all() ###filter(publish)which product you want to display in homepage
    main_category=Main_Category.objects.all().order_by('-id')
    categoryID = request.GET.get('main_category')
    if categoryID:
        allproduct=Product.objects.filter(sub_category=categoryID)
    else:
        allproduct=Product.objects.all().order_by('-id')

    paginator=Paginator(allproduct,10)
    page_number=request.GET.get('page')
    pagedata=paginator.get_page(page_number)
    totalpage=pagedata.paginator.num_pages
    print(allproduct)
    context= {'allproduct':allproduct,
              'main_category':main_category,
              'allproduct':pagedata,
              'totalpagelist':[n+1 for n in range(totalpage)]
              
    }

    return render (request,"shop/catview.html",context)









def index(request):
    allproduct=Product.objects.all() ###filter(publish)which product you want to display in homepage
    main_category=Main_Category.objects.all().order_by('-id')
    categoryID = request.GET.get('main_category')
    if categoryID:
        allproduct=Product.objects.filter(sub_category=categoryID)
    else:
        allproduct=Product.objects.all().order_by('-id')

    paginator=Paginator(allproduct,5)
    page_number=request.GET.get('page')
    pagedata=paginator.get_page(page_number)
    totalpage=pagedata.paginator.num_pages
    print(allproduct)
    context= {'allproduct':allproduct,
              'main_category':main_category,
              'allproduct':pagedata,
              'totalpagelist':[n+1 for n in range(totalpage)]
              
    }


   
    return render (request,"shop/index.html",context)

def productView(request,slug):
    allproduct=Product.objects.filter(slug=slug).first()

    context={'allproduct':allproduct}  
    return render (request,"shop/productview.html",context)

def service(request):
    return render (request,"shop/service.html")



    





def search(request):
    Query=request.GET.get('query')
    print(Query)
    product=Product.objects.filter(name__icontains=Query)
    context={
       "product":product
    }

    return render (request,"shop/search.html",context)

def cheackout(request):
    if  request.method == 'POST':
        uid=request.session.get('_auth_user_id')
        user=User.objects.get(id=uid)
        cart=request.session.get('cart')
        print(cart)
        name=request.POST.get('name')
        email=request.POST.get('email')
        address=request.POST.get('address')
        phone=request.POST.get('phone')
        city=request.POST.get('city')
        state=request.POST.get('state')
        zip_code=request.POST.get('zip_code')
        Order_id=request.POST.get('Order_id')
        
        
        order=Orders(name=name,email=email,address=address,phone=phone,city=city,state=state,zip_code=zip_code,Order_id=Order_id,user=user)
        order.save()


        for i in cart:
            a=(int(cart[i]['price']))
            b=cart[i]['quantity']
            total=a*b+60


            Item=OrderItem(
                user=user,
                order=order,
                product=cart[i]['name'],
                image=cart[i]['image'],
                quantity=cart[i]['quantity'],
                price=cart[i]['price'],
                total=total
            )
            Item.save()
        return redirect('thanks')
    
    return render (request,"shop/cheackout.html")
            

def My_account(request):
    return render(request,"account/my_account.html")

    

def REGISTER(request):
    if  request.method == 'POST':
        username=request.POST['username']
        email=request.POST['email']
        first_name=request.POST['first_name']
        password1=request.POST['password1']
        password2=request.POST['password2']
        print(username,email,first_name,password1,password2)
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username taken")
                return redirect('my_account')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email taken")
                return redirect('my_account')
            else:
                user=User.objects.create_user( username=username, email=email,first_name=first_name, password=password1,)
                user.save()
                messages.info(request,"User created")
                return redirect('my_account')
           
        else:
            messages.info(request,"Password not match")
            return redirect('my_account')
            
    else:
        return render(request,'my_account.html')

def login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect("/shop")
        else:
            messages.info(request,'invalid crdential')
            return redirect('my_account')



    else:
        return render(request,'my_account.html')

def logout(request):
    auth.logout(request)
    return redirect("/shop")


def thanks(request):
    
    return render(request,'shop/thanks.html')

def your_order(request):

    uid=request.session.get('_auth_user_id')
    user=User.objects.get(id=uid)
    order=OrderItem.objects.filter(user=user)
    print(order)
    context={
        "order":order
    }
    
    return render(request,'shop/your_order.html',context)


@login_required(login_url="/users/login")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("/shop")


@login_required(login_url="/users/login")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def cart_detail(request):
    return render(request, 'cart/cart_detail.html')