import jwt
import json
import re

from django.http import JsonResponse
from django.db.models import Q

from user.models import User

from my_settings import ALGORITHM, SECRET_KEY
from decorators  import utils

def check_duplication(account, email,phone):
    return User.objects.filter(Q(account=account) | Q(email=email) | Q(phone=phone)).exists()



def login_required(func):
    def wrapper(self, request, *args, **kwargs):
        try:
            token        = request.headers['Authorization']
            payload      = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM) 
            user_id      = User.object.get(id=payload['user_id'])
            setattr(request, 'user', user_id)
            return func(request, *args, **kwargs)
        
        except jwt.DecodeError:
            return JsonResponse({'MESSAGE':'JWT DECODE ERROR'}, status=400)
        except TypeError:
            return JsonResponse({"MESSAGE":"LOGIN_REQUIRED"}, status = 401)
        except User.DoesNotExist:
            return JsonResponse({"MESSAGE":"USER_DOES_NOT_EXIST"}, status = 401)
        return func(request, *args, **kwargs)
    return wrapper