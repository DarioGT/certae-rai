# -*- coding: utf-8 -*-

import traceback

from protoLib.utilsBase import slugify


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
    from rai02db.actions.domAffairesActions import doRaiActions
    return doRaiActions( modeladmin, request, queryset, parameters, 'IMPORT' )


def doMatchRAI( modeladmin, request, queryset, parameters):
    from rai02db.actions.domAffairesActions import doRaiActions
    return doRaiActions( modeladmin, request, queryset, parameters, 'MATCH' )


def doMatrixRacc( modelAdmin,request, queryset, detKeys, parameters):
    from rai02db.actions.racMatrix import doMatrixRaccordement

    try:
        return doMatrixRaccordement(  modelAdmin, request, queryset, detKeys, parameters  )
    except Exception as e:
        traceback.print_exc()
        return  {'success':False, 'message' : 'Generation error' }



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

    from rai02db.actions.entiteAddModel import extractModel

    try:
        extractModel(request, queryset, parameters)
    except Exception as e:
        traceback.print_exc()
        return  {'success':False, 'message' : 'Extraction error' }

    return {'success':True, 'message' :  'Ok ...' }