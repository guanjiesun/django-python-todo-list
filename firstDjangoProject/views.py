from django.shortcuts import render


def homepage(request):
    # 从查询参数中获取数据，默认值用 .get(key, default)
    name = request.GET.get('name', '访客')
    age = request.GET.get('age', '未知')

    context = {
        'name': name,
        'age': age,
    }

    return render(request, 'index.html', context)
