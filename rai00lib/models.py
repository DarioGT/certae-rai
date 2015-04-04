# -*- coding: utf-8 -*-

# This is an auto-generated model module by CeRTAE SoftMachine v13.12dgt
# for model : "rai"
# You'll have to do the following manually to clean this up:
#     * Add specific procedures  (WFlow)

from django.db import models
from protoLib.models import ProtoModel
from protoLib.utilsBase import slugify
from protoLib.fields import JSONField, JSONAwareManager


CONCEPTS = [(s, s) for s in ('ARTEFACT', 'CAPACITY', 'REQUIREMENT')]
BASE_TYPES = [(s, s) for s in ('string', 'text', 'bool', 'int', 'decimal', 'combo', 'date', 'time')]


class RaiType(ProtoModel):
    """ 
    Definicion de los tipos segun las 3 categorias ( capacidades, artefactos, exigencias )
    """
    concept = models.CharField(blank= False, null= False, max_length= 11, choices= CONCEPTS )
    ctype = models.CharField(blank= False, null= False, max_length= 200)

    category = models.CharField(max_length=50, blank=True, null=True)
    description  = models.TextField(blank = True, null = True)

    def __unicode__(self):
        return slugify(self.concept + '.' + self.ctype)

    class Meta:
        unique_together = ('concept', 'ctype')



class RaiAttribute(ProtoModel):
    """ 
    Propiedades segun cada tipo de concepto 
    """
    rtype = models.ForeignKey('RaiType', blank=False, null=False)
    code = models.CharField(blank=False, null=False, max_length=200)

    """baseType, prpLength:  Caracteristicas generales q definen el campo """
    baseType = models.CharField(blank=True, null=True, max_length=50, choices=BASE_TYPES, default='string')
    prpLength = models.IntegerField(blank=True, null=True)
    prpScale = models.IntegerField(blank=True, null=True)

    """vType : validation type ( formatos predefinidos email, .... ) """
    vType = models.CharField(blank=True, null=True, max_length=50, choices=BASE_TYPES, default='string')

    """prpDefault: Puede variar en cada instancia """ 
    prpDefault = models.CharField(blank=True, null=True, max_length=50)
    
    """prpChoices:  Lista de valores CSV ( idioma?? ) """ 
    prpChoices = models.TextField(blank=True, null=True)

    description = models.TextField(blank=True, null=True)

    """isRequired: tiene q ver con el llenado de datos"""
    isRequired = models.BooleanField(default=False)

    """isSensitive: Should increase security level """  
    isSensitive = models.BooleanField(default=False)

    class Meta:
        unique_together = ('rtype', 'code' )

    def __unicode__(self):
        return slugify( self.rtype.concept + '.' + self.rtype.ctype + '.' + self.code)      

    unicode_sort = ('rtype', 'code',)



class RaiDomain(ProtoModel):
    code = models.CharField(blank= False, null= False, max_length= 200)
    description = models.TextField(blank = True, null = True)

    class Meta:
        unique_together = ( 'code', )

    def __unicode__(self):
        return slugify( self.code)      

    unicode_sort = ('code',)




class RaiModel(models.Model):
    """ Tabla de base para los diferentes tipos de conceptos de rai,  las instancias 
    tendran cada una su propia tabla q heredara de esta, 
    La llamada al menu se hara con el la tabla se hara con :type, este parametro ira 
    a la seleccion de la tabla,  para la definicion del modelo se buscaran los campos q corresponden 
    a la definicion del tipo  
    """

    code = models.CharField( max_length=200, null=False, blank=False)
    domain  = models.ForeignKey('RaiDomain', blank= False, null= False )
    rtype = models.ForeignKey('RayType', blank=False, null=False)

    description = models.TextField(blank = True, null = True)


    """ Guarda la definicion de campos leida de RaiAttribute """
    info = JSONField(default={})
    objects = JSONAwareManager(json_fields=['info'])
    protoExt = { 'jsonField' : 'info' }


    # Indica q debe leer los campos de la forma al momento de configurar el modelo o cargar campos en la meta
    _getFields = True


    def __unicode__(self):
        return slugify( self.rtype.code + '.' + self.code )  


    class Meta:
        abstract = True


    def getfields(self, *args, **kwargs):
        """ Busca los campos en RaiAttribute y los retorna para completar el modelo 
        """ 
        return {'campo1' : 'xxx'}

