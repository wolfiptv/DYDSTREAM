# -*- coding: utf8 -*-
import urllib,urllib2,sys,re,xbmcplugin,xbmcgui,xbmcaddon,datetime,os,json,base64,plugintools
import xml.etree.ElementTree as ElementTree
reload(sys)
sys.setdefaultencoding('utf8')
SKIN_VIEW_FOR_MOVIES="515"
addonDir = plugintools.get_runtime_path()
global auth
background = "YmFja2dyb3VuZC5wbmc="
defaultlogo = "ZGVmYXVsdGxvZ28ucG5n"
noposter = "bm9wb3N0ZXIuanBn"
addonxml = "YWRkb24ueG1s"
addonpy = "ZGVmYXVsdC5weQ=="
icon = "aWNvbi5wbmc="
fanart = "ZmFuYXJ0LnBuZw=="
def run():
    global index
    global livetv
    global vodlink
    global serieslink
    global infolink
    global host
    global LOAD_LIVE
    global ADDON
    global crtparent
    global version
    global password
    global usuario
    global puerto
    global brand
    version = int(get_live("Mg=="))
    usuario=plugintools.get_setting(get_live("dXN1YXJpbw=="))
    password=plugintools.get_setting(vod_channels("cGFzc3dvcmQ="))
    host=plugintools.get_setting(vod_channels("aG9zdA=="))
    puerto=plugintools.get_setting(get_live("cHVlcnRv"))
    crtparent=plugintools.get_setting(sync_data("Y3J0cGFyZW50"))
    index = get_live("WHRyZWFtLUNvZGVzIA==")
    brand = get_live("Sm9NeVNvbiBQbHVz")
    LOAD_LIVE = os.path.join( plugintools.get_runtime_path() , get_live("cmVzb3VyY2Vz") , vod_channels("aW1n") )
    ADDON = os.path.join( plugintools.get_runtime_path() )
    plugintools.log(index+get_live("U3RhcnRpbmcgdXA="))
    livetv = get_live("JXM6JXMvZW5pZ21hMi5waHA/dXNlcm5hbWU9JXMmcGFzc3dvcmQ9JXMmdHlwZT1nZXRfbGl2ZV9jYXRlZ29yaWVz")%(host,puerto,usuario,password)
    vodlink = vod_channels("JXM6JXMvZW5pZ21hMi5waHA/dXNlcm5hbWU9JXMmcGFzc3dvcmQ9JXMmdHlwZT1nZXRfdm9kX2NhdGVnb3JpZXM=")%(host,puerto,usuario,password)
    serieslink = vod_channels("JXM6JXMvZW5pZ21hMi5waHA/dXNlcm5hbWU9JXMmcGFzc3dvcmQ9JXMmdHlwZT1nZXRfc2VyaWVzX2NhdGVnb3JpZXM=")%(host,puerto,usuario,password)
    infolink = vod_channels("JXM6JXMvcGFuZWxfYXBpLnBocD91c2VybmFtZT0lcyZwYXNzd29yZD0lcw==")%(host,puerto,usuario,password)
    params = plugintools.get_params()
    if(usuario == "" or password == ""):
        xbmcgui.Dialog().notification("DYD STREAM PRO Addon", "Configura el plugin.")
        xbmcaddon.Addon().openSettings()
        exit(0)
    if params.get("action") is None:
        main(params)
    else:
        action = params.get("action")
        exec action+"(params)"
    plugintools.close_item_list()
