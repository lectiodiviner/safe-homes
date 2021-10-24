from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

def signup(request):
    if request.method == 'POST':
        if request.POST['pasword1'] == request.POST['password2']:
            user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
            return redirect('accounts: login')
            
    else:
        return render(request, 'accounts/signup.html')

def login(request):
    if request.method =='POST':
         # POST 요청일 경우 로그인 기능 수행
        username = request.POST['username']  # 클라이언트에서 form > input name이 username인 값 가져오기
        password = request.POST['password']  # 클라이언트에서 form > input name이 username인 값 가져오기
        user = authenticate(request, username=username, password=password)  # 장고에서 제공하는 사옹자 확인 함수 / 있는 경우 User 반환, 없는 경우 None 반환
        if user is not None:  # User가 None이 아닌 경우
            auth_login(request, user)  # 장고에서 제공하는 로그인 처리 함수
            return redirect('home')  # 다른 URL 경로 응답, URL name 사용 가능
        else:
            context = {'error': '아이디 또는 비밀번호가 잘못되었습니다.'}  # Template에서 사용할 데이터 정의
            return render(request, 'accounts/login.html', context)
    else:
        # GET 요청일 경우 로그인 HTML 응답
        return render(request, 'accounts/login.html')       