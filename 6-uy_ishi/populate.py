import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from api.models import Genre, Book

# Janrlarni qo'shish
g1 = Genre.objects.create(name="Badiiy adabiyot")
g2 = Genre.objects.create(name="Sarguzasht")
g3 = Genre.objects.create(name="Ilmiy-fantastika")

# Kitoblarni qo'shish
Book.objects.create(title="O'tkan kunlar", price=45000, genre=g1)
Book.objects.create(title="Shaytanat", price=55000, genre=g1)
Book.objects.create(title="Garri Potter", price=60000, genre=g2)
Book.objects.create(title="Robinzon Kruzo", price=40000, genre=g2)
Book.objects.create(title="Marslik", price=50000, genre=g3)

print("Baza muvaffaqiyatli to'ldirildi!")