def main(params):
    plugintools.log(index+vod_channels("TWFpbiBNZW51")+repr(params))
    check_channels()
    if not host:
       plugintools.open_settings_dialog()
    channels = auth()
    login_accept()
    if channels == 1:
       plugintools.log(index+vod_channels("TG9naW4gU3VjY2Vzcw=="))
       plugintools.add_item( action=vod_channels("ZXhlY3V0ZV9haW5mbw=="),   title=vod_channels("TUkgQ1VFTlRB") , thumbnail=os.path.join(LOAD_LIVE,vod_channels("dXNlci1pbmZvLnBuZw==")) , fanart=os.path.join(LOAD_LIVE,vod_channels("YmFja2dyb3VuZC5wbmc=")) , folder=True )
       plugintools.add_item( action=vod_channels("c2VjdXJpdHlfY2hlY2s="),  title=vod_channels("VFY=") , thumbnail=os.path.join(LOAD_LIVE,vod_channels("dHYucG5n")) , fanart=os.path.join(LOAD_LIVE,vod_channels("YmFja2dyb3VuZC5wbmc=")) , folder=True )
       plugintools.add_item( action=vod_channels("ZGV0ZWN0X21vZGlmaWNhdGlvbg=="),   title=vod_channels("UEVMw41DVUxBUw==") , thumbnail=os.path.join(LOAD_LIVE,vod_channels("cGVsaWN1bGFzLnBuZw==")) , fanart=os.path.join(LOAD_LIVE,vod_channels("YmFja2dyb3VuZC5wbmc=")) , folder=True )
       plugintools.add_item( action=vod_channels("c2VyaWVzX2NhdGVnb3JpZXM="),   title=vod_channels("U0VSSUVT") , thumbnail=os.path.join(LOAD_LIVE,vod_channels("c2VyaWVzLnBuZw==")) , fanart=os.path.join(LOAD_LIVE,vod_channels("YmFja2dyb3VuZC5wbmc=")) , folder=True )
       plugintools.add_item( action=vod_channels("bGljZW5zZV9jaGVjaw=="), title=vod_channels("Q09ORklHVVJBQ0nDk04=") , thumbnail=os.path.join(LOAD_LIVE,vod_channels("Y29uZmlnLnBuZw==")) , fanart=os.path.join(LOAD_LIVE,vod_channels("YmFja2dyb3VuZC5wbmc=")), folder=False )
       plugintools.set_view( plugintools.LIST )
    else:
       plugintools.log(index+vod_channels("TG9naW4gaW5jb3JyZWN0bw=="))
       plugintools.message(vod_channels("TG9naW4gaW5jb3JyZWN0bw=="), vod_channels("UmF6b25lcyBwb3NpYmxlczogdW5hIG8gdmFyaWFzIGRlIGxhcyBjb25maWd1cmFjaW9uZXMgbm8gc29uIHZhbGlkYXMgdmVyaWZpcXVlIHF1ZSBlbCBob3N0LCB1c3VhcmlvLCBjb250cmFzZcOxYSBvIHB1ZXJ0byBzZWFuIGxvcyBjb3JyZWN0b3Mu"+"IFBvciBmYXZvciBjb25maWd1cmUgIFtDT0xPUiB5ZWxsb3ddJXMgWy9DT0xPUl0gY29uIGxvcyBkYXRvcyBjb3JyZWN0b3M=")%(brand))
       plugintools.open_settings_dialog()
       exit()  
    if plugintools.get_setting("advconf")=="true":
        tseaded = xbmc.translatePath(sync_data("c3BlY2lhbDovL3VzZXJkYXRhL2FkdmFuY2Vkc2V0dGluZ3MueG1s"))
        if not os.path.exists(tseaded):
            file = open( os.path.join(plugintools.get_runtime_path(),vod_channels("cmVzb3VyY2Vz"),sync_data("YWR2YW5jZWRzZXR0aW5ncy54bWw=")) )
            data = file.read()
            file.close()
            file = open(tseaded,"w")
            file.write(data)
            file.close()
            plugintools.message(index, get_live("RWwgYXJjaGl2byAtIGFkdmFuY2Vkc2V0dGluZ3MueG1sIGEgc2lkbyBjYXJnYWRvIGNvcnJlY3RhbWVudGU="))
