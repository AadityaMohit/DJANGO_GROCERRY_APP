from sqlite3 import IntegrityError
import re 
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseBadRequest
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from .models import Cart, Product, Order
from django.core.mail import send_mail
import random
from django.urls import reverse
from django.core.exceptions import ValidationError
from .models import Message

def home(request):
    return render(request, "home.html")

def seller(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        product_name = request.POST.get('product_name')
        price = request.POST.get('price')
        description = request.POST.get('description')
        email = request.POST.get('email')
        image = request.FILES.get('image')
        if image:
            try:
                product = Product.objects.create(
                    username=username,
                    product_name=product_name,
                    price=price,
                    description=description,
                    image=image,
                    email=email
                )
                send_mail(
                    f"New Order: {username}",
                    f"Your order has been confirmed and will be delivered to you between 4-5 business days.\n\n"
                    f"Your order details:\nProduct: {product_name}\nPrice: {price}\nEmail: {email}",
                    "aadityamohit0308@gmail.com",
                    [request.user.email],
                    fail_silently=False,
                )
                messages.success(request, 'Product added successfully!')
                return redirect(reverse('sform') + f'?product_name={product_name}&price={price}&description={description}&image_url={product.image.url}')
            except Exception as e:
                messages.error(request, f'Error: {e}')
        else:
            messages.error(request, 'Please upload an image.')

    return render(request, 'seller.html')

def sform(request):
    product_name = request.session.get('product_name')
    price = request.session.get('price')
    description = request.session.get('description')
    image_url = request.session.get('image_url')
    return render(request, 'sform.html', {'product_name': product_name, 'price': price, 'description': description, 'image_url': image_url})

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST['email']
        message = request.POST['message']

        # Save the data to the database
        new_message = Message(name=name, email=email, message=message)
        new_message.save()

        print('The data has been written to the db')
        print(name, email, message)

        return HttpResponse("Your message has been sent successfully!")

    return render(request, "contact.html")
def about(request):
    return render(request, "about.html")

def fruit(request):
    return render(request, "fruit.html")

def veggie(request):
    return render(request, "veggie.html")

def milk(request):
    return render(request, "milk.html")

def usersignup(request):
    return render(request, "usersignup.html")

def oil(request):
    return render(request, "oil.html")

def spice(request):
    return render(request, "spice.html")

def dal(request):
    return render(request, "dal.html")

def snacks(request):
    return render(request, "snacks.html")

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        fname = request.POST['fname']
        lname = request.POST['lname']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if len(username) < 10:
            return HttpResponseBadRequest("Your username must be at least 10 characters long.")

        if not username.isalnum():
            return HttpResponseBadRequest("Username should only contain letters and numbers")

        if pass1 != pass2:
            return HttpResponseBadRequest("Passwords do not match, make sure to add the same password inside of password and confirm password")

        # Check if password contains at least one special character and one number
        if not re.search(r'[!@#$%^&*()\[\]{};:,.<>?\/\|\\\-_=+~]', pass1) or not re.search(r'\d', pass1):
            return HttpResponseBadRequest("Password should contain at least one special character and one number")

        if User.objects.filter(username=username).exists():
            return HttpResponse("Username already exists")
            print("Username already exists")
            return redirect('home')

        try:
            myuser = User.objects.create_user(username, email, pass1)
            myuser.first_name = fname
            myuser.last_name = lname
            myuser.save()
            send_mail(
                "Account Creation Confirmation",
                "Your account has been successfully created. Now make login.",
                "aadityamohit0308@gmail.com",
                [email],
                fail_silently=False,
            )
            print([email])
            messages.success(request, "Your account has been successfully created")
            return redirect('home')
            messages.success(request, "Your account has been successfully created")
            return redirect('home')
        except IntegrityError:
            messages.error(request, "An error occurred while creating your account. Please try again later.")
            return redirect('home')

    return render(request, 'signup.html')
def login(request):
    if request.method == 'POST':
        if 'otp' in request.POST:
            entered_otp = request.POST['otp']
            stored_otp = request.session.get('otp')
            if stored_otp == entered_otp:
                user_id = request.session.get('user_id')
                user = User.objects.get(id=user_id)
                auth_login(request, user)
                del request.session['otp']
                del request.session['user_id']
                return redirect('home')
            else:
                return HttpResponse("Invalid OTP. Please try again.")
        else:
            loginusername = request.POST['loginusername']
            loginpassword = request.POST['loginpass']

            user = authenticate(request, username=loginusername, password=loginpassword)
            if user is not None:
                otp = ''.join([str(random.randint(0, 9)) for _ in range(6)])
                request.session['otp'] = otp
                request.session['user_id'] = user.id

                send_mail(
                    "Login OTP",
                    f"Your OTP for login is: {otp}",
                    "aadityamohit0308@gmail.com",
                    [user.email],
                    fail_silently=False,
                )
                print({otp})
                return render(request, 'login.html', {'otp_required': True})
            else:
                return HttpResponse("Invalid username or password")

    return render(request, 'login.html', {'otp_required': False})


def logout(request):
    auth_logout(request)
    print('logout')
    return redirect('home')

def sales(request):
    return render(request, "sales.html")

def detergent(request):
    return render(request, "detergent.html")

def thank(request):
    return render(request, "thank.html")

def addtocart(request):
    if request.method == 'POST':
        # Retrieve data from the POST request
        username = request.POST.get('username')
        name = request.POST.get('name')
        price = request.POST.get('price')
        
        # Create a new Cart object with the retrieved data
        Cart.objects.create(username=username, name=name, price=price)
        
        # Store product name and price in session
        request.session['product_name'] = name
        request.session['price'] = price
        
        # You can choose to display a message indicating the item was added to the cart
        
        # Retrieve and display the cart items
        cart_items = Cart.objects.filter(username=request.user.username)
        return render(request, 'addtocart.html', {'cart_items': cart_items})

    # If it's not a POST request, retrieve and display the cart items
    cart_items = Cart.objects.filter(username=request.user.username)
    return render(request, 'addtocart.html', {'cart_items': cart_items})

def ordernow(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        productname = request.POST.get('productname', '')
        address = request.POST.get('address', '')
        phone = request.POST.get('phone', '')
        email = request.POST.get('email', '')
        state = request.POST.get('state', '')
        city = request.POST.get('city', '')
        price = request.POST.get('price', '')
        landmark = request.POST.get('landmark', '')
        if len(phone) != 10:
            return HttpResponse("Phone number must be 10 digits long.", status=400)
        # if len(address) >= 5:
        #     return HttpResponse("Adress must be 10 digits long.", status=400)
        # if len(state) != 5:
        #     return HttpResponse("State  must be gretae digits long.", status=400)
        # if len(city) >= 4:
        #     return HttpResponse("city number must be 10 digits long.", status=400)

        order = Order.objects.create(
            username=username,
            email=email,
            address=address,
            state=state,
            city=city,
            landmark=landmark,
            phone=phone,
            productname=productname,
            price=price
        )
        send_mail(
            f"New Order: {username}",
            f"Your order has been confirmed and will be delivered to you between 4-5 business days.\n\n"
            f"Your order details:\nProduct: {productname}\nPrice: {price}\nEmail: {email}",
            "aadityamohit0308@gmail.com",
            [request.user.email],
            fail_silently=False,
        )

        return redirect('thank')

    product_name = request.session.get('product_name')
    price = request.session.get('price', 0)

    context = {
        'product_name': product_name,
        'price': price,
    }
    return render(request, 'ordernow.html', context)

def delete_cart_item(request, cart_item_id):
    cart_item = get_object_or_404(Cart, id=cart_item_id)
    cart_item.delete()
    return redirect('addtocart')

def cashondelivery(request):
    if request.method == "POST":
        username = request.POST.get('username')
        name = request.POST.get('name')
        price = request.POST.get('price')
        cart = Cart.objects.create(
            username=username,
            name=name,
            price=price,
        )
        request.session['price'] = price
        request.session['name'] = name
        return render(request, 'addtocart.html')
    else:
        name = request.GET.get('name')
        price = request.GET.get('price')
        request.session['price'] = price
        request.session['name'] = name
        return render(request, 'cashondelivery.html', {'name': name, 'price': price})

def cashpay(request):
    if request.method == "POST":
        username = request.POST.get('username')
        productname = request.POST.get('productname')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        state = request.POST.get('state')
        city = request.POST.get('city')
        price = request.POST.get('price')
        landmark = request.POST.get('landmark')
        otp = ''.join([str(random.randint(0, 9)) for _ in range(6)])

        order = Order.objects.create(
            username=username,
            productname=productname,
            address=address,
            phone=phone,
            email=email,
            state=state,
            city=city,
            price=price,
            landmark=landmark
        )

        send_mail(
            f"New Order: {username}",
            f"Your order has been confirmed and will be delivered to you between 4-5 business days.\n\n"
            f"Your order details:\nProduct: {productname}\nPrice: {price}\nEmail: {email}",
            "aadityamohit0308@gmail.com",
            [request.user.email],
            fail_silently=False,
        )

        request.session['price'] = price
        request.session['name'] = productname

        print("Price set in session:", price)

        return redirect('thank')

    price = request.session.get('price')
    name = request.session.get('name')
    user_email = request.session.get('user_email')
    print("Price retrieved from session:", price)

    return render(request, 'cashpay.html', {'name': name, 'price': price, 'user_email': user_email})
