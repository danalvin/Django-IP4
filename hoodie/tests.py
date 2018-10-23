from .models import *
import datetime as dt


# Create your tests here.
class BusinessTestClass(TestCase):
    def setUp(self):
        self.Biz = Business(name='Dan', )

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.Biz
        `, Business))

        def test_save_method(self):
            self.Biz.save_business()
            business = Business.objects.all()
            self.assertTrue(len(business) > 0)

        def test_data(self):
            self.assertTrue(self.Business.name, "mama mboga")

        def test_delete(self):
            business = Business.objects.filter(id=1)
            business.delete()
            business = Business.objects.all()
            self.assertTrue(len(business) == 0)

    class PostTestClass(TestCase):
        def setUp(self):
            self.Posta = Post(name='mypost', description='a post of mine')

        def test_instance(self):
            self.assertTrue(isinstance(self.Posta, Post))

        def test_save_post(self):
            self.Posta.save_project()
            posts = Post.objects.all()
            self.assertTrue(len(posts) > 0)

        def test_data(self):
            self.assertTrue(self.Posta.name, "mypost")

        def test_delete_post(self):
            post = Post.objects.filter(id=1)
            post.delete()
            posts = Post.objects.all()
            self.assertTrue(len(posts) == 0)