def license_check(params):
    plugintools.log(index+get_live("U2V0dGluZ3MgbWVudQ==")+repr(params))
    plugintools.open_settings_dialog()
def security_check(params):
    plugintools.log(index+sync_data("TGl2ZSBNZW51")+repr(params))
    request = urllib2.Request(livetv, headers={"Accept" : "application/xml"})
    u = urllib2.urlopen(request)
    tree = ElementTree.parse(u)
    rootElem = tree.getroot()
    for channel in tree.findall(sync_data("Y2hhbm5lbA==")):
        ch_title = channel.find(get_live("dGl0bGU=")).text
        ch_title = base64.b64decode(ch_title)
        playlist_url = channel.find(vod_channels("cGxheWxpc3RfdXJs")).text
        plugintools.add_item( action=get_live("c3RyZWFtX3ZpZGVv"), title=ch_title , url=playlist_url, thumbnail=os.path.join(LOAD_LIVE,vod_channels("Y2FycGV0YS5wbmc=")) , fanart=os.path.join(LOAD_LIVE,vod_channels("YmFja2dyb3VuZC5wbmc=")) , folder=True )
    plugintools.set_view( plugintools.LIST )
def detect_modification(params):
    plugintools.log(index+vod_channels("Vk9EIE1lbnUg")+repr(params))       
    request = urllib2.Request(vodlink, headers={"Accept" : "application/xml"})
    u = urllib2.urlopen(request)
    tree = ElementTree.parse(u)
    rootElem = tree.getroot()
    for channel in tree.findall(sync_data("Y2hhbm5lbA==")): 
        vod_title = channel.find(get_live("dGl0bGU=")).text 
        vod_title = base64.b64decode(vod_title)
        playlist_url = channel.find(vod_channels("cGxheWxpc3RfdXJs")).text
        plugintools.add_item( action=vod_channels("Z2V0X215YWNjb3VudA=="), title=vod_title , url=playlist_url , thumbnail=os.path.join(LOAD_LIVE,vod_channels("Y2FycGV0YS5wbmc=")) , fanart=os.path.join(LOAD_LIVE,sync_data("YmFja2dyb3VuZC5wbmc=")) , folder=True )
    plugintools.set_view( plugintools.LIST )
def series_categories(params):
    plugintools.log(index+vod_channels("U0VSSUVTIE1lbnU=")+repr(params))       
    request = urllib2.Request(serieslink, headers={"Accept" : "application/xml"})
    u = urllib2.urlopen(request)
    tree = ElementTree.parse(u)
    rootElem = tree.getroot()
    for channel in tree.findall(sync_data("Y2hhbm5lbA==")):
        scat_title = channel.find(get_live("dGl0bGU=")).text
        scat_title = base64.b64decode(scat_title)
        playlist_url = channel.find(vod_channels("cGxheWxpc3RfdXJs")).text 
        plugintools.add_item( action=vod_channels("c2VyaWVz"), title=scat_title , url=playlist_url , thumbnail=os.path.join(LOAD_LIVE,vod_channels("Y2FycGV0YS5wbmc=")) , fanart=os.path.join(LOAD_LIVE,sync_data("YmFja2dyb3VuZC5wbmc=")) , folder=True )
    plugintools.set_view( plugintools.LIST )
