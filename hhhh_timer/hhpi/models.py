from django.db import models

# This class defines rider information

class Rider(models.Model):
    id = models.IntegerField(primary_key=True)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    bib_id = models.IntegerField()
    course_id = models.IntegerField()

    def __unicode__(self):
	return unicode(self.bib_id)

# This class defines checkpoint information

class Checkpoint(models.Model):
    id = models.IntegerField(primary_key=True)
    bib_id = models.IntegerField()
    course_id = models.IntegerField()
    cp_id = models.IntegerField()
    cp_timestamp = models.TimeField('timecheck', auto_now_add=True)