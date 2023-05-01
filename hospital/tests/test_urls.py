from django.test import SimpleTestCase
from django.urls import reverse, resolve
from hospital.views import homepage,aboutpage,createaccountpage,loginpage,Logout,Home,profile,MakeAppointments,viewappointments,Login_admin,Logout_admin,adminaddDoctor,adminviewDoctor,adminviewAppointment, AdminHome

class TestUrls(SimpleTestCase):

    def test_homepage_url(self):
       url= reverse('homepage')
       self.assertEquals(resolve(url).func,homepage)

    def test_aboutpage_url(self):
       url= reverse('aboutpage')
       self.assertEquals(resolve(url).func,aboutpage)


    def test_createaccountpage_url(self):
       url= reverse('createaccountpage')
       self.assertEquals(resolve(url).func,createaccountpage)

    def test_loginpage_url(self):
       url= reverse('loginpage')
       self.assertEquals(resolve(url).func,loginpage)


    def test_Logout_url(self):
       url= reverse('logout')
       self.assertEquals(resolve(url).func,Logout)

    def test_Home_url(self):
       url= reverse('home')
       self.assertEquals(resolve(url).func,Home)


    def test_profile_url(self):
       url= reverse('profile')
       self.assertEquals(resolve(url).func,profile)



    def test_viewappointments_url(self):
       url= reverse('viewappointments')
       self.assertEquals(resolve(url).func,viewappointments)

    def test_Login_admin_url(self):
       url= reverse('login_admin')
       self.assertEquals(resolve(url).func,Login_admin)



    def test_adminaddDoctor_url(self):
       url= reverse('adminaddDoctor')
       self.assertEquals(resolve(url).func,adminaddDoctor)

    def test_adminviewDoctor_url(self):
       url= reverse('adminviewDoctor')
       self.assertEquals(resolve(url).func,adminviewDoctor)

    def test_adminviewAppointment_url(self):
       url= reverse('adminviewAppointment')
       self.assertEquals(resolve(url).func,adminviewAppointment)

  

