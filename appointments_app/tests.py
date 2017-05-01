from django.test import TestCase
from django.http import HttpRequest
from django.core.urlresolvers import resolve

from .views import setAppointment


# Create your tests here.

class AppointmentsTest(TestCase):

    def test_root_url_resolves_to_setAppointmets_view(self):
        url = resolve('/')
        self.assertEqual(url.func, setAppointment)

    def test_appointments_form_csrf_presence(self):
        request = HttpRequest()
        response = setAppointment(request)
        html = response.content.decode('utf8')
        self.assertIn('csrfmiddlewaretoken', html)