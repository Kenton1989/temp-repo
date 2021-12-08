from django.http import HttpResponse, HttpRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
import logging
import io
from PIL import Image

log = logging.getLogger('my_app')


def fail_response_template(request):
    def fail_response(err_msg):
        param = {'err_msg': err_msg}
        return render(request, 'rec_error.html', param)
    return fail_response


def handle_recognize(request: HttpRequest):
    fail_response = fail_response_template(request)

    if request.method != 'POST':
        return fail_response('Invalid access.')

    request_img = request.FILES.get('hand_writing_img')
    if request_img == None:
        return fail_response('No file uploaded')

    image_bytes = request_img.read()
    data_stream = io.BytesIO(image_bytes)
    try:
        image = Image.open(data_stream)
    except:
        return fail_response('Unknown image format')

    # get result from image
    result = 1283

    return render(request, 'rec_result.html', {'result': result})


def handle_home(request: HttpRequest):
    return render(request, 'index.html')
