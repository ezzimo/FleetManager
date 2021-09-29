from django import forms
from django.contrib.auth.forms import (
    AuthenticationForm,
    PasswordResetForm,
    SetPasswordForm,
    UserChangeForm,
    UserCreationForm,
)
from django.core.exceptions import ValidationError
from django.forms import fields
from django.utils.translation import gettext_lazy as _

from .models import Address, User


class UserAddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = [
            "phone",
            "address_line_1",
            "address_line_2",
            "town_city",
            "postcode",
            "delivery_instructions",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["phone"].widget.attrs.update({"class": "form-control mb-2 account-form", "Placeholder": "phone"})
        self.fields["address_line_1"].widget.attrs.update(
            {"class": "form-control mb-2 account-form", "Placeholder": "address "}
        )
        self.fields["address_line_2"].widget.attrs.update(
            {"class": "form-control mb-2 account-form", "Placeholder": "address"}
        )
        self.fields["town_city"].widget.attrs.update(
            {"class": "form-control mb-2 account-form", "Placeholder": "town city"}
        )
        self.fields["postcode"].widget.attrs.update(
            {"class": "form-control mb-2 account-form", "Placeholder": "postcode"}
        )
        self.fields["delivery_instructions"].widget.attrs.update(
            {"class": "form-control mb-2 account-form", "Placeholder": "delivery instructions"}
        )


class UserLoginForm(AuthenticationForm):

    username = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control mb-3", "placeholder": "Username", "id": "login-username"})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Password",
                "id": "login-pwd",
            }
        )
    )


class UserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = "__all__"


class UserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = "__all__"


class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(label=_("Enter First name"), min_length=4, max_length=50, help_text="Required")
    last_name = forms.CharField(label=_("Enter Last name"), min_length=4, max_length=50, help_text="Required")
    email = forms.EmailField(
        max_length=100, help_text=_("Required"), error_messages={"Required": "Sorry, you will need an email"}
    )
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repeat password", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "email",
        )

    def clean_username(self):
        first_name = self.cleaned_data["first_name"].lower()
        last_name = self.cleaned_data["last_name"].lower()
        r = User.objects.filter(first_name=first_name, last_name=last_name)
        if r.count():
            raise forms.ValidationError("Name already exists")
        return first_name + " " + last_name

    def clean_password2(self):
        # cd = self.cleaned_data
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise ValidationError("Les mots de passes sont differents")

        return password2
        # if cd["password"] != cd["password2"]:
        # raise forms.ValidationError("Passwords do not match.")
        # return cd["password2"]

    def clean_email(self):
        email = self.cleaned_data["email"]
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Please use another Email, that is already taken")
        return email

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["first_name"].widget.attrs.update({"class": "form-control mb-3", "placeholder": "First name"})
        self.fields["last_name"].widget.attrs.update({"class": "form-control mb-3", "placeholder": "Last name"})
        self.fields["email"].widget.attrs.update(
            {"class": "form-control mb-3", "placeholder": "E-mail", "name": "email", "id": "id_email"}
        )
        self.fields["password"].widget.attrs.update({"class": "form-control mb-3", "placeholder": "Password"})
        self.fields["password2"].widget.attrs.update({"class": "form-control", "placeholder": "Repeat Password"})


