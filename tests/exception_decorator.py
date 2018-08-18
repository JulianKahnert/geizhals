from functools import wraps
from requests.exceptions import HTTPError

def except_httperror(func):
    def _decorator(request, *args, **kwargs):
        try:
            func(request, *args, **kwargs)
        except HTTPError as e:
            print(e)

    return wraps(func)(_decorator)
