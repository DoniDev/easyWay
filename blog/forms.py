from django import forms
from . models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # fields = '__all__'
        fields = ['title', 'body', 'slug', 'tags', 'image']

    def clean_title(self):
        title = self.cleaned_data['title']
        instance = self.instance
        print(instance)
        qs = Post.objects.filter(title__iexact=title)
        if instance is not None:
            qs = qs.exclude(pk=instance.pk)   # id = instance.id

        if qs.exists():
            raise forms.ValidationError("This title has already been used try again")
        return title



class PostDeleteForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = []


