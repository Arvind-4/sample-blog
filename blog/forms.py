from blog.models import Blog, Comments



from django import forms

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'description', 'tags', 'draft']