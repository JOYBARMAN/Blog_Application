from django import forms
from .models import Post,Category

cat=Category.objects.all().values_list('name','name')

choice=[]
for item in cat:
	choice.append(item)


class PostForm(forms.ModelForm):
	class Meta:
		model=Post
		fields=('title','author','category','body',)

		widgets={
		'title':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Blog Title'}),
		'author':forms.Select(attrs={'class':'form-control'}),
		'category':forms.Select(choices=choice,attrs={'class':'form-control'}),
		'body':forms.Textarea(attrs={'class':'form-control'}),
		}


class UpdateForm(forms.ModelForm):
	class Meta:
		model=Post
		fields=('title','category','body')

		widgets={
		'title':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Blog Title'}),
		'category':forms.Select(choices=choice,attrs={'class':'form-control'}),
		'body':forms.Textarea(attrs={'class':'form-control'}),
		}


