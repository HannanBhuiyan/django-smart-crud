from tkinter import Widget
from turtle import width
from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
 
     class Meta:
          model = Product
          fields = '__all__'
         
     
 
     # def __init__(self, *args, **kwargs):
     #      super().__init__(*args, **kwargs)
     #      self.fields['product_title'].label = 'Product Title'
     #      self.fields['product_title'].widget.attrs.update(
     #           {
     #                'class': 'form-control',
     #                'placeholder' : 'Enter Product Title'
     #           })

     #      self.fields['product_desc'].label = 'Product Description'
     #      self.fields['product_desc'].widget.attrs.update({
     #                'class' : 'form-control',
     #                'rows' : 5,
     #                'placeholder' : 'Enter Product Description'
     #           })
     
     # product_price = forms.FloatField(widget=forms.TextInput(
     #           attrs={'class' : 'form-control', 'placeholder' : 'Enter Price'}),
     #           label = "Product Price"
     #           )
     # product_varient = forms.CharField(
     #           widget=forms.TextInput(attrs ={'class' : 'form-control', 'placeholder' : 'Enter Varient'}),
     #           label = "Product Varient",
     #           error_messages={'required' : 'Product varient is required !!!'},
     #           )
               
     # in_stock = forms.IntegerField(
     #      widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Enter stock number'}),
     #      label = "Stock Quantity",
     #      error_messages= {'required' : 'Stock Quantity is required !!!'}
     #      )
              
          
          
               



     
     # product_title = forms.CharField(
     #      widget=forms.TextInput(
     #           attrs={
     #                'class' : 'form-control', 
     #                'Placeholder' : 'Product Title',

     #                }),
     #           label="Product Title"
     #      )
 

     