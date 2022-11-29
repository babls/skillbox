from _csv import reader
from datetime import datetime

from app_blog.forms import UploadFileForm, UploadFilePostListForm
from app_blog.models import BlogPost, FilesPost
from django import forms
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View


class NewPostBlog(View):

    def get(self, request):
        upload_file_form = UploadFileForm()
        upload_file_form.fields['author'].widget = forms.HiddenInput()
        upload_file_form.fields['dateEdit'].widget = forms.HiddenInput()
        upload_file_form.fields['activity'].widget = forms.HiddenInput()
        upload_file_form.fields['dataCreate'].widget = forms.HiddenInput()
        return render(request, 'app_blog/new_post_blog.html', context={'form': upload_file_form})

    def post(self, request):
        upload_file_form = UploadFileForm(request.POST, request.FILES)
        if upload_file_form.is_valid():
            upload_file_form.author = request.user
            upload_file_form.activity = 'True'
            upload_file_form.dataCreate = datetime.now()
            post_form = upload_file_form.save(commit=False)
            post_form.author = User.objects.get(id=request.user.id)
            post_form.save()
            files = request.FILES.getlist('image')
            for f in files:
                instance = FilesPost(file=f, post_id=BlogPost.objects.get(id=post_form.id))
                instance.save()
            upload_file_form.save()
            post_form.save()
            # return HttpResponse(content=file.name, status=200)
            return HttpResponseRedirect(reverse('main'))
        context = {
            'form': upload_file_form
        }

        return render(request, 'app_blog/new_post_blog.html', context=context)


def list_post_view(request):
    if request.method == "GET":
        post_list = BlogPost.objects.filter(author=request.user)
        form = UploadFilePostListForm()
        return render(request, 'app_blog/list_post.html', {'post_list': post_list, 'form': form})

    else:
        upload_file_form = UploadFilePostListForm(request.POST, request.FILES)
        print(upload_file_form)
        if upload_file_form.is_valid():
            post_file = upload_file_form.cleaned_data['file'].read()
            post_str = post_file.decode('utf-8').split('\n')
            csv_reader = reader(post_str, delimiter=",", quotechar="'")
            user = User.objects.get(id=request.user.id)
            for row in csv_reader:
                # NewPostBlog.objects.filter(code=row[0]).update(price=Decimal(row[1]))
                NewPost = BlogPost.objects.create()
                NewPost.author = user
                NewPost.name = row[0]
                NewPost.text = row[1]
                NewPost.save()
            return HttpResponseRedirect(reverse('list_post'))


class InfoPost(View):
    def get(self, request, post_id):
        post = BlogPost.objects.get(id=post_id)
        user_post = User.objects.get(username=post.author)
        files = FilesPost.objects.filter(post_id=post_id)
        # print(files)
        return render(request, 'app_blog/infopost.html',
                      {'title': 'Детальная страница записи', 'post': post, 'user_post': user_post, 'files': files})
