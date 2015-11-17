from django import forms
from main.models import People, Planet, Starship, Vehicles, Species
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, HTML, Layout, Div
from crispy_forms.bootstrap import FormActions
# from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# from main.models import CustomUser

# The People Edit Form


class PeopleEditForm(forms.ModelForm):
    class Meta:
        model = People
        fields = '__all__'
        #['NAME', 'county', 'state']

    def __init__(self, *args, **kwargs):
        super(PeopleEditForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = '/people_edit/%s' % self.instance.pk
        self.helper.layout.append(
            FormActions(
                Submit('save_changes', "Save Changes", css_class="btn-primary")
                )
            )

# The Planet Edit Form


class PlanetEditForm(forms.ModelForm):
    class Meta:
        model = Planet
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(PlanetEditForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = '/planet_edit/%s' % self.instance.pk
        self.helper.layout.append(
            FormActions(
                Submit('save_changes', "Save Changes", css_class="btn-primary")
                )
            )

# The Starship Edit Form


class StarshipEditForm(forms.ModelForm):
    class Meta:
        model = Starship
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(StarshipEditForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = '/starship_edit/%s' % self.instance.pk
        self.helper.layout.append(
            FormActions(
                Submit('save_changes', "Save Changes", css_class="btn-primary")
                )
            )


# The Vehicle Edit Form

class VehicleEditForm(forms.ModelForm):
    class Meta:
        model = Vehicles
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(VehicleEditForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = '/vehicle_edit/%s' % self.instance.pk
        self.helper.layout.append(
            FormActions(
                Submit('save_changes', "Save Changes", css_class="btn-primary")
                )
            )

# The Species Edit Form


class SpeciesEditForm(forms.ModelForm):
    class Meta:
        model = Species
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(SpeciesEditForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = '/species_edit/%s' % self.instance.pk
        self.helper.layout.append(
            FormActions(
                Submit('save_changes', "Save Changes", css_class="btn-primary")
                )
            )
# class CustomUserCreationForm(UserCreationForm):
#     def __init__(self, *args, **kwargs):
#         super(CustomUserCreationForm, self).__init__(*args, **kwargs)

#     class Meta:
#         model = CustomUser
#         fields = ("email",)


# # class CustomUserChangeForm(UserChangeForm):
#     def __init__(self, *args, **kwargs):
#         super(CustomUserChangeForm, self).__init__(*args, **kwargs)
#         del self.fields['username']

#     class Meta:
#         model = CustomUser
#         fields = ['email']
#         exclude = ['username']


# # class UserSignUp(forms.Form):
#     name = forms.CharField(required=True)
#     email = forms.CharField(required=True)
#     password = forms.CharField(required=True, forms.PasswordInput())


# # class UserLogin(forms.Form):
#     email = forms.CharField(required=True)
#     password = forms.CharField(required=True, widget=forms.PasswordInput())
