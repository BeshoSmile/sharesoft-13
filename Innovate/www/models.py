from django.db import models
from django.utils.timezone import utc
import datetime
from datetime import timedelta
# Create your models here.

#album table defines elements of the ablum with the title,descr and date of the pictures regarding that album
class Album(models.Model):
	title = models.CharField(max_length=100)
	description = models.CharField(max_length=500, null=True)
	event_date = models.DateField(null=True)


#table pics defines the pictures regarding one ablum (no limit)
class Pictures(models.Model):
    picture1 = models.ImageField(upload_to='media', blank=True)
    album = models.ForeignKey(Album)


class AblumCover(models.Model):
	picture = models.ForeignKey(Pictures)
	album = models.ForeignKey(Album)

class AboutUs(models.Model):
	maintitle=models.CharField(max_length=50)
	title1=models.CharField(max_length=50)
	description1=models.TextField(max_length='1000')
	picture1 = models.ImageField(upload_to='media')
	title2=models.CharField(max_length=50)
	description2=models.TextField(max_length='1000')
	picture2 = models.ImageField(upload_to='media')
	title3=models.CharField(max_length=50)
	description3=models.TextField(max_length='1000')
	picture3 = models.ImageField(upload_to='media')
	title4=models.CharField(max_length=50)
	description4=models.TextField(max_length='1000')
	picture4 = models.ImageField(upload_to='media')
	def __unicode__(self):
	    return str(self.id)+":"+self.maintitle



class video(models.Model):
	youtube_url = models.CharField(max_length='150')
	video_cover = models.ImageField(upload_to='media')
	title = models.CharField(max_length='150')
	director = models.CharField(max_length='50')
	producer = models.CharField(max_length='50')
	photographer = models.CharField(max_length='50')
	number_of_views = models.IntegerField(default='0')
	video_choices = (
		('W', 'Wedding'),
		('P', 'Promo'),
		('D', 'Documentaries'),
	)
	video_genre = models.CharField(max_length=1, choices=video_choices)
	def __unicode__(self):
	    return str(self.id)+":"+self.title


class contact(models.Model):
	email = models.CharField(max_length='100')
	address_line1 = models.CharField(max_length='100')
	address_line2 = models.CharField(max_length='100')
	address_line3 = models.CharField(max_length='100')
	skype_name = models.CharField(max_length='50')
	telephone_number = models.CharField(max_length='100')
	def __unicode__(self):
	    return str(self.id)+":"+self.email


class main_page(models.Model):
	title=models.CharField(max_length='100')
	logo=models.ImageField(upload_to='mainpage')
	lens=models.ImageField(upload_to='mainpage')
	slogan=models.CharField(max_length='100')
	is_active=models.BooleanField(default=False)
	def __unicode__(self):
	    return str(self.id)+":"+self.title

class main_page_moviestrip(models.Model):
	main_page = models.ForeignKey(main_page)
	image=models.ImageField(upload_to='mainpage/moviestrip')
	title=models.CharField(max_length='100')
	def __unicode__(self):
	    return self.title

class radio_ad(models.Model):
	title=models.CharField(max_length='500')
	url = models.TextField(max_length='1000')
	def __unicode__(self):
	    return self.title



class sorl_test(models.Model):
	image=models.ImageField(upload_to='testsorl')

