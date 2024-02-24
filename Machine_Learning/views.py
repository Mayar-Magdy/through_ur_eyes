from django.shortcuts import render
from django.http import JsonResponse

# from PIL import Image

# import joblib


# def predict_view (request):
#     if request.method=='POST':
#         user = request.user
#         upload_image = request.FILES['image'] 
#         prediction  = ML_MODEL(upload_image)
#         disease = request.POST.get('type')
#         image_output = ImageOutput(user=user, image=upload_image, output=prediction, disease=disease)
#         image_output.save()
#         context = {'prediction': prediction}

def img(request):
     return render(request, 'img.html')

def i(request):
    if request.method == 'POST' and request.FILES['image']:
        image = request.FILES['image']
        # post = Post(img_brief=image)
        # post.save()
        print(image)
        response_data = {'message': 'DONE '}
        return JsonResponse(response_data)
    



# def predict_view(request):
#     if request.method == "POST":
#         user = request.user
#         # upload_image =  request.POST.get('file')
#         upload_image = request.FILES['file'] 
#         disease =  request.POST.get('type')
#         result = ML_MODEL(upload_image)
#         image_output = ImageOutput(user=user, image=upload_image, output=result, disease=disease)
#         image_output.save()
#         # print(upload_image)
#         # print(type)
#     return JsonResponse({
#         "result": result
#     })