def stream_video(params):
    plugintools.log(index+sync_data("TGl2ZSBDaGFubmVscyBNZW51IA==")+repr(params))
    if crtparent == "true":
       key_title = params.get(sync_data("dGl0bGU="))
       parental_lock(key_title)
    url = params.get(get_live("dXJs"))
    request = urllib2.Request(url, headers={"Accept" : "application/xml"})
    u = urllib2.urlopen(request)
    tree = ElementTree.parse(u)
    rootElem = tree.getroot()
    for channel in tree.findall(sync_data("Y2hhbm5lbA==")):
        ch_title = channel.find(get_live("dGl0bGU=")).text
        ch_title = base64.b64decode(ch_title)
        ch_title = ch_title.partition("[")
        stream_url = channel.find(get_live("c3RyZWFtX3VybA==")).text
        desc_image = channel.find(vod_channels("ZGVzY19pbWFnZQ==")).text
        corch = ch_title[1]+ch_title[2]
        corch = corch.partition("]")
        corch = corch[2]
        corch = corch.partition("   ")
        corch = corch[2]
        desc_title = get_live("W0NPTE9SIHdoaXRlXSVzIFsvQ09MT1Jd")%(ch_title[0])+corch
        descripcion = channel.find(sync_data("ZGVzY3JpcHRpb24=")).text
        if descripcion:
           descripcion = base64.b64decode(descripcion)
           ahora = descripcion.partition("(")
           ahora = sync_data("QUhPUkE6IA==") +ahora[0]
           siguiente = descripcion.partition(")\n")
           siguiente = siguiente[2].partition("(")
           siguiente = sync_data("U0lHVUlFTlRFOiA=") +siguiente[0]
           total = ahora+siguiente
        else:
           total = ""
        if desc_image:
           plugintools.add_item( action=sync_data("cnVuX2Nyb25qb2I="), title=desc_title , url=stream_url, thumbnail=desc_image, plot=total, fanart=os.path.join(LOAD_LIVE,vod_channels("YmFja2dyb3VuZC5wbmc=")), extra="", isPlayable=True, folder=False )
        else:
           plugintools.add_item( action=sync_data("cnVuX2Nyb25qb2I="), title=desc_title , url=stream_url, thumbnail=os.path.join(LOAD_LIVE,sync_data("ZGVmYXVsdGxvZ28ucG5n")) , plot=total, fanart=os.path.join(LOAD_LIVE,sync_data("YmFja2dyb3VuZC5wbmc=")) , extra="", isPlayable=True, folder=False )
    plugintools.set_view( plugintools.EPISODES )
    xbmc.executebuiltin(vod_channels("Q29udGFpbmVyLlNldFZpZXdNb2RlKDUwMyk="))
def get_myaccount(params):
        plugintools.log(index+get_live("Vk9EIGNoYW5uZWxzIG1lbnUg")+repr(params))
        if crtparent == "true":
           key_title = params.get(sync_data("dGl0bGU="))
           parental_lock(key_title)
        purl = params.get(get_live("dXJs"))
        request = urllib2.Request(purl, headers={"Accept" : "application/xml"})
        u = urllib2.urlopen(request)
        tree = ElementTree.parse(u)
        rootElem = tree.getroot()
        for channel in tree.findall(sync_data("Y2hhbm5lbA==")):
            vod_title = channel.find(get_live("dGl0bGU=")).text
            vod_title = base64.b64decode(vod_title)
            stream_url = channel.find(sync_data("c3RyZWFtX3VybA==")).text
            desc_image = channel.find(sync_data("ZGVzY19pbWFnZQ==")).text
            descripcion = channel.find(vod_channels("ZGVzY3JpcHRpb24=")).text
            if descripcion:
               descripcion = base64.b64decode(descripcion) 
            if desc_image:
               plugintools.add_item( action="restart_service", title=vod_title , url=stream_url , thumbnail=desc_image, plot=descripcion, fanart=os.path.join(LOAD_LIVE,"YmFja2dyb3VuZC5wbmc=") , extra="", isPlayable=True, folder=False )
            else:
               plugintools.add_item( action="restart_service", title=vod_title , url=stream_url , thumbnail=os.path.join(LOAD_LIVE,"bm9wb3N0ZXIuanBn"), plot=descripcion, fanart=os.path.join(LOAD_LIVE,"YmFja2dyb3VuZC5wbmc=") , extra="", isPlayable=True, folder=False )
        plugintools.set_view( plugintools.EPISODES )
        xbmc.executebuiltin('Container.SetViewMode(515)')
