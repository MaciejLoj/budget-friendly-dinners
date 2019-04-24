from . settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',  # connection string
    }
}
# In-memory sqlite database makes tests really fast

EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'

# local memory, sending emails
