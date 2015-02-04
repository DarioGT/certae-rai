# -*- coding: utf-8 -*-

# This is an auto-generated model module by CeRTAE SoftMachine v13.12dgt
# for model : "inspectdb"


from django.db import models
from protoLib.models import ProtoModel
from protoLib.utilsBase import slugify

class Evenement(ProtoModel):
    typeevenement = models.CharField(blank=True, null=True, max_length=255)
    evenement = models.CharField(blank=True, null=True, max_length=255)

    def __unicode__(self):
        return slugify( self.evenement ) 

               
class Processus(ProtoModel):
    processus = models.CharField(blank=True, null=True, max_length=255)
    description = models.CharField(blank=True, null=True, max_length=255)

    def __unicode__(self):
        return slugify( self.processus ) 

class Service(ProtoModel):
    services = models.CharField(blank=True, null=True, max_length=255)
    description = models.CharField(blank=True, null=True, max_length=255)
    responsable = models.CharField(blank=True, null=True, max_length=255)
    volumetrie = models.CharField(blank=True, null=True, max_length=255)
    nature = models.CharField(blank=True, null=True, max_length=255)
    niveauxservice = models.CharField(blank=True, null=True, max_length=255)
    applications = models.CharField(blank=True, null=True, max_length=255)

    def __unicode__(self):
        return slugify( self.services ) 

class Actionterr(ProtoModel):
    actionterr = models.CharField(blank=True, null=True, max_length=255)
    description = models.CharField(blank=True, null=True, max_length=255)

    def __unicode__(self):
        return slugify( self.actionterr ) 

class ServiceEv(ProtoModel):
    k_services = models.CharField(blank=True, null=True, max_length=255)
    k_evenement = models.CharField(blank=True, null=True, max_length=255)

    service = models.ForeignKey(Service, blank=True, null=True)
    evenement = models.ForeignKey(Evenement, blank=True, null=True)

    def __unicode__(self):
        return slugify(str(self.service) + '.' + str(self.evenement))

class ServiceProc(ProtoModel):
    k_services = models.CharField(blank=True, null=True, max_length=255)
    k_processus = models.CharField(blank=True, null=True, max_length=255)

    service = models.ForeignKey(Service, blank=True, null=True)
    processus = models.ForeignKey(Processus, blank=True, null=True)

    def __unicode__(self):
        return slugify(str(self.service) + '.' + str(self.processus))


class ServiceAt(ProtoModel):
    k_services = models.CharField(blank=True, null=True, max_length=255)
    k_actionterr = models.CharField(blank=True, null=True, max_length=255)

    service = models.ForeignKey(Service, blank=True, null=True)
    actionterr = models.ForeignKey(Actionterr, blank=True, null=True)

    def __unicode__(self):
        return slugify(str(self.service) + '.' + str(self.actionterr))

class Servicecanal(ProtoModel):
    k_services = models.CharField(blank=True, null=True, max_length=255)

    web = models.CharField(blank=True, null=True, max_length=255)
    telephone = models.CharField(blank=True, null=True, max_length=255)
    personnel = models.CharField(blank=True, null=True, max_length=255)
    courrier = models.CharField(blank=True, null=True, max_length=255)

    service = models.ForeignKey(Service, blank=True, null=True)

    def __unicode__(self):
        return slugify(str(self.service))