def series(params):
    purl = params.get(get_live("dXJs"))
    plugintools.log(index+vod_channels("U0VSSUVTIE1lbnU=")+repr(params))
    request = urllib2.Request(purl, headers={"Accept" : "application/xml"})
    u = urllib2.urlopen(request)
    tree = ElementTree.parse(u)
    rootElem = tree.getroot()
    for channel in tree.findall(sync_data("Y2hhbm5lbA==")):
        seriet = channel.find(get_live("dGl0bGU=")).text
        seriet = base64.b64decode(seriet)
        playlist_url = channel.find(vod_channels("cGxheWxpc3RfdXJs")).text
        plugintools.add_item( action=vod_channels("c2Vhc29ucw=="), title=seriet , url=playlist_url , thumbnail=os.path.join(LOAD_LIVE,vod_channels("Y2FycGV0YS5wbmc=")), fanart=os.path.join(LOAD_LIVE,sync_data("YmFja2dyb3VuZC5wbmc=")) , folder=True )
    plugintools.set_view( plugintools.LIST )
def seasons(params):
    purl = params.get(get_live("dXJs"))
    plugintools.log(index+vod_channels("U0VSSUVTIE1lbnU=")+repr(params))
    request = urllib2.Request(purl, headers={"Accept" : "application/xml"})
    u = urllib2.urlopen(request)
    tree = ElementTree.parse(u)
    rootElem = tree.getroot()
    for channel in tree.findall(sync_data("Y2hhbm5lbA==")):
        seasont = channel.find(get_live("dGl0bGU=")).text
        seasont = base64.b64decode(seasont)
        playlist_url = channel.find(vod_channels("cGxheWxpc3RfdXJs")).text
        plugintools.add_item( action=vod_channels("c2VyaWVfc2Vhc29ucw=="), title="Temporada "+seasont[7] , url=playlist_url , thumbnail=os.path.join(LOAD_LIVE,vod_channels("Y2FycGV0YS5wbmc=")), fanart=os.path.join(LOAD_LIVE,sync_data("YmFja2dyb3VuZC5wbmc=")) , folder=True )
    plugintools.set_view( plugintools.LIST )   
def serie_seasons(params):
    plugintools.log(index+sync_data("TGl2ZSBDaGFubmVscyBNZW51IA==")+repr(params)) 
    if crtparent == "true":
       key_title = params.get(sync_data("dGl0bGU="))
       parental_lock(key_title)
    url = params.get(get_live("dXJs"))
    request = urllib2.Request(url, headers={"Accept" : "application/xml"})
    u = urllib2.urlopen(request)
    tree = ElementTree.parse(u)
    rootElem = tree.getroot()
    for channel in tree.findall(sync_data("Y2hhbm5lbA==")):
        ch_title = channel.find(get_live("dGl0bGU=")).text
        ch_title = base64.b64decode(ch_title)
        stream_url = channel.find(get_live("c3RyZWFtX3VybA==")).text
        desc_image = channel.find(vod_channels("ZGVzY19pbWFnZQ==")).text
        descripcion = channel.find(sync_data("ZGVzY3JpcHRpb24=")).text
        if descripcion:
           descripcion = base64.b64decode(descripcion)
        else:
           total = ""
        if desc_image:
           plugintools.add_item( action=sync_data("cnVuX2Nyb25qb2I="), title="Capitulo "+ch_title[8]+ch_title[9] , url=stream_url, thumbnail=desc_image, plot=total, fanart=os.path.join(LOAD_LIVE,vod_channels("YmFja2dyb3VuZC5wbmc=")), extra="", isPlayable=True, folder=False )
        else:
           plugintools.add_item( action=sync_data("cnVuX2Nyb25qb2I="), title="Capitulo "+ch_title[8]+ch_title[9] , url=stream_url, thumbnail=os.path.join(LOAD_LIVE,sync_data("ZGVmYXVsdGxvZ28ucG5n")) , plot=total, fanart=os.path.join(LOAD_LIVE,sync_data("YmFja2dyb3VuZC5wbmc=")) , extra="", isPlayable=True, folder=False )
    plugintools.set_view( plugintools.EPISODES )
    xbmc.executebuiltin(vod_channels("Q29udGFpbmVyLlNldFZpZXdNb2RlKDUwMyk="))
