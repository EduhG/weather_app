from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string

from temp_viewer.views import home_page


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        """Root url should resolve to home page view"""

        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        """Home page rendered from server should return correct html"""

        request = HttpRequest()
        response = home_page(request)
        expected_html = render_to_string('index.html')

        self.assertEqual(response.content.decode(), expected_html)

    def test_page_not_found(self):
        """Pages which dont exist should be directed to a 404 page"""

        response = self.client.get('/a-page-which-doesnt-exist')
        self.assertTrue(response.status_code, 404)
