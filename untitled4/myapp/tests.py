from django.test import TestCase
from django.core.urlresolvers import resolve, reverse
from . import views


class PageTest(TestCase):
    """All pages should:
    1. Resolve to the proper view
    2. Return a 200 (login_required urls return 302 if not logged in)
    3. Use the appropriate template
    4. Contain the proper context data
    """

    fixtures = []

    def test_home_page(self):
        """
        Test the home page and view
        """

        url = reverse('myapp:home')
        v = resolve(url)
        self.assertEqual(v.func.__name__, views.HomeView.__name__)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'myapp/home.html')

    def test_about_page(self):
        """
        Test the about page and view
        """

        url = reverse('myapp:about')
        v = resolve(url)
        self.assertEqual(v.func.__name__, views.AboutView.__name__)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'myapp/about.html')

    def test_people_page(self):
        """
        Test the about page and view
        """

        url = reverse('myapp:people')
        v = resolve(url)
        self.assertEqual(v.func.__name__, views.PeopleView.__name__)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'myapp/people.html')

