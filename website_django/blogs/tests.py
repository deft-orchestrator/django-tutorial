
from django.test import TestCase, Client
from django.urls import reverse
from .models import Post

class PostModelTest(TestCase):
	def test_create_post(self):
		post = Post.objects.create(title="Judul", content="Isi konten")
		self.assertEqual(str(post), "Judul")

class BlogViewsTest(TestCase):
	def setUp(self):
		self.post = Post.objects.create(title="Judul", content="Isi konten")
		self.client = Client()

	def test_post_list_view(self):
		response = self.client.get(reverse('post_list'))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, self.post.title)

	def test_post_detail_view(self):
		response = self.client.get(reverse('post_detail', args=[self.post.id]))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, self.post.title)

