# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    phone_number = models.TextField(max_length=255, null=True, blank=True)
    email = models.TextField(max_length=255, null=True, blank=True)
    function = models.TextField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Projects(models.Model):

    #__Projects_FIELDS__
    project_code = models.CharField(max_length=255, null=True, blank=True)
    project_name = models.TextField(max_length=255, null=True, blank=True)
    project_description = models.TextField(max_length=255, null=True, blank=True)
    project_start = models.DateTimeField(blank=True, null=True, default=timezone.now)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)

    #__Projects_FIELDS__END

    class Meta:
        verbose_name        = _("Projects")
        verbose_name_plural = _("Projects")


class Customer(models.Model):

    #__Customer_FIELDS__
    customer_domain = models.TextField(max_length=255, null=True, blank=True)
    customer_email = models.TextField(max_length=255, null=True, blank=True)
    customer_id = models.CharField(max_length=255, null=True, blank=True)
    customer_name = models.TextField(max_length=255, null=True, blank=True)
    customer_phone = models.CharField(max_length=255, null=True, blank=True)
    domains = models.TextField(max_length=255, null=True, blank=True)
    ip_ranges = models.TextField(max_length=255, null=True, blank=True)

    #__Customer_FIELDS__END

    class Meta:
        verbose_name        = _("Customer")
        verbose_name_plural = _("Customer")


class Monitoring(models.Model):

    #__Monitoring_FIELDS__
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    darkweb = models.BooleanField()
    domains = models.ForeignKey(Customer, on_delete=models.CASCADE)
    emails = models.TextField(max_length=255, null=True, blank=True)
    ip_ranges = models.ForeignKey(Customer, on_delete=models.CASCADE)

    #__Monitoring_FIELDS__END

    class Meta:
        verbose_name        = _("Monitoring")
        verbose_name_plural = _("Monitoring")


class Incidents(models.Model):

    #__Incidents_FIELDS__
    incident_id = models.TextField(max_length=255, null=True, blank=True)
    title = models.TextField(max_length=255, null=True, blank=True)
    description = models.TextField(max_length=255, null=True, blank=True)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    priority = models.CharField(max_length=255, null=True, blank=True)
    severity_rating = models.TextField(max_length=255, null=True, blank=True)
    date_discovered = models.DateTimeField(blank=True, null=True, default=timezone.now)
    date_alert = models.DateTimeField(blank=True, null=True, default=timezone.now)
    detection_source = models.TextField(max_length=255, null=True, blank=True)
    affected_systems = models.TextField(max_length=255, null=True, blank=True)
    affected_users = models.TextField(max_length=255, null=True, blank=True)
    incident_ongoing = models.BooleanField()
    mitre_tactic = models.CharField(max_length=255, null=True, blank=True)
    iocs = models.CharField(max_length=255, null=True, blank=True)
    action_taken = models.TextField(max_length=255, null=True, blank=True)
    origin = models.CharField(max_length=255, null=True, blank=True)
    report = models.TextField(max_length=255, null=True, blank=True)

    #__Incidents_FIELDS__END

    class Meta:
        verbose_name        = _("Incidents")
        verbose_name_plural = _("Incidents")



#__MODELS__END
