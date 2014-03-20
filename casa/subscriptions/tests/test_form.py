from django.test import TestCase
from casa.subscriptions.form import SubscriptionForm


class SubscriptionFormTest(TestCase):
	def test_has_fields(self):
		form = SubscriptionForm()
		self.assertItemEqual(['name','email','cpf','phone'],form.fields)
		