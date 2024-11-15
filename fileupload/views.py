from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect
from .forms import UploadFileForm
from .models import UploadedFile
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib import messages

@login_required
def upload_file(request):
    if request.method == 'POST' and request.FILES['file']:
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your file was uploaded successfully!')
            return redirect('upload_file')
    else:
        form = UploadFileForm()
    return render(request, 'fileupload/upload.html', {'form': form})

@staff_member_required
def list_uploaded_files(request):
    files = UploadedFile.objects.all()
    return render(request, 'fileupload/list_files.html', {'files': files})

class CustomLoginView(LoginView):
    template_name = 'fileupload/login.html'

    def form_valid(self, form):
        """Override to redirect non-admin users to a different page."""
        login(self.request, form.get_user())
        if self.request.user.is_staff:
            return redirect('admin:index')  # Redirect to the admin page for admin users
        else:
            return redirect('upload_file')  # Redirect non-admin users to the upload page
        

def home(request):
    return render(request, 'fileupload/home.html')  # We'll create this template next