from django.http import HttpResponse

from django.views import View


class ToDoView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse('<ul>'
                            '<li>Установить python - Готово</li>'
                            '<li>Установить django - Готово</li>'
                            '<li>Запустить сервер - Готово</li>'
                            '<li>Порадоваться результату - х2 Готово</li>'
                            '<li>GIT add - Готово</li>'
                            '<li>GIT commit - Готово</li>'
                            '<li>GIT push - Готово</li>'
                            '<li>GIT узнать как создавать новые ветки</li>'
                            '<li>GIT создать новую ветку</li>'
                            '</ul>')