class UserEditForm(forms.ModelForm):

    email = forms.EmailField(
        label="Account email (can not be changed)",
        max_length=200,
        widget=forms.EmailInput(
            attrs={"class": "form-control mb-3", "placeholder": "email", "id": "form-email", "readonly": "readonly"}
        ),
    )
    first_name = forms.CharField(
        label="User name",
        min_length=4,
        max_length=50,
        widget=forms.TextInput(
            attrs={"class": "form-control mb-3", "placeholder": "first name", "id": "form-firstname"}
        ),
    )
    last_name = forms.CharField(
        label="User name",
        min_length=4,
        max_length=50,
        widget=forms.TextInput(
            attrs={"class": "form-control mb-3", "placeholder": "Last name", "id": "form-lastname"}
        ),
    )
    mobile = forms.CharField(
        label="User mobile 1",
        min_length=4,
        max_length=50,
        widget=forms.TextInput(
            attrs={"class": "form-control mb-3", "placeholder": "mobile number", "id": "form-mobile_1"}
        ),
    )
    registration_number = forms.CharField(
        label="Company name",
        min_length=4,
        max_length=50,
        widget=forms.TextInput(
            attrs={"class": "form-control mb-3", "placeholder": "Company name", "id": "form-company_name"}
        ),
    )
    cni = forms.CharField(
        label="Company ice",
        min_length=4,
        max_length=50,
        widget=forms.TextInput(attrs={"class": "form-control mb-3", "placeholder": "Company ice", "id": "form-ice"}),
    )
    picture = forms.FileField(
        label="website",
        widget=forms.FileInput(attrs={"class": "form-control mb-3", "placeholder": "Website", "id": "form-website"}),
    )
    birth_date = forms.DateField(
        label="User mobile 2",
        widget=forms.DateInput(
            attrs={"class": "form-control mb-3", "placeholder": "mobile number", "id": "form-mobile_2"}
        ),
    )
    birth_city = forms.ChoiceField(
        label="User landline",
        widget=forms.Select(
            attrs={"class": "form-control mb-3", "placeholder": "landline number", "id": "form-landline"}
        ),
    )
    cnss_registration_number = forms.CharField(
        label="Company ice",
        min_length=4,
        max_length=50,
        widget=forms.TextInput(attrs={"class": "form-control mb-3", "placeholder": "Company ice", "id": "form-ice"}),
    )
    recruitment_date = forms.DateField(
        label="website",
        widget=forms.DateInput(attrs={"class": "form-control mb-3", "placeholder": "Website", "id": "form-website"}),
    )
    city_id = forms.ChoiceField(
        label="User mobile 2",
        widget=forms.Select(
            attrs={"class": "form-control mb-3", "placeholder": "mobile number", "id": "form-mobile_2"}
        ),
    )
    rib_bank = forms.IntegerField(
        label="User landline",
        widget=forms.NumberInput(
            attrs={"class": "form-control mb-3", "placeholder": "landline number", "id": "form-landline"}
        ),
    )
    bank_address = forms.CharField(
        label="Company ice",
        min_length=4,
        max_length=50,
        widget=forms.TextInput(attrs={"class": "form-control mb-3", "placeholder": "Company ice", "id": "form-ice"}),
    )
    bank_id = forms.ChoiceField(
        label="website",
        widget=forms.Select(attrs={"class": "form-control mb-3", "placeholder": "Website", "id": "form-website"}),
    )
    driving_licence = forms.ImageField(
        label="Driver Licence",
        widget=forms.FileInput(
            attrs={"class": "form-control mb-3", "placeholder": "driving licence", "id": "form-driving_licence"}
        ),
    )
    driver_licence_expiration_date = forms.DateField(
        label="Driver Licence Exp",
        widget=forms.DateInput(
            attrs={
                "class": "form-control mb-3",
                "placeholder": "Driver Licence Exp",
                "id": "form-driver_licence_expiration_date",
            }
        ),
    )
    glasses = forms.BooleanField(
        label="Driver Use Glasses",
        widget=forms.RadioSelect(attrs={"class": "form-control mb-3", "id": "form-mobile_2"}),
    )
    glasses_certificat = forms.FileField(
        label="Driver Glasse Certificate",
        widget=forms.FileInput(
            attrs={
                "class": "form-control mb-3",
                "placeholder": "Driver Glasse Certificate",
                "id": "form-glasses_certificat",
            }
        ),
    )

    class Meta:
        model = User
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["first_name"].required = True
        self.fields["last_name"].required = True
        self.fields["email"].required = True
        self.fields["mobile"].required = True


class PwdResetForm(PasswordResetForm):
    email = forms.EmailField(
        max_length=254,
        widget=forms.TextInput(attrs={"class": "form-control mb-3", "placeholder": "Email", "id": "form-email"}),
    )

    def clean_email(self):
        email = self.cleaned_data["email"]
        usr = User.objects.filter(email=email)
        if not usr:
            raise forms.ValidationError("Unfortunatley we can not find that email address")
        return email


class PwdResetConfirmForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label="New password",
        widget=forms.PasswordInput(
            attrs={"class": "form-control mb-3", "placeholder": "New Password", "id": "form-newpass"}
        ),
    )
    new_password2 = forms.CharField(
        label="Repeat password",
        widget=forms.PasswordInput(
            attrs={"class": "form-control mb-3", "placeholder": "New Password", "id": "form-new-pass2"}
        ),
    )
