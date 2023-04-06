from django.test import TestCase, Client
from django.urls import reverse
from hospital.models import Patient, Doctor, Appointment
import json

class TestViews(TestCase):

    
    
    def test_homepage_GET(self):
        client=Client()
        response=client.get(reverse('homepage'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,'index.html','navbar.html')

    
    
    def test_aboutpage_GET(self):
        client=Client()
        response=client.get(reverse('aboutpage'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,'about.html')


   
   
    def test_loginpage_GET(self):
        client=Client()
        response=client.get(reverse('loginpage'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,'login.html')

    
    
    
    def test_Login_admin_GET(self):
        client=Client()
        response=client.get(reverse('login_admin'))
        self.assertEquals(response.status_code, 200)
        

   
   
    def test_Logout_GET(self):
        client=Client()
        response=client.get(reverse('logout'))
        self.assertEquals(response.status_code, 302)
        

   
    
    def test_Home_GET(self):
        client=Client()
        response=client.get(reverse('home'))
        self.assertEquals(response.status_code,200)
        


   
   
    def test_profile_GET(self):
        client=Client()
        response=client.get(reverse('profile'))
        self.assertEquals(response.status_code, 302)

    
    
    def test_MakeAppointments_GET(self):
        client=Client()
        response=client.get(reverse('aboutpage'))
        self.assertEquals(response.status_code, 200)

   
   
    def test_viewappointments_GET(self):
        client=Client()
        response=client.get(reverse('viewappointments'))
        self.assertEquals(response.status_code, 302)

    
    
    def test_adminaddDoctor_GET(self):
        client=Client()
        response=client.get(reverse('adminaddDoctor'))
        self.assertEquals(response.status_code, 302)

    
    
    def test_adminviewDoctor_GET(self):
        client=Client()
        response=client.get(reverse('viewappointments'))
        self.assertEquals(response.status_code, 302)

    


        

    

    