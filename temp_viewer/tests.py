from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string
from temp_viewer.models import Temperature

from temp_viewer.views import home_page, login, get_json_temps


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        """Root url should resolve to home page view"""

        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        """Home page rendered from server should return correct html"""

        request = HttpRequest()
        response = home_page(request)
        self.assertIn('Weather App', response.content.decode('utf8'))

    def test_page_not_found(self):
        """
        Pages which dont exist should be directed to a 404 page
        """

        response = self.client.get('/a-page-which-doesnt-exist')
        self.assertTrue(response.status_code, 404)

    def test_home_page_can_save_a_POST_request(self):
        """
        Home page should save data to databse
        """
        request = HttpRequest()
        request.method = 'POST'
        request.POST['date_time'] = '2016-11-07'
        request.POST['temp'] = '45.45'

        response = home_page(request)
        temps = [temp.temp for temp in Temperature.objects.all()]

        self.assertIn('45.45', str(temps[0]))
        self.assertTrue(response.status_code, 404)

    def test_get_json_temps(self):
        """
        Should return a json object of records in database
        """
        request = HttpRequest()
        request.method = 'POST'
        request.POST['date_time'] = '2016-11-07'
        request.POST['temp'] = '45.45'

        response = get_json_temps(request)

        self.assertTrue(response.status_code, 200)
        self.assertTrue(response.content, 'application/json')
