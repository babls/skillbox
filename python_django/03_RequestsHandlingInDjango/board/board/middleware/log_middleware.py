from collections import defaultdict
from django.core.exceptions import PermissionDenied
import datetime
import time

# Осушествляет задержку в несколько секунд при обработке для каждого n-го запроса
class LogMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response
        self.count_views = defaultdict(int)
    
    def __call__(self, request):
        timestamp = time.monotonic()
        response = self.get_response(request)
        ip = request.META.get('REMOTE_ADDR')
        self.count_views[ip] +=1
        f = open('text.txt', 'a')
        f.write("Номер запроса - " + str(self.count_views[ip]))
        f.write(" запрошенный метод - " + str(request.method))
        f.write(" запрошенный URL - " + str(request.path))
        f.write(" дата и время события - " + str(datetime.datetime.now()))
        f.write("\n")
        f.close()
        print(
            f'Номер запроса - {self.count_views[ip]}\n'
            f'запрошенный метод - {request.method}\n'
            f'запрошенный URL - {request.path}\n'
            f'дата и время события - {datetime.datetime.now()}\n'
        )

        return response