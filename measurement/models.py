from django.db import models


class Sensor(models.Model):
    title = models.CharField(max_length=150)
    discription = models.CharField(max_length=300)


class Measurement(models.Model):
    sensor_id = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    temperature = models.IntegerField()
    create_at = models.DateTimeField(auto_now_add=True)

