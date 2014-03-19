from django.test import TestCase
from casa.subscriptions.forms import SubscriptionForm


class SubscribeTest(TestCase):
 	def setUp(self):
 		self.resp = self.client.get('/inscricao')
   
 	def test_get(self):
 		self.assertEqual(200,self.resp.status_code)

	def test_template(self):
 		 self.assertTemplateUsed(self.resp,'subscriptions/subscriptions_form.html')
    
    def test_html(self):
    	self.assertContains(self.resp,'<form')
    	self.assertContains(self.resp,'<input',5)
    	self.assertContains(self.resp,'type="text"',3)
    	self.assertContains(self.resp,'type="submit"')

    	def teste_csrf(self):
    		self.assertContains(self.resp,'çsrfmiddlewareroken')



# Create your tests here.
