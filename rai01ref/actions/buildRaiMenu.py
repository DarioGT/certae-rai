# -*- coding: utf-8 -*-

import json

from protoLib.models import CustomDefinition, ProtoDefinition 
from protoLib.protoAuth import getUserProfile

DOCUMENTS = ( 'ARTEFACT', 'CAPACITY', 'REQUIREMENT' ) 


def doBuildRaiMenu( request, queryset ):
    """ 
    Genera el menu de rai 
    """

    currentUser = request.user
    userProfile = getUserProfile(currentUser, 'getMenu', '') 
    viewIcon = 'icon-1'

#-- Generacion de menu 

    lMenu = {}
    Ix = 0
    for document in DOCUMENTS:
        lMenu[ document ] = {
            'text': document.lower()  ,
            'expanded': True ,
            'index':  Ix,
            'iconCls': 'rai_{}'.format( document[:3].lower())  ,
            'leaf': False, 
            'children': [],
        }
        Ix +=1 

    for pDoc in queryset:

        viewCode = 'rai01ref.{0}.{1}'.format( pDoc.document , str( pDoc.pk ) ).lower()
        model_dict = {
            'viewCode': viewCode, 
            'text': pDoc.dtype ,
            'index': Ix ,
            'iconCls': viewIcon ,
            'leaf': True,
        }
        Ix +=1 

        lMenu[ pDoc.document ]['children'].append( model_dict  )  


        # Borra la anterior definicion  
        ProtoDefinition.objects.filter( code=viewCode ).delete()


#-- Lectura de la Db ------------------------------------------------------------- 

    viewCode = '__menu'
    protoDef = CustomDefinition.objects.get_or_create(
           code=viewCode, smOwningTeam=userProfile.userTeam,
           defaults={'active': False, 'code' : viewCode, 'smOwningTeam' : userProfile.userTeam }
           )[0]

    # El default solo parece funcionar al insertar en la Db
    if not protoDef.active :  
        return  {'success':False, 'message' : 'Menu not found' }

    menuData = json.loads( protoDef.metaDefinition  ) 


#-- Update de la Db ------------------------------------------------------------- 

    try:
        raiMenu = menuData[0]
        if unicode( raiMenu['text'] ) == unicode( 'RAI MENU' ): 
            raiMenu = menuData.pop(0)
    except : pass 


    raiMenu = {
            'text': 'RAI MENU'  ,
            'expanded': False ,
            'index':  0,
            'leaf': False, 
            'children': [],
        }

    for raiDoc in lMenu.itervalues():
        raiMenu['children'].append( raiDoc )

    menuData.insert( 0, raiMenu)

    protoDef.metaDefinition = json.dumps( menuData )
    protoDef.save()


    return  {'success':False, 'message' : 'Menu not found' }

