import os
from django.conf import settings
from django.http import HttpResponseRedirect, HttpResponseBadRequest, HttpResponse
from django.shortcuts import render
# from .forms.forms import VideoUploadForm

def upload_big_file(request):
    if request.method == 'POST':
        file = request.FILES['file']

        # Check if the file is too big
        if file.size > 10000000:
            return HttpResponseBadRequest('File is too big')

        # Save the file
        destination = os.path.join(settings.MEDIA_ROOT, file.name)
        with open(destination, 'wb') as f:
            for chunk in file.chunks():
                f.write(chunk)

        return HttpResponseRedirect('/success')

def upload_video(request):
    return render(request, template_name="index.html")

