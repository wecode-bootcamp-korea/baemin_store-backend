SECRET_KEY = '6^f#0g*b6nh95$w9ngekbhmr$hay%0h7@7(99@%8b4i=yx9d&7'

DATABASES = {
    'default' : {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'baemin_store',
        'USER': 'root',
        'PASSWORD': '3220',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

ALGORITHM= 'HS256'
