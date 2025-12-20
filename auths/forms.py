from django import forms
from .models import Auth

class FormularioRegistro(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Ingresar Contraseña',
        'class': 'form-control',
    }))

    confirmar_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Confirmar Contraseña',
        'class': 'form-control',
    }))

    class Meta:
        model= Auth
        fields=['name','lastname','email','phone_number','password'] # Indica que campos se incluiran en el formulario
    
    def __init__(self, *args,**kwargs): # Método constructor de la clase y sus parametros extras 
        super(FormularioRegistro,self).__init__(*args,**kwargs)
        self.fields['name'].widget.attrs['placeholder']= 'ingresar Nombre'
        self.fields['lastname'].widget.attrs['placeholder']= 'Ingresar Apellido'
        self.fields['email'].widget.attrs['placeholder']= 'ingresar Email'
        self.fields['phone_number'].widget.attrs['placeholder']= 'ingresar Telefono'
        for field in self.fields: # agrega a todos los campos la clase form-control de bootstrap
            self.fields[field].widget.attrs['class'] = 'form-control'
                      
    def clean(self):
        limpiar_datos= super(FormularioRegistro, self).clean()
        password= limpiar_datos.get('password')
        confirmar_password= limpiar_datos.get('confirmar_password')

        if password != confirmar_password:
            raise forms.ValidationError(
                "Ups las contraseñas no Coinciden!"
            )

