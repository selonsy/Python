from django.http import HttpResponse
from django.shortcuts import render
from .models import IMG
from django.views.decorators.csrf import csrf_exempt
import json
import os
import uuid

def hello(request):
    return HttpResponse("Hello world ! ")

def getMatchFaces(request):
    if request.method == 'get':
        return render(request, 'error.html')
    else:
        data = [
            {
                'id':1,
                'score':97.1,
                'src':'http://img5.imgtn.bdimg.com/it/u=415293130,2419074865&fm=26&gp=0.jpg'
            },
            {
                'id':2,
                'score':86.2,
                'src':'http://img.zcool.cn/community/015da9554971170000019ae9f43459.jpg@2o.jpg'
            },
            {
                'id':3,
                'score':59.3,
                'src':'http://txt25-2.book118.com/2017/0425/book102185/102184432.jpg'
            }
        ]
        result = {
            'code': 200,
            'message': 'success',
            'data': data
        }
        return HttpResponse(json.dumps(result), content_type="application/json")

def getMatchFacesTest(request):
    if request.method == 'GET':
        return render(request, 'error.html')
    else:
        _type = int(request.POST['num'])

        data1 = [
            {
                'id':1,
                'score':97.1,
                'name':'刘亦菲',
                'src':'http://img.duoziwang.com/2018/18/06011824502842.jpg'
            },
            {
                'id':2,
                'score':86.2,
                'name':'刘诗诗',
                'src':'http://www.vstou.com/upload/image/421/201608/1472387329491771.jpg'
            },
            {
                'id':3,
                'score':59.3,
                'name':'金恩智',
                'src':'http://www.facelib.org/images/lib/400/201801031706480001.jpg'
            }
        ]
        data2 = [
            {
                'id':1,
                'score':90.2,
                'name':'杨幂',
                'src':'http://imgtu.5011.net/uploads/content/20170327/9355601490582583.jpg'
            },
            {
                'id':2,
                'score':80.5,
                'name':'卓亨瑜',
                'src':'https://ss1.baidu.com/6ONXsjip0QIZ8tyhnq/it/u=842059297,2907363609&fm=175&app=25&f=JPEG?w=550&h=381&s=A49019DFD862621FDC2C6DBC03001023'
            },
            {
                'id':3,
                'score':79.9,
                'name':'北川景子',
                'src':'https://ss1.baidu.com/6ONXsjip0QIZ8tyhnq/it/u=2175383419,2298658857&fm=175&app=25&f=JPEG?w=639&h=422&s=6A3A08C75CFA229E493C142B0300D044'
            }
        ]
              
        if _type==1:
            data =data1
        elif _type==2:
            data =data2
        else:
            data =data1

        result = {
            'code': 200,
            'message': 'success',
            'data': data
        }
        return HttpResponse(json.dumps(result), content_type="application/json")

def test(request):
    return render(request,'test.html')

@csrf_exempt
def uploadImg(request):
    if request.method == 'POST':
        # new_img = IMG(
        #     img=request.FILES.get('img'),
        #     name = request.FILES.get('img').name
        # )
        # new_img.save()
        f = request.FILES.get('img')
        baseDir = os.path.dirname(os.path.abspath(__name__))
        jpgdir = os.path.join(baseDir,'static','media','openface','upload')        
        
        # 获取图片后缀
        suffix = f.name.split('.')[1]
        # prin t(suffix)
        # 修改上传图片名称，避免重复       
        new_name = str(uuid.uuid1())+'.'+suffix
        # 判断图片格式是否符合要求
        
        filename = os.path.join(jpgdir,new_name)

        fobj = open(filename,'wb')
        for chrunk in f.chunks():
            fobj.write(chrunk)
        fobj.close()
    return render(request, 'uploadimg.html')

@csrf_exempt
def showImg(request):    
    return render(request, 'showimg.html')