from django.db import models

class Board(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    options_month = [
        ('ENE','Enero'),
        ('FEB','Febrero'),
        ('MAR','Marzo'),
        ('ABR','Abril'),
        ('MAY','Mayo'),
        ('JUN','Junio'),
        ('JUL','Julio'),
        ('AGO','Agosto'),
        ('SEP','Septiembre'),
        ('OCT','Octubre'),
        ('NOV','Noviembre'),
        ('DIC','Diciembre'),
    ]
    month = models.CharField(max_length=20, choices=options_month, default='ENE')