def run_cronjob(params):
    plugintools.log(index+sync_data("UExBWV9MSVZF")+repr(params))
    if crtparent == "true":
       key_title = params.get(sync_data("dGl0bGU="))
       parental_lock(key_title)
    mis_url = params.get(vod_channels("dXJs"))
    plugintools.play_resolved_url( mis_url )
def sync_data(channel):
    video = base64.b64decode(channel)
    return video
def restart_service(params):
    plugintools.log(index+get_live("UExBWSBWT0Qg")+repr(params))
    if crtparent == "true":
       key_title = params.get(sync_data("dGl0bGU="))
       parental_lock(key_title)
    mis_url = params.get(vod_channels("dXJs"))
    plugintools.play_resolved_url( mis_url )
def grab_epg():
    req = urllib2.Request(infolink)
    req.add_header(sync_data("VXNlci1BZ2VudA==") , vod_channels("TW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzY1LjAuMzMyNS4xODEgU2FmYXJpLzUzNy4zNg=="))
    response = urllib2.urlopen(req)
    link=response.read()
    jdata = json.loads(link.decode('utf8'))
    response.close()
    if jdata:
       plugintools.log(index+sync_data("amRhdGEgbG9hZGVkIA=="))
       return jdata
def login_accept():
    statinfo = os.stat(LOAD_LIVE+"/"+get_live("Y29uZmlnLnBuZw=="))

    statinfo = os.stat(LOAD_LIVE+"/"+get_live("ZGVtby5wbmc="))

    statinfo = os.stat(LOAD_LIVE+"/"+get_live("ZXN0YWRvLnBuZw=="))

    statinfo = os.stat(LOAD_LIVE+"/"+get_live("cGVsaWN1bGFzLnBuZw=="))

    statinfo = os.stat(LOAD_LIVE+"/"+get_live("c2VyaWVzLnBuZw=="))

    statinfo = os.stat(LOAD_LIVE+"/"+get_live("dXNlci1pbmZvLnBuZw=="))

    statinfo = os.stat(LOAD_LIVE+"/"+get_live("dHYucG5n"))

    statinfo = os.stat(ADDON+"/"+get_live("YWRkb24ueG1s"))

def auth():
    datos_epg = grab_epg()
    userinfo = datos_epg[sync_data("dXNlcl9pbmZv")]
    auth = userinfo[get_live("YXV0aA==")]
    return auth
def get_live(channel):
    video = base64.b64decode(channel)
    return video
