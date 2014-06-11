/*
Copyright(c) 2012 CeRTAE
*/
Ext.define("RAI.model.Raccordement",{extend:"Ext.data.Model",fields:["id","sourceId","sourceName","targetId","targetName","modelId","modelName"]});Ext.define("RAI.model.ElementDonnee",{extend:"Ext.data.Model",fields:["id","attributeName","entityId","entityName"]});Ext.define("RAI.store.Raccordements",{extend:"Ext.data.Store",requires:["RAI.model.Raccordement","Ext.data.proxy.Memory","Ext.data.reader.Json"],autoLoad:false,sorters:["sourceName","targetName","modelName"],groupField:"modelName",constructor:function(a){var b=this;a=a||{};b.callParent([Ext.apply({model:"RAI.model.Raccordement",storeId:"RaccordementStore",proxy:{type:"ajax",api:{read:"rai/listRaccordement/",create:"rai/createRaccordement/",destroy:"rai/deleteRaccordement/"},reader:{type:"json",root:"raccordements",successProperty:"success"},pageParam:false,startParam:false,limitParam:false}},a)])}});Ext.define("RAI.store.ElementsDonneeLeftGrid",{extend:"Ext.data.Store",requires:["RAI.model.ElementDonnee","Ext.data.proxy.Memory","Ext.data.reader.Json"],sorters:["attributeName","entityName"],groupField:"entityName",constructor:function(a){var b=this;a=a||{};b.callParent([Ext.apply({model:"RAI.model.ElementDonnee",storeId:"ElementsDonneeLGStore",proxy:{type:"memory",reader:{type:"json"}}},a)])}});Ext.define("RAI.store.ElementsDonneeRightGrid",{extend:"Ext.data.Store",requires:["RAI.model.ElementDonnee","Ext.data.proxy.Memory","Ext.data.reader.Json"],sorters:["attributeName","entityName"],groupField:"entityName",constructor:function(a){var b=this;a=a||{};b.callParent([Ext.apply({model:"RAI.model.ElementDonnee",storeId:"ElementsDonneeRGStore",proxy:{type:"memory",reader:{type:"json"}}},a)])}});Ext.define("RAI.view.raccordement.GridPanel",{extend:"Ext.panel.Panel",alias:"widget.raccordementGridPanel",itemId:"raccordementGridPanel",layout:{type:"hbox",align:"stretch",padding:5},defaults:{flex:1},initComponent:function(){var a=this;Ext.applyIf(a,{items:[{xtype:"gridpanel",store:"ElementsDonneeLeftGrid",itemId:"gridLeft",iconCls:"icon-grid",frame:true,features:[Ext.create("Ext.grid.feature.Grouping",{groupHeaderTpl:'Entity: {name} ({rows.length} Item{[values.rows.length > 1 ? "s" : ""]})'})],selModel:Ext.create("Ext.selection.CheckboxModel",{injectCheckbox:"last"}),columns:[{text:"Attribute",flex:1,dataIndex:"attributeName"},{text:"Entity",flex:1,dataIndex:"entityName"}],listeners:{afterrender:function(){this.setLoading(true)}}},{xtype:"gridpanel",store:"ElementsDonneeRightGrid",itemId:"gridRight",iconCls:"icon-grid",frame:true,features:[Ext.create("Ext.grid.feature.Grouping",{groupHeaderTpl:'Entity: {name} ({rows.length} Item{[values.rows.length > 1 ? "s" : ""]})'})],selModel:Ext.create("Ext.selection.CheckboxModel",{injectCheckbox:"last"}),columns:[{text:"Attribute",flex:1,dataIndex:"attributeName"},{text:"Entity",flex:1,dataIndex:"entityName"}],listeners:{afterrender:function(){this.setLoading(true)}}}],fbar:[{type:"button",text:"Raccorder",itemId:"btRaccorderElements"}]});a.callParent(arguments)}});Ext.define("RAI.view.raccordement.ListRaccordement",{extend:"Ext.grid.Panel",alias:"widget.listRaccordementGrid",itemId:"listRaccordementGrid",frame:true,store:"Raccordements",title:"Raccordement",modelRaccordement:null,columns:[{text:"Element raccordant",flex:1,dataIndex:"sourceName"},{text:"Element raccorde",flex:1,dataIndex:"targetName"},{text:"Modele de raccordement",flex:1,dataIndex:"modelName"}],initComponent:function(){this.dockedItems=[{xtype:"toolbar",items:["->",{iconCls:"x-tool-rowDel",text:_SM.__language.Text_Delete_Button,action:"delete"}]}];this.callParent(arguments)},getModelRaccordement:function(){return this.modelRaccordement},setModelRaccordement:function(a){this.modelRaccordement=a}});Ext.define("RAI.view.raccordement.MainWindow",{extend:"Ext.window.Window",alias:"widget.raccordementMainWindow",itemId:"raccordementMainWindow",layout:{type:"vbox",align:"stretch"},selectedModel:null,maximizable:true,modal:true,height:600,width:800,initComponent:function(){var a=this;Ext.applyIf(a,{items:[{xtype:"raccordementGridPanel",flex:1},{xtype:"listRaccordementGrid",selModel:Ext.create("Ext.selection.CheckboxModel",{injectCheckbox:"last"}),flex:1}]});a.addEvents("openModeleRaccordement");a.on("beforeshow",function(){this.fireEvent("openModeleRaccordement",a)});a.callParent(arguments)},getActiveModel:function(){return this.selectedModel[0]}});Ext.define("RAI.controller.RaccordementController",{extend:"Ext.app.Controller",stores:["ElementsDonneeRightGrid","ElementsDonneeLeftGrid","Raccordements"],views:["raccordement.MainWindow","raccordement.GridPanel","raccordement.ListRaccordement"],refs:[{ref:"mainWindow",selector:"#raccordementMainWindow"}],createAjaxRequest:function(b,f,d,c,a,e){Ext.Ajax.request({url:b,method:f,params:d,jsonData:c,success:a,failure:e})},getReadRaccordementOperation:function(){var a=new Ext.data.Operation({action:"read",params:{modelId:this.getMainWindow().getActiveModel()}});return a},syncListRaccordement:function(b){var a=this;b.getStore().sync({success:function(d,c){b.getStore().load(a.getReadRaccordementOperation())},failure:function(d,c){Ext.Msg.alert("Error","Failed to sync raccordement")},scope:this})},loadDataToGridPanel:function(b,a){b.setTitle(a.modelName);b.getStore().loadData(a.attributes)},removeMask:function(a){a.getComponent("gridLeft").setLoading(false);a.getComponent("gridRight").setLoading(false)},openModeleRaccordement:function(c){var b,a=this;b=c.getActiveModel();params={modelID:b};successFunction=function(e){var h=e.responseText;var g=Ext.JSON.decode(h);if(g.models){var f=a.getMainWindow().down("panel");a.loadDataToGridPanel(f.getComponent("gridLeft"),g.models[0]);a.loadDataToGridPanel(f.getComponent("gridRight"),g.models[1]);a.removeMask(f);if(g.models[2]){var d=a.getMainWindow().getComponent("listRaccordementGrid");d.setModelRaccordement(g.models[2].nomModele);d.getStore().loadData(g.models[2].raccordements)}}};failureFunction=function(d){a.removeMask(a.getMainWindow().down("panel"));Ext.Msg.alert("Error","Error on openModeleRaccordement method")};this.createAjaxRequest("rai/getModeleRaccordement/","GET",params,null,successFunction,failureFunction)},createRaccordementAttribute:function(a,d,b,c){return Ext.create("RAI.model.Raccordement",{sourceId:b.id,sourceName:b.attributeName,targetId:c.id,targetName:c.attributeName,modelId:d,modelName:a})},raccorderElements:function(l,n,o){var q,m,a,c,p,d,h,g,k=this;q=k.getMainWindow().getComponent("listRaccordementGrid");m=k.getMainWindow().down("panel");a=m.getComponent("gridLeft").getSelectionModel().getSelection();c=m.getComponent("gridRight").getSelectionModel().getSelection();p=[];d=false;for(h=0;h<a.length;h++){for(g=0;g<c.length;g++){var b=k.createRaccordementAttribute(q.getModelRaccordement(),k.getMainWindow().getActiveModel(),a[h].data,c[g].data);var f=q.getStore().findBy(function(e,i){if(e.get("modelName")===q.getModelRaccordement()&&e.get("sourceName")===b.data.sourceName&&e.get("targetName")===b.data.targetName){return true}return false});if(f===-1){p.push({model:k.getMainWindow().getActiveModel(),source:a[h].data,target:c[g].data});q.getStore().insert(0,b);d=true}}}if(d){k.syncListRaccordement(q)}},deleteRaccordement:function(c){var b=this;var a=b.getMainWindow().getComponent("listRaccordementGrid");var d=a.getSelectionModel().getSelection();a.getStore().remove(d);b.syncListRaccordement(a)},init:function(a){this.control({window:{openModeleRaccordement:this.openModeleRaccordement},"#btRaccorderElements":{click:this.raccorderElements},"listRaccordementGrid button[action=delete]":{click:this.deleteRaccordement}})}});Ext.application({name:"RAI",paths:{RAI:"static/js/rai"},extend:"ProtoUL.Application",controllers:["RAI.controller.RaccordementController"]});