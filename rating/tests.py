from django.test import TestCase
from .models import Profile, Project
import datetime as dt
# Create your tests here.

class ProfileTestClass(TestCase):
    #Set up method
    def setUp(self):
        self.profile=Profile(user="beryl",profile_pic="default.png",bio="award_official",contacts='berybery@gmail.com')
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.new_profile,Profile))

    def test_save_method(self):
        self.profile.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)

    def test_delete_method(self):
        self.profile.delete_profile()
        profiles= Profile.objects.all()
        self.assertTrue(len(profiles) == 0)

class ProjecTestClass(TestCase):
    def setUp(self):
        self.profile=Profile(user="beryl",profile_pic="default.png",bio="award_official",contacts='berybery@gmail.com')
        self.project=Project(image="image.png",title="title",description="mypictoday",link='https;//mypictoday',profile=self.profile)

    def test_instance(self):
        self.assertTrue(isinstance(self.project, Project))

    def test_save_method(self):
        self.project.save_project()
        projects = Project.objects.all()
        self.assertTrue(len(projects) > 0) 

    def test_search_method(self):
        self.assertQuerysetEqual(Project.objects.filter(title__icontains='image'), ["<Project: image>"])  

    def test_delete_method(self):
        self.project.delete_project()
        projects=Project.objects.all()
        self.assertTrue(len(projects) == 0) 

           

