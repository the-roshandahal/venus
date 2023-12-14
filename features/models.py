from autoslug import AutoSlugField
from django.db import models
from django.contrib.auth.models import User

class CompanySetup(models.Model):
    data_set = models.CharField(max_length=200)
    logo = models.ImageField(upload_to="logos",verbose_name="White Logo (236*65)")

    company_name = models.CharField(max_length=255)

    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    address = models.CharField(max_length=200)

    opening_hours = models.CharField(max_length=200)
    
    facebook_url = models.URLField(null=True,blank=True)
    instagram_url = models.URLField(null=True,blank=True)
    youtube_url = models.URLField(null=True,blank=True)

    created = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.data_set
    class Meta:
        verbose_name_plural = "01. Company Setup" 



class Contact(models.Model):
    name = models.TextField()
    email = models.TextField()
    contact = models.TextField()
    subject = models.TextField(null=True, blank=True)
    message = models.TextField()
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "05. Contact"




class Blog(models.Model):
    title = models.CharField(max_length=200)
    blog = models.TextField()
    image = models.ImageField(upload_to="blogs_images/",verbose_name="Blog Image (800*460)")
    slug = AutoSlugField(populate_from='title', unique=True)
    created = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = "06. Blogs" 


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to="projects_images/",verbose_name="Project Image (1200*800)")
    slug = AutoSlugField(populate_from='title', unique=True)
    created = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = "06. Projects" 

class Partner(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="partner_images/",verbose_name="Project Image (220*150)")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "06. Partners" 


class Slider(models.Model):
    heading = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to="slider_images/",verbose_name="Project Image (1920*900)")
    def __str__(self):
        return self.heading
    class Meta:
        verbose_name_plural = "06. Slider" 



# class HomeContent(models.Model):
#     data_set = models.CharField(max_length=200)

#     header_heading = models.CharField(max_length=150)
#     header_text = models.TextField()
#     header_image = models.ImageField(upload_to="home_images/", verbose_name="Header Image (585*335)")
#     header_button_text = models.CharField(max_length=100)
#     header_button_url = models.URLField()

#     service_title = models.CharField(max_length=255)

#     bottom_title = models.CharField(max_length=150)
#     bottom_sub_title = models.CharField(max_length=150)
#     bottom_text = models.TextField()
#     bottom_image = models.ImageField(upload_to="home_images/", verbose_name="Bottom Image (570*465)")


#     years_of_experience = models.IntegerField()
#     countries = models.FloatField()
#     employees = models.IntegerField()
#     clients = models.IntegerField()
#     def __str__(self):
#         return self.data_set
#     class Meta:
#         verbose_name_plural = "02.Home Page Content" 



# class AboutPageContent(models.Model):
#     data_set = models.CharField(max_length=200)

#     title = models.CharField(max_length=150)
#     title_description = models.TextField()
#     title_image = models.ImageField(upload_to="about_images/", null=True, blank=True,verbose_name="Image (470*450)")


#     sub_title = models.CharField(max_length=150)
#     sub_text = models.TextField()

#     why_us = models.TextField()
    
#     mission = models.TextField()
#     vision = models.TextField()
#     goal = models.TextField()
#     def __str__(self):
#         return self.data_set
#     class Meta:
#         verbose_name_plural = "03.About Page Content" 



# class Slider(models.Model):
#     image = models.ImageField(upload_to="slider_images",verbose_name="Image (1920*800)")
#     heading_text = models.CharField(max_length=200) 
#     sub_heading_text = models.CharField(max_length=200) 
#     button_text = models.CharField(max_length=50)
#     button_url = models.URLField()
#     def __str__(self):
#         return self.heading_text
#     class Meta:
#         verbose_name_plural = "04. Slider" 







# class Service(models.Model):
#     service_title = models.CharField(max_length=200)
#     service_description = models.TextField(null=True,blank=True)
#     service_image = models.ImageField(upload_to="Services_images/",verbose_name="Service Image (370*250)")
#     order = models.IntegerField(default=0)
#     slug = AutoSlugField(populate_from='service_title', unique=True)
#     created = models.DateField(auto_now_add=True)
#     def __str__(self):
#         return self.service_title
#     class Meta:
#         verbose_name_plural = "07. Sectors" 



# class ServiceInquiry(models.Model):
#     name = models.CharField(max_length = 255)
#     email = models.CharField(max_length = 255)
#     contact = models.CharField(max_length = 255)
#     message = models.CharField(max_length = 255)
#     service = models.CharField(max_length = 255)
#     created = models.DateField(auto_now_add=True)

#     def __str__(self):
#         return self.name
#     class Meta:
#         verbose_name_plural = "08. Service Inquiry"







# class JobVacancyCategory(models.Model):
#     category_title = models.CharField(max_length=255)

#     def __str__(self):
#         return self.category_title
#     class Meta:
#         verbose_name_plural = "09. Vacancy Category"

# GENDER_CHOICES = (
#     ('male','male'),
#     ('female','female'),
#     ('both','both'),
# )

# class JobVacancy(models.Model):
#     category = models.ForeignKey(JobVacancyCategory, on_delete=models.SET_NULL,null=True,blank=True)
#     job_title = models.CharField(max_length=255)
#     location = models.CharField(max_length=255)
#     salary = models.CharField(max_length=255)
#     qualification = models.CharField(max_length=255)
#     experience = models.CharField(max_length=255)
#     gender = models.CharField(max_length=255,choices = GENDER_CHOICES)
#     openings = models.IntegerField()
#     job_description = models.TextField()
#     job_image = models.ImageField(upload_to="job_images/",verbose_name="Featured Image (270*170)")
#     is_active = models.BooleanField(default=True)
#     created = models.DateTimeField(auto_now_add=True)
#     slug = AutoSlugField(populate_from='job_title', unique=True)

#     def __str__(self):
#         return self.job_title
#     class Meta:
#         verbose_name_plural = "10. Vacancy "




# class JobVacancyInquiry(models.Model):
#     name = models.CharField(max_length = 255)
#     phone = models.CharField(max_length = 255)
#     email = models.CharField(max_length = 255)
#     message = models.CharField(max_length = 255)

#     vacancy = models.CharField(max_length = 255)
#     created = models.DateField(auto_now_add=True)

#     def __str__(self):
#         return self.name
#     class Meta:
#         verbose_name_plural = "11. Demand Inquiry"



# class ServicePageContent(models.Model):
#     data_set = models.CharField(max_length=255, default= 'Click to Edit')
#     service_title = models.TextField()
#     why_chose_us = models.TextField()
#     get_started = models.TextField()    
    
#     def __str__(self):
#         return self.data_set
#     class Meta:
#         verbose_name_plural = "12. Service Page Content"

# class CompanyService(models.Model):
#     service_title = models.CharField(max_length=255, verbose_name="Service title.")
#     service_description = models.TextField()
#     order = models.IntegerField(default=0)


#     def __str__(self):
#         return self.service_title
#     class Meta:
#         verbose_name_plural = "13. Services"