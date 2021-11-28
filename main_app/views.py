from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Pet, Photo
import uuid
import boto3
#const variables
S3_BASE_URL = 'https://s3.us-west-2.amazonaws.com/'
BUCKET = 'whoseyourhuman'

# Create your views here.
class Home(LoginView):
  template_name = "home.html"

def about(request):
  return render(request, 'about.html')

def pets_index(request):
  pets=Pet.objects.filter(user=request.user)
  return render(request, 'pets/index.html', {'pets':pets})

def pets_detail(request, pet_id):
  pet=Pet.objects.get(id=pet_id)
  return render(request, 'pets/detail.html', {'pet' : pet})




class PetCreate(CreateView):
  model = Pet
  fields = ['name', 'breed', 'parent1', "parent2", 'play_date', 'insta', 'email',"phone_number", 'description']
  
  # This inherited method is called when a
  # valid cat form is being submitted
  def form_valid(self, form):
    # Assign the logged in user (self.request.user)
    form.instance.user = self.request.user  # form.instance is the cat
    # Let the CreateView do its job as usual
    return super().form_valid(form)

class PetUpdate(UpdateView):
  model = Pet
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = ['name', 'breed', 'parent1', "parent2", 'play_date', 'insta', 'email',"phone_number", 'description']

class PetDelete(DeleteView):
  model = Pet
  success_url = '/pets/'


def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in
      login(request, user)
      return redirect('pets_index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)


def add_photo(request, pet_id):
  # photo-file will be the "name" attribute on the <input type="file">
  photo_file = request.FILES.get('photo-file', None)
  if photo_file:
    s3 = boto3.client('s3')
    # need a unique "key" for S3 / needs image file extension too
		# uuid.uuid4().hex generates a random hexadecimal Universally Unique Identifier
    # Add on the file extension using photo_file.name[photo_file.name.rfind('.'):]
    key = uuid.uuid4().hex + photo_file.name[photo_file.name.rfind('.'):]
    # just in case something goes wrong
    try:
      s3.upload_fileobj(photo_file, BUCKET, key)
      # build the full url string
      url = f"{S3_BASE_URL}{BUCKET}/{key}"
      # we can assign to cat_id or cat (if you have a cat object)
      photo = Photo(url=url, pet_id=pet_id)
      # Remove old photo if it exists
      pet_photo = Photo.objects.filter(pet_id=pet_id)
      if pet_photo.first():
        pet_photo.first().delete()
      photo.save()
    except Exception as err:
      print('An error occurred uploading file to S3: %s' % err)
  return redirect('pets_detail', pet_id=pet_id)

  # name = models.CharField(max_length=100)
  # breed = models.CharField(max_length=100)
  # description = models.TextField(max_length=250)
  # parent1 = models.CharField(max_length=100)
  # parent2 = models.CharField(max_length=100)
  # insta= models.CharField(max_length=100)
  # phone_number = models.IntegerField()
  # play_date=models.BooleanField()
  # email= models.EmailField(max_length=254)
  # user = models.ForeignKey(User, on_delete=models.CASCADE)