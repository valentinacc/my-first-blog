from django import forms
from .models import Post

# Create your models here.

class PostForm(forms.ModelForm):

	class Meta:
		model = Post
		fields = ('title','text',)

		