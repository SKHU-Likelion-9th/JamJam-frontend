from django.shortcuts import render

# Create your views here.


def layout1(request):
    return render(request, 'layout1.html')

def layout2(request):
    return render(request, 'layout2.html')

def login(request):
    return render(request, 'login.html')

def main(request):
    return render(request, 'main.html')

def community(request):
    return render(request, 'community/community.html')

def commu_write(request):
    return render(request, 'community/commu_write.html')

def commu_edit(request):
    return render(request, 'community/commu_edit.html')

def detail(request):
    return render(request, 'community/detail.html')

def mypage(request):
    return render(request, 'mypage/mypage.html')

def profile(request):
    return render(request, 'mypage/profile.html')

def connection(request):
    return render(request, 'mypage/connection.html')

def purchaselist(request):
    return render(request, 'mypage/purchaselist.html')

def profile_edit(request):
    return render(request, 'mypage/profile_edit.html')
    
def day_detail(request):
    return render(request, 'day_detail.html')

def theme(request):
    return render(request, 'shop/theme.html')

def diary(request):
    return render(request, 'diary.html')