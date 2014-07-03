# -*- coding: utf-8 -*-

import traceback

from protoLib.utilsBase import slugify
from protoLib.utils.downloadFile import getFullPath



def doFindReplace(modeladmin, request, queryset, parameters):
    """
    find and replace sobre la tabla actual
    parameters   campo,  findText, replaceText
    """

#   El QSet viene con la lista de Ids
    if queryset.count() < 1:
        return  {'success':False, 'message' : 'Multiple selection required'}

    if len(parameters) != 3:
        return  {'success':False, 'message' : 'required: fieldName, findText, replaceText' }

    from protoLib.actions.findReplace import actionFindReplace
    return actionFindReplace(request, queryset, parameters)



def doImportRAI( modeladmin, request, queryset, parameters):

    return doRaiActions( modeladmin, request, queryset, parameters, 'IMPORT' )


def doMatchRAI( modeladmin, request, queryset, parameters):

    return doRaiActions( modeladmin, request, queryset, parameters, 'MATCH' )



def doRaiActions( modeladmin, request, queryset, parameters, action ):
    """
    funcion para importar modelos realizados en OMS ( Open Model Spher )
    """


    def doBaseImport( cOMS ):
    
        try:
            cOMS.doImport()
            cOMS.doFkMatch( )
    
        except Exception as e:
            traceback.print_exc()
            return  {'success':False, 'message' : 'Load error' }


#   El QSet viene con la lista de Ids
    if queryset.count() != 1:
        return  {'success':False, 'message' : 'No record selected' }

    from protoLib.protoAuth import getUserProfile
    userProfile = getUserProfile( request.user, 'prototype', '' )

    from rai.actions.domAffimportOMS import importOMS_RAI
    cOMS = importOMS_RAI( userProfile, queryset[0]  )

    if action == 'IMPORT':

        actionFiles = request.POST.get( "actionFiles", {} )

    #   load and validate xml file
        try:

            import os
            fileName = actionFiles[ 'file']

            cOMS.loadFile( fileName  )

        except Exception as e:
            traceback.print_exc()
            return  {'success':False, 'message' : 'Load error' }


        # Return and continue 
        from threading import Thread
        t = Thread(target= doBaseImport, args=( cOMS,))
        t.daemon = True 
        t.start()

        return {'success':True, 'message' :  'runing ...' }


    elif action == 'MATCH':
        try:
            cOMS.doRacMatch()

    #   Recorre los registros selccionados
        except Exception as e:
            traceback.print_exc()
            return  {'success':False, 'message' : 'Load error' }


        return {'success':True, 'message' :  'runing ...' }

    

def doMatrixRacc( modelAdmin,request, queryset, detKeys, parameters):

    from rai.actions.racMatrix import doMatrixRaccordement

    try:
        doMatrixRaccordement(  modelAdmin, request, queryset, detKeys, parameters  )
    except Exception as e:
        traceback.print_exc()
        return  {'success':False, 'message' : 'Generation error' }
    return {'success':True, 'message' :  'Ok ...' }




def doAddModel(modeladmin, request, queryset, parameters):
    """
    Adicion de entidades a modelos existentes
    """

#   selectionMode = multi
    if queryset.count() < 1:
        return  {'success':False, 'message' : 'Multiple selection required'}

#   parameters [ entite_mod, entite_mod_id  ]
    if len(parameters) != 2:
        return  {'success':False, 'message' : 'required: entite_mod, entite_mod_id' }

    from rai.actions.entiteAddModel import extractModel

    try:
        extractModel(request, queryset, parameters)
    except Exception as e:
        traceback.print_exc()
        return  {'success':False, 'message' : 'Extraction error' }

    return {'success':True, 'message' :  'Ok ...' }
