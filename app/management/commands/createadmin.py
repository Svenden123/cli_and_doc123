from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
	help = 'Create Superuser users and allow password to be provided'

	def handle(self, *args, **options):
		username = input('Username: ')
		password = input('Password: ')
		password2 = input('Password (again): ')

		while password != password2:
			print("Error: Your passwords didn't match.")
			return False

		User.objects.create_superuser(username=username, email='', password=password)
		print('Superuser created successfully')

		# добавим в базу
		if password:
			user = User.objects.get(username=username)
			user.set_password(password)
			user.save()
