from django.shortcuts import render
from .models import UserMessage #the .model means it share the same catalog with views

def getform(request):  # Http request object
    message = None
    all_message = UserMessage.objects.filter(name='chen') #objects are django's database manage tool all() means fetch all data
    for message in all_message:
        message = all_message[0]
    # user_message = UserMessage()
    # user_message.name = 'bobby2'
    # user_message.message = 'helloworld2'
    # user_message.address = '127.0.0.2'
    # user_message.email = 'bobby2@e.com'
    # user_message.object_id = 'helloworld2'
    # user_message.save()  # 调用save()功能, 能保存对数据库表的修改.
    # if request.method == "POST":  # method也可能是GET, 当method等于POST时才运行以下代码
    #     name = request.POST.get('name', '')  # 这里的get是python字典的一种方法, 如果有'name'这一项, 则取出,如果没有则返回''.
    #     message = request.POST.get('message', '')
    #     address = request.POST.get('address', '')
    #     email = request.POST.get('email', '')
    #     user_message = UserMessage()
    #     user_message.name = name  # 将从POST字典中取出的值赋予给数据库的键.
    #     user_message.message = message
    #     user_message.address = address
    #     user_message.email = email
    #     user_message.object_id = 'helloworld3'  # 这里随意赋予一个值.
    #     user_message.save()
    return render(request, 'message/form.html',{"my_message": message})