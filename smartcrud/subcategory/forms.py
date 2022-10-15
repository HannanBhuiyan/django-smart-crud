from django import forms

from account.models import Subcategory


class SubcategoryForm(forms.ModelForm):
     class Meta:
          model = Subcategory
          fields = '__all__'


     subcategory_name = forms.CharField(error_messages={'required' : 'Subcategory is require !!!'})
      
 
