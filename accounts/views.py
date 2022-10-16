from multiprocessing import context
from urllib import request
import email
from django.shortcuts import render , redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .models import UserProfile
from products.models import Product 
import re
from django.contrib import auth



def profile(request):
   if request.method == 'POST' and 'btnsave' in request.POST:

      if request.user is not None and request.user.id != None:
         userprofile = UserProfile.objects.get(user=request.user)
         if request.POST['fname'] and request.POST['lname'] and request.POST['address'] and request.POST['city'] and request.POST['gender'] and request.POST['zip'] and request.POST['email'] and request.POST['user'] and request.POST['pass']:
            request.user.first_name = request.POST['fname']
            request.user.last_name = request.POST['lname']
            userprofile.address = request.POST['address']
            userprofile.city = request.POST['city']
            userprofile.gender = request.POST['gender']
            userprofile.zip_numper = request.POST['zip']
            # request.user.email = request.POST['email']
            # request.user.username = request.POST['user']
            if not request.POST['pass'].startswith('pbkdf2_sha256$'):
               request.user.set_password(request.POST['pass'])
            request.user.save()
            userprofile.save()
            auth.login(request, request.user)
            messages.success(request, 'Your data has been saved')
            
         else:
               messages.error(request, 'Check your values and elements')

      return redirect('profile')
            

   
   else:
      # if request.user.is_anonymous: return redirect('profile')
      # if request.user.id == None: return redirect('index')
      if request.user is not None:

         context = None

         if request.user.is_anonymous:
            userprofile = UserProfile.objects.get(user=request.user)

            context = {
               'fname':request.user.first_name,
               'lname':request.user.last_name,
               'address':request.userprofile.address,
               'city':request.userprofile.city,
               'gender':request.userprofile.gender,
               'zip':request.userprofile.zip_numper,
               'email':request.user.email,
               'user':request.user.username,
               'pass':request.user.password,

            }





            return redirect('profile')
         else:
                  return render( request  , 'accounts/profile.html' , context )


def login(request):
   if request.method == 'POST' and 'btnlogin' in request.POST:
      username = request.POST['user']
      password = request.POST['pass']



      user = auth.authenticate(username=username, password=password)


      if user is not None:
         if 'rememberme' not in request.POST:
            request.session.set_expiry(0)
         auth.login(request, user)
         messages.success(request, 'You are now logged in')

      else:
         messages.error(request, 'Username or password invalid')



      return redirect('login')
   else:
      return render( request , 'accounts/login.html' )



def myaccount(request):
   return render( request , 'accounts/my-account.html' )



def logout(request):
      if request.user.is_authenticated:
         auth.logout(request)
      return redirect('index')



def signup(request):
   if request.method == 'POST' and 'btnsignup' in request.POST:

      fname = None
      lname = None
      address = None 
      city = None
      gender = None
      zip_numper = None
      email = None
      username = None
      password = None
      terms = None
      is_added = None


      if 'fname' in request.POST: fname = request.POST['fname']
      else: messages.error(request, 'Error in frist name')

      if 'lname' in request.POST: lname = request.POST['lname']
      else: messages.error(request, 'Error last name')


      if 'address' in request.POST: address = request.POST['address']
      else: messages.error(request, 'Error in address')

      if 'city' in request.POST: city = request.POST['city']
      else: messages.error(request, 'Error in city')

      if 'gender' in request.POST: gender = request.POST['gender']
      else: messages.error(request, 'Error in gender')

      if 'zip' in request.POST: zip_numper = request.POST['zip']
      else: messages.error(request, 'Error in zip')

      if 'email' in request.POST: email = request.POST['email']
      else: messages.error(request, 'Error in email')

      if 'user' in request.POST: username = request.POST['user']
      else: messages.error(request, 'Error in user name')

      if 'pass' in request.POST: password = request.POST['pass']
      else: messages.error(request, 'Error in password')

      if 'terms' in request.POST: terms = request.POST['terms']



      if fname and lname and address and city and gender and zip_numper and email and username and password:
          if terms == 'on':
              if User.objects.filter(username=username).exists():
                messages.error(request, 'This username is teken')
              else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'This email is teken')
                else:
                    patt = "^\w+([-+.']\w+)*@\w+([-.]\w+)*\.\w+([-.]\ww+)*$"
                    if re.match(patt, email):
                        user = User.objects.create_user(first_name=username, last_name=lname, email=email, username=username, password=password)
                        user.save()
                        userprofile = UserProfile(user=user, address=address, city=city, gender=gender, zip_numper=zip_numper)
                        userprofile.save()
                        fname = ''
                        lname = ''
                        address = '' 
                        city = ''
                        gender = ''
                        zip_numper = ''
                        email = ''
                        username = ''
                        password = ''
                        terms = None

                        messages.info(request, 'your account was created')
                        is_added = True 

                    else:
                        messages.error(request, 'Invalid email')



          else:
            messages.error(request, 'You must agree to the terms')
 
      else:
        messages.error(request, 'Check empty fields')






   # else:
   return render( request , 'accounts/signup.html' )






def product_favorite(request, pro_id):
   if request.user.is_authenticated and not request.user.is_anonymous:
      pro_fav = Product.objects.get(pk=pro_id)
      if UserProfile.objects.filter(user=request.user, 
      product_favorites=pro_fav).exists():
        messages.success(request, 'Already product in the favorite list')
      else:
         userprofile = UserProfile.objects.get(user=request.user)
         userprofile.product_favorites.add(pro_fav)
         messages.success(request, 'Product has been favorited')

      
   else:
         messages.error(request, 'you must be  logges in ')
   return redirect('/products/' + str(pro_id))
   




def show_product_favorite(request):
   context = None
   if request.user.is_authenticated and not request.user.is_anonymous:
      userInfo = UserProfile.objects.get(user=request.user)
      pro = userInfo.product_favorites.all()
      context = {'products':pro}
   return render(request, 'products/showfav.html', context)