from django.shortcuts import render

# Create your views here.


def layout1(request):
    return render(request, 'layout1.html')

def layout2(request):
    return render(request, 'layout2.html')

def login(request):
    return render(request, 'login/login.html')

def signup(request):
    return render(request, 'login/signup.html')

def findpw(request):
    return render(request, 'login/findpw.html')

def main(request):
    return render(request, 'main.html')

def community(request):
    return render(request, 'community/community.html')

def commu_write(request):
    return render(request, 'community/commu_write.html')

def commu_edit(request):
    return render(request, 'community/commu_edit.html')

def commu_detail(request):
    return render(request, 'community/commu_detail.html')

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

def course(request):
    return render(request, 'course/course.html')

def course_detail(request):
    return render(request, 'course/course_detail.html')

def course_write(request):
    return render(request, 'course/course_write.html')

def course_edit(request):
    return render(request, 'course/course_edit.html')

def purchase_example(request):
    return render(request, 'mypage/purchase_example.html')

def diary(request):
    return render(request, 'diary.html')

def option(request):
    return render(request, 'shop/option.html')

def shop(request):
    return render(request, 'shop/shop.html')

def diary_edit(request):
    return render(request, 'diary_edit.html')

def jampay(request):
    return render(request, 'shop/jampay.html')
    
def scrap(request):
    return render(request, 'scrap.html')