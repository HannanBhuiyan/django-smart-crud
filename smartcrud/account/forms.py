from django import forms
from account.models import Category, Subcategory


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'  
        
        
    category_name = forms.CharField(error_messages={'required' : 'Category Name field is required !!!!'})
    category_slug = forms.CharField(error_messages={'required': 'Category slug field is required !!! '})
        

    
 