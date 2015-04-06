# -*- coding: utf-8 -*-

import traceback

from protoLib.utilsBase import slugify
from protoLib.utils.downloadFile import getFullPath 



def doBPD(modeladmin, request, queryset, parameters):
    """ 
    Business Process Diagram  ( Artefact Based )
    """

#   El QSet viene con la lista de Ids  
    if queryset.count() < 1:
        return  {'success':False, 'message' : 'No record selected' }

    try:
        from graphProcess import GraphProcess 
        gModel = GraphProcess()
    
        gModel.getDiagramDefinition( queryset  )
        dotData = gModel.generateDotModel( )

#   Recorre los registros selccionados   
    except Exception as e:
        traceback.print_exc()
        return  {'success':False, 'message' : 'Load error' }
        pass


#   Genera el archvivo dot     
    fileName = 'bp_' + slugify( queryset[0].code ) + '.dot'
    fullPath = getFullPath( request, fileName )
 
    fo = open( fullPath , "wb")
    fo.write( dotData.encode('utf-8'))
    fo.close()
 
    try:
        import pygraphviz
        fileNamePdf = fileName.replace( '.dot', '.pdf') 
        fullPathPdf = getFullPath( request, fileNamePdf )
 
        graph = pygraphviz.AGraph( fullPath )
        graph.layout( prog= 'dot' )
        graph.draw( fullPathPdf, format ='pdf')
 
        fileName = fileNamePdf
    except ImportError:
        pass

    return  {'success':True , 'message' : fileName,  'fileName' : fileName }


 
def doRaiMenu(modeladmin, request, queryset, parameters):
    """ 
    Genera el menu de rai 
    """

#   El QSet viene con la lista de Ids  
    if queryset.count() < 1:
        return  {'success':False, 'message' : 'No record selected' }

    from buildRaiMenu import doBuildRaiMenu
    doBuildRaiMenu( request, queryset )


    # TODO add returnMsg
    return {'success':True, 'message' : 'Ok' }

