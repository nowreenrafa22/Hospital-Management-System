from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import *
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse
from django.utils import timezone
# Create your views here.


def homepage(request):
    return render(request, 'index.html')


def aboutpage(request):
    return render(request, 'about.html')


def createaccountpage(request):
    user = "none"
    error = ""
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        requestpassword = request.POST['repeatpassword']
        gender = request.POST['gender']
        address = request.POST['address']
        phonenumber = request.POST['phonenumber']
        birthdate = request.POST['dateofbirth']
        bloodgroup = request.POST['bloodgroup']

        try:
            if password == repeatpassword:  # repeatpassword
                Patient.objects.create(name=name, email=email, gender=gender, address=address,
                                       phonenumber=phonenumber, birthdate=birthdate, bloodgroup=bloodgroup)
                user = User.objects.create_user(
                    first_name=name, email=email, password=password, username=email)
                pat_group = Group.objects.get(name='Patient')
                pat_group.user_set.add(user)
                user.save()
                error = "no"
            else:
                error = "yes"

        except Exception as e:
            # raise e
            error = "yes"
    d = {'error': error}

    return render(request, 'createaccount.html', d)


def loginpage(request):
    error = ""

    if request.method == 'POST':
        u = request.POST['email']
        p = request.POST['password']

        user = authenticate(request, username=u, password=p)
        try:
            if user is not None:
                error = "no"
                login(request, user)
                g = request.user.groups.all()[0].name
                if g == 'Patient':
                    d = {'error': error}
                    return render(request, 'patienthome.html', d)
                elif g == 'Doctor':
                    d = {'error': error}
                    return render(request, 'doctorhome.html', d)
        except Exception as e:
            print(e)

    return render(request, 'login.html')


def Logout(request):
    logout(request)
    return redirect('loginpage')


def Home(request):
    if not request.user.is_active:
        return redirect('loginpage')
    django_user = request.user
    if django_user.groups.filter(name="Patient").exists():
        return render(request, 'patienthome.html')
    if django_user.groups.filter(name="Doctor").exists():
        return render(request, 'doctorhome.html')


def profile(request):
    #g = Group.objects.get(name='Patient')
    if not request.user.is_active:
        return redirect('loginpage')

    g-request.user.groups.all()[0].name

    if g == 'Patient':
        patient_details = Patient.objects.all().filter(email=request.user)
        d = {'patient_details': patient_details}
        return render(request, 'patientprofile.html', d)
    if g == 'Doctor':
        doctor_details = Doctor.objects.all().filter(email=request.user)
        d = {'doctor_details': doctor_details}
        return render(request, 'doctorprofile.html', d)


def MakeAppointments(request):
    error = ""
    if not request.user.is_active:
        return redirect('loginpage')
    alldoctors = Doctor.objects.all()
    d = {'alldoctors': alldoctors}
    g = request.user.groups.all()[0].name
    if g == 'Patient':
        if request.method == 'POST':
            doctoremail = request.POST['doctoremail']
            doctorname = request.POST['doctorname']
            patientname = request.POST['patientname']
            patientemail = request.POST['patientemail']
            appointmentdate = request.POST['appointmentdate']
            appointmenttime = request.POST['appointmenttime']
            symptoms = request.POST['symptoms']
            try:
                Appointment.objects.create(doctorname=doctorname, doctoremail=doctoremail, patientname=patientname, patientemail=patientemail,
                                           appointmentdate=appointmentdate, appointmenttime=appointmenttime, symptoms=symptoms, status=True, prescription="")
                error = "no"
            except:
                error = "yes"
            e = {"error": error}
            return render(request, 'patientmakeappointments.html', e)
        elif request.method == 'GET':
            return render(request, 'patientmakeappointments.html', d)


