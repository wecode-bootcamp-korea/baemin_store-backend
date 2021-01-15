import json
import re
import bcrypt
import jwt

from django.http    import JsonResponse
from django.views   import View

from user.models    import User
from user           import utils

from my_settings    import SECRET_KEY, ALGORITHM


class SignUpView(View):
    def post(self, request):
        try:
            data     = json.loads(request.body)
            account  = data['account']
            password = data['password']
            name     = data['name']
            email    = data['email']
            phone    = data['phone']

            if not utils.account_validation(account): 
                return JsonResponse({"MESSAGE":'NOT VALID ACCOUNT'}, status=400)

            utils.password_check(password)

            if not utils.email_validation(email):
                return JsonResponse({"MESSAGE":'NOT VALID EMAIL'}, status=400)

            if not utils.username_validation(name):
                return JsonResponse({"MESSAGE":'NOT VALID NAME'}, status=400)

            if not utils.phone_validation(phone):
                return JsonResponse({"MESSAGE":'NOT VALID PHONE'}, status=400)
            
            if utils.check_duplication(account=account,email=email, phone=phone): 
                return JsonResponse({'MESSAGE': 'INFORMATION REGISTERED ALREADY!'}, status=409)

            hash_pwd = bcrypt.hashpw(password.encode('utf-8'),bcrypt.gensalt()).decode() 

            User.objects.create(
                account =account,
                password=hash_pwd,
                name    =name,
                email   =email,
                phone   =phone

            )
            return JsonResponse({'MESSAGE': 'SUCCESS TO MAKE ACCOUNT'}, status=201)

        except KeyError:
            return JsonResponse({'MESSAGE': 'KEY ERROR FOUND!'}, status=400)
        except ValueError:
            return JsonResponse({'MESSAGE': 'VALUE ERROR FOUND!'}, status=400)

class LoginView(View):
    def post(self, request):
        try:
            data      = json.loads(request.body)
            account   = data['account']
            password  = data['password']

            user           = User.objects.get(account=account)
            password_in_db = user.password


            if bcrypt.checkpw(password.encode('utf-8'), password_in_db.encode('utf-8')):
                payload = {"user_id":user.id}
                login_token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
                return JsonResponse({'MESSAGE':'SUCCESS','TOKEN':login_token}, status=200, safe=True)
            return JsonResponse({'MESSAGE':'INVALID ACCOUNT'}, status= 401)

        except KeyError :
            return JsonResponse({'MESSAGE':'KEY ERROR'}, status=400)
        except ValueError:
            return JsonResponse({'MESSAGE':'VALUE ERROR'},status=400)
        except User.DoesNotExist:
            return JsonResponse({"error": "ACCOUNT NOT EXISTS."}, status=404)

