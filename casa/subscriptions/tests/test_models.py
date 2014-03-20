from django.test import TestCase
from casa.subscriptions.models import Subscriptions

class subscriptionTest(TestCase):
	def setUp(self):
		self.obj = Subscriptions (
		name='Henrique',
		email='admin@admin.com',
		cpf='11122233345',
		phone='21-96186180'


    def test_create(self):
		'subscription must have name,cpf,email,phones'
	    self.obj.save()
	    self.assertEqual(1,self.obj.pk)