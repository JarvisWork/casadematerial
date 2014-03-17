from django.test import TestCase


class SubscribeTest(TestCase):
 	def setUp(self):
 		self.resp = self.client.get('/inscricao')
   
 	def test_get(self):
 		self.assertEqual(200,self.resp.status_code)

	def test_template(self):
 		 self.assertTemplateUsed(self.resp,'subscriptions/subscriptions_form.html')
# Create your tests here.