def viewappointments(request):
    if not request.user.is_active:
        return redirect('loginpage')
    # print(request.user)
    g = request.user.groups.all()[0].name
    if g == 'Patient':
        upcoming_appointments = Appointment.objects.filter(
            patientemail=request.user, appointmentdate__gte=timezone.now(), status=True).order_by('appointmentdate')

        previous_appointments = Appointment.objects.filter(patientemail=request.user, appointmentdate__lt=timezone.now()).order_by(
            '-appointmentdate') | Appointment.objects.filter(patientemail=request.user, status=False).order_by('-appointmentdate')

        d = {"upcoming_appointments": upcoming_appointments,
             "previous_appointments": previous_appointments}
    return render(request, 'patientviewappointments.html', d)
    # elif g == 'Doctor':
    # 	if request.method == 'POST':
    # 		prescriptiondata = request.POST['prescription']
    # 		idvalue = request.POST['idofappointment']
    # 		Appointment.objects.filter(id=idvalue).update(prescription=prescriptiondata,status=False)
    # 		#print(idvalue)
    # 		#print(pname)
    # 		#p = {"idvalue":idvalue,"pname":pname}
    # 		#return render(request,'doctoraddprescription.html',p)
    # 	upcoming_appointments = Appointment.objects.filter(doctoremail=request.user,appointmentdate__gte=timezone.now(),status=True).order_by('appointmentdate')
    # 	#print("Upcoming Appointment",upcoming_appointments)
    # 	previous_appointments = Appointment.objects.filter(doctoremail=request.user,appointmentdate__lt=timezone.now()).order_by('-appointmentdate') | Appointment.objects.filter(doctoremail=requsest.user,status=False).order_by('-appointmentdate')
    # 	#print("Previous Appointment",previous_appointments)
    # 	d = { "upcoming_appointments" : upcoming_appointments, "previous_appointments" : previous_appointments }
    # 	return render(request,'doctorviewappointment.html',d)
    # elif g == 'Receptionist':
    # 	upcoming_appointments = Appointment.objects.filter(appointmentdate__gte=timezone.now(),status=True).order_by('appointmentdate')
    # 	#print("Upcoming Appointment",upcoming_appointments)
    # 	previous_appointments = Appointment.objects.filter(appointmentdate__lt=timezone.now()).order_by('-appointmentdate') | Appointment.objects.filter(status=False).order_by('-appointmentdate')
    # 	#print("Previous Appointment",previous_appointments)
    # 	d = { "upcoming_appointments" : upcoming_appointments, "previous_appointments" : previous_appointments }
    # 	return render(request,'receptionviewappointments.html',d)


def Login_admin(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['username']
        p = request.POST['password']
        user = authenticate(username=u, password=p)
        try:
            if user.is_staff:
                login(request, user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'adminlogin.html', d)


def AdminHome(request):
    # after login user comes to this page.
    if not request.user.is_staff:
        return redirect('login_admin')
    return render(request, 'adminhome.html')


def Logout_admin(request):
    if not request.user.is_staff:
        return redirect('login_admin')
    logout(request)
    return redirect('login_admin')


def adminviewAppointment(request):
    if not request.user.is_staff:
        return redirect('login_admin')
    upcoming_appointments = Appointment.objects.filter(
        appointmentdate__gte=timezone.now(), status=True).order_by('appointmentdate')
    #print("Upcoming Appointment",upcoming_appointments)
    previous_appointments = Appointment.objects.filter(appointmentdate__lt=timezone.now()).order_by(
        '-appointmentdate') | Appointment.objects.filter(status=False).order_by('-appointmentdate')
    #print("Previous Appointment",previous_appointments)
    d = {"upcoming_appointments": upcoming_appointments,
         "previous_appointments": previous_appointments}
    return render(request, 'adminviewappointments.html', d)


def adminaddDoctor(request):
    error = ""
    user = "none"
    if not request.user.is_staff:
        return redirect('login_admin')

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        repeatpassword = request.POST['repeatpasssword']
        gender = request.POST['gender']
        phonenumber = request.POST['phonenumber']
        address = request.POST['address']
        birthdate = request.POST['dateofbirth']
        bloodgroup = request.POST['bloodgroup']
        specialization = request.POST['specialization']

        try:
            if password == repeatpassword:
                Doctor.objects.create(name=name, email=email, password=password, gender=gender, phonenumber=phonenumber,
                                      address=address, birthdate=birthdate, bloodgroup=bloodgroup, specialization=specialization)
                user = User.objects.create_user(
                    first_name=name, email=email, password=password, username=email)
                doc_group = Group.objects.get(name='Doctor')
                doc_group.user_set.add(user)
                user.save()
                error = "no"
            else:
                error = "yes"
        except Exception as e:
            error = "yes"
    d = {'error': error}
    return render(request, 'adminadddoctor.html', d)


def adminviewDoctor(request):
    if not request.user.is_staff:
        return redirect('login_admin')
    doc = Doctor.objects.all()
    d = {'doc': doc}
    return render(request, 'adminviewDoctors.html', d)