def execute_ainfo(params):
    plugintools.log(index+get_live("TXkgYWNjb3VudCBNZW51IA==")+repr(params)) 
    datos_epg = grab_epg()
    user_info = datos_epg[sync_data("dXNlcl9pbmZv")]
    estado = user_info[get_live("c3RhdHVz")]
    caducidad = user_info[sync_data("ZXhwX2RhdGU=")]
    
    if estado:
        estado = sync_data("QWN0aXZh")
    else:
        estado = sync_data("SW5hY3RpdmE=")
        
    if caducidad:
       caducidad = datetime.datetime.fromtimestamp(int(caducidad)).strftime('%H:%M %d.%m.%Y')
    else:
       caducidad = vod_channels("TnVuY2E=") 
    demo = user_info[vod_channels("aXNfdHJpYWw=")]
    if demo == "0":
       demo = sync_data("Tm8=")
    else:
       demo = sync_data("U2k=")

    max_conex = user_info[get_live("bWF4X2Nvbm5lY3Rpb25z")]
    usrinf = user_info[sync_data("dXNlcm5hbWU=")]
    plugintools.add_item( action="",   title=sync_data("W0NPTE9SID0gd2hpdGVdVXN1YXJpbzogWy9DT0xPUl0=")+usrinf , thumbnail=os.path.join(LOAD_LIVE,sync_data("dXNlci1pbmZvLnBuZw==")) , fanart=os.path.join(LOAD_LIVE,sync_data("YmFja2dyb3VuZC5wbmc=")) , folder=False )
    plugintools.add_item( action="",   title=sync_data("W0NPTE9SID0gd2hpdGVdRXN0YWRvOiBbL0NPTE9SXQ==")+estado , thumbnail=os.path.join(LOAD_LIVE,sync_data("ZXN0YWRvLnBuZw==")) , fanart=os.path.join(LOAD_LIVE,sync_data("YmFja2dyb3VuZC5wbmc=")) , folder=False )
    plugintools.add_item( action="",   title=get_live("W0NPTE9SID0gd2hpdGVdQ2FkdWNpZGFkOiBbL0NPTE9SXQ==")+caducidad , thumbnail=os.path.join(LOAD_LIVE,sync_data("Y2FkdWNpZGFkLnBuZw==")) , fanart=os.path.join(LOAD_LIVE,sync_data("YmFja2dyb3VuZC5wbmc=")) , folder=False )
    plugintools.add_item( action="",   title=vod_channels("W0NPTE9SID0gd2hpdGVdQ3VlbnRhIGRlbW86IFsvQ09MT1Jd")+demo , thumbnail=os.path.join(LOAD_LIVE,sync_data("ZGVtby5wbmc=")) , fanart=os.path.join(LOAD_LIVE,sync_data("YmFja2dyb3VuZC5wbmc=")) , folder=False )
    plugintools.add_item( action="",   title=vod_channels("W0NPTE9SID0gd2hpdGVdQ29uZXhpb25lcyBtYXhpbWFzOiBbL0NPTE9SXQ==")+max_conex , thumbnail=os.path.join(LOAD_LIVE,sync_data("Y29uZXgtbWF4LnBuZw==")) , fanart=os.path.join(LOAD_LIVE,sync_data("YmFja2dyb3VuZC5wbmc=")) , folder=False )
    plugintools.set_view( plugintools.LIST )
def parental_lock(name):
        plugintools.log(index+sync_data("UGFyZW50YWwgbG9jayA="))
        a = 'XXX', 'Adulto', 'Adultos', 'ADULTO', 'ADULTOS', 'adulto', 'adultos', 'Porno', 'PORNO','porno', 'Adult', 'Adults','ADULT','ADULTS','adult','adults','Porn','PORN','porn','Porn','xxx', '+18'
        if any(s in name for s in a):
           xbmc.executebuiltin((u'XBMC.Notification("Bloqueo Parental", "Este canal es solo para adultos ", 2000)'))
           text = plugintools.keyboard_input(default_text="", title=get_live("QmxvcXVlbyBQYXJlbnRhbA=="))
           if text==plugintools.get_setting(sync_data("a2V5cGFyZW50")):
              return
           else:
              exit()
        else:
           name = ""
def check_channels():
    statinfo = os.stat(LOAD_LIVE+"/"+get_live("YmFja2dyb3VuZC5wbmc="))

    statinfo = os.stat(LOAD_LIVE+"/"+get_live("ZGVmYXVsdGxvZ28ucG5n"))

    statinfo = os.stat(LOAD_LIVE+"/"+get_live("Y2FkdWNpZGFkLnBuZw=="))

    statinfo = os.stat(LOAD_LIVE+"/"+get_live("Y2FycGV0YS5wbmc="))

    statinfo = os.stat(LOAD_LIVE+"/"+get_live("Y29uZXgtbWF4LnBuZw=="))

def vod_channels(channel):
    video = base64.b64decode(channel)
    return video
run()