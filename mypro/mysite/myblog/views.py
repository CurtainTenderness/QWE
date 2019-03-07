from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from . import models
from django.shortcuts import redirect,reverse
# Ajax内容引入
from django.views.decorators.http import require_GET,require_POST
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
from django.core.serializers import serialize
from django.core.cache import cache
# 分页使用
from django.core.paginator import Paginator,Page
# 事物的导入
from django.db import transaction
# 字节流
from io import BytesIO
from . import ubils
# 封装
from . import forms

# Create your views here.
# 主页
@csrf_exempt
def index(request):
    # print('博客')
    # return HttpResponse('博客')
    return render(request,'myblog/index.html',{'msg':'今天真烦'})

# 登录
def login(req):
    if req.method=='GET':
        return render(req,"myblog/login.html",{'msg':'登录页面'})
    elif req.method=='POST':
        name=req.POST.get('name')
        password=req.POST.get('password')

        try:
            models.Users.objects.get(name=name,password=password)
            user=models.Users.objects.get(id=1)
            print(user.name)
            return HttpResponse('登陆成功')
        except:
            return render(req,'myblog/login.html',{'msg':'登陆成功'})

# 注册
def signin(req):
    if req.method == 'GET':
        return render(req, "myblog/signin.html", {'msg': '注册页面'})
    elif req.method== 'POST':
        name = req.POST.get('name')
        password = req.POST.get('password')
        email = req.POST.get('email')
        age = req.POST.get('age')
        # 头像图片
        # 拼接上传路径
        avater = req.FILES['avater']
        # 头像图片保存的位置，只能在根目录中
        path='static/img/'+avater.name
        # 以流的方式打开上传
        with open(path,'wb') as file:
            # 分片写入
            for f in avater.chunks():
                file.write(f)
        # print(avater)
        try:
            user=models.Users(name=name,password=password,email=email,age=age,avater=path)
            user.save()
            return HttpResponse('注册成功')
            # return render(req,'myblog/login.html',{'msg':'请登录'})
        except:
            return render(req,"myblog/signin.html",{'msg':'注册失败'})




# 确保整个方法具有原子性，事物不能用后台admin打开，需要用网址直接打开
@transaction.atomic()
# 发表文章
def addarticle(req):
    if req.method=='GET':
        # return HttpResponse('chulaimei ')
        return render(req, 'myblog/addarticle.html')
    elif req.method=='POST':
        title=req.POST['title']
        content=req.POST['content']
        user=models.Users.objects.get(pk=1)
        # 设置还原点
        s_id=transaction.savepoint()
        try:
            # 测试时最容易使用的一个错误
            # 1/0
            article=models.Article(title=title,content=content,author=user)
            article.save()
            transaction.savepoint_commit(s_id)
            return HttpResponse('成功')
        except:
            transaction.savepoint_rollback(s_id)
            return HttpResponse('失败')
        # return redirect(reverse('myblog:index'))

# 缓存
def list(req):
    users = cache.get('users')
    print(users)
    if users is None:
        print('数据库查询')
        users = models.Users.objects.all()
        print()
        print('存入缓存')
        cache.set('users',users)
        print(cache.get('users'))
    return HttpResponse('成功')


# 验证码
def createmage(req):
    # 准备个空间防止验证码图片
    b=BytesIO()
    # 生成验证码图片
    img,code=ubils.create_code()
    # 把验证码图片保存到流里面,图片不能用JPG格式，只能用png格式
    img.save(b,'PNG')
    # 方便拿过来用户输入做验证
    req.session['code']=code
    return HttpResponse(b.getvalue())



# ajax
@csrf_exempt
def jsontest(req):
    # 单个对象的处理
    u=models.Users.objects.get(pk=1)
    u=model_to_dict(u)
    # return JsonResponse(u)
    # 多个对象的列表
    users=models.Users.objects.all()
    users=serialize('json',users)
    return HttpResponse(users)



from django.core.mail import send_mail
from django.conf import settings
def sendmails(req):
    send_mail('发送邮件','第一次尝试',settings.EMAIL_FROM,['529095032@qq.com'])
    return HttpResponse('发送成功')