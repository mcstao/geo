from django.contrib.gis.db import models

class Place(models.Model):
    location = models.PointField()

    def __str__(self):
        return f"({self.location.x}, {self.location.y})"


class Review(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    text = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"({self.place})"