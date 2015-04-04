# -*- coding: utf-8 -*-


from django.db import models
from protoLib.models import ProtoModel
from protoLib.utilsBase import slugify
from protoLib.fields import JSONField, JSONAwareManager


""" Los tipos de documentos son 'ARTEFACT', 'CAPACITY', 'REQUIREMENT'

    COMPOSITION podria corresponder a los arcos entre dos ARTEFACT, 
                dependiendo el tipo de arco los campos podrian ser diferentes, 
                luego el tipo de artefacto determinaria el tipo de arcos q pueda manejar 
                en un proceso pueden ser conexiones, en un modelo relacional puede ser la cardinalidad 

"""

CONCEPTS = [(s, s) for s in ('ARTEFACT', 'CAPACITY', 'REQUIREMENT')]
BASE_TYPES = [(s, s) for s in ('string', 'text', 'bool', 'int', 'decimal', 'combo', 'date', 'time')]


class DocumentType(ProtoModel):
    """ 
    Definicion de los tipos segun las 3 categorias ( capacidades, artefactos, exigencias )
    DGT: 1504 El manejo jerarquico podria ser determinado en el tipo 
        - allowHierarchy,  
        - childTypes  [ lista de tipos permitidos en los hijos ] 
    """
    concept = models.CharField(blank= False, null= False, max_length= 11, choices= CONCEPTS )
    ctype = models.CharField(blank= False, null= False, max_length= 200)

    category = models.CharField(max_length=50, blank=True, null=True)

    notes  = models.TextField(blank = True, null = True)
    description  = models.TextField(blank = True, null = True)

    def __unicode__(self):
        return slugify(self.concept + '.' + self.ctype)

    class Meta:
        app_label = 'rai01ref'
        unique_together = ('concept', 'ctype')



class DocAttribute(ProtoModel):
    """ 
    Propiedades segun cada tipo de concepto 
    DGT: 1504 Si manejara relaciones, podria encadenar diferentes tipos de artefacto 
         - isReference,  referenceDocument 
    """
    documentType = models.ForeignKey('DocumentType', blank=False, null=False)
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
        app_label = 'rai01ref'
        unique_together = ('documentType', 'code' )

    def __unicode__(self):
        return slugify( str( self.documentType ) + '.' + self.code)      

    unicode_sort = ('documentType', 'code',)



class Domain(ProtoModel):
    code = models.CharField(blank= False, null= False, max_length= 200)
    description = models.TextField(blank = True, null = True)

    class Meta:
        app_label = 'rai01ref'
        unique_together = ( 'code', )

    def __unicode__(self):
        return slugify( self.code)      

    unicode_sort = ('code',)



class RaiModel(ProtoModel):
    """ Tabla de base para los diferentes tipos de conceptos de rai,  las instancias 
    tendran cada una su propia tabla q heredara de esta, 
    La llamada al menu se hara con el la tabla se hara con :type, este parametro ira 
    a la seleccion de la tabla,  para la definicion del modelo se buscaran los campos q corresponden 
    a la definicion del tipo  
    """

    code = models.CharField( max_length=200, null=False, blank=False)
    domain  = models.ForeignKey('Domain', blank= False, null= False )
    documentType = models.ForeignKey('DocumentType', blank=False, null=False)

    description = models.TextField(blank = True, null = True)


    """ Guarda la definicion de campos leida de RaiAttribute """
    info = JSONField(default={})
    objects = JSONAwareManager(json_fields=['info'])
    protoExt = { 'jsonField' : 'info' }


    # Indica q debe leer los campos de la forma al momento de configurar el modelo o cargar campos en la meta
    _getFields = True


    def __unicode__(self):
        return slugify( self.documentType.code + '.' + self.code )  


    class Meta:
        app_label = 'rai01ref'
        abstract = True
        unique_together = ('code',)


    def getfields(self, *args, **kwargs):
        """ Busca los campos en RaiAttribute y los retorna para completar el modelo 
        """ 
        return {'campo1' : 'xxx'}

