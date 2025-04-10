from django.shortcuts import render
import qrcode
from io import BytesIO
from django.http import HttpResponse
from qrcode.constants import ERROR_CORRECT_L
import base64
# Create your views here.


def home(request):
    context = {
        'title': 'Home'
    }
    template = 'app_general/home.html'
    return render(request, template, context)



def generate_qr(request):
    img_data = None
    if request.method == 'POST':
        data = request.POST.get('data')
        qr = qrcode.QRCode(
            version=1,
            error_correction=ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img_io = BytesIO()
        img.save(img_io, format='PNG')
        img_io.seek(0)


        # Encode the image to base64
        img_base64 = base64.b64encode(img_io.getvalue()).decode('utf-8')
        img_data = f'data:image/png;base64, {img_base64}'
    context = {
        'title':'Generate QR Code',
        'img_data': img_data,
    }
    template = 'app_general/generate_qr.html'
    return render(request, template, context)