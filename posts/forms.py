from django import forms
from django.forms import widgets
from .models import Post, Comment

 
class AddPostForm(forms.ModelForm):
    class Meta :
        model = Post
        fields = ('body','category',)

        widgets = {
            'body':forms.Textarea(attrs={
                'class' :'form-control' ,
            }),
            'category':forms.Select(attrs={
                'class' :'form-control' ,
            }),
        }
        
        error_messages = {
            'body': {
                'required': 'این فیلد اجباری است'
            }
        }



class EditPostForm(forms.ModelForm):
    class Meta :
        model = Post
        fields = ('body','category',)

        widgets = {
            'body':forms.Textarea(attrs={
                'class' :'form-control' ,
            }),
            'category':forms.Select(attrs={
                'class' :'form-control' ,
            }),
        }
        
        error_messages = {
            'body': {
                'required': 'این فیلد اجباری است'
            }
        }



class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        widgets = {
            'body':forms.Textarea(attrs={
                'class' :'form-control' ,
                'rows' : "3"
            }),
        }
        labels = {
            'body' : '',
        }
        error_messages = {
            'body': {
                'required': 'این فیلد اجباری است'
            }
        }



class AddReplyForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        widgets = {
            'body':forms.Textarea(attrs={
                'class' :'form-control' ,
            }),
        }
        
