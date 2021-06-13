from django.test import TestCase

# Create your tests here.


class snacks_tests(TestCase):
    def test_home_status_code(self):
        response = self.client.get('/snacks/')
        self.assertEqual(response.status_code , 200)
        self.assertTemplateUsed(response, 'snacks/index.html')

    def test_about_status_code(self):
        response = self.client.get('/snacks/about')
        self.assertEqual(response.status_code , 200)
        self.assertTemplateUsed(response, 'snacks/about.html')

    def test_base_template(self):
        pass
