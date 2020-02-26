from django.shortcuts import render, redirect
from django.contrib import messages
import qrcode, bcrypt, random, string
from .models import User, Master, QR, All_QR

def index(request):
    return render(request, 'index.html')

def code_process(request):
    codes = QR.objects.all()
    print(request.POST)
    for index in codes:
        if index.text == request.POST['usercode']:
            return render(request,'REAL.html')
    return render(request,'FAKE.html')

# def success(request):
#     return render(request,'REAL.html')

def create_qr(request):
    qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
    )
    x = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    qr.add_data(x)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    filename = x + '.jpg'
    img.save('media/qr_img/' + filename)
    # img.save('/media/qr_img')
    QR.objects.create(text=x, imgfile=filename)
    a = QR.objects.get(text=x)
    return redirect(f'/qr_created/{a.id}')

def qr_created(request,qr_id):
    context={
        'this':QR.objects.get(id=qr_id)
    }
    return render(request,'this_qr.html',context)

def login(request):
    return render(request,'login.html')

def login_process(request):
    if request.POST['email']=='email@email.com':
        return redirect('/master')
    elif User.objects.filter(email=request.POST['email']):
        user = User.objects.get(email=request.POST['email'])
        if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
            request.session['user.id'] = user.id
            return redirect(index)
    messages.error(request, 'email/password does not match')
    return redirect(login)

def register(request):
    return render(request,'register.html')

def register_process(request):
    print('in validator')
    errors = User.objects.validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(index)
    print('valid arguments')
    print('hashing password')
    password = request.POST['password']
    pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    print('user hash:')
    print(pw_hash)
    User.objects.create(first_name=request.POST['first_name'],
                        last_name=request.POST['last_name'],
                        email=request.POST['email'],
                        password=pw_hash)
    print('created user')
    return redirect('/login')

def master(request):
    context = {
        'all_qr': QR.objects.all()
    }
    return render(request,'master.html',context)

def process(request):
    print('in validator')
    errors = User.objects.validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(index)
    print('valid arguments')
    print('hashing password')
    password = request.POST['password']
    pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    print('user hash:')
    print(pw_hash)
    User.objects.create(first_name=request.POST['first_name'],
                        last_name=request.POST['last_name'],
                        email=request.POST['email'],
                        password=pw_hash)
    print('created user')
    return redirect(login_index)
