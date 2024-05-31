from django.test import TestCase
from .models import Image, Category


class CategoryModelTest(TestCase):

    def setUp(self):
        self.category = Category.objects.create(category="Nature")

    def test_category_creation(self):
        self.assertEqual(self.category.category, "Nature")

    def test_category_str_method(self):
        self.assertEqual(str(self.category), "Nature")


class ImageModelTest(TestCase):

    def setUp(self):
        self.category1 = Category.objects.create(category="Nature")
        self.category2 = Category.objects.create(category="Wildlife")
        self.image = Image.objects.create(
            title="Sunset",
            image="https://example.com/image.jpg",
            age_limit=18
        )
        self.image.categories.add(self.category1, self.category2)

    def test_image_creation(self):
        self.assertEqual(self.image.title, "Sunset")
        self.assertEqual(self.image.image, "https://example.com/image.jpg")
        self.assertEqual(self.image.age_limit, 18)

    def test_image_categories(self):
        self.assertEqual(self.image.categories.count(), 2)
        self.assertIn(self.category1, self.image.categories.all())
        self.assertIn(self.category2, self.image.categories.all())

    def test_image_creation_date(self):
        self.assertIsNotNone(self.image.created_date)
