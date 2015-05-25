#
# File: trends/models.py
#
# Description: 
#
from django.db import models

class Tag(models.Model):
    """ 
    Tag Model: PCS Archived Tag information 
    
    Tag archived in PCS, therefore available for archive trending and 
    can be added into a predefined trend.
    """
    SERVER_CHOICES = (
        ('CP','OSCPA'),
        ('CR','OSCRA'),
        ('P1','OSP1A'),
        ('R1','OSR1A'),
        ('P2','OSP2A'),
        ('R2','OSR2A'),
        ('P3','OSP3A'),
        ('R3','OSR3A'),
    )
    UNIT_CHOICES = (
        ('Flow', (
                ('m3/h', 'm3/h'),
            )
        ),
        ('Percent', (
                ('%', '% (Percent)'),
            )
        ),
        ('Time', (
                ('h', 'Hours'),
                ('s', 'Seconds'),
            )
        ),
        ('Pressure', (
                ('kPa', 'Kilo Pascal'),
            )
        ),
    )
    server = models.CharField(max_length=2, choices=SERVER_CHOICES)
    tag_name = models.CharField(unique=True, max_length=128)
    min_trend_default = models.DecimalField(max_digits=10, decimal_places=1)
    max_trend_default = models.DecimalField(max_digits=10, decimal_places=1)
    tag_units = models.CharField(max_length=8, choices=UNIT_CHOICES)
    
    def __str__(self):
        return self.tag_name
    
class Trend(models.Model):
    """ 
    Trend: PCS Predefined trend 
 
    Contains a group of archived tags, shown in one predefined trend.
    It has some global properties associated.
    """
    
    trend_name = models.CharField(unique=True, max_length=128)
    time_base = models.IntegerField()
    time_factor = models.IntegerField()
    trend_thickness = models.IntegerField()
    
    def __str__(self):
        return self.trend_name

class TagInTrend(models.Model):
    """
    TagInTrend: pre-defined
    """
    COLOUR_CHOICES = (
        ('Bk','Black'),
        ('Bu','Blue'),
        ('M','Magenta'),
        ('R','Red'),
        ('Gy','Grey'),
        ('C','Cyan'),
        ('Gn','Green'),
        ('O','Orange'),
    )
    trend = models.ForeignKey(Trend)
    tag = models.ForeignKey(Tag)
    description = models.CharField(max_length=128)
    min_trend = models.DecimalField(max_digits=10, decimal_places=1)
    max_trend = models.DecimalField(max_digits=10, decimal_places=1)
    colour = models.CharField(max_length=2, choices=COLOUR_CHOICES)
    
    def __str__(self):
        return "{0}.{1}".format(self.trend.trend_name, self.tag.tag_name)