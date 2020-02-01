from django import forms
 
class password_reset(forms.Form):
   Email = forms.EmailField()
   def __str__(self):
       return self.Email