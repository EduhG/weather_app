from __future__ import unicode_literals

from django.db import models


class Temperature(models.Model):
    """
    Temperatures database model
    The __repr__ method returns an object representaion of the model
    The to_json function returns a json representation of the model
    """

    date_time = models.DateField()
    temp = models.FloatField()

    def __repr__(self):
        return "<Temperature(id='%s', date_time='%s', temp='%s')>" % (
            self.id, self.date_time, self.temp)

    def to_json(self):
        return dict(
            date_time=self.date_time.strftime('%d/%m/%Y'),
            temp=self.temp
        )
