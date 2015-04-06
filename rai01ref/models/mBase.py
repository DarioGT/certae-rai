# -*- coding: utf-8 -*-


from django.db import models
from protoLib.models import ProtoModel
from protoLib.utilsBase import slugify
from protoLib.fields import JSONField, JSONAwareManager

from protobase.protoRules import  BASE_TYPES, CRUD_TYPES, docProperty2Field


""" Los tipos de documentos son 'ARTEFACT', 'CAPACITY', 'REQUIREMENT'

    COMPOSITION podria corresponder a los arcos entre dos ARTEFACT, 
                dependiendo el tipo de arco los campos podrian ser diferentes, 
                luego el tipo de artefacto determinaria el tipo de arcos q pueda manejar 
                en un proceso pueden ser conexiones, en un modelo relacional puede ser la cardinalidad 

"""

DOCUMENTS = [(s, s) for s in ('ARTEFACT', 'CAPACITY', 'REQUIREMENT')]


class DocType(ProtoModel):
    """ 
    Definicion de los tipos segun las 3 categorias ( capacidades, artefactos, exigencias )
    DGT: 1504 El manejo jerarquico podria ser determinado en el tipo 
        - allowHierarchy,  
        - childTypes  [ lista de tipos permitidos en los hijos ] 
    """
    document = models.CharField(blank= False, null= False, max_length= 11, choices= DOCUMENTS )
    dtype = models.CharField(blank= False, null= False, max_length= 200)

    category = models.CharField(max_length=50, blank=True, null=True)

    notes  = models.TextField(blank = True, null = True)
    description  = models.TextField(blank = True, null = True)

    def __unicode__(self):
        return slugify(self.document + '.' + self.dtype)

    class Meta:
        app_label = 'rai01ref'
        unique_together = ('document', 'dtype')


    protoExt = {
        "actions": [
            { "name": "doRaiMenu" , "selectionMode" : "multiple" },
        ],
        "gridConfig" : {
            "listDisplay": [ "document", "dtype", "description", "__str__",],
            "others": {
                "filtersSet": [
                {
                    "name": "Artefacts",
                    "customFilter": [{
                        "property": "document",
                        "filterStmt": "^ARTERFACT"
                    }]
                },{
                    "name": "Capacities",
                    "customFilter": [{
                        "property": "document",
                        "filterStmt": "^CAPACITY"
                    }]
                },{
                    "name": "Requirements",
                    "customFilter": [{
                        "property": "document",
                        "filterStmt": "^REQUIREMENT"
                    }]
                }
                ],
            }
        }
    }



class DocAttribute(ProtoModel):
    """ 
    Propiedades segun cada tipo de documento 
    DGT: 1504 Si manejara relaciones, podria encadenar diferentes tipos de artefacto 
         - isReference,  referenceDocument 
    """
    docType = models.ForeignKey('DocType', blank=False, null=False)
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

    """isRequired: tiene q ver con el llenado de datos"""
    isRequired = models.BooleanField(default=False)

    """isSensitive: Should increase security level """  
    isSensitive = models.BooleanField(default=False)

    crudType = models.CharField(blank=True, null=True, max_length=20, choices=CRUD_TYPES)
    description = models.TextField(blank=True, null=True)

    class Meta:
        app_label = 'rai01ref'
        unique_together = ('docType', 'code' )

    def __unicode__(self):
        return slugify( str( self.docType ) + '.' + self.code)      

    unicode_sort = ('docType', 'code',)

    protoExt = {
        "gridConfig" : {
            "listDisplay": [ "docType", "code", "description", ],
        }
    }


class Domain(ProtoModel):
    code = models.CharField(blank= False, null= False, max_length= 200)
    description = models.TextField(blank = True, null = True)

    class Meta:
        app_label = 'rai01ref'
        unique_together = ( 'code', )

    def __unicode__(self):
        return slugify( self.code)      

    unicode_sort = ('code',)



class DocModel(ProtoModel):
    """ Tabla de base para los diferentes tipos de documentos de rai02db,  las instancias 
    tendran cada una su propia tabla q heredara de esta, 
    La llamada al menu se hara con el la tabla se hara con :type, este parametro ira 
    a la seleccion de la tabla,  para la definicion del modelo se buscaran los campos q corresponden 
    a la definicion del tipo  
    """

    code = models.CharField( max_length=200, null=False, blank=False)
    domain  = models.ForeignKey('Domain', blank= True, null= True, related_name = '+') 
    dtype = models.CharField(blank= False, null= False, max_length= 200 )

    description = models.TextField(blank = True, null = True)


    """ Guarda la definicion de campos leida de RaiAttribute """
    info = JSONField(default={})
    objects = JSONAwareManager(json_fields=['info'])
    protoExt = { 'jsonField' : 'info' }


    # User Defined Document 
    _uddObject = True
    _jField = 'info'


    def __unicode__(self):
        return slugify( self.dtype + '.' + self.code )  


    class Meta:
        app_label = 'rai01ref'
        abstract = True
        unique_together = ('code',)

    @staticmethod
    def getJfields( dBase, dtype ):
        """ Busca los campos en RaiAttribute y los retorna para completar el modelo 
        """ 

        fDict = {}
        jFields = DocAttribute.objects.filter(docType__document = dBase , docType__dtype = dtype )

        for pProperty in jFields:

            fName  =  slugify( pProperty.code ) 
            fDict[ 'info__' + fName  ] = docProperty2Field( fName, pProperty.__dict__ , 'info'  )

        return fDict
