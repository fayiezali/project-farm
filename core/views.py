from django.shortcuts import render , redirect
#
#
# View the dashboard Page
def dashboard(request):
    return render(request,'core/index.html')