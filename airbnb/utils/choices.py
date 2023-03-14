from django.db import models


class Gender(models.TextChoices):
    Male = "male", "Male"
    Female = "female", "Female"
    Other = "other, Other"


class Language(models.TextChoices):
    English = "en", "English"
    Korean = "kr", "Korean"


class Currency(models.TextChoices):
    USD = "usd", "USD"
    KRW = "krw", "KRW"


class OrderBy(models.TextChoices):
    Title = "title", "Title"
    Popularity = "-popularity", "Popularity"
    Price = "price", "Price"
    StartDate = "start_date", "Start date"


class PublishedStatus(models.TextChoices):
    Draft = ("draft", "Draft")
    Published = ("published", "Published")


class EnrolledStatus(models.TextChoices):
    Pending = ("pending", "Pending")
    Enrolled = ("enrolled", "Enrolled")
