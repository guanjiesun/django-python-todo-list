from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
# from django.contrib.messages import get_messages

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '注册成功！请登录')
            return redirect('users:login')  # 遵循 POST/Redirect/GET 模式
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    """显示当前用户的信息"""
    return render(request, 'users/profile.html', {
        'user': request.user
    })


def get_session(request):
    all_data = dict(request.session)
    return HttpResponse(f"Session Data: {all_data}")


# def show_messages(request):
#     storage = get_messages(request)
#     message_texts = [str(message) for message in storage]
#     return HttpResponse(f"Messages: {message_texts}")
    

# def test_messages(request):
#     storage = get_messages(request)
#     results = [str(message) for message in storage]

#     # 再次读取
#     storage2 = get_messages(request)
#     results2 = [str(message) for message in storage2]

#     return HttpResponse(f"第一次读取: {results}<br>第二次读取: {results2}")