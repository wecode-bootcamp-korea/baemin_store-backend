import jwt

from django.http    import JsonResponse

from user.models     import User
from baemin.settings import SECRET_KEY, ALGORITHM

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
    return wrapper