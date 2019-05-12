from django.db import models
from django.conf import settings
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.core.validators import RegexValidator

USERNAME_REGX = '^[a-zA-Z0-9.+-_]*$'

STATES = (
    ("Andaman and Nicobar Islands", "Andaman and Nicobar Islands"),
    ("Andhra Pradesh", "Andhra Pradesh",),
    ("Arunachal Pradesh", "Arunachal Pradesh"),
    ("Bihar", "Bihar"),
    ("Chandigarh", "Chandigarh"),
    ("Chhattisgarh", "Chhattisgarh"),
    ("Dadra and Nagar Haveli", "Dadra and Nagar Haveli"),
    ("Daman and Diu", "Daman and Diu"),
    ("Delhi NCR", "Delhi NCR",),
    ("Goa", "Goa",),
    ("Gujarat", "Gujarat",),
    ("Haryana", "Haryana",),
    ("Himachal Pradesh", "Himachal Pradesh",),
    ("Jammu and Kashmir", "Jammu and Kashmir",),
    ("Jharkhand", "Jharkhand",),
    ("Karnataka", "Karnataka",),
    ("Kerala", "Kerala",),
    ("Lakshadweep", "Lakshadweep",),
    ("Madhya Pradesh", "Madhya Pradesh",),
    ("Maharashtra", "Maharashtra",),
    ("Manipur", "Manipur",),
    ("Meghalaya", "Meghalaya",),
    ("Mizoram", "Mizoram",),
    ("Nagaland", "Nagaland",),
    ("Puducherry", "Puducherry",),
    ("Punjab", "Punjab",),
    ("Rajasthan", "Rajasthan",),
    ("Sikkim", "Sikkim",),
    ("Tamil Nadu", "Tamil Nadu",),
    ("Tripura", "Tripura",),
    ("Uttar Pradesh", "Uttar Pradesh",),
    ("Uttarakhand", "Uttarakhand",),
    ("West Bengal", "West Bengal",),
)


class MyUserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            username=username,
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            username,
            email,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    username = models.CharField(max_length=64, unique=True, validators=[RegexValidator(regex=USERNAME_REGX, message="Username only contain A-Z,a-z,0-9 or . _ + - $", code="Invalid Username")])
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phone_regex = RegexValidator(regex=r'^\d{10}$', message="Please Enter Correct Mobile Number...")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=False, unique=True)
    state = models.CharField(max_length=50, choices=STATES)
    date_of_birth = models.DateTimeField(auto_now=False)
    balance = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    bonus = models.DecimalField(max_digits=4, decimal_places=2, default=25)
    widhdrawable_balance = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    match_played = models.IntegerField(default=0)
    total_wins = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username


class OTPVerification(models.Model):
    mobile_no = models.CharField(max_length=10)
    otp_send_detail = models.CharField(max_length=64)
    sent_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.mobile_no


class OTPVerificationEmail(models.Model):
    email = models.CharField(max_length=100)
    otp_send = models.CharField(max_length=10)
    sent_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email

# # class UsersProfileInfo(models.Model):
# #     user = models.OneToOneField(User, on_delete=models.CASCADE)
# #     balance = models.DecimalField(max_digits=8, decimal_places=2)
# #     phone_regex = RegexValidator(regex=r'^\d{10}$', message="Please Enter Correct Mobile Number...")
# #     phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
# #     state = models.CharField(max_length=50, choices=STATES)
# #     date_of_birth = models.DateField(auto_now=False)

# #     def __str__(self):
# #         return self.user.username





























# from django.db import models
# from django.contrib.auth.models import User
# # from django.contrib.auth.models import User
# from django.core.validators import RegexValidator
# from django.contrib.auth.models import (
#     BaseUserManager, AbstractBaseUser
# )

# # from django.db.models.signals import post_save
# # from django.dispatch import receiver

# # STATES = (
# #     ('ny', 'New York'),
# #     ('sm', 'Santa Monica')
# # )

# USERNAME_REGEX = '^[a-zA-Z0-9.$+-_]*'


# class MyUserManager(BaseUserManager):
#     def create_user(self, username, email, password=None):
#         """
#         Creates and saves a User with the given email, date of
#         birth and password.
#         """
#         if not email:
#             raise ValueError('Users must have an email address')

#         user = self.model(
#             username=username,
#             email=self.normalize_email(email),
#         )

#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, username, email, password):
#         """
#         Creates and saves a superuser with the given email, date of
#         birth and password.
#         """
#         user = self.create_user(
#             username,
#             email,
#             password=password,
#         )
#         user.is_admin = True
#         user.is_staff = True
#         user.save(using=self._db)
#         return user


# class MyUser(AbstractBaseUser):
#     username = models.CharField(max_length=64, unique=True, validators=[RegexValidator(
#             regex=USERNAME_REGEX,
#             message="Username can only Contain Alphanumeric and . + - _ $ Characters.",
#             code="invali_username"
#         )])
#     email = models.EmailField(
#         verbose_name='email address',
#         max_length=255,
#         unique=True,
#     )
#     balance = models.DecimalField(max_digits=8, decimal_places=2, default=0)

#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#     is_admin = models.BooleanField(default=False)

#     objects = MyUserManager()

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['username', 'email']

#     def __str__(self):
#         return self.email

#     def has_perm(self, perm, obj=None):
#         "Does the user have a specific permission?"
#         # Simplest possible answer: Yes, always
#         return True

#     def has_module_perms(self, app_label):
#         "Does the user have permissions to view the app `app_label`?"
#         # Simplest possible answer: Yes, always
#         return True

#     # @property
#     # def is_staff(self):
#     #     "Is the user a member of staff?"
#     #     # Simplest possible answer: All admins are staff
#     #     return self.is_admin


# STATES = (
#     ("Andaman and Nicobar Islands", "Andaman and Nicobar Islands"),
#     ("Andhra Pradesh", "Andhra Pradesh",),
#     ("Arunachal Pradesh", "Arunachal Pradesh"),
#     ("Bihar", "Bihar"),
#     ("Chandigarh", "Chandigarh"),
#     ("Chhattisgarh", "Chhattisgarh"),
#     ("Dadra and Nagar Haveli", "Dadra and Nagar Haveli"),
#     ("Daman and Diu", "Daman and Diu"),
#     ("Delhi NCR", "Delhi NCR",),
#     ("Goa", "Goa",),
#     ("Gujarat", "Gujarat",),
#     ("Haryana", "Haryana",),
#     ("Himachal Pradesh", "Himachal Pradesh",),
#     ("Jammu and Kashmir", "Jammu and Kashmir",),
#     ("Jharkhand", "Jharkhand",),
#     ("Karnataka", "Karnataka",),
#     ("Kerala", "Kerala",),
#     ("Lakshadweep", "Lakshadweep",),
#     ("Madhya Pradesh", "Madhya Pradesh",),
#     ("Maharashtra", "Maharashtra",),
#     ("Manipur", "Manipur",),
#     ("Meghalaya", "Meghalaya",),
#     ("Mizoram", "Mizoram",),
#     ("Nagaland", "Nagaland",),
#     ("Puducherry", "Puducherry",),
#     ("Punjab", "Punjab",),
#     ("Rajasthan", "Rajasthan",),
#     ("Sikkim", "Sikkim",),
#     ("Tamil Nadu", "Tamil Nadu",),
#     ("Tripura", "Tripura",),
#     ("Uttar Pradesh", "Uttar Pradesh",),
#     ("Uttarakhand", "Uttarakhand",),
#     ("West Bengal", "West Bengal",),
# )


# # class UsersProfileInfo(models.Model):
# #     user = models.OneToOneField(User, on_delete=models.CASCADE)
# #     balance = models.DecimalField(max_digits=8, decimal_places=2)
# #     phone_regex = RegexValidator(regex=r'^\d{10}$', message="Please Enter Correct Mobile Number...")
# #     phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
# #     state = models.CharField(max_length=50, choices=STATES)
# #     date_of_birth = models.DateField(auto_now=False)

# #     def __str__(self):
# #         return self.user.username
