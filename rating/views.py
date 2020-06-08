from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect,Http404, JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from .forms import Registration,NewProjectForm, NewRatingForm, NewProfileForm
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import  Project,Profile,Profiles,Projects,Rating
from .serializer import ProfileSerializer,ProjectSerializer
from rest_framework import status
from .permissions import IsAdminOrReadOnly
import datetime as dt
from django.contrib.auth.models import User

def register(request):
  if request.method == 'POST':
    form = Registration(request.POST)
    if form.is_valid():
      form.save()
      email = form.cleaned_data['email']
      username = form.cleaned_data.get('username')
      return redirect('login')
  else:
    form = Registration()
  return render(request,'auth/registration.html',{"form":form})

def convert_dates(dates):
    # function that gets the weekday number for the date.
    day_number = dt.date.weekday(dates)
    days = ['Monday','Tuesday','Wednesday','thursday','Friday','Saturday','Sunday']
    '''
    Returns the actual day of the week
    '''
    day = days[day_number]
    return day

def index(request):
  date = dt.date.today()
  return render(request, 'index.html',{"date": date })

@login_required
def myprojects(request):
    projects = Project.objects.all().order_by()
    return render(request,'myprojects.html', {'projects':projects})

@login_required
def project(request, id):
  ida = request.user.id
  project = Project.objects.get(pk=id)
  ratings = Rating.objects.filter(project=id)
  return render(request, 'project.html',{'profile':profile,'project':project,'ratings':ratings})

@login_required
def new_projects(request):
  ida = request.user.id
  if request.method == 'POST':
    form = NewProjectForm(request.POST, request.FILES)
    if form.is_valid():
      project = form.save(commit=False)
      project.save()
    return redirect('index')
  else:
    form = NewProjectForm()
  return render(request, 'new_project.html',{'form':form,'profile':profile})
 
@login_required
def profile(request, id):
  ida = request.user.id
  profile = Profile.objects.get(user=ida)
  user = request.user
  myprofile = Profile.objects.get(pk=id)
  return render(request, 'profile.html',{'profile':profile,'projects':projects})

@login_required
def edit_profile(request):
  ida = request.user.id
  profile = Profile.objects.get()
  if request.method == 'POST':
    instance = get_object_or_404(Profile, user=ida)
    form = NewProfileForm(request.POST, request.FILES,instance=instance)
    if form.is_valid():
      form.save()
    return redirect('profile', ida)
  else:
    form = NewProfileForm()
  return render(request, 'edit_profile.html',{'form':form,'profile':profile})

def search(request):
    if 'project' in request.GET and request.GET["project"]:
        search_term = request.GET.get("project")
        searched_projects = project.search_by_title(search_term)
        message = f"{search_term}"
        return render(request, 'search.html',{"message":message,"projects": searched_projects})
    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

class ProfileList(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get(self, request, format=None):
        all_profile = Profiles.objects.all()
        serializers = ProfileSerializer(all_profile, many=True)
        return Response(serializers.data)
    def post(self, request, format=None):
        serializers = ProfileSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
       
class ProjectList(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get(self, request, format=None):
        all_project = Projects.objects.all()
        serializers = ProjectSerializer(all_project, many=True)
        return Response(serializers.data)
    def post(self, request, format=None):
        serializers =  ProjectSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
      
class ProfileDescription(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get_profile(self, pk):
        try:
            return ProfileList.objects.get(pk=pk)
        except ProfileList.DoesNotExist:
            return Http404
    def get(self, request, pk, format=None):
        merch = self.get_profile(pk)
        serializers = ProfileSerializer(merch)
        return Response(serializers.data)

class ProjectDescription(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get_project(self, pk):
        try:
            return ProjectList.objects.get(pk=pk)
        except ProjectList.DoesNotExist:
            return Http404
    def get(self, request, pk, format=None):
        merch = self.get_project(pk)
        serializers = ProjectSerializer(merch)
        return Response(serializers.data)
        
@login_required
def newrating(request,id):
  ida = request.user.id
  idd = id
  current_username = request.user.username
  project = Project.objects.get(pk=id)
  if request.method == 'POST':
    form = NewRatingForm(request.POST)
    if form.is_valid():
      rating = form.save(commit=False)
      design_rating = form.cleaned_data['design']
      usability_rating = form.cleaned_data['usability']
      content_rating = form.cleaned_data['content']
      rating.postername = current_username
      rating.project = Project.objects.get(pk=id)
      rating.save()
    return redirect('project',id)
  else:
    form = NewRatingForm()
  return render(request, 'newrating.html',{'project':project,'form':form,'profile':profile,'idd':idd})