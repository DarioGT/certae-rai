# -*- coding: utf-8 -*-

# Import Database class

import traceback


def doRaiActions( modeladmin, request, queryset, parameters, action ):
    """
    funcion para importar modelos realizados en OMS ( Open Model Spher )
    """

    # Background function 
    def doBaseImport( cOMS ):
    
        try:
            cOMS.doImport()
            cOMS.doFkMatch( )
    
        except Exception as e:
            traceback.print_exc()


#   El QSet viene con la lista de Ids
    if queryset.count() != 1:
        return  {'success':False, 'message' : 'No record selected' }

    from protoLib.protoAuth import getUserProfile
    userProfile = getUserProfile( request.user, 'prototype', '' )

    from rai02db.actions.domAffimportOMS import importOMS_RAI
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

