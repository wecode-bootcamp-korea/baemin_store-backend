import jwt
import json

from django.http    import JsonResponse

from user.models     import User
from baemin.settings import SECRET_KEY, ALGORITHM

def login_required(func):
    def wrapper(self, request, *args, **kwargs):
        try:
            access_token = request.headers['Authorization']
            payload      = jwt.decode(access_token, SECRET_KEY, algorithms=ALGORITHM) 
            user         = User.object.get(id=payload['user_id'])
            request.user = user
        
        except jwt.DecodeError:
            return JsonResponse({'MESSAGE':'JWT_DECODE_ERROR'}, status=400)
        except TypeError:
            return JsonResponse({"MESSAGE":"LOGIN_REQUIRED"}, status = 401)
        except User.DoesNotExist:
            return JsonResponse({"MESSAGE":"USER_DOES_NOT_EXIST"}, status = 401)
        
        return func(request, *args, **kwargs)
    return wrapper