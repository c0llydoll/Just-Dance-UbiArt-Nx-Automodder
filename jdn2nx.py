import os, json, requests, zipfile, subprocess, shutil, sys
from random import randint
import numpy as np
from urllib.request import urlopen
from urllib.error import HTTPError
from PIL import Image
from io import BytesIO
from wand import image




print('''

                                                                                                                                            


     ___  ______   __    _    _______  _______    __    _  __   __ 
    |   ||      | |  |  | |  |       ||       |  |  |  | ||  |_|  |
    |   ||  _    ||   |_| |  |_     _||   _   |  |   |_| ||       |
    |   || | |   ||       |    |   |  |  | |  |  |       ||       |
 ___|   || |_|   ||  _    |    |   |  |  |_|  |  |  _    | |     | 
|       ||       || | |   |    |   |  |       |  | | |   ||   _   |
|_______||______| |_|  |__|    |___|  |_______|  |_|  |__||__| |__|




WELCOME TO JDN2NX.
This tool was last modified on 2022-11-17.

Please provide WEBM, OGG & menuarts.

Delete temp after running.

''')

name = input("Please insert your name. ")
namelower = name.lower()


os.makedirs("temp\\", exist_ok=True)

#NX Mainscene Gen by Kirby (Gets the cache/world stuff ready)
try:
    coachnum = int(input("Coach Count?: "))
except:
    print("Use only numbers!")
    exit()

output = (os.getcwd() + "\\" + "temp\\" + name.lower() + "_nx")
try:
    #Cache Folder
    cache_path = (output + "\\cache\\itf_cooked\\nx\\world\\maps\\" + name.lower() + "\\")
    os.makedirs(cache_path, exist_ok=True)
    cache_audio = (cache_path + "audio\\")
    os.makedirs(cache_audio, exist_ok=True)
    cache_autodance = (cache_path + "autodance\\")
    os.makedirs(cache_autodance, exist_ok=True)
    cache_cinematics = (cache_path + "cinematics\\")
    os.makedirs(cache_cinematics, exist_ok=True)
    cache_graph = (cache_path + "graph\\")
    os.makedirs(cache_graph, exist_ok=True)
    cache_menuart = (cache_path + "menuart\\")
    cache_tex_menuart = (cache_path + "menuart\\textures\\")
    os.makedirs(cache_tex_menuart, exist_ok=True)
    cache_act_menuart = (cache_path + "menuart\\actors\\")
    os.makedirs(cache_act_menuart, exist_ok=True)
    cache_timeline = (cache_path + "timeline\\")
    cache_pictos = (cache_path + "timeline\\pictos\\")
    os.makedirs(cache_pictos, exist_ok=True)
    cache_videoscoach = (cache_path + "videoscoach\\")
    os.makedirs(cache_videoscoach, exist_ok=True)
    #Cache Folder

    #World Folder
    world_path = (output + "\\world\\maps\\" + name.lower() + "\\")
    os.makedirs(world_path, exist_ok=True)
    worldaudio = (world_path + "audio\\")
    os.makedirs(worldaudio, exist_ok=True)
    world_moves = (world_path + "timeline\\moves\\wiiu\\")
    os.makedirs(world_moves, exist_ok=True)
    world_videoscoach = (world_path + "videoscoach\\")
    os.makedirs(world_videoscoach, exist_ok=True)

    #World Folder

    #Audio Files
    ##
    stapefile = open(cache_audio + name.lower() + ".stape.ckd", "w", encoding="utf-8")
    stapefile.write('{"__class":"Tape","Clips":[],"TapeClock":0,"TapeBarCount":1,"FreeResourcesAfterPlay":0,"name":"' + name + '"}')
    stapefile.close()
    ##

    ##
    audioisc = open(cache_audio + name.lower() + "_audio.isc.ckd", "w", encoding="utf-8")
    audioisc.write('''<?xml version="1.0" encoding="ISO-8859-1"?>
<root>
    <Scene ENGINE_VERSION="253653" GRIDUNIT="0.500000" DEPTH_SEPARATOR="0" NEAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" FAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" viewFamily="0">
        <ACTORS NAME="Actor">
            <Actor RELATIVEZ="0.000000" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="MusicTrack" MARKER="" POS2D="1.125962 -0.418641" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="world/maps/''' + name.lower() + '''/audio/''' + name.lower() + '''_musictrack.tpl">
                <COMPONENTS NAME="MusicTrackComponent">
                    <MusicTrackComponent />
                </COMPONENTS>
            </Actor>
        </ACTORS>
        <ACTORS NAME="Actor">
            <Actor RELATIVEZ="0.000001" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="''' + name + '''_sequence" MARKER="" POS2D="-0.006158 -0.006158" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="world/maps/''' + name.lower() + '''/audio/''' + name.lower() + '''_sequence.tpl">
                <COMPONENTS NAME="TapeCase_Component">
                    <TapeCase_Component />
                </COMPONENTS>
            </Actor>
        </ACTORS>
        <sceneConfigs>
            <SceneConfigs activeSceneConfig="0" />
        </sceneConfigs>
    </Scene>
</root>
''')
    audioisc.close()
    ##
    
    ##
    audiosequence = open(cache_audio + name.lower() + "_sequence.tpl.ckd", "w", encoding="utf-8")
    audiosequence.write('{"__class":"Actor_Template","WIP":0,"LOWUPDATE":0,"UPDATE_LAYER":0,"PROCEDURAL":0,"STARTPAUSED":0,"FORCEISENVIRONMENT":0,"COMPONENTS":[{"__class":"TapeCase_Template","TapesRack":[{"__class":"TapeGroup","Entries":[{"__class":"TapeEntry","Label":"TML_Sequence","Path":"world/maps/' + name.lower() + '/audio/' + name.lower() + '.stape"}]}]}]}')
    audiosequence.close()
    ##

    #Cinematic Files
    ##
    cinetape = open(cache_cinematics + name.lower() + "_mainsequence.tape.ckd", "w", encoding="utf-8")
    cinetape.write('{"__class":"Tape","Clips":[],"TapeClock":0,"TapeBarCount":1,"FreeResourcesAfterPlay":0,"name":"' + name + '"}')
    cinetape.close()
    ##
    
    ##
    cineisc = open(cache_cinematics + name.lower() + "_cine.isc.ckd", "w", encoding="utf-8")
    cineisc.write('''<?xml version="1.0" encoding="ISO-8859-1"?>
<root>
    <Scene ENGINE_VERSION="253653" GRIDUNIT="0.500000" DEPTH_SEPARATOR="0" NEAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" FAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" viewFamily="0">
        <ACTORS NAME="Actor">
            <Actor RELATIVEZ="0.000000" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="''' + name + '''_MainSequence" MARKER="" POS2D="0.000000 0.000000" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="world/maps/''' + name.lower() + '''/cinematics/''' + name.lower() + '''_mainsequence.tpl">
                <COMPONENTS NAME="MasterTape">
                    <MasterTape />
                </COMPONENTS>
            </Actor>
        </ACTORS>
        <sceneConfigs>
            <SceneConfigs activeSceneConfig="0" />
        </sceneConfigs>
    </Scene>
</root>''')
    cineisc.close()
    ##

    ##
    cinesequence = open(cache_cinematics + name.lower() + "_mainsequence.tpl.ckd", "w", encoding="utf-8")
    cinesequence.write('{"__class":"Actor_Template","WIP":0,"LOWUPDATE":0,"UPDATE_LAYER":0,"PROCEDURAL":0,"STARTPAUSED":0,"FORCEISENVIRONMENT":0,"COMPONENTS":[{"__class":"MasterTape_Template","TapesRack":[{"__class":"TapeGroup","Entries":[{"__class":"TapeEntry","Label":"master","Path":"world/maps/' + name.lower() + '/cinematics/' + name.lower() + '_mainsequence.tape"}]}]}]}')
    cinesequence.close()
    ##

    #GraphFile
    graphisc = open(cache_graph + name.lower() + "_graph.isc.ckd", "w", encoding="utf-8")
    graphisc.write('''<?xml version="1.0" encoding="ISO-8859-1"?>
<root>
    <Scene ENGINE_VERSION="253653" GRIDUNIT="0.500000" DEPTH_SEPARATOR="0" NEAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" FAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" viewFamily="0">
        <ACTORS NAME="Actor">
            <Actor RELATIVEZ="10.000000" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="Camera_JD_Dummy" MARKER="" POS2D="0.000000 0.000000" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/tpl_emptyactor.tpl" />
        </ACTORS>
        <sceneConfigs>
            <SceneConfigs activeSceneConfig="0" />
        </sceneConfigs>
    </Scene>
</root>''')
    graphisc.close()
    #GraphFile

    #Menuart ISC
    menuartisc = open(cache_menuart + name.lower() + "_menuart.isc.ckd", "w", encoding="utf-8")
    menuartisc_content = ""
    if(coachnum == 1):
       menuartisc_content = ('''<?xml version="1.0" encoding="ISO-8859-1"?>
<root>
    <Scene ENGINE_VERSION="253653" GRIDUNIT="0.500000" DEPTH_SEPARATOR="0" NEAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" FAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" viewFamily="1">
        <ACTORS NAME="Actor">
            <Actor RELATIVEZ="0.000000" SCALE="0.300000 0.300000" xFLIPPED="0" USERFRIENDLY="''' + name + '''_cover_generic" MARKER="" POS2D="266.087555 197.629959" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
                <COMPONENTS NAME="MaterialGraphicComponent">
                    <MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="4294967295" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
                        <PrimitiveParameters>
                            <GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000">
                                <ENUM NAME="gfxOccludeInfo" SEL="0" />
                            </GFXPrimitiveParam>
                        </PrimitiveParameters>
                        <ENUM NAME="anchor" SEL="1" />
                        <material>
                            <GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/_common/matshader/multitexture_1layer.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
                                <textureSet>
                                    <GFXMaterialTexturePathSet diffuse="world/maps/''' + name.lower() + '''/menuart/textures/''' + name.lower() + '''_cover_generic.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4="" />
                                </textureSet>
                                <materialParams>
                                    <GFXMaterialSerializableParam Reflector_factor="0.000000" />
                                </materialParams>
                            </GFXMaterialSerializable>
                        </material>
                        <ENUM NAME="oldAnchor" SEL="1" />
                    </MaterialGraphicComponent>
                </COMPONENTS>
            </Actor>
        </ACTORS>
        <ACTORS NAME="Actor">
            <Actor RELATIVEZ="0.000000" SCALE="0.300000 0.300000" xFLIPPED="0" USERFRIENDLY="''' + name + '''_cover_online" MARKER="" POS2D="-150.000000 0.000000" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
                <COMPONENTS NAME="MaterialGraphicComponent">
                    <MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="4294967295" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
                        <PrimitiveParameters>
                            <GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000">
                                <ENUM NAME="gfxOccludeInfo" SEL="0" />
                            </GFXPrimitiveParam>
                        </PrimitiveParameters>
                        <ENUM NAME="anchor" SEL="1" />
                        <material>
                            <GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/_common/matshader/multitexture_1layer.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
                                <textureSet>
                                    <GFXMaterialTexturePathSet diffuse="world/maps/''' + name.lower() + '''/menuart/textures/''' + name.lower() + '''_cover_online.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4="" />
                                </textureSet>
                                <materialParams>
                                    <GFXMaterialSerializableParam Reflector_factor="0.000000" />
                                </materialParams>
                            </GFXMaterialSerializable>
                        </material>
                        <ENUM NAME="oldAnchor" SEL="1" />
                    </MaterialGraphicComponent>
                </COMPONENTS>
            </Actor>
        </ACTORS>
        <ACTORS NAME="Actor">
            <Actor RELATIVEZ="0.000000" SCALE="0.300000 0.300000" xFLIPPED="0" USERFRIENDLY="''' + name + '''_cover_albumcoach" MARKER="" POS2D="738.106323 359.612030" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
                <COMPONENTS NAME="MaterialGraphicComponent">
                    <MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="4294967295" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
                        <PrimitiveParameters>
                            <GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000">
                                <ENUM NAME="gfxOccludeInfo" SEL="0" />
                            </GFXPrimitiveParam>
                        </PrimitiveParameters>
                        <ENUM NAME="anchor" SEL="6" />
                        <material>
                            <GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/_common/matshader/multitexture_1layer.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
                                <textureSet>
                                    <GFXMaterialTexturePathSet diffuse="world/maps/''' + name.lower() + '''/menuart/textures/''' + name.lower() + '''_cover_albumcoach.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4="" />
                                </textureSet>
                                <materialParams>
                                    <GFXMaterialSerializableParam Reflector_factor="0.000000" />
                                </materialParams>
                            </GFXMaterialSerializable>
                        </material>
                        <ENUM NAME="oldAnchor" SEL="6" />
                    </MaterialGraphicComponent>
                </COMPONENTS>
            </Actor>
        </ACTORS>
        <ACTORS NAME="Actor">
            <Actor RELATIVEZ="0.000000" SCALE="0.300000 0.300000" xFLIPPED="0" USERFRIENDLY="''' + name + '''_cover_albumbkg" MARKER="" POS2D="1067.972168 201.986328" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
                <COMPONENTS NAME="MaterialGraphicComponent">
                    <MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="4294967295" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
                        <PrimitiveParameters>
                            <GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000">
                                <ENUM NAME="gfxOccludeInfo" SEL="0" />
                            </GFXPrimitiveParam>
                        </PrimitiveParameters>
                        <ENUM NAME="anchor" SEL="1" />
                        <material>
                            <GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/_common/matshader/multitexture_1layer.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
                                <textureSet>
                                    <GFXMaterialTexturePathSet diffuse="world/maps/''' + name.lower() + '''/menuart/textures/''' + name.lower() + '''_cover_albumbkg.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4="" />
                                </textureSet>
                                <materialParams>
                                    <GFXMaterialSerializableParam Reflector_factor="0.000000" />
                                </materialParams>
                            </GFXMaterialSerializable>
                        </material>
                        <ENUM NAME="oldAnchor" SEL="1" />
                    </MaterialGraphicComponent>
                </COMPONENTS>
            </Actor>
        </ACTORS>
        <ACTORS NAME="Actor">
            <Actor RELATIVEZ="0.000000" SCALE="0.290211 0.290211" xFLIPPED="0" USERFRIENDLY="''' + name + '''_coach_1" MARKER="" POS2D="212.784500 663.680176" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
                <COMPONENTS NAME="MaterialGraphicComponent">
                    <MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="4294967295" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
                        <PrimitiveParameters>
                            <GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000">
                                <ENUM NAME="gfxOccludeInfo" SEL="0" />
                            </GFXPrimitiveParam>
                        </PrimitiveParameters>
                        <ENUM NAME="anchor" SEL="6" />
                        <material>
                            <GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/_common/matshader/multitexture_1layer.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
                                <textureSet>
                                    <GFXMaterialTexturePathSet diffuse="world/maps/''' + name.lower() + '''/menuart/textures/''' + name.lower() + '''_coach_1.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4="" />
                                </textureSet>
                                <materialParams>
                                    <GFXMaterialSerializableParam Reflector_factor="0.000000" />
                                </materialParams>
                            </GFXMaterialSerializable>
                        </material>
                        <ENUM NAME="oldAnchor" SEL="6" />
                    </MaterialGraphicComponent>
                </COMPONENTS>
            </Actor>
        </ACTORS>
        <ACTORS NAME="Actor">
            <Actor RELATIVEZ="0.000000" SCALE="256.000000 128.000000" xFLIPPED="0" USERFRIENDLY="''' + name + '''_map_bkg" MARKER="" POS2D="1487.410156 -32.732918" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
                <COMPONENTS NAME="MaterialGraphicComponent">
                    <MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="1" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
                        <PrimitiveParameters>
                            <GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000">
                                <ENUM NAME="gfxOccludeInfo" SEL="0" />
                            </GFXPrimitiveParam>
                        </PrimitiveParameters>
                        <ENUM NAME="anchor" SEL="1" />
                        <material>
                            <GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/_common/matshader/multitexture_1layer.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
                                <textureSet>
                                    <GFXMaterialTexturePathSet diffuse="world/maps/''' + name.lower() + '''/menuart/textures/''' + name.lower() + '''_map_bkg.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4="" />
                                </textureSet>
                                <materialParams>
                                    <GFXMaterialSerializableParam Reflector_factor="0.000000" />
                                </materialParams>
                            </GFXMaterialSerializable>
                        </material>
                        <ENUM NAME="oldAnchor" SEL="1" />
                    </MaterialGraphicComponent>
                </COMPONENTS>
            </Actor>
        </ACTORS>
        <sceneConfigs>
            <SceneConfigs activeSceneConfig="0" />
        </sceneConfigs>
    </Scene>
</root>''')
    if(coachnum == 2):
        menuartisc_content = ('''<?xml version="1.0" encoding="ISO-8859-1"?>
<root>
    <Scene ENGINE_VERSION="253653" GRIDUNIT="0.500000" DEPTH_SEPARATOR="0" NEAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" FAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" viewFamily="1">
        <ACTORS NAME="Actor">
            <Actor RELATIVEZ="0.000000" SCALE="0.300000 0.300000" xFLIPPED="0" USERFRIENDLY="''' + name + '''_cover_generic" MARKER="" POS2D="266.087555 197.629959" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
                <COMPONENTS NAME="MaterialGraphicComponent">
                    <MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="4294967295" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
                        <PrimitiveParameters>
                            <GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000">
                                <ENUM NAME="gfxOccludeInfo" SEL="0" />
                            </GFXPrimitiveParam>
                        </PrimitiveParameters>
                        <ENUM NAME="anchor" SEL="1" />
                        <material>
                            <GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/_common/matshader/multitexture_1layer.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
                                <textureSet>
                                    <GFXMaterialTexturePathSet diffuse="world/maps/''' + name.lower() + '''/menuart/textures/''' + name.lower() + '''_cover_generic.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4="" />
                                </textureSet>
                                <materialParams>
                                    <GFXMaterialSerializableParam Reflector_factor="0.000000" />
                                </materialParams>
                            </GFXMaterialSerializable>
                        </material>
                        <ENUM NAME="oldAnchor" SEL="1" />
                    </MaterialGraphicComponent>
                </COMPONENTS>
            </Actor>
        </ACTORS>
        <ACTORS NAME="Actor">
            <Actor RELATIVEZ="0.000000" SCALE="0.300000 0.300000" xFLIPPED="0" USERFRIENDLY="''' + name + '''_cover_online" MARKER="" POS2D="-150.000000 0.000000" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
                <COMPONENTS NAME="MaterialGraphicComponent">
                    <MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="4294967295" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
                        <PrimitiveParameters>
                            <GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000">
                                <ENUM NAME="gfxOccludeInfo" SEL="0" />
                            </GFXPrimitiveParam>
                        </PrimitiveParameters>
                        <ENUM NAME="anchor" SEL="1" />
                        <material>
                            <GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/_common/matshader/multitexture_1layer.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
                                <textureSet>
                                    <GFXMaterialTexturePathSet diffuse="world/maps/''' + name.lower() + '''/menuart/textures/''' + name.lower() + '''_cover_online.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4="" />
                                </textureSet>
                                <materialParams>
                                    <GFXMaterialSerializableParam Reflector_factor="0.000000" />
                                </materialParams>
                            </GFXMaterialSerializable>
                        </material>
                        <ENUM NAME="oldAnchor" SEL="1" />
                    </MaterialGraphicComponent>
                </COMPONENTS>
            </Actor>
        </ACTORS>
        <ACTORS NAME="Actor">
            <Actor RELATIVEZ="0.000000" SCALE="0.300000 0.300000" xFLIPPED="0" USERFRIENDLY="''' + name + '''_cover_albumcoach" MARKER="" POS2D="738.106323 359.612030" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
                <COMPONENTS NAME="MaterialGraphicComponent">
                    <MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="4294967295" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
                        <PrimitiveParameters>
                            <GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000">
                                <ENUM NAME="gfxOccludeInfo" SEL="0" />
                            </GFXPrimitiveParam>
                        </PrimitiveParameters>
                        <ENUM NAME="anchor" SEL="6" />
                        <material>
                            <GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/_common/matshader/multitexture_1layer.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
                                <textureSet>
                                    <GFXMaterialTexturePathSet diffuse="world/maps/''' + name.lower() + '''/menuart/textures/''' + name.lower() + '''_cover_albumcoach.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4="" />
                                </textureSet>
                                <materialParams>
                                    <GFXMaterialSerializableParam Reflector_factor="0.000000" />
                                </materialParams>
                            </GFXMaterialSerializable>
                        </material>
                        <ENUM NAME="oldAnchor" SEL="6" />
                    </MaterialGraphicComponent>
                </COMPONENTS>
            </Actor>
        </ACTORS>
        <ACTORS NAME="Actor">
            <Actor RELATIVEZ="0.000000" SCALE="0.300000 0.300000" xFLIPPED="0" USERFRIENDLY="''' + name + '''_cover_albumbkg" MARKER="" POS2D="1067.972168 201.986328" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
                <COMPONENTS NAME="MaterialGraphicComponent">
                    <MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="4294967295" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
                        <PrimitiveParameters>
                            <GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000">
                                <ENUM NAME="gfxOccludeInfo" SEL="0" />
                            </GFXPrimitiveParam>
                        </PrimitiveParameters>
                        <ENUM NAME="anchor" SEL="1" />
                        <material>
                            <GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/_common/matshader/multitexture_1layer.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
                                <textureSet>
                                    <GFXMaterialTexturePathSet diffuse="world/maps/''' + name.lower() + '''/menuart/textures/''' + name.lower() + '''_cover_albumbkg.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4="" />
                                </textureSet>
                                <materialParams>
                                    <GFXMaterialSerializableParam Reflector_factor="0.000000" />
                                </materialParams>
                            </GFXMaterialSerializable>
                        </material>
                        <ENUM NAME="oldAnchor" SEL="1" />
                    </MaterialGraphicComponent>
                </COMPONENTS>
            </Actor>
        </ACTORS>
        <ACTORS NAME="Actor">
            <Actor RELATIVEZ="0.000000" SCALE="0.290211 0.290211" xFLIPPED="0" USERFRIENDLY="''' + name + '''_coach_1" MARKER="" POS2D="212.784500 663.680176" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
                <COMPONENTS NAME="MaterialGraphicComponent">
                    <MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="4294967295" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
                        <PrimitiveParameters>
                            <GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000">
                                <ENUM NAME="gfxOccludeInfo" SEL="0" />
                            </GFXPrimitiveParam>
                        </PrimitiveParameters>
                        <ENUM NAME="anchor" SEL="6" />
                        <material>
                            <GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/_common/matshader/multitexture_1layer.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
                                <textureSet>
                                    <GFXMaterialTexturePathSet diffuse="world/maps/''' + name.lower() + '''/menuart/textures/''' + name.lower() + '''_coach_1.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4="" />
                                </textureSet>
                                <materialParams>
                                    <GFXMaterialSerializableParam Reflector_factor="0.000000" />
                                </materialParams>
                            </GFXMaterialSerializable>
                        </material>
                        <ENUM NAME="oldAnchor" SEL="6" />
                    </MaterialGraphicComponent>
                </COMPONENTS>
            </Actor>
        </ACTORS>
        <ACTORS NAME="Actor">
            <Actor RELATIVEZ="0.000000" SCALE="0.290211 0.290211" xFLIPPED="0" USERFRIENDLY="''' + name + '''_coach_2" MARKER="" POS2D="212.784500 663.680176" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
                <COMPONENTS NAME="MaterialGraphicComponent">
                    <MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="4294967295" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
                        <PrimitiveParameters>
                            <GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000">
                                <ENUM NAME="gfxOccludeInfo" SEL="0" />
                            </GFXPrimitiveParam>
                        </PrimitiveParameters>
                        <ENUM NAME="anchor" SEL="6" />
                        <material>
                            <GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/_common/matshader/multitexture_1layer.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
                                <textureSet>
                                    <GFXMaterialTexturePathSet diffuse="world/maps/''' + name.lower() + '''/menuart/textures/''' + name.lower() + '''_coach_2.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4="" />
                                </textureSet>
                                <materialParams>
                                    <GFXMaterialSerializableParam Reflector_factor="0.000000" />
                                </materialParams>
                            </GFXMaterialSerializable>
                        </material>
                        <ENUM NAME="oldAnchor" SEL="6" />
                    </MaterialGraphicComponent>
                </COMPONENTS>
            </Actor>
        </ACTORS>
        <ACTORS NAME="Actor">
            <Actor RELATIVEZ="0.000000" SCALE="256.000000 128.000000" xFLIPPED="0" USERFRIENDLY="''' + name + '''_map_bkg" MARKER="" POS2D="1487.410156 -32.732918" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
                <COMPONENTS NAME="MaterialGraphicComponent">
                    <MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="1" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
                        <PrimitiveParameters>
                            <GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000">
                                <ENUM NAME="gfxOccludeInfo" SEL="0" />
                            </GFXPrimitiveParam>
                        </PrimitiveParameters>
                        <ENUM NAME="anchor" SEL="1" />
                        <material>
                            <GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/_common/matshader/multitexture_1layer.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
                                <textureSet>
                                    <GFXMaterialTexturePathSet diffuse="world/maps/''' + name.lower() + '''/menuart/textures/''' + name.lower() + '''_map_bkg.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4="" />
                                </textureSet>
                                <materialParams>
                                    <GFXMaterialSerializableParam Reflector_factor="0.000000" />
                                </materialParams>
                            </GFXMaterialSerializable>
                        </material>
                        <ENUM NAME="oldAnchor" SEL="1" />
                    </MaterialGraphicComponent>
                </COMPONENTS>
            </Actor>
        </ACTORS>
        <sceneConfigs>
            <SceneConfigs activeSceneConfig="0" />
        </sceneConfigs>
    </Scene>
</root>''')
    if(coachnum == 3):
        menuartisc_content = ('''<?xml version="1.0" encoding="ISO-8859-1"?>
<root>
    <Scene ENGINE_VERSION="253653" GRIDUNIT="0.500000" DEPTH_SEPARATOR="0" NEAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" FAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" viewFamily="1">
        <ACTORS NAME="Actor">
            <Actor RELATIVEZ="0.000000" SCALE="0.300000 0.300000" xFLIPPED="0" USERFRIENDLY="''' + name + '''_cover_generic" MARKER="" POS2D="266.087555 197.629959" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
                <COMPONENTS NAME="MaterialGraphicComponent">
                    <MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="4294967295" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
                        <PrimitiveParameters>
                            <GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000">
                                <ENUM NAME="gfxOccludeInfo" SEL="0" />
                            </GFXPrimitiveParam>
                        </PrimitiveParameters>
                        <ENUM NAME="anchor" SEL="1" />
                        <material>
                            <GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/_common/matshader/multitexture_1layer.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
                                <textureSet>
                                    <GFXMaterialTexturePathSet diffuse="world/maps/''' + name.lower() + '''/menuart/textures/''' + name.lower() + '''_cover_generic.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4="" />
                                </textureSet>
                                <materialParams>
                                    <GFXMaterialSerializableParam Reflector_factor="0.000000" />
                                </materialParams>
                            </GFXMaterialSerializable>
                        </material>
                        <ENUM NAME="oldAnchor" SEL="1" />
                    </MaterialGraphicComponent>
                </COMPONENTS>
            </Actor>
        </ACTORS>
        <ACTORS NAME="Actor">
            <Actor RELATIVEZ="0.000000" SCALE="0.300000 0.300000" xFLIPPED="0" USERFRIENDLY="''' + name + '''_cover_online" MARKER="" POS2D="-150.000000 0.000000" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
                <COMPONENTS NAME="MaterialGraphicComponent">
                    <MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="4294967295" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
                        <PrimitiveParameters>
                            <GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000">
                                <ENUM NAME="gfxOccludeInfo" SEL="0" />
                            </GFXPrimitiveParam>
                        </PrimitiveParameters>
                        <ENUM NAME="anchor" SEL="1" />
                        <material>
                            <GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/_common/matshader/multitexture_1layer.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
                                <textureSet>
                                    <GFXMaterialTexturePathSet diffuse="world/maps/''' + name.lower() + '''/menuart/textures/''' + name.lower() + '''_cover_online.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4="" />
                                </textureSet>
                                <materialParams>
                                    <GFXMaterialSerializableParam Reflector_factor="0.000000" />
                                </materialParams>
                            </GFXMaterialSerializable>
                        </material>
                        <ENUM NAME="oldAnchor" SEL="1" />
                    </MaterialGraphicComponent>
                </COMPONENTS>
            </Actor>
        </ACTORS>
        <ACTORS NAME="Actor">
            <Actor RELATIVEZ="0.000000" SCALE="0.300000 0.300000" xFLIPPED="0" USERFRIENDLY="''' + name + '''_cover_albumcoach" MARKER="" POS2D="738.106323 359.612030" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
                <COMPONENTS NAME="MaterialGraphicComponent">
                    <MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="4294967295" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
                        <PrimitiveParameters>
                            <GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000">
                                <ENUM NAME="gfxOccludeInfo" SEL="0" />
                            </GFXPrimitiveParam>
                        </PrimitiveParameters>
                        <ENUM NAME="anchor" SEL="6" />
                        <material>
                            <GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/_common/matshader/multitexture_1layer.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
                                <textureSet>
                                    <GFXMaterialTexturePathSet diffuse="world/maps/''' + name.lower() + '''/menuart/textures/''' + name.lower() + '''_cover_albumcoach.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4="" />
                                </textureSet>
                                <materialParams>
                                    <GFXMaterialSerializableParam Reflector_factor="0.000000" />
                                </materialParams>
                            </GFXMaterialSerializable>
                        </material>
                        <ENUM NAME="oldAnchor" SEL="6" />
                    </MaterialGraphicComponent>
                </COMPONENTS>
            </Actor>
        </ACTORS>
        <ACTORS NAME="Actor">
            <Actor RELATIVEZ="0.000000" SCALE="0.300000 0.300000" xFLIPPED="0" USERFRIENDLY="''' + name + '''_cover_albumbkg" MARKER="" POS2D="1067.972168 201.986328" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
                <COMPONENTS NAME="MaterialGraphicComponent">
                    <MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="4294967295" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
                        <PrimitiveParameters>
                            <GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000">
                                <ENUM NAME="gfxOccludeInfo" SEL="0" />
                            </GFXPrimitiveParam>
                        </PrimitiveParameters>
                        <ENUM NAME="anchor" SEL="1" />
                        <material>
                            <GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/_common/matshader/multitexture_1layer.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
                                <textureSet>
                                    <GFXMaterialTexturePathSet diffuse="world/maps/''' + name.lower() + '''/menuart/textures/''' + name.lower() + '''_cover_albumbkg.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4="" />
                                </textureSet>
                                <materialParams>
                                    <GFXMaterialSerializableParam Reflector_factor="0.000000" />
                                </materialParams>
                            </GFXMaterialSerializable>
                        </material>
                        <ENUM NAME="oldAnchor" SEL="1" />
                    </MaterialGraphicComponent>
                </COMPONENTS>
            </Actor>
        </ACTORS>
        <ACTORS NAME="Actor">
            <Actor RELATIVEZ="0.000000" SCALE="0.290211 0.290211" xFLIPPED="0" USERFRIENDLY="''' + name + '''_coach_1" MARKER="" POS2D="212.784500 663.680176" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
                <COMPONENTS NAME="MaterialGraphicComponent">
                    <MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="4294967295" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
                        <PrimitiveParameters>
                            <GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000">
                                <ENUM NAME="gfxOccludeInfo" SEL="0" />
                            </GFXPrimitiveParam>
                        </PrimitiveParameters>
                        <ENUM NAME="anchor" SEL="6" />
                        <material>
                            <GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/_common/matshader/multitexture_1layer.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
                                <textureSet>
                                    <GFXMaterialTexturePathSet diffuse="world/maps/''' + name.lower() + '''/menuart/textures/''' + name.lower() + '''_coach_1.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4="" />
                                </textureSet>
                                <materialParams>
                                    <GFXMaterialSerializableParam Reflector_factor="0.000000" />
                                </materialParams>
                            </GFXMaterialSerializable>
                        </material>
                        <ENUM NAME="oldAnchor" SEL="6" />
                    </MaterialGraphicComponent>
                </COMPONENTS>
            </Actor>
        </ACTORS>
        <ACTORS NAME="Actor">
            <Actor RELATIVEZ="0.000000" SCALE="0.290211 0.290211" xFLIPPED="0" USERFRIENDLY="''' + name + '''_coach_2" MARKER="" POS2D="212.784500 663.680176" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
                <COMPONENTS NAME="MaterialGraphicComponent">
                    <MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="4294967295" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
                        <PrimitiveParameters>
                            <GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000">
                                <ENUM NAME="gfxOccludeInfo" SEL="0" />
                            </GFXPrimitiveParam>
                        </PrimitiveParameters>
                        <ENUM NAME="anchor" SEL="6" />
                        <material>
                            <GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/_common/matshader/multitexture_1layer.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
                                <textureSet>
                                    <GFXMaterialTexturePathSet diffuse="world/maps/''' + name.lower() + '''/menuart/textures/''' + name.lower() + '''_coach_2.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4="" />
                                </textureSet>
                                <materialParams>
                                    <GFXMaterialSerializableParam Reflector_factor="0.000000" />
                                </materialParams>
                            </GFXMaterialSerializable>
                        </material>
                        <ENUM NAME="oldAnchor" SEL="6" />
                    </MaterialGraphicComponent>
                </COMPONENTS>
            </Actor>
        </ACTORS>
        <ACTORS NAME="Actor">
            <Actor RELATIVEZ="0.000000" SCALE="0.290211 0.290211" xFLIPPED="0" USERFRIENDLY="''' + name + '''_coach_3" MARKER="" POS2D="212.784500 663.680176" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
                <COMPONENTS NAME="MaterialGraphicComponent">
                    <MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="4294967295" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
                        <PrimitiveParameters>
                            <GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000">
                                <ENUM NAME="gfxOccludeInfo" SEL="0" />
                            </GFXPrimitiveParam>
                        </PrimitiveParameters>
                        <ENUM NAME="anchor" SEL="6" />
                        <material>
                            <GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/_common/matshader/multitexture_1layer.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
                                <textureSet>
                                    <GFXMaterialTexturePathSet diffuse="world/maps/''' + name.lower() + '''/menuart/textures/''' + name.lower() + '''_coach_3.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4="" />
                                </textureSet>
                                <materialParams>
                                    <GFXMaterialSerializableParam Reflector_factor="0.000000" />
                                </materialParams>
                            </GFXMaterialSerializable>
                        </material>
                        <ENUM NAME="oldAnchor" SEL="6" />
                    </MaterialGraphicComponent>
                </COMPONENTS>
            </Actor>
        </ACTORS>
        <ACTORS NAME="Actor">
            <Actor RELATIVEZ="0.000000" SCALE="256.000000 128.000000" xFLIPPED="0" USERFRIENDLY="''' + name + '''_map_bkg" MARKER="" POS2D="1487.410156 -32.732918" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
                <COMPONENTS NAME="MaterialGraphicComponent">
                    <MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="1" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
                        <PrimitiveParameters>
                            <GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000">
                                <ENUM NAME="gfxOccludeInfo" SEL="0" />
                            </GFXPrimitiveParam>
                        </PrimitiveParameters>
                        <ENUM NAME="anchor" SEL="1" />
                        <material>
                            <GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/_common/matshader/multitexture_1layer.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
                                <textureSet>
                                    <GFXMaterialTexturePathSet diffuse="world/maps/''' + name.lower() + '''/menuart/textures/''' + name.lower() + '''_map_bkg.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4="" />
                                </textureSet>
                                <materialParams>
                                    <GFXMaterialSerializableParam Reflector_factor="0.000000" />
                                </materialParams>
                            </GFXMaterialSerializable>
                        </material>
                        <ENUM NAME="oldAnchor" SEL="1" />
                    </MaterialGraphicComponent>
                </COMPONENTS>
            </Actor>
        </ACTORS>
        <sceneConfigs>
            <SceneConfigs activeSceneConfig="0" />
        </sceneConfigs>
    </Scene>
</root>''')
    if(coachnum == 4):
        menuartisc_content = ('''<?xml version="1.0" encoding="ISO-8859-1"?>
<root>
    <Scene ENGINE_VERSION="253653" GRIDUNIT="0.500000" DEPTH_SEPARATOR="0" NEAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" FAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" viewFamily="1">
        <ACTORS NAME="Actor">
            <Actor RELATIVEZ="0.000000" SCALE="0.300000 0.300000" xFLIPPED="0" USERFRIENDLY="''' + name + '''_cover_generic" MARKER="" POS2D="266.087555 197.629959" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
                <COMPONENTS NAME="MaterialGraphicComponent">
                    <MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="4294967295" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
                        <PrimitiveParameters>
                            <GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000">
                                <ENUM NAME="gfxOccludeInfo" SEL="0" />
                            </GFXPrimitiveParam>
                        </PrimitiveParameters>
                        <ENUM NAME="anchor" SEL="1" />
                        <material>
                            <GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/_common/matshader/multitexture_1layer.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
                                <textureSet>
                                    <GFXMaterialTexturePathSet diffuse="world/maps/''' + name.lower() + '''/menuart/textures/''' + name.lower() + '''_cover_generic.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4="" />
                                </textureSet>
                                <materialParams>
                                    <GFXMaterialSerializableParam Reflector_factor="0.000000" />
                                </materialParams>
                            </GFXMaterialSerializable>
                        </material>
                        <ENUM NAME="oldAnchor" SEL="1" />
                    </MaterialGraphicComponent>
                </COMPONENTS>
            </Actor>
        </ACTORS>
        <ACTORS NAME="Actor">
            <Actor RELATIVEZ="0.000000" SCALE="0.300000 0.300000" xFLIPPED="0" USERFRIENDLY="''' + name + '''_cover_online" MARKER="" POS2D="-150.000000 0.000000" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
                <COMPONENTS NAME="MaterialGraphicComponent">
                    <MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="4294967295" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
                        <PrimitiveParameters>
                            <GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000">
                                <ENUM NAME="gfxOccludeInfo" SEL="0" />
                            </GFXPrimitiveParam>
                        </PrimitiveParameters>
                        <ENUM NAME="anchor" SEL="1" />
                        <material>
                            <GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/_common/matshader/multitexture_1layer.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
                                <textureSet>
                                    <GFXMaterialTexturePathSet diffuse="world/maps/''' + name.lower() + '''/menuart/textures/''' + name.lower() + '''_cover_online.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4="" />
                                </textureSet>
                                <materialParams>
                                    <GFXMaterialSerializableParam Reflector_factor="0.000000" />
                                </materialParams>
                            </GFXMaterialSerializable>
                        </material>
                        <ENUM NAME="oldAnchor" SEL="1" />
                    </MaterialGraphicComponent>
                </COMPONENTS>
            </Actor>
        </ACTORS>
        <ACTORS NAME="Actor">
            <Actor RELATIVEZ="0.000000" SCALE="0.300000 0.300000" xFLIPPED="0" USERFRIENDLY="''' + name + '''_cover_albumcoach" MARKER="" POS2D="738.106323 359.612030" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
                <COMPONENTS NAME="MaterialGraphicComponent">
                    <MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="4294967295" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
                        <PrimitiveParameters>
                            <GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000">
                                <ENUM NAME="gfxOccludeInfo" SEL="0" />
                            </GFXPrimitiveParam>
                        </PrimitiveParameters>
                        <ENUM NAME="anchor" SEL="6" />
                        <material>
                            <GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/_common/matshader/multitexture_1layer.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
                                <textureSet>
                                    <GFXMaterialTexturePathSet diffuse="world/maps/''' + name.lower() + '''/menuart/textures/''' + name.lower() + '''_cover_albumcoach.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4="" />
                                </textureSet>
                                <materialParams>
                                    <GFXMaterialSerializableParam Reflector_factor="0.000000" />
                                </materialParams>
                            </GFXMaterialSerializable>
                        </material>
                        <ENUM NAME="oldAnchor" SEL="6" />
                    </MaterialGraphicComponent>
                </COMPONENTS>
            </Actor>
        </ACTORS>
        <ACTORS NAME="Actor">
            <Actor RELATIVEZ="0.000000" SCALE="0.300000 0.300000" xFLIPPED="0" USERFRIENDLY="''' + name + '''_cover_albumbkg" MARKER="" POS2D="1067.972168 201.986328" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
                <COMPONENTS NAME="MaterialGraphicComponent">
                    <MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="4294967295" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
                        <PrimitiveParameters>
                            <GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000">
                                <ENUM NAME="gfxOccludeInfo" SEL="0" />
                            </GFXPrimitiveParam>
                        </PrimitiveParameters>
                        <ENUM NAME="anchor" SEL="1" />
                        <material>
                            <GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/_common/matshader/multitexture_1layer.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
                                <textureSet>
                                    <GFXMaterialTexturePathSet diffuse="world/maps/''' + name.lower() + '''/menuart/textures/''' + name.lower() + '''_cover_albumbkg.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4="" />
                                </textureSet>
                                <materialParams>
                                    <GFXMaterialSerializableParam Reflector_factor="0.000000" />
                                </materialParams>
                            </GFXMaterialSerializable>
                        </material>
                        <ENUM NAME="oldAnchor" SEL="1" />
                    </MaterialGraphicComponent>
                </COMPONENTS>
            </Actor>
        </ACTORS>
        <ACTORS NAME="Actor">
            <Actor RELATIVEZ="0.000000" SCALE="0.290211 0.290211" xFLIPPED="0" USERFRIENDLY="''' + name + '''_coach_1" MARKER="" POS2D="212.784500 663.680176" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
                <COMPONENTS NAME="MaterialGraphicComponent">
                    <MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="4294967295" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
                        <PrimitiveParameters>
                            <GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000">
                                <ENUM NAME="gfxOccludeInfo" SEL="0" />
                            </GFXPrimitiveParam>
                        </PrimitiveParameters>
                        <ENUM NAME="anchor" SEL="6" />
                        <material>
                            <GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/_common/matshader/multitexture_1layer.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
                                <textureSet>
                                    <GFXMaterialTexturePathSet diffuse="world/maps/''' + name.lower() + '''/menuart/textures/''' + name.lower() + '''_coach_1.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4="" />
                                </textureSet>
                                <materialParams>
                                    <GFXMaterialSerializableParam Reflector_factor="0.000000" />
                                </materialParams>
                            </GFXMaterialSerializable>
                        </material>
                        <ENUM NAME="oldAnchor" SEL="6" />
                    </MaterialGraphicComponent>
                </COMPONENTS>
            </Actor>
        </ACTORS>
        <ACTORS NAME="Actor">
            <Actor RELATIVEZ="0.000000" SCALE="0.290211 0.290211" xFLIPPED="0" USERFRIENDLY="''' + name + '''_coach_2" MARKER="" POS2D="212.784500 663.680176" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
                <COMPONENTS NAME="MaterialGraphicComponent">
                    <MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="4294967295" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
                        <PrimitiveParameters>
                            <GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000">
                                <ENUM NAME="gfxOccludeInfo" SEL="0" />
                            </GFXPrimitiveParam>
                        </PrimitiveParameters>
                        <ENUM NAME="anchor" SEL="6" />
                        <material>
                            <GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/_common/matshader/multitexture_1layer.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
                                <textureSet>
                                    <GFXMaterialTexturePathSet diffuse="world/maps/''' + name.lower() + '''/menuart/textures/''' + name.lower() + '''_coach_2.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4="" />
                                </textureSet>
                                <materialParams>
                                    <GFXMaterialSerializableParam Reflector_factor="0.000000" />
                                </materialParams>
                            </GFXMaterialSerializable>
                        </material>
                        <ENUM NAME="oldAnchor" SEL="6" />
                    </MaterialGraphicComponent>
                </COMPONENTS>
            </Actor>
        </ACTORS>
        <ACTORS NAME="Actor">
            <Actor RELATIVEZ="0.000000" SCALE="0.290211 0.290211" xFLIPPED="0" USERFRIENDLY="''' + name + '''_coach_3" MARKER="" POS2D="212.784500 663.680176" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
                <COMPONENTS NAME="MaterialGraphicComponent">
                    <MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="4294967295" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
                        <PrimitiveParameters>
                            <GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000">
                                <ENUM NAME="gfxOccludeInfo" SEL="0" />
                            </GFXPrimitiveParam>
                        </PrimitiveParameters>
                        <ENUM NAME="anchor" SEL="6" />
                        <material>
                            <GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/_common/matshader/multitexture_1layer.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
                                <textureSet>
                                    <GFXMaterialTexturePathSet diffuse="world/maps/''' + name.lower() + '''/menuart/textures/''' + name.lower() + '''_coach_3.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4="" />
                                </textureSet>
                                <materialParams>
                                    <GFXMaterialSerializableParam Reflector_factor="0.000000" />
                                </materialParams>
                            </GFXMaterialSerializable>
                        </material>
                        <ENUM NAME="oldAnchor" SEL="6" />
                    </MaterialGraphicComponent>
                </COMPONENTS>
            </Actor>
        </ACTORS>
        <ACTORS NAME="Actor">
            <Actor RELATIVEZ="0.000000" SCALE="0.290211 0.290211" xFLIPPED="0" USERFRIENDLY="''' + name + '''_coach_4" MARKER="" POS2D="212.784500 663.680176" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
                <COMPONENTS NAME="MaterialGraphicComponent">
                    <MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="4294967295" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
                        <PrimitiveParameters>
                            <GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000">
                                <ENUM NAME="gfxOccludeInfo" SEL="0" />
                            </GFXPrimitiveParam>
                        </PrimitiveParameters>
                        <ENUM NAME="anchor" SEL="6" />
                        <material>
                            <GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/_common/matshader/multitexture_1layer.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
                                <textureSet>
                                    <GFXMaterialTexturePathSet diffuse="world/maps/''' + name.lower() + '''/menuart/textures/''' + name.lower() + '''_coach_4.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4="" />
                                </textureSet>
                                <materialParams>
                                    <GFXMaterialSerializableParam Reflector_factor="0.000000" />
                                </materialParams>
                            </GFXMaterialSerializable>
                        </material>
                        <ENUM NAME="oldAnchor" SEL="6" />
                    </MaterialGraphicComponent>
                </COMPONENTS>
            </Actor>
        </ACTORS>
        <ACTORS NAME="Actor">
            <Actor RELATIVEZ="0.000000" SCALE="256.000000 128.000000" xFLIPPED="0" USERFRIENDLY="''' + name + '''_map_bkg" MARKER="" POS2D="1487.410156 -32.732918" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
                <COMPONENTS NAME="MaterialGraphicComponent">
                    <MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="1" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
                        <PrimitiveParameters>
                            <GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000">
                                <ENUM NAME="gfxOccludeInfo" SEL="0" />
                            </GFXPrimitiveParam>
                        </PrimitiveParameters>
                        <ENUM NAME="anchor" SEL="1" />
                        <material>
                            <GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/_common/matshader/multitexture_1layer.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
                                <textureSet>
                                    <GFXMaterialTexturePathSet diffuse="world/maps/''' + name.lower() + '''/menuart/textures/''' + name.lower() + '''_map_bkg.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4="" />
                                </textureSet>
                                <materialParams>
                                    <GFXMaterialSerializableParam Reflector_factor="0.000000" />
                                </materialParams>
                            </GFXMaterialSerializable>
                        </material>
                        <ENUM NAME="oldAnchor" SEL="1" />
                    </MaterialGraphicComponent>
                </COMPONENTS>
            </Actor>
        </ACTORS>
        <sceneConfigs>
            <SceneConfigs activeSceneConfig="0" />
        </sceneConfigs>
    </Scene>
</root>''')
    menuartisc.write(menuartisc_content)
    menuartisc.close()
    #Menuart ISC

    #Timeline Files
    ##
    timelineisc = open(cache_timeline + name.lower() + "_tml.isc.ckd", "w", encoding="utf-8")
    timelineisc.write('''<?xml version="1.0" encoding="ISO-8859-1"?>
<root>
    <Scene ENGINE_VERSION="253653" GRIDUNIT="0.500000" DEPTH_SEPARATOR="0" NEAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" FAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" viewFamily="0">
        <ACTORS NAME="Actor">
            <Actor RELATIVEZ="0.000001" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="''' + name + '''_tml_dance" MARKER="" POS2D="-1.157740 0.006158" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="world/maps/''' + name.lower() + '''/timeline/''' + name.lower() + '''_tml_dance.tpl">
                <COMPONENTS NAME="TapeCase_Component">
                    <TapeCase_Component />
                </COMPONENTS>
            </Actor>
        </ACTORS>
        <ACTORS NAME="Actor">
            <Actor RELATIVEZ="0.000001" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="''' + name + '''_tml_karaoke" MARKER="" POS2D="-1.157740 0.006158" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="world/maps/''' + name.lower() + '''/timeline/''' + name.lower() + '''_tml_karaoke.tpl">
                <COMPONENTS NAME="TapeCase_Component">
                    <TapeCase_Component />
                </COMPONENTS>
            </Actor>
        </ACTORS>
        <sceneConfigs>
            <SceneConfigs activeSceneConfig="0" />
        </sceneConfigs>
    </Scene>
</root>''')
    timelineisc.close()
    ##

    ##
    dancetape = open(cache_timeline + name.lower() + "_tml_dance.tpl.ckd", "w", encoding="utf-8")
    dancetape.write('{"__class":"Actor_Template","WIP":0,"LOWUPDATE":0,"UPDATE_LAYER":0,"PROCEDURAL":0,"STARTPAUSED":0,"FORCEISENVIRONMENT":0,"COMPONENTS":[{"__class":"TapeCase_Template","TapesRack":[{"__class":"TapeGroup","Entries":[{"__class":"TapeEntry","Label":"TML_Motion","Path":"world/maps/' + name.lower() + '/timeline/' + name.lower() + '_tml_dance.dtape"}]}]}]}')
    dancetape.close()
    ##

    ##
    karaoketape = open(cache_timeline + name.lower() + "_tml_karaoke.tpl.ckd", "w", encoding="utf-8")
    karaoketape.write('{"__class":"Actor_Template","WIP":0,"LOWUPDATE":0,"UPDATE_LAYER":0,"PROCEDURAL":0,"STARTPAUSED":0,"FORCEISENVIRONMENT":0,"COMPONENTS":[{"__class":"TapeCase_Template","TapesRack":[{"__class":"TapeGroup","Entries":[{"__class":"TapeEntry","Label":"TML_karaoke","Path":"world/maps/' + name.lower() + '/timeline/' + name.lower() + '_tml_karaoke.ktape"}]}]}]}')
    karaoketape.close()
    ##
    #Timeline Files

    #VideosCoach ISC
    videoisc = open(cache_videoscoach + name.lower() + "_video.isc.ckd", "w", encoding="utf-8")
    videoisc.write('''<?xml version="1.0" encoding="ISO-8859-1"?>
<root>
    <Scene ENGINE_VERSION="253653" GRIDUNIT="0.500000" DEPTH_SEPARATOR="0" NEAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" FAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" viewFamily="0">
        <ACTORS NAME="Actor">
            <Actor RELATIVEZ="-1.000000" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="VideoScreen" MARKER="" POS2D="0.000000 -4.500000" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="world/_common/videoscreen/video_player_main.tpl">
                <COMPONENTS NAME="PleoComponent">
                    <PleoComponent video="world/maps/''' + name.lower() + '''/videoscoach/''' + name.lower() + '''.webm" dashMPD="world/maps/''' + name.lower() + '''/videoscoach/''' + name.lower() + '''.mpd" channelID="" />
                </COMPONENTS>
            </Actor>
        </ACTORS>
        <ACTORS NAME="Actor">
            <Actor RELATIVEZ="0.000000" SCALE="3.941238 2.220000" xFLIPPED="0" USERFRIENDLY="VideoOutput" MARKER="" POS2D="0.000000 0.000000" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="world/_common/videoscreen/video_output_main.tpl">
                <COMPONENTS NAME="PleoTextureGraphicComponent">
                    <PleoTextureGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="4294967295" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000" channelID="">
                        <PrimitiveParameters>
                            <GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000">
                                <ENUM NAME="gfxOccludeInfo" SEL="0" />
                            </GFXPrimitiveParam>
                        </PrimitiveParameters>
                        <ENUM NAME="anchor" SEL="1" />
                        <material>
                            <GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/_common/matshader/pleofullscreen.msh" stencilTest="0" alphaTest="0" alphaRef="0">
                                <textureSet>
                                    <GFXMaterialTexturePathSet diffuse="" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4="" />
                                </textureSet>
                                <materialParams>
                                    <GFXMaterialSerializableParam Reflector_factor="0.000000" />
                                </materialParams>
                            </GFXMaterialSerializable>
                        </material>
                        <ENUM NAME="oldAnchor" SEL="1" />
                    </PleoTextureGraphicComponent>
                </COMPONENTS>
            </Actor>
        </ACTORS>
        <sceneConfigs>
            <SceneConfigs activeSceneConfig="0" />
        </sceneConfigs>
    </Scene>
</root>''')
    videoisc.close()
    #VideosCoach ISC
    
    #VideosCoachPreview ISC
    videopreviewisc = open(cache_videoscoach + name.lower() + "_video_map_preview.isc.ckd", "w", encoding="utf-8")
    videopreviewisc.write('''<?xml version="1.0" encoding="ISO-8859-1"?>
<root>
   <Scene ENGINE_VERSION="284789" GRIDUNIT="0.500000" DEPTH_SEPARATOR="0" NEAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" FAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" viewFamily="0">
      <ACTORS NAME="Actor">
         <Actor RELATIVEZ="-1.000000" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="VideoScreen" MARKER="" DEFAULTENABLE="1" POS2D="0.000000 -4.500000" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="world/_common/videoscreen/video_player_map_preview.tpl">
            <COMPONENTS NAME="PleoComponent">
               <PleoComponent video="world/maps/''' + name.lower() + '''/videoscoach/''' + name.lower() + '''.webm" dashMPD="world/maps/''' + name.lower() + '''/videoscoach/''' + name.lower() + '''.mpd" channelID="''' + name + '''" />
            </COMPONENTS>
         </Actor>
      </ACTORS>
      <sceneConfigs>
         <SceneConfigs activeSceneConfig="0" />
      </sceneConfigs>
   </Scene>
</root>''')
    videopreviewisc.close()
    #VideosCoachPreview ISC

    #MAINSCENE ISC
    #MAINSCENE ISC
    #MAINSCENE ISC
    mainsceneisc = open(cache_path + name.lower() + "_main_scene.isc.ckd", "w", encoding="utf-8")
    mainsceneisc_content = ""
    if(coachnum == 1):
       mainsceneisc_content = ('''<?xml version="1.0" encoding="ISO-8859-1"?>
<root>
    <Scene ENGINE_VERSION="253653" GRIDUNIT="2.000000" DEPTH_SEPARATOR="0" NEAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" FAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" viewFamily="0">
        <PLATFORM_FILTER>
            <TargetFilterList platform="WII">
                <objects VAL="''' + name + '''_AUTODANCE" />
            </TargetFilterList>
        </PLATFORM_FILTER>
        <ACTORS NAME="SubSceneActor">
            <SubSceneActor RELATIVEZ="0.000000" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="''' + name + '''_AUDIO" MARKER="" POS2D="0.000000 0.000000" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/subscene.tpl" RELATIVEPATH="world/maps/''' + name.lower() + '''/audio/''' + name.lower() + '''_audio.isc" EMBED_SCENE="1" IS_SINGLE_PIECE="0" ZFORCED="1" DIRECT_PICKING="1" IGNORE_SAVE="0">
                <ENUM NAME="viewType" SEL="2" />
                <SCENE>
                    <Scene ENGINE_VERSION="253653" GRIDUNIT="0.500000" DEPTH_SEPARATOR="0" NEAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" FAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" viewFamily="0">
                        <ACTORS NAME="Actor">
                            <Actor RELATIVEZ="0.000000" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="MusicTrack" MARKER="" POS2D="1.125962 -0.418641" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="world/maps/''' + name.lower() + '''/audio/''' + name.lower() + '''_musictrack.tpl">
                                <COMPONENTS NAME="MusicTrackComponent">
                                    <MusicTrackComponent />
                                </COMPONENTS>
                            </Actor>
                        </ACTORS>
                        <ACTORS NAME="Actor">
                            <Actor RELATIVEZ="0.000001" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="''' + name + '''_sequence" MARKER="" POS2D="-0.006158 -0.006158" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="world/maps/''' + name.lower() + '''/audio/''' + name.lower() + '''_sequence.tpl">
                                <COMPONENTS NAME="TapeCase_Component">
                                    <TapeCase_Component />
                                </COMPONENTS>
                            </Actor>
                        </ACTORS>
                        <sceneConfigs>
                            <SceneConfigs activeSceneConfig="0" />
                        </sceneConfigs>
                    </Scene>
                </SCENE>
            </SubSceneActor>
        </ACTORS>
        <ACTORS NAME="SubSceneActor">
            <SubSceneActor RELATIVEZ="0.000000" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="''' + name + '''_CINE" MARKER="" POS2D="0.000000 0.000000" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/subscene.tpl" RELATIVEPATH="world/maps/''' + name.lower() + '''/cinematics/''' + name.lower() + '''_cine.isc" EMBED_SCENE="1" IS_SINGLE_PIECE="0" ZFORCED="1" DIRECT_PICKING="1" IGNORE_SAVE="0">
                <ENUM NAME="viewType" SEL="2" />
                <SCENE>
                    <Scene ENGINE_VERSION="253653" GRIDUNIT="0.500000" DEPTH_SEPARATOR="0" NEAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" FAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" viewFamily="0">
                        <ACTORS NAME="Actor">
                            <Actor RELATIVEZ="0.000000" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="''' + name + '''_MainSequence" MARKER="" POS2D="0.000000 0.000000" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="world/maps/''' + name.lower() + '''/cinematics/''' + name.lower() + '''_mainsequence.tpl">
                                <COMPONENTS NAME="MasterTape">
                                    <MasterTape />
                                </COMPONENTS>
                            </Actor>
                        </ACTORS>
                        <sceneConfigs>
                            <SceneConfigs activeSceneConfig="0" />
                        </sceneConfigs>
                    </Scene>
                </SCENE>
            </SubSceneActor>
        </ACTORS>
        <ACTORS NAME="SubSceneActor">
            <SubSceneActor RELATIVEZ="0.000000" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="''' + name + '''_GRAPH" MARKER="" POS2D="0.000000 0.000000" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/subscene.tpl" RELATIVEPATH="world/maps/''' + name.lower() + '''/graph/''' + name.lower() + '''_graph.isc" EMBED_SCENE="1" IS_SINGLE_PIECE="0" ZFORCED="1" DIRECT_PICKING="1" IGNORE_SAVE="0">
                <ENUM NAME="viewType" SEL="2" />
                <SCENE>
                    <Scene ENGINE_VERSION="253653" GRIDUNIT="0.500000" DEPTH_SEPARATOR="0" NEAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" FAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" viewFamily="0">
                        <ACTORS NAME="Actor">
                            <Actor RELATIVEZ="10.000000" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="Camera_JD_Dummy" MARKER="" POS2D="0.000000 0.000000" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/tpl_emptyactor.tpl" />
                        </ACTORS>
                        <sceneConfigs>
                            <SceneConfigs activeSceneConfig="0" />
                        </sceneConfigs>
                    </Scene>
                </SCENE>
            </SubSceneActor>
        </ACTORS>
        <ACTORS NAME="SubSceneActor">
            <SubSceneActor RELATIVEZ="0.000000" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="''' + name + '''_TML" MARKER="" POS2D="0.000000 0.000000" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/subscene.tpl" RELATIVEPATH="world/maps/''' + name.lower() + '''/timeline/''' + name.lower() + '''_tml.isc" EMBED_SCENE="1" IS_SINGLE_PIECE="0" ZFORCED="1" DIRECT_PICKING="1" IGNORE_SAVE="0">
                <ENUM NAME="viewType" SEL="2" />
                <SCENE>
                    <Scene ENGINE_VERSION="253653" GRIDUNIT="0.500000" DEPTH_SEPARATOR="0" NEAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" FAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" viewFamily="0">
                        <ACTORS NAME="Actor">
                            <Actor RELATIVEZ="0.000001" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="''' + name + '''_tml_dance" MARKER="" POS2D="-1.157740 0.006158" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="world/maps/''' + name.lower() + '''/timeline/''' + name.lower() + '''_tml_dance.tpl">
                                <COMPONENTS NAME="TapeCase_Component">
                                    <TapeCase_Component />
                                </COMPONENTS>
                            </Actor>
                        </ACTORS>
                        <ACTORS NAME="Actor">
                            <Actor RELATIVEZ="0.000001" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="''' + name + '''_tml_karaoke" MARKER="" POS2D="-1.157740 0.006158" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="world/maps/''' + name.lower() + '''/timeline/''' + name.lower() + '''_tml_karaoke.tpl">
                                <COMPONENTS NAME="TapeCase_Component">
                                    <TapeCase_Component />
                                </COMPONENTS>
                            </Actor>
                        </ACTORS>
                        <sceneConfigs>
                            <SceneConfigs activeSceneConfig="0" />
                        </sceneConfigs>
                    </Scene>
                </SCENE>
            </SubSceneActor>
        </ACTORS>
        <ACTORS NAME="SubSceneActor">
            <SubSceneActor RELATIVEZ="0.000000" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="''' + name + '''_VIDEO" MARKER="" POS2D="0.000000 0.000000" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/subscene.tpl" RELATIVEPATH="world/maps/''' + name.lower() + '''/videoscoach/''' + name.lower() + '''_video.isc" EMBED_SCENE="1" IS_SINGLE_PIECE="0" ZFORCED="1" DIRECT_PICKING="1" IGNORE_SAVE="0">
                <ENUM NAME="viewType" SEL="2" />
                <SCENE>
                    <Scene ENGINE_VERSION="253653" GRIDUNIT="0.500000" DEPTH_SEPARATOR="0" NEAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" FAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" viewFamily="0">
                        <ACTORS NAME="Actor">
                            <Actor RELATIVEZ="-1.000000" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="VideoScreen" MARKER="" POS2D="0.000000 -4.500000" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="world/_common/videoscreen/video_player_main.tpl">
                                <COMPONENTS NAME="PleoComponent">
                                    <PleoComponent video="world/maps/''' + name.lower() + '''/videoscoach/''' + name.lower() + '''.webm" dashMPD="world/maps/''' + name.lower() + '''/videoscoach/''' + name.lower() + '''.mpd" channelID="" />
                                </COMPONENTS>
                            </Actor>
                        </ACTORS>
                        <ACTORS NAME="Actor">
                            <Actor RELATIVEZ="0.000000" SCALE="3.941238 2.220000" xFLIPPED="0" USERFRIENDLY="VideoOutput" MARKER="" POS2D="0.000000 0.000000" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="world/_common/videoscreen/video_output_main.tpl">
                                <COMPONENTS NAME="PleoTextureGraphicComponent">
                                    <PleoTextureGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="4294967295" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000" channelID="">
                                        <PrimitiveParameters>
                                            <GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000">
                                                <ENUM NAME="gfxOccludeInfo" SEL="0" />
                                            </GFXPrimitiveParam>
                                        </PrimitiveParameters>
                                        <ENUM NAME="anchor" SEL="1" />
                                        <material>
                                            <GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/_common/matshader/pleofullscreen.msh" stencilTest="0" alphaTest="0" alphaRef="0">
                                                <textureSet>
                                                    <GFXMaterialTexturePathSet diffuse="" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4="" />
                                                </textureSet>
                                                <materialParams>
                                                    <GFXMaterialSerializableParam Reflector_factor="0.000000" />
                                                </materialParams>
                                            </GFXMaterialSerializable>
                                        </material>
                                        <ENUM NAME="oldAnchor" SEL="1" />
                                    </PleoTextureGraphicComponent>
                                </COMPONENTS>
                            </Actor>
                        </ACTORS>
                        <sceneConfigs>
                            <SceneConfigs activeSceneConfig="0" />
                        </sceneConfigs>
                    </Scene>
                </SCENE>
            </SubSceneActor>
        </ACTORS>
        <ACTORS NAME="Actor">
            <Actor RELATIVEZ="0.000000" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="''' + name + ''' : Template Artist - Template Title&#10;JDVer = 5, ID = 842776738, Type = 1 (Flags 0x00000000), NbCoach = 2, Difficulty = 2" MARKER="" POS2D="-3.531976 -1.485322" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="world/maps/''' + name.lower() + '''/songdesc.tpl">
                <COMPONENTS NAME="JD_SongDescComponent">
                    <JD_SongDescComponent />
                </COMPONENTS>
            </Actor>
        </ACTORS>
        <ACTORS NAME="SubSceneActor">
            <SubSceneActor RELATIVEZ="0.000000" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="''' + name + '''_menuart" MARKER="" POS2D="0.000000 0.000000" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/subscene.tpl" RELATIVEPATH="world/maps/''' + name.lower() + '''/menuart/''' + name.lower() + '''_menuart.isc" EMBED_SCENE="1" IS_SINGLE_PIECE="0" ZFORCED="1" DIRECT_PICKING="1" IGNORE_SAVE="0">
                <ENUM NAME="viewType" SEL="3" />
                <SCENE>
                    <Scene ENGINE_VERSION="253653" GRIDUNIT="0.500000" DEPTH_SEPARATOR="0" NEAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" FAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" viewFamily="1">
                        <ACTORS NAME="Actor">
                            <Actor RELATIVEZ="0.000000" SCALE="0.300000 0.300000" xFLIPPED="0" USERFRIENDLY="''' + name + '''_cover_generic" MARKER="" POS2D="266.087555 197.629959" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
                                <COMPONENTS NAME="MaterialGraphicComponent">
                                    <MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="4294967295" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
                                        <PrimitiveParameters>
                                            <GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000">
                                                <ENUM NAME="gfxOccludeInfo" SEL="0" />
                                            </GFXPrimitiveParam>
                                        </PrimitiveParameters>
                                        <ENUM NAME="anchor" SEL="1" />
                                        <material>
                                            <GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/ui/materials/alpha_mul_b.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
                                                <textureSet>
                                                    <GFXMaterialTexturePathSet diffuse="world/maps/''' + name.lower() + '''/menuart/textures/''' + name.lower() + '''_cover_generic.tga" back_light="" normal="" separateAlpha="" diffuse_2="world/ui/textures/mask_square.tga" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4="" />
                                                </textureSet>
                                                <materialParams>
                                                    <GFXMaterialSerializableParam Reflector_factor="0.000000" />
                                                </materialParams>
                                            </GFXMaterialSerializable>
                                        </material>
                                        <ENUM NAME="oldAnchor" SEL="1" />
                                    </MaterialGraphicComponent>
                                </COMPONENTS>
                            </Actor>
                        </ACTORS>
                        <ACTORS NAME="Actor">
                            <Actor RELATIVEZ="0.000000" SCALE="0.300000 0.300000" xFLIPPED="0" USERFRIENDLY="''' + name + '''_cover_online" MARKER="" POS2D="-150.000000 0.000000" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
                                <COMPONENTS NAME="MaterialGraphicComponent">
                                    <MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="4294967295" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
                                        <PrimitiveParameters>
                                            <GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000">
                                                <ENUM NAME="gfxOccludeInfo" SEL="0" />
                                            </GFXPrimitiveParam>
                                        </PrimitiveParameters>
                                        <ENUM NAME="anchor" SEL="1" />
                                        <material>
                                            <GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/ui/materials/alpha_mul_b.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
                                                <textureSet>
                                                    <GFXMaterialTexturePathSet diffuse="world/maps/''' + name.lower() + '''/menuart/textures/''' + name.lower() + '''_cover_online.tga" back_light="" normal="" separateAlpha="" diffuse_2="world/ui/textures/mask_square.tga" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4="" />
                                                </textureSet>
                                                <materialParams>
                                                    <GFXMaterialSerializableParam Reflector_factor="0.000000" />
                                                </materialParams>
                                            </GFXMaterialSerializable>
                                        </material>
                                        <ENUM NAME="oldAnchor" SEL="1" />
                                    </MaterialGraphicComponent>
                                </COMPONENTS>
                            </Actor>
                        </ACTORS>
                        <ACTORS NAME="Actor">
                            <Actor RELATIVEZ="0.000000" SCALE="0.300000 0.300000" xFLIPPED="0" USERFRIENDLY="''' + name + '''_cover_albumcoach" MARKER="" POS2D="738.106323 359.612030" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
                                <COMPONENTS NAME="MaterialGraphicComponent">
                                    <MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="4294967295" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
                                        <PrimitiveParameters>
                                            <GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000">
                                                <ENUM NAME="gfxOccludeInfo" SEL="0" />
                                            </GFXPrimitiveParam>
                                        </PrimitiveParameters>
                                        <ENUM NAME="anchor" SEL="6" />
                                        <material>
                                            <GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/ui/materials/alpha.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
                                                <textureSet>
                                                    <GFXMaterialTexturePathSet diffuse="world/maps/''' + name.lower() + '''/menuart/textures/''' + name.lower() + '''_cover_albumcoach.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4="" />
                                                </textureSet>
                                                <materialParams>
                                                    <GFXMaterialSerializableParam Reflector_factor="0.000000" />
                                                </materialParams>
                                            </GFXMaterialSerializable>
                                        </material>
                                        <ENUM NAME="oldAnchor" SEL="6" />
                                    </MaterialGraphicComponent>
                                </COMPONENTS>
                            </Actor>
                        </ACTORS>
                        <ACTORS NAME="Actor">
                            <Actor RELATIVEZ="0.000000" SCALE="0.300000 0.300000" xFLIPPED="0" USERFRIENDLY="''' + name + '''_cover_albumbkg" MARKER="" POS2D="1067.972168 201.986328" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
                                <COMPONENTS NAME="MaterialGraphicComponent">
                                    <MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="4294967295" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
                                        <PrimitiveParameters>
                                            <GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000">
                                                <ENUM NAME="gfxOccludeInfo" SEL="0" />
                                            </GFXPrimitiveParam>
                                        </PrimitiveParameters>
                                        <ENUM NAME="anchor" SEL="1" />
                                        <material>
                                            <GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/ui/materials/alpha_mul_b.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
                                                <textureSet>
                                                    <GFXMaterialTexturePathSet diffuse="world/maps/''' + name.lower() + '''/menuart/textures/''' + name.lower() + '''_cover_albumbkg.tga" back_light="" normal="" separateAlpha="" diffuse_2="world/ui/textures/mask_square.tga" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4="" />
                                                </textureSet>
                                                <materialParams>
                                                    <GFXMaterialSerializableParam Reflector_factor="0.000000" />
                                                </materialParams>
                                            </GFXMaterialSerializable>
                                        </material>
                                        <ENUM NAME="oldAnchor" SEL="1" />
                                    </MaterialGraphicComponent>
                                </COMPONENTS>
                            </Actor>
                        </ACTORS>
                        <ACTORS NAME="Actor">
                            <Actor RELATIVEZ="0.000000" SCALE="0.290211 0.290211" xFLIPPED="0" USERFRIENDLY="''' + name + '''_coach_1" MARKER="" POS2D="212.784500 663.680176" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
                                <COMPONENTS NAME="MaterialGraphicComponent">
                                    <MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="4294967295" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
                                        <PrimitiveParameters>
                                            <GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000">
                                                <ENUM NAME="gfxOccludeInfo" SEL="0" />
                                            </GFXPrimitiveParam>
                                        </PrimitiveParameters>
                                        <ENUM NAME="anchor" SEL="6" />
                                        <material>
                                            <GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/ui/materials/alpha.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
                                                <textureSet>
                                                    <GFXMaterialTexturePathSet diffuse="world/maps/''' + name.lower() + '''/menuart/textures/''' + name.lower() + '''_coach_1.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4="" />
                                                </textureSet>
                                                <materialParams>
                                                    <GFXMaterialSerializableParam Reflector_factor="0.000000" />
                                                </materialParams>
                                            </GFXMaterialSerializable>
                                        </material>
                                        <ENUM NAME="oldAnchor" SEL="6" />
                                    </MaterialGraphicComponent>
                                </COMPONENTS>
                            </Actor>
                        </ACTORS>
                        <ACTORS NAME="Actor">
                            <Actor RELATIVEZ="0.000000" SCALE="256.000000 128.000000" xFLIPPED="0" USERFRIENDLY="''' + name + '''_map_bkg" MARKER="" POS2D="1487.410156 -32.732918" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
                                <COMPONENTS NAME="MaterialGraphicComponent">
                                    <MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="1" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
                                        <PrimitiveParameters>
                                            <GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000">
                                                <ENUM NAME="gfxOccludeInfo" SEL="0" />
                                            </GFXPrimitiveParam>
                                        </PrimitiveParameters>
                                        <ENUM NAME="anchor" SEL="1" />
                                        <material>
                                            <GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/_common/matshader/multitexture_1layer.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
                                                <textureSet>
                                                    <GFXMaterialTexturePathSet diffuse="world/maps/''' + name.lower() + '''/menuart/textures/''' + name.lower() + '''_map_bkg.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4="" />
                                                </textureSet>
                                                <materialParams>
                                                    <GFXMaterialSerializableParam Reflector_factor="0.000000" />
                                                </materialParams>
                                            </GFXMaterialSerializable>
                                        </material>
                                        <ENUM NAME="oldAnchor" SEL="1" />
                                    </MaterialGraphicComponent>
                                </COMPONENTS>
                            </Actor>
                        </ACTORS>
                        <sceneConfigs>
                            <SceneConfigs activeSceneConfig="0" />
                        </sceneConfigs>
                    </Scene>
                </SCENE>
            </SubSceneActor>
        </ACTORS>
        <ACTORS NAME="SubSceneActor">
            <SubSceneActor RELATIVEZ="0.000000" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="''' + name + '''_AUTODANCE" MARKER="" POS2D="0.000000 -0.033823" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/subscene.tpl" RELATIVEPATH="world/maps/''' + name.lower() + '''/autodance/''' + name.lower() + '''_autodance.isc" EMBED_SCENE="1" IS_SINGLE_PIECE="0" ZFORCED="1" DIRECT_PICKING="1" IGNORE_SAVE="0">
                <ENUM NAME="viewType" SEL="2" />
                <SCENE>
                    <Scene ENGINE_VERSION="253653" GRIDUNIT="0.500000" DEPTH_SEPARATOR="0" NEAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" FAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" viewFamily="0">
                        <ACTORS NAME="Actor">
                            <Actor RELATIVEZ="0.000000" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="''' + name + '''_autodance" MARKER="" POS2D="-0.006150 -0.003075" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="world/maps/''' + name.lower() + '''/autodance/''' + name.lower() + '''_autodance.tpl">
                                <COMPONENTS NAME="JD_AutodanceComponent">
                                    <JD_AutodanceComponent />
                                </COMPONENTS>
                            </Actor>
                        </ACTORS>
                        <sceneConfigs>
                            <SceneConfigs activeSceneConfig="0" />
                        </sceneConfigs>
                    </Scene>
                </SCENE>
            </SubSceneActor>
        </ACTORS>
        <sceneConfigs>
            <SceneConfigs activeSceneConfig="0">
                <sceneConfigs NAME="JD_MapSceneConfig">
                    <JD_MapSceneConfig name="" soundContext="" hud="0" phoneTitleLocId="4294967295" phoneImage="">
                        <ENUM NAME="Pause_Level" SEL="6" />
                        <ENUM NAME="type" SEL="1" />
                        <ENUM NAME="musicscore" SEL="2" />
                    </JD_MapSceneConfig>
                </sceneConfigs>
            </SceneConfigs>
        </sceneConfigs>
    </Scene>
</root>''')
    if(coachnum == 2):
        mainsceneisc_content = ('''<?xml version="1.0" encoding="ISO-8859-1"?>
<root>
    <Scene ENGINE_VERSION="253653" GRIDUNIT="2.000000" DEPTH_SEPARATOR="0" NEAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" FAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" viewFamily="0">
        <PLATFORM_FILTER>
            <TargetFilterList platform="WII">
                <objects VAL="''' + name + '''_AUTODANCE" />
            </TargetFilterList>
        </PLATFORM_FILTER>
        <ACTORS NAME="SubSceneActor">
            <SubSceneActor RELATIVEZ="0.000000" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="''' + name + '''_AUDIO" MARKER="" POS2D="0.000000 0.000000" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/subscene.tpl" RELATIVEPATH="world/maps/''' + name.lower() + '''/audio/''' + name.lower() + '''_audio.isc" EMBED_SCENE="1" IS_SINGLE_PIECE="0" ZFORCED="1" DIRECT_PICKING="1" IGNORE_SAVE="0">
                <ENUM NAME="viewType" SEL="2" />
                <SCENE>
                    <Scene ENGINE_VERSION="253653" GRIDUNIT="0.500000" DEPTH_SEPARATOR="0" NEAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" FAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" viewFamily="0">
                        <ACTORS NAME="Actor">
                            <Actor RELATIVEZ="0.000000" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="MusicTrack" MARKER="" POS2D="1.125962 -0.418641" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="world/maps/''' + name.lower() + '''/audio/''' + name.lower() + '''_musictrack.tpl">
                                <COMPONENTS NAME="MusicTrackComponent">
                                    <MusicTrackComponent />
                                </COMPONENTS>
                            </Actor>
                        </ACTORS>
                        <ACTORS NAME="Actor">
                            <Actor RELATIVEZ="0.000001" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="''' + name + '''_sequence" MARKER="" POS2D="-0.006158 -0.006158" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="world/maps/''' + name.lower() + '''/audio/''' + name.lower() + '''_sequence.tpl">
                                <COMPONENTS NAME="TapeCase_Component">
                                    <TapeCase_Component />
                                </COMPONENTS>
                            </Actor>
                        </ACTORS>
                        <sceneConfigs>
                            <SceneConfigs activeSceneConfig="0" />
                        </sceneConfigs>
                    </Scene>
                </SCENE>
            </SubSceneActor>
        </ACTORS>
        <ACTORS NAME="SubSceneActor">
            <SubSceneActor RELATIVEZ="0.000000" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="''' + name + '''_CINE" MARKER="" POS2D="0.000000 0.000000" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/subscene.tpl" RELATIVEPATH="world/maps/''' + name.lower() + '''/cinematics/''' + name.lower() + '''_cine.isc" EMBED_SCENE="1" IS_SINGLE_PIECE="0" ZFORCED="1" DIRECT_PICKING="1" IGNORE_SAVE="0">
                <ENUM NAME="viewType" SEL="2" />
                <SCENE>
                    <Scene ENGINE_VERSION="253653" GRIDUNIT="0.500000" DEPTH_SEPARATOR="0" NEAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" FAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" viewFamily="0">
                        <ACTORS NAME="Actor">
                            <Actor RELATIVEZ="0.000000" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="''' + name + '''_MainSequence" MARKER="" POS2D="0.000000 0.000000" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="world/maps/''' + name.lower() + '''/cinematics/''' + name.lower() + '''_mainsequence.tpl">
                                <COMPONENTS NAME="MasterTape">
                                    <MasterTape />
                                </COMPONENTS>
                            </Actor>
                        </ACTORS>
                        <sceneConfigs>
                            <SceneConfigs activeSceneConfig="0" />
                        </sceneConfigs>
                    </Scene>
                </SCENE>
            </SubSceneActor>
        </ACTORS>
        <ACTORS NAME="SubSceneActor">
            <SubSceneActor RELATIVEZ="0.000000" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="''' + name + '''_GRAPH" MARKER="" POS2D="0.000000 0.000000" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/subscene.tpl" RELATIVEPATH="world/maps/''' + name.lower() + '''/graph/''' + name.lower() + '''_graph.isc" EMBED_SCENE="1" IS_SINGLE_PIECE="0" ZFORCED="1" DIRECT_PICKING="1" IGNORE_SAVE="0">
                <ENUM NAME="viewType" SEL="2" />
                <SCENE>
                    <Scene ENGINE_VERSION="253653" GRIDUNIT="0.500000" DEPTH_SEPARATOR="0" NEAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" FAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" viewFamily="0">
                        <ACTORS NAME="Actor">
                            <Actor RELATIVEZ="10.000000" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="Camera_JD_Dummy" MARKER="" POS2D="0.000000 0.000000" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/tpl_emptyactor.tpl" />
                        </ACTORS>
                        <sceneConfigs>
                            <SceneConfigs activeSceneConfig="0" />
                        </sceneConfigs>
                    </Scene>
                </SCENE>
            </SubSceneActor>
        </ACTORS>
        <ACTORS NAME="SubSceneActor">
            <SubSceneActor RELATIVEZ="0.000000" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="''' + name + '''_TML" MARKER="" POS2D="0.000000 0.000000" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/subscene.tpl" RELATIVEPATH="world/maps/''' + name.lower() + '''/timeline/''' + name.lower() + '''_tml.isc" EMBED_SCENE="1" IS_SINGLE_PIECE="0" ZFORCED="1" DIRECT_PICKING="1" IGNORE_SAVE="0">
                <ENUM NAME="viewType" SEL="2" />
                <SCENE>
                    <Scene ENGINE_VERSION="253653" GRIDUNIT="0.500000" DEPTH_SEPARATOR="0" NEAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" FAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" viewFamily="0">
                        <ACTORS NAME="Actor">
                            <Actor RELATIVEZ="0.000001" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="''' + name + '''_tml_dance" MARKER="" POS2D="-1.157740 0.006158" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="world/maps/''' + name.lower() + '''/timeline/''' + name.lower() + '''_tml_dance.tpl">
                                <COMPONENTS NAME="TapeCase_Component">
                                    <TapeCase_Component />
                                </COMPONENTS>
                            </Actor>
                        </ACTORS>
                        <ACTORS NAME="Actor">
                            <Actor RELATIVEZ="0.000001" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="''' + name + '''_tml_karaoke" MARKER="" POS2D="-1.157740 0.006158" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="world/maps/''' + name.lower() + '''/timeline/''' + name.lower() + '''_tml_karaoke.tpl">
                                <COMPONENTS NAME="TapeCase_Component">
                                    <TapeCase_Component />
                                </COMPONENTS>
                            </Actor>
                        </ACTORS>
                        <sceneConfigs>
                            <SceneConfigs activeSceneConfig="0" />
                        </sceneConfigs>
                    </Scene>
                </SCENE>
            </SubSceneActor>
        </ACTORS>
        <ACTORS NAME="SubSceneActor">
            <SubSceneActor RELATIVEZ="0.000000" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="''' + name + '''_VIDEO" MARKER="" POS2D="0.000000 0.000000" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/subscene.tpl" RELATIVEPATH="world/maps/''' + name.lower() + '''/videoscoach/''' + name.lower() + '''_video.isc" EMBED_SCENE="1" IS_SINGLE_PIECE="0" ZFORCED="1" DIRECT_PICKING="1" IGNORE_SAVE="0">
                <ENUM NAME="viewType" SEL="2" />
                <SCENE>
                    <Scene ENGINE_VERSION="253653" GRIDUNIT="0.500000" DEPTH_SEPARATOR="0" NEAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" FAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" viewFamily="0">
                        <ACTORS NAME="Actor">
                            <Actor RELATIVEZ="-1.000000" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="VideoScreen" MARKER="" POS2D="0.000000 -4.500000" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="world/_common/videoscreen/video_player_main.tpl">
                                <COMPONENTS NAME="PleoComponent">
                                    <PleoComponent video="world/maps/''' + name.lower() + '''/videoscoach/''' + name.lower() + '''.webm" dashMPD="world/maps/''' + name.lower() + '''/videoscoach/''' + name.lower() + '''.mpd" channelID="" />
                                </COMPONENTS>
                            </Actor>
                        </ACTORS>
                        <ACTORS NAME="Actor">
                            <Actor RELATIVEZ="0.000000" SCALE="3.941238 2.220000" xFLIPPED="0" USERFRIENDLY="VideoOutput" MARKER="" POS2D="0.000000 0.000000" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="world/_common/videoscreen/video_output_main.tpl">
                                <COMPONENTS NAME="PleoTextureGraphicComponent">
                                    <PleoTextureGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="4294967295" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000" channelID="">
                                        <PrimitiveParameters>
                                            <GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000">
                                                <ENUM NAME="gfxOccludeInfo" SEL="0" />
                                            </GFXPrimitiveParam>
                                        </PrimitiveParameters>
                                        <ENUM NAME="anchor" SEL="1" />
                                        <material>
                                            <GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/_common/matshader/pleofullscreen.msh" stencilTest="0" alphaTest="0" alphaRef="0">
                                                <textureSet>
                                                    <GFXMaterialTexturePathSet diffuse="" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4="" />
                                                </textureSet>
                                                <materialParams>
                                                    <GFXMaterialSerializableParam Reflector_factor="0.000000" />
                                                </materialParams>
                                            </GFXMaterialSerializable>
                                        </material>
                                        <ENUM NAME="oldAnchor" SEL="1" />
                                    </PleoTextureGraphicComponent>
                                </COMPONENTS>
                            </Actor>
                        </ACTORS>
                        <sceneConfigs>
                            <SceneConfigs activeSceneConfig="0" />
                        </sceneConfigs>
                    </Scene>
                </SCENE>
            </SubSceneActor>
        </ACTORS>
        <ACTORS NAME="Actor">
            <Actor RELATIVEZ="0.000000" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="''' + name + ''' : Template Artist - Template Title&#10;JDVer = 5, ID = 842776738, Type = 1 (Flags 0x00000000), NbCoach = 2, Difficulty = 2" MARKER="" POS2D="-3.531976 -1.485322" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="world/maps/''' + name.lower() + '''/songdesc.tpl">
                <COMPONENTS NAME="JD_SongDescComponent">
                    <JD_SongDescComponent />
                </COMPONENTS>
            </Actor>
        </ACTORS>
        <ACTORS NAME="SubSceneActor">
            <SubSceneActor RELATIVEZ="0.000000" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="''' + name + '''_menuart" MARKER="" POS2D="0.000000 0.000000" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/subscene.tpl" RELATIVEPATH="world/maps/''' + name.lower() + '''/menuart/''' + name.lower() + '''_menuart.isc" EMBED_SCENE="1" IS_SINGLE_PIECE="0" ZFORCED="1" DIRECT_PICKING="1" IGNORE_SAVE="0">
                <ENUM NAME="viewType" SEL="3" />
                <SCENE>
                    <Scene ENGINE_VERSION="253653" GRIDUNIT="0.500000" DEPTH_SEPARATOR="0" NEAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" FAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" viewFamily="1">
                        <ACTORS NAME="Actor">
                            <Actor RELATIVEZ="0.000000" SCALE="0.300000 0.300000" xFLIPPED="0" USERFRIENDLY="''' + name + '''_cover_generic" MARKER="" POS2D="266.087555 197.629959" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
                                <COMPONENTS NAME="MaterialGraphicComponent">
                                    <MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="4294967295" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
                                        <PrimitiveParameters>
                                            <GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000">
                                                <ENUM NAME="gfxOccludeInfo" SEL="0" />
                                            </GFXPrimitiveParam>
                                        </PrimitiveParameters>
                                        <ENUM NAME="anchor" SEL="1" />
                                        <material>
                                            <GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/ui/materials/alpha_mul_b.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
                                                <textureSet>
                                                    <GFXMaterialTexturePathSet diffuse="world/maps/''' + name.lower() + '''/menuart/textures/''' + name.lower() + '''_cover_generic.tga" back_light="" normal="" separateAlpha="" diffuse_2="world/ui/textures/mask_square.tga" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4="" />
                                                </textureSet>
                                                <materialParams>
                                                    <GFXMaterialSerializableParam Reflector_factor="0.000000" />
                                                </materialParams>
                                            </GFXMaterialSerializable>
                                        </material>
                                        <ENUM NAME="oldAnchor" SEL="1" />
                                    </MaterialGraphicComponent>
                                </COMPONENTS>
                            </Actor>
                        </ACTORS>
                        <ACTORS NAME="Actor">
                            <Actor RELATIVEZ="0.000000" SCALE="0.300000 0.300000" xFLIPPED="0" USERFRIENDLY="''' + name + '''_cover_online" MARKER="" POS2D="-150.000000 0.000000" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
                                <COMPONENTS NAME="MaterialGraphicComponent">
                                    <MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="4294967295" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
                                        <PrimitiveParameters>
                                            <GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000">
                                                <ENUM NAME="gfxOccludeInfo" SEL="0" />
                                            </GFXPrimitiveParam>
                                        </PrimitiveParameters>
                                        <ENUM NAME="anchor" SEL="1" />
                                        <material>
                                            <GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/ui/materials/alpha_mul_b.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
                                                <textureSet>
                                                    <GFXMaterialTexturePathSet diffuse="world/maps/''' + name.lower() + '''/menuart/textures/''' + name.lower() + '''_cover_online.tga" back_light="" normal="" separateAlpha="" diffuse_2="world/ui/textures/mask_square.tga" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4="" />
                                                </textureSet>
                                                <materialParams>
                                                    <GFXMaterialSerializableParam Reflector_factor="0.000000" />
                                                </materialParams>
                                            </GFXMaterialSerializable>
                                        </material>
                                        <ENUM NAME="oldAnchor" SEL="1" />
                                    </MaterialGraphicComponent>
                                </COMPONENTS>
                            </Actor>
                        </ACTORS>
                        <ACTORS NAME="Actor">
                            <Actor RELATIVEZ="0.000000" SCALE="0.300000 0.300000" xFLIPPED="0" USERFRIENDLY="''' + name + '''_cover_albumcoach" MARKER="" POS2D="738.106323 359.612030" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
                                <COMPONENTS NAME="MaterialGraphicComponent">
                                    <MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="4294967295" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
                                        <PrimitiveParameters>
                                            <GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000">
                                                <ENUM NAME="gfxOccludeInfo" SEL="0" />
                                            </GFXPrimitiveParam>
                                        </PrimitiveParameters>
                                        <ENUM NAME="anchor" SEL="6" />
                                        <material>
                                            <GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/ui/materials/alpha.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
                                                <textureSet>
                                                    <GFXMaterialTexturePathSet diffuse="world/maps/''' + name.lower() + '''/menuart/textures/''' + name.lower() + '''_cover_albumcoach.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4="" />
                                                </textureSet>
                                                <materialParams>
                                                    <GFXMaterialSerializableParam Reflector_factor="0.000000" />
                                                </materialParams>
                                            </GFXMaterialSerializable>
                                        </material>
                                        <ENUM NAME="oldAnchor" SEL="6" />
                                    </MaterialGraphicComponent>
                                </COMPONENTS>
                            </Actor>
                        </ACTORS>
                        <ACTORS NAME="Actor">
                            <Actor RELATIVEZ="0.000000" SCALE="0.300000 0.300000" xFLIPPED="0" USERFRIENDLY="''' + name + '''_cover_albumbkg" MARKER="" POS2D="1067.972168 201.986328" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
                                <COMPONENTS NAME="MaterialGraphicComponent">
                                    <MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="4294967295" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
                                        <PrimitiveParameters>
                                            <GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000">
                                                <ENUM NAME="gfxOccludeInfo" SEL="0" />
                                            </GFXPrimitiveParam>
                                        </PrimitiveParameters>
                                        <ENUM NAME="anchor" SEL="1" />
                                        <material>
                                            <GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/ui/materials/alpha_mul_b.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
                                                <textureSet>
                                                    <GFXMaterialTexturePathSet diffuse="world/maps/''' + name.lower() + '''/menuart/textures/''' + name.lower() + '''_cover_albumbkg.tga" back_light="" normal="" separateAlpha="" diffuse_2="world/ui/textures/mask_square.tga" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4="" />
                                                </textureSet>
                                                <materialParams>
                                                    <GFXMaterialSerializableParam Reflector_factor="0.000000" />
                                                </materialParams>
                                            </GFXMaterialSerializable>
                                        </material>
                                        <ENUM NAME="oldAnchor" SEL="1" />
                                    </MaterialGraphicComponent>
                                </COMPONENTS>
                            </Actor>
                        </ACTORS>
                        <ACTORS NAME="Actor">
                            <Actor RELATIVEZ="0.000000" SCALE="0.290211 0.290211" xFLIPPED="0" USERFRIENDLY="''' + name + '''_coach_1" MARKER="" POS2D="212.784500 663.680176" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
                                <COMPONENTS NAME="MaterialGraphicComponent">
                                    <MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="4294967295" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
                                        <PrimitiveParameters>
                                            <GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000">
                                                <ENUM NAME="gfxOccludeInfo" SEL="0" />
                                            </GFXPrimitiveParam>
                                        </PrimitiveParameters>
                                        <ENUM NAME="anchor" SEL="6" />
                                        <material>
                                            <GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/ui/materials/alpha.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
                                                <textureSet>
                                                    <GFXMaterialTexturePathSet diffuse="world/maps/''' + name.lower() + '''/menuart/textures/''' + name.lower() + '''_coach_1.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4="" />
                                                </textureSet>
                                                <materialParams>
                                                    <GFXMaterialSerializableParam Reflector_factor="0.000000" />
                                                </materialParams>
                                            </GFXMaterialSerializable>
                                        </material>
                                        <ENUM NAME="oldAnchor" SEL="6" />
                                    </MaterialGraphicComponent>
                                </COMPONENTS>
                            </Actor>
                        </ACTORS>
                        <ACTORS NAME="Actor">
                            <Actor RELATIVEZ="0.000000" SCALE="0.290211 0.290211" xFLIPPED="0" USERFRIENDLY="''' + name + '''_coach_2" MARKER="" POS2D="524.381104 670.829834" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
                                <COMPONENTS NAME="MaterialGraphicComponent">
                                    <MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="4294967295" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
                                        <PrimitiveParameters>
                                            <GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000">
                                                <ENUM NAME="gfxOccludeInfo" SEL="0" />
                                            </GFXPrimitiveParam>
                                        </PrimitiveParameters>
                                        <ENUM NAME="anchor" SEL="6" />
                                        <material>
                                            <GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/ui/materials/alpha.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
                                                <textureSet>
                                                    <GFXMaterialTexturePathSet diffuse="world/maps/''' + name.lower() + '''/menuart/textures/''' + name.lower() + '''_coach_2.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4="" />
                                                </textureSet>
                                                <materialParams>
                                                    <GFXMaterialSerializableParam Reflector_factor="0.000000" />
                                                </materialParams>
                                            </GFXMaterialSerializable>
                                        </material>
                                        <ENUM NAME="oldAnchor" SEL="6" />
                                    </MaterialGraphicComponent>
                                </COMPONENTS>
                            </Actor>
                        </ACTORS>
                        <ACTORS NAME="Actor">
                            <Actor RELATIVEZ="0.000000" SCALE="256.000000 128.000000" xFLIPPED="0" USERFRIENDLY="''' + name + '''_map_bkg" MARKER="" POS2D="1487.410156 -32.732918" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
                                <COMPONENTS NAME="MaterialGraphicComponent">
                                    <MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="1" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
                                        <PrimitiveParameters>
                                            <GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000">
                                                <ENUM NAME="gfxOccludeInfo" SEL="0" />
                                            </GFXPrimitiveParam>
                                        </PrimitiveParameters>
                                        <ENUM NAME="anchor" SEL="1" />
                                        <material>
                                            <GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/_common/matshader/multitexture_1layer.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
                                                <textureSet>
                                                    <GFXMaterialTexturePathSet diffuse="world/maps/''' + name.lower() + '''/menuart/textures/''' + name.lower() + '''_map_bkg.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4="" />
                                                </textureSet>
                                                <materialParams>
                                                    <GFXMaterialSerializableParam Reflector_factor="0.000000" />
                                                </materialParams>
                                            </GFXMaterialSerializable>
                                        </material>
                                        <ENUM NAME="oldAnchor" SEL="1" />
                                    </MaterialGraphicComponent>
                                </COMPONENTS>
                            </Actor>
                        </ACTORS>
                        <sceneConfigs>
                            <SceneConfigs activeSceneConfig="0" />
                        </sceneConfigs>
                    </Scene>
                </SCENE>
            </SubSceneActor>
        </ACTORS>
        <ACTORS NAME="SubSceneActor">
            <SubSceneActor RELATIVEZ="0.000000" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="''' + name + '''_AUTODANCE" MARKER="" POS2D="0.000000 -0.033823" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/subscene.tpl" RELATIVEPATH="world/maps/''' + name.lower() + '''/autodance/''' + name.lower() + '''_autodance.isc" EMBED_SCENE="1" IS_SINGLE_PIECE="0" ZFORCED="1" DIRECT_PICKING="1" IGNORE_SAVE="0">
                <ENUM NAME="viewType" SEL="2" />
                <SCENE>
                    <Scene ENGINE_VERSION="253653" GRIDUNIT="0.500000" DEPTH_SEPARATOR="0" NEAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" FAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" viewFamily="0">
                        <ACTORS NAME="Actor">
                            <Actor RELATIVEZ="0.000000" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="''' + name + '''_autodance" MARKER="" POS2D="-0.006150 -0.003075" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="world/maps/''' + name.lower() + '''/autodance/''' + name.lower() + '''_autodance.tpl">
                                <COMPONENTS NAME="JD_AutodanceComponent">
                                    <JD_AutodanceComponent />
                                </COMPONENTS>
                            </Actor>
                        </ACTORS>
                        <sceneConfigs>
                            <SceneConfigs activeSceneConfig="0" />
                        </sceneConfigs>
                    </Scene>
                </SCENE>
            </SubSceneActor>
        </ACTORS>
        <sceneConfigs>
            <SceneConfigs activeSceneConfig="0">
                <sceneConfigs NAME="JD_MapSceneConfig">
                    <JD_MapSceneConfig name="" soundContext="" hud="0" phoneTitleLocId="4294967295" phoneImage="">
                        <ENUM NAME="Pause_Level" SEL="6" />
                        <ENUM NAME="type" SEL="1" />
                        <ENUM NAME="musicscore" SEL="2" />
                    </JD_MapSceneConfig>
                </sceneConfigs>
            </SceneConfigs>
        </sceneConfigs>
    </Scene>
</root>''')
    if(coachnum == 3):
        mainsceneisc_content = ('''<?xml version="1.0" encoding="ISO-8859-1"?>
<root>
    <Scene ENGINE_VERSION="253653" GRIDUNIT="2.000000" DEPTH_SEPARATOR="0" NEAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" FAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" viewFamily="0">
        <PLATFORM_FILTER>
            <TargetFilterList platform="WII">
                <objects VAL="''' + name + '''_AUTODANCE" />
            </TargetFilterList>
        </PLATFORM_FILTER>
        <ACTORS NAME="SubSceneActor">
            <SubSceneActor RELATIVEZ="0.000000" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="''' + name + '''_AUDIO" MARKER="" POS2D="0.000000 0.000000" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/subscene.tpl" RELATIVEPATH="world/maps/''' + name.lower() + '''/audio/''' + name.lower() + '''_audio.isc" EMBED_SCENE="1" IS_SINGLE_PIECE="0" ZFORCED="1" DIRECT_PICKING="1" IGNORE_SAVE="0">
                <ENUM NAME="viewType" SEL="2" />
                <SCENE>
                    <Scene ENGINE_VERSION="253653" GRIDUNIT="0.500000" DEPTH_SEPARATOR="0" NEAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" FAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" viewFamily="0">
                        <ACTORS NAME="Actor">
                            <Actor RELATIVEZ="0.000000" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="MusicTrack" MARKER="" POS2D="1.125962 -0.418641" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="world/maps/''' + name.lower() + '''/audio/''' + name.lower() + '''_musictrack.tpl">
                                <COMPONENTS NAME="MusicTrackComponent">
                                    <MusicTrackComponent />
                                </COMPONENTS>
                            </Actor>
                        </ACTORS>
                        <ACTORS NAME="Actor">
                            <Actor RELATIVEZ="0.000001" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="''' + name + '''_sequence" MARKER="" POS2D="-0.006158 -0.006158" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="world/maps/''' + name.lower() + '''/audio/''' + name.lower() + '''_sequence.tpl">
                                <COMPONENTS NAME="TapeCase_Component">
                                    <TapeCase_Component />
                                </COMPONENTS>
                            </Actor>
                        </ACTORS>
                        <sceneConfigs>
                            <SceneConfigs activeSceneConfig="0" />
                        </sceneConfigs>
                    </Scene>
                </SCENE>
            </SubSceneActor>
        </ACTORS>
        <ACTORS NAME="SubSceneActor">
            <SubSceneActor RELATIVEZ="0.000000" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="''' + name + '''_CINE" MARKER="" POS2D="0.000000 0.000000" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/subscene.tpl" RELATIVEPATH="world/maps/''' + name.lower() + '''/cinematics/''' + name.lower() + '''_cine.isc" EMBED_SCENE="1" IS_SINGLE_PIECE="0" ZFORCED="1" DIRECT_PICKING="1" IGNORE_SAVE="0">
                <ENUM NAME="viewType" SEL="2" />
                <SCENE>
                    <Scene ENGINE_VERSION="253653" GRIDUNIT="0.500000" DEPTH_SEPARATOR="0" NEAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" FAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" viewFamily="0">
                        <ACTORS NAME="Actor">
                            <Actor RELATIVEZ="0.000000" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="''' + name + '''_MainSequence" MARKER="" POS2D="0.000000 0.000000" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="world/maps/''' + name.lower() + '''/cinematics/''' + name.lower() + '''_mainsequence.tpl">
                                <COMPONENTS NAME="MasterTape">
                                    <MasterTape />
                                </COMPONENTS>
                            </Actor>
                        </ACTORS>
                        <sceneConfigs>
                            <SceneConfigs activeSceneConfig="0" />
                        </sceneConfigs>
                    </Scene>
                </SCENE>
            </SubSceneActor>
        </ACTORS>
        <ACTORS NAME="SubSceneActor">
            <SubSceneActor RELATIVEZ="0.000000" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="''' + name + '''_GRAPH" MARKER="" POS2D="0.000000 0.000000" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/subscene.tpl" RELATIVEPATH="world/maps/''' + name.lower() + '''/graph/''' + name.lower() + '''_graph.isc" EMBED_SCENE="1" IS_SINGLE_PIECE="0" ZFORCED="1" DIRECT_PICKING="1" IGNORE_SAVE="0">
                <ENUM NAME="viewType" SEL="2" />
                <SCENE>
                    <Scene ENGINE_VERSION="253653" GRIDUNIT="0.500000" DEPTH_SEPARATOR="0" NEAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" FAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" viewFamily="0">
                        <ACTORS NAME="Actor">
                            <Actor RELATIVEZ="10.000000" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="Camera_JD_Dummy" MARKER="" POS2D="0.000000 0.000000" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/tpl_emptyactor.tpl" />
                        </ACTORS>
                        <sceneConfigs>
                            <SceneConfigs activeSceneConfig="0" />
                        </sceneConfigs>
                    </Scene>
                </SCENE>
            </SubSceneActor>
        </ACTORS>
        <ACTORS NAME="SubSceneActor">
            <SubSceneActor RELATIVEZ="0.000000" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="''' + name + '''_TML" MARKER="" POS2D="0.000000 0.000000" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/subscene.tpl" RELATIVEPATH="world/maps/''' + name.lower() + '''/timeline/''' + name.lower() + '''_tml.isc" EMBED_SCENE="1" IS_SINGLE_PIECE="0" ZFORCED="1" DIRECT_PICKING="1" IGNORE_SAVE="0">
                <ENUM NAME="viewType" SEL="2" />
                <SCENE>
                    <Scene ENGINE_VERSION="253653" GRIDUNIT="0.500000" DEPTH_SEPARATOR="0" NEAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" FAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" viewFamily="0">
                        <ACTORS NAME="Actor">
                            <Actor RELATIVEZ="0.000001" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="''' + name + '''_tml_dance" MARKER="" POS2D="-1.157740 0.006158" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="world/maps/''' + name.lower() + '''/timeline/''' + name.lower() + '''_tml_dance.tpl">
                                <COMPONENTS NAME="TapeCase_Component">
                                    <TapeCase_Component />
                                </COMPONENTS>
                            </Actor>
                        </ACTORS>
                        <ACTORS NAME="Actor">
                            <Actor RELATIVEZ="0.000001" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="''' + name + '''_tml_karaoke" MARKER="" POS2D="-1.157740 0.006158" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="world/maps/''' + name.lower() + '''/timeline/''' + name.lower() + '''_tml_karaoke.tpl">
                                <COMPONENTS NAME="TapeCase_Component">
                                    <TapeCase_Component />
                                </COMPONENTS>
                            </Actor>
                        </ACTORS>
                        <sceneConfigs>
                            <SceneConfigs activeSceneConfig="0" />
                        </sceneConfigs>
                    </Scene>
                </SCENE>
            </SubSceneActor>
        </ACTORS>
        <ACTORS NAME="SubSceneActor">
            <SubSceneActor RELATIVEZ="0.000000" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="''' + name + '''_VIDEO" MARKER="" POS2D="0.000000 0.000000" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/subscene.tpl" RELATIVEPATH="world/maps/''' + name.lower() + '''/videoscoach/''' + name.lower() + '''_video.isc" EMBED_SCENE="1" IS_SINGLE_PIECE="0" ZFORCED="1" DIRECT_PICKING="1" IGNORE_SAVE="0">
                <ENUM NAME="viewType" SEL="2" />
                <SCENE>
                    <Scene ENGINE_VERSION="253653" GRIDUNIT="0.500000" DEPTH_SEPARATOR="0" NEAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" FAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" viewFamily="0">
                        <ACTORS NAME="Actor">
                            <Actor RELATIVEZ="-1.000000" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="VideoScreen" MARKER="" POS2D="0.000000 -4.500000" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="world/_common/videoscreen/video_player_main.tpl">
                                <COMPONENTS NAME="PleoComponent">
                                    <PleoComponent video="world/maps/''' + name.lower() + '''/videoscoach/''' + name.lower() + '''.webm" dashMPD="world/maps/''' + name.lower() + '''/videoscoach/''' + name.lower() + '''.mpd" channelID="" />
                                </COMPONENTS>
                            </Actor>
                        </ACTORS>
                        <ACTORS NAME="Actor">
                            <Actor RELATIVEZ="0.000000" SCALE="3.941238 2.220000" xFLIPPED="0" USERFRIENDLY="VideoOutput" MARKER="" POS2D="0.000000 0.000000" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="world/_common/videoscreen/video_output_main.tpl">
                                <COMPONENTS NAME="PleoTextureGraphicComponent">
                                    <PleoTextureGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="4294967295" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000" channelID="">
                                        <PrimitiveParameters>
                                            <GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000">
                                                <ENUM NAME="gfxOccludeInfo" SEL="0" />
                                            </GFXPrimitiveParam>
                                        </PrimitiveParameters>
                                        <ENUM NAME="anchor" SEL="1" />
                                        <material>
                                            <GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/_common/matshader/pleofullscreen.msh" stencilTest="0" alphaTest="0" alphaRef="0">
                                                <textureSet>
                                                    <GFXMaterialTexturePathSet diffuse="" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4="" />
                                                </textureSet>
                                                <materialParams>
                                                    <GFXMaterialSerializableParam Reflector_factor="0.000000" />
                                                </materialParams>
                                            </GFXMaterialSerializable>
                                        </material>
                                        <ENUM NAME="oldAnchor" SEL="1" />
                                    </PleoTextureGraphicComponent>
                                </COMPONENTS>
                            </Actor>
                        </ACTORS>
                        <sceneConfigs>
                            <SceneConfigs activeSceneConfig="0" />
                        </sceneConfigs>
                    </Scene>
                </SCENE>
            </SubSceneActor>
        </ACTORS>
        <ACTORS NAME="Actor">
            <Actor RELATIVEZ="0.000000" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="''' + name + ''' : Template Artist - Template Title&#10;JDVer = 5, ID = 842776738, Type = 1 (Flags 0x00000000), NbCoach = 2, Difficulty = 2" MARKER="" POS2D="-3.531976 -1.485322" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="world/maps/''' + name.lower() + '''/songdesc.tpl">
                <COMPONENTS NAME="JD_SongDescComponent">
                    <JD_SongDescComponent />
                </COMPONENTS>
            </Actor>
        </ACTORS>
        <ACTORS NAME="SubSceneActor">
            <SubSceneActor RELATIVEZ="0.000000" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="''' + name + '''_menuart" MARKER="" POS2D="0.000000 0.000000" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/subscene.tpl" RELATIVEPATH="world/maps/''' + name.lower() + '''/menuart/''' + name.lower() + '''_menuart.isc" EMBED_SCENE="1" IS_SINGLE_PIECE="0" ZFORCED="1" DIRECT_PICKING="1" IGNORE_SAVE="0">
                <ENUM NAME="viewType" SEL="3" />
                <SCENE>
                    <Scene ENGINE_VERSION="253653" GRIDUNIT="0.500000" DEPTH_SEPARATOR="0" NEAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" FAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" viewFamily="1">
                        <ACTORS NAME="Actor">
                            <Actor RELATIVEZ="0.000000" SCALE="0.300000 0.300000" xFLIPPED="0" USERFRIENDLY="''' + name + '''_cover_generic" MARKER="" POS2D="266.087555 197.629959" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
                                <COMPONENTS NAME="MaterialGraphicComponent">
                                    <MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="4294967295" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
                                        <PrimitiveParameters>
                                            <GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000">
                                                <ENUM NAME="gfxOccludeInfo" SEL="0" />
                                            </GFXPrimitiveParam>
                                        </PrimitiveParameters>
                                        <ENUM NAME="anchor" SEL="1" />
                                        <material>
                                            <GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/ui/materials/alpha_mul_b.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
                                                <textureSet>
                                                    <GFXMaterialTexturePathSet diffuse="world/maps/''' + name.lower() + '''/menuart/textures/''' + name.lower() + '''_cover_generic.tga" back_light="" normal="" separateAlpha="" diffuse_2="world/ui/textures/mask_square.tga" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4="" />
                                                </textureSet>
                                                <materialParams>
                                                    <GFXMaterialSerializableParam Reflector_factor="0.000000" />
                                                </materialParams>
                                            </GFXMaterialSerializable>
                                        </material>
                                        <ENUM NAME="oldAnchor" SEL="1" />
                                    </MaterialGraphicComponent>
                                </COMPONENTS>
                            </Actor>
                        </ACTORS>
                        <ACTORS NAME="Actor">
                            <Actor RELATIVEZ="0.000000" SCALE="0.300000 0.300000" xFLIPPED="0" USERFRIENDLY="''' + name + '''_cover_online" MARKER="" POS2D="-150.000000 0.000000" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
                                <COMPONENTS NAME="MaterialGraphicComponent">
                                    <MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="4294967295" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
                                        <PrimitiveParameters>
                                            <GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000">
                                                <ENUM NAME="gfxOccludeInfo" SEL="0" />
                                            </GFXPrimitiveParam>
                                        </PrimitiveParameters>
                                        <ENUM NAME="anchor" SEL="1" />
                                        <material>
                                            <GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/ui/materials/alpha_mul_b.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
                                                <textureSet>
                                                    <GFXMaterialTexturePathSet diffuse="world/maps/''' + name.lower() + '''/menuart/textures/''' + name.lower() + '''_cover_online.tga" back_light="" normal="" separateAlpha="" diffuse_2="world/ui/textures/mask_square.tga" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4="" />
                                                </textureSet>
                                                <materialParams>
                                                    <GFXMaterialSerializableParam Reflector_factor="0.000000" />
                                                </materialParams>
                                            </GFXMaterialSerializable>
                                        </material>
                                        <ENUM NAME="oldAnchor" SEL="1" />
                                    </MaterialGraphicComponent>
                                </COMPONENTS>
                            </Actor>
                        </ACTORS>
                        <ACTORS NAME="Actor">
                            <Actor RELATIVEZ="0.000000" SCALE="0.300000 0.300000" xFLIPPED="0" USERFRIENDLY="''' + name + '''_cover_albumcoach" MARKER="" POS2D="738.106323 359.612030" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
                                <COMPONENTS NAME="MaterialGraphicComponent">
                                    <MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="4294967295" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
                                        <PrimitiveParameters>
                                            <GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000">
                                                <ENUM NAME="gfxOccludeInfo" SEL="0" />
                                            </GFXPrimitiveParam>
                                        </PrimitiveParameters>
                                        <ENUM NAME="anchor" SEL="6" />
                                        <material>
                                            <GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/ui/materials/alpha.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
                                                <textureSet>
                                                    <GFXMaterialTexturePathSet diffuse="world/maps/''' + name.lower() + '''/menuart/textures/''' + name.lower() + '''_cover_albumcoach.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4="" />
                                                </textureSet>
                                                <materialParams>
                                                    <GFXMaterialSerializableParam Reflector_factor="0.000000" />
                                                </materialParams>
                                            </GFXMaterialSerializable>
                                        </material>
                                        <ENUM NAME="oldAnchor" SEL="6" />
                                    </MaterialGraphicComponent>
                                </COMPONENTS>
                            </Actor>
                        </ACTORS>
                        <ACTORS NAME="Actor">
                            <Actor RELATIVEZ="0.000000" SCALE="0.300000 0.300000" xFLIPPED="0" USERFRIENDLY="''' + name + '''_cover_albumbkg" MARKER="" POS2D="1067.972168 201.986328" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
                                <COMPONENTS NAME="MaterialGraphicComponent">
                                    <MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="4294967295" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
                                        <PrimitiveParameters>
                                            <GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000">
                                                <ENUM NAME="gfxOccludeInfo" SEL="0" />
                                            </GFXPrimitiveParam>
                                        </PrimitiveParameters>
                                        <ENUM NAME="anchor" SEL="1" />
                                        <material>
                                            <GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/ui/materials/alpha_mul_b.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
                                                <textureSet>
                                                    <GFXMaterialTexturePathSet diffuse="world/maps/''' + name.lower() + '''/menuart/textures/''' + name.lower() + '''_cover_albumbkg.tga" back_light="" normal="" separateAlpha="" diffuse_2="world/ui/textures/mask_square.tga" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4="" />
                                                </textureSet>
                                                <materialParams>
                                                    <GFXMaterialSerializableParam Reflector_factor="0.000000" />
                                                </materialParams>
                                            </GFXMaterialSerializable>
                                        </material>
                                        <ENUM NAME="oldAnchor" SEL="1" />
                                    </MaterialGraphicComponent>
                                </COMPONENTS>
                            </Actor>
                        </ACTORS>
                        <ACTORS NAME="Actor">
                            <Actor RELATIVEZ="0.000000" SCALE="0.290211 0.290211" xFLIPPED="0" USERFRIENDLY="''' + name + '''_coach_1" MARKER="" POS2D="212.784500 663.680176" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
                                <COMPONENTS NAME="MaterialGraphicComponent">
                                    <MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="4294967295" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
                                        <PrimitiveParameters>
                                            <GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000">
                                                <ENUM NAME="gfxOccludeInfo" SEL="0" />
                                            </GFXPrimitiveParam>
                                        </PrimitiveParameters>
                                        <ENUM NAME="anchor" SEL="6" />
                                        <material>
                                            <GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/ui/materials/alpha.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
                                                <textureSet>
                                                    <GFXMaterialTexturePathSet diffuse="world/maps/''' + name.lower() + '''/menuart/textures/''' + name.lower() + '''_coach_1.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4="" />
                                                </textureSet>
                                                <materialParams>
                                                    <GFXMaterialSerializableParam Reflector_factor="0.000000" />
                                                </materialParams>
                                            </GFXMaterialSerializable>
                                        </material>
                                        <ENUM NAME="oldAnchor" SEL="6" />
                                    </MaterialGraphicComponent>
                                </COMPONENTS>
                            </Actor>
                        </ACTORS>
                        <ACTORS NAME="Actor">
                            <Actor RELATIVEZ="0.000000" SCALE="0.290211 0.290211" xFLIPPED="0" USERFRIENDLY="''' + name + '''_coach_2" MARKER="" POS2D="524.381104 670.829834" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
                                <COMPONENTS NAME="MaterialGraphicComponent">
                                    <MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="4294967295" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
                                        <PrimitiveParameters>
                                            <GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000">
                                                <ENUM NAME="gfxOccludeInfo" SEL="0" />
                                            </GFXPrimitiveParam>
                                        </PrimitiveParameters>
                                        <ENUM NAME="anchor" SEL="6" />
                                        <material>
                                            <GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/ui/materials/alpha.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
                                                <textureSet>
                                                    <GFXMaterialTexturePathSet diffuse="world/maps/''' + name.lower() + '''/menuart/textures/''' + name.lower() + '''_coach_2.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4="" />
                                                </textureSet>
                                                <materialParams>
                                                    <GFXMaterialSerializableParam Reflector_factor="0.000000" />
                                                </materialParams>
                                            </GFXMaterialSerializable>
                                        </material>
                                        <ENUM NAME="oldAnchor" SEL="6" />
                                    </MaterialGraphicComponent>
                                </COMPONENTS>
                            </Actor>
                        </ACTORS>
                        <ACTORS NAME="Actor">
                            <Actor RELATIVEZ="0.000000" SCALE="0.290211 0.290211" xFLIPPED="0" USERFRIENDLY="''' + name + '''_coach_3" MARKER="" POS2D="524.381104 670.829834" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
                                <COMPONENTS NAME="MaterialGraphicComponent">
                                    <MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="4294967295" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
                                        <PrimitiveParameters>
                                            <GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000">
                                                <ENUM NAME="gfxOccludeInfo" SEL="0" />
                                            </GFXPrimitiveParam>
                                        </PrimitiveParameters>
                                        <ENUM NAME="anchor" SEL="6" />
                                        <material>
                                            <GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/ui/materials/alpha.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
                                                <textureSet>
                                                    <GFXMaterialTexturePathSet diffuse="world/maps/''' + name.lower() + '''/menuart/textures/''' + name.lower() + '''_coach_3.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4="" />
                                                </textureSet>
                                                <materialParams>
                                                    <GFXMaterialSerializableParam Reflector_factor="0.000000" />
                                                </materialParams>
                                            </GFXMaterialSerializable>
                                        </material>
                                        <ENUM NAME="oldAnchor" SEL="6" />
                                    </MaterialGraphicComponent>
                                </COMPONENTS>
                            </Actor>
                        </ACTORS>
                        <ACTORS NAME="Actor">
                            <Actor RELATIVEZ="0.000000" SCALE="256.000000 128.000000" xFLIPPED="0" USERFRIENDLY="''' + name + '''_map_bkg" MARKER="" POS2D="1487.410156 -32.732918" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
                                <COMPONENTS NAME="MaterialGraphicComponent">
                                    <MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="1" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
                                        <PrimitiveParameters>
                                            <GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000">
                                                <ENUM NAME="gfxOccludeInfo" SEL="0" />
                                            </GFXPrimitiveParam>
                                        </PrimitiveParameters>
                                        <ENUM NAME="anchor" SEL="1" />
                                        <material>
                                            <GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/_common/matshader/multitexture_1layer.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
                                                <textureSet>
                                                    <GFXMaterialTexturePathSet diffuse="world/maps/''' + name.lower() + '''/menuart/textures/''' + name.lower() + '''_map_bkg.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4="" />
                                                </textureSet>
                                                <materialParams>
                                                    <GFXMaterialSerializableParam Reflector_factor="0.000000" />
                                                </materialParams>
                                            </GFXMaterialSerializable>
                                        </material>
                                        <ENUM NAME="oldAnchor" SEL="1" />
                                    </MaterialGraphicComponent>
                                </COMPONENTS>
                            </Actor>
                        </ACTORS>
                        <sceneConfigs>
                            <SceneConfigs activeSceneConfig="0" />
                        </sceneConfigs>
                    </Scene>
                </SCENE>
            </SubSceneActor>
        </ACTORS>
        <ACTORS NAME="SubSceneActor">
            <SubSceneActor RELATIVEZ="0.000000" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="''' + name + '''_AUTODANCE" MARKER="" POS2D="0.000000 -0.033823" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/subscene.tpl" RELATIVEPATH="world/maps/''' + name.lower() + '''/autodance/''' + name.lower() + '''_autodance.isc" EMBED_SCENE="1" IS_SINGLE_PIECE="0" ZFORCED="1" DIRECT_PICKING="1" IGNORE_SAVE="0">
                <ENUM NAME="viewType" SEL="2" />
                <SCENE>
                    <Scene ENGINE_VERSION="253653" GRIDUNIT="0.500000" DEPTH_SEPARATOR="0" NEAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" FAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" viewFamily="0">
                        <ACTORS NAME="Actor">
                            <Actor RELATIVEZ="0.000000" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="''' + name + '''_autodance" MARKER="" POS2D="-0.006150 -0.003075" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="world/maps/''' + name.lower() + '''/autodance/''' + name.lower() + '''_autodance.tpl">
                                <COMPONENTS NAME="JD_AutodanceComponent">
                                    <JD_AutodanceComponent />
                                </COMPONENTS>
                            </Actor>
                        </ACTORS>
                        <sceneConfigs>
                            <SceneConfigs activeSceneConfig="0" />
                        </sceneConfigs>
                    </Scene>
                </SCENE>
            </SubSceneActor>
        </ACTORS>
        <sceneConfigs>
            <SceneConfigs activeSceneConfig="0">
                <sceneConfigs NAME="JD_MapSceneConfig">
                    <JD_MapSceneConfig name="" soundContext="" hud="0" phoneTitleLocId="4294967295" phoneImage="">
                        <ENUM NAME="Pause_Level" SEL="6" />
                        <ENUM NAME="type" SEL="1" />
                        <ENUM NAME="musicscore" SEL="2" />
                    </JD_MapSceneConfig>
                </sceneConfigs>
            </SceneConfigs>
        </sceneConfigs>
    </Scene>
</root>''')
    if(coachnum == 4):
        mainsceneisc_content = ('''<?xml version="1.0" encoding="ISO-8859-1"?>
<root>
    <Scene ENGINE_VERSION="253653" GRIDUNIT="2.000000" DEPTH_SEPARATOR="0" NEAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" FAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" viewFamily="0">
        <PLATFORM_FILTER>
            <TargetFilterList platform="WII">
                <objects VAL="''' + name + '''_AUTODANCE" />
            </TargetFilterList>
        </PLATFORM_FILTER>
        <ACTORS NAME="SubSceneActor">
            <SubSceneActor RELATIVEZ="0.000000" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="''' + name + '''_AUDIO" MARKER="" POS2D="0.000000 0.000000" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/subscene.tpl" RELATIVEPATH="world/maps/''' + name.lower() + '''/audio/''' + name.lower() + '''_audio.isc" EMBED_SCENE="1" IS_SINGLE_PIECE="0" ZFORCED="1" DIRECT_PICKING="1" IGNORE_SAVE="0">
                <ENUM NAME="viewType" SEL="2" />
                <SCENE>
                    <Scene ENGINE_VERSION="253653" GRIDUNIT="0.500000" DEPTH_SEPARATOR="0" NEAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" FAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" viewFamily="0">
                        <ACTORS NAME="Actor">
                            <Actor RELATIVEZ="0.000000" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="MusicTrack" MARKER="" POS2D="1.125962 -0.418641" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="world/maps/''' + name.lower() + '''/audio/''' + name.lower() + '''_musictrack.tpl">
                                <COMPONENTS NAME="MusicTrackComponent">
                                    <MusicTrackComponent />
                                </COMPONENTS>
                            </Actor>
                        </ACTORS>
                        <ACTORS NAME="Actor">
                            <Actor RELATIVEZ="0.000001" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="''' + name + '''_sequence" MARKER="" POS2D="-0.006158 -0.006158" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="world/maps/''' + name.lower() + '''/audio/''' + name.lower() + '''_sequence.tpl">
                                <COMPONENTS NAME="TapeCase_Component">
                                    <TapeCase_Component />
                                </COMPONENTS>
                            </Actor>
                        </ACTORS>
                        <sceneConfigs>
                            <SceneConfigs activeSceneConfig="0" />
                        </sceneConfigs>
                    </Scene>
                </SCENE>
            </SubSceneActor>
        </ACTORS>
        <ACTORS NAME="SubSceneActor">
            <SubSceneActor RELATIVEZ="0.000000" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="''' + name + '''_CINE" MARKER="" POS2D="0.000000 0.000000" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/subscene.tpl" RELATIVEPATH="world/maps/''' + name.lower() + '''/cinematics/''' + name.lower() + '''_cine.isc" EMBED_SCENE="1" IS_SINGLE_PIECE="0" ZFORCED="1" DIRECT_PICKING="1" IGNORE_SAVE="0">
                <ENUM NAME="viewType" SEL="2" />
                <SCENE>
                    <Scene ENGINE_VERSION="253653" GRIDUNIT="0.500000" DEPTH_SEPARATOR="0" NEAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" FAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" viewFamily="0">
                        <ACTORS NAME="Actor">
                            <Actor RELATIVEZ="0.000000" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="''' + name + '''_MainSequence" MARKER="" POS2D="0.000000 0.000000" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="world/maps/''' + name.lower() + '''/cinematics/''' + name.lower() + '''_mainsequence.tpl">
                                <COMPONENTS NAME="MasterTape">
                                    <MasterTape />
                                </COMPONENTS>
                            </Actor>
                        </ACTORS>
                        <sceneConfigs>
                            <SceneConfigs activeSceneConfig="0" />
                        </sceneConfigs>
                    </Scene>
                </SCENE>
            </SubSceneActor>
        </ACTORS>
        <ACTORS NAME="SubSceneActor">
            <SubSceneActor RELATIVEZ="0.000000" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="''' + name + '''_GRAPH" MARKER="" POS2D="0.000000 0.000000" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/subscene.tpl" RELATIVEPATH="world/maps/''' + name.lower() + '''/graph/''' + name.lower() + '''_graph.isc" EMBED_SCENE="1" IS_SINGLE_PIECE="0" ZFORCED="1" DIRECT_PICKING="1" IGNORE_SAVE="0">
                <ENUM NAME="viewType" SEL="2" />
                <SCENE>
                    <Scene ENGINE_VERSION="253653" GRIDUNIT="0.500000" DEPTH_SEPARATOR="0" NEAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" FAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" viewFamily="0">
                        <ACTORS NAME="Actor">
                            <Actor RELATIVEZ="10.000000" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="Camera_JD_Dummy" MARKER="" POS2D="0.000000 0.000000" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/tpl_emptyactor.tpl" />
                        </ACTORS>
                        <sceneConfigs>
                            <SceneConfigs activeSceneConfig="0" />
                        </sceneConfigs>
                    </Scene>
                </SCENE>
            </SubSceneActor>
        </ACTORS>
        <ACTORS NAME="SubSceneActor">
            <SubSceneActor RELATIVEZ="0.000000" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="''' + name + '''_TML" MARKER="" POS2D="0.000000 0.000000" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/subscene.tpl" RELATIVEPATH="world/maps/''' + name.lower() + '''/timeline/''' + name.lower() + '''_tml.isc" EMBED_SCENE="1" IS_SINGLE_PIECE="0" ZFORCED="1" DIRECT_PICKING="1" IGNORE_SAVE="0">
                <ENUM NAME="viewType" SEL="2" />
                <SCENE>
                    <Scene ENGINE_VERSION="253653" GRIDUNIT="0.500000" DEPTH_SEPARATOR="0" NEAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" FAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" viewFamily="0">
                        <ACTORS NAME="Actor">
                            <Actor RELATIVEZ="0.000001" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="''' + name + '''_tml_dance" MARKER="" POS2D="-1.157740 0.006158" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="world/maps/''' + name.lower() + '''/timeline/''' + name.lower() + '''_tml_dance.tpl">
                                <COMPONENTS NAME="TapeCase_Component">
                                    <TapeCase_Component />
                                </COMPONENTS>
                            </Actor>
                        </ACTORS>
                        <ACTORS NAME="Actor">
                            <Actor RELATIVEZ="0.000001" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="''' + name + '''_tml_karaoke" MARKER="" POS2D="-1.157740 0.006158" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="world/maps/''' + name.lower() + '''/timeline/''' + name.lower() + '''_tml_karaoke.tpl">
                                <COMPONENTS NAME="TapeCase_Component">
                                    <TapeCase_Component />
                                </COMPONENTS>
                            </Actor>
                        </ACTORS>
                        <sceneConfigs>
                            <SceneConfigs activeSceneConfig="0" />
                        </sceneConfigs>
                    </Scene>
                </SCENE>
            </SubSceneActor>
        </ACTORS>
        <ACTORS NAME="SubSceneActor">
            <SubSceneActor RELATIVEZ="0.000000" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="''' + name + '''_VIDEO" MARKER="" POS2D="0.000000 0.000000" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/subscene.tpl" RELATIVEPATH="world/maps/''' + name.lower() + '''/videoscoach/''' + name.lower() + '''_video.isc" EMBED_SCENE="1" IS_SINGLE_PIECE="0" ZFORCED="1" DIRECT_PICKING="1" IGNORE_SAVE="0">
                <ENUM NAME="viewType" SEL="2" />
                <SCENE>
                    <Scene ENGINE_VERSION="253653" GRIDUNIT="0.500000" DEPTH_SEPARATOR="0" NEAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" FAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" viewFamily="0">
                        <ACTORS NAME="Actor">
                            <Actor RELATIVEZ="-1.000000" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="VideoScreen" MARKER="" POS2D="0.000000 -4.500000" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="world/_common/videoscreen/video_player_main.tpl">
                                <COMPONENTS NAME="PleoComponent">
                                    <PleoComponent video="world/maps/''' + name.lower() + '''/videoscoach/''' + name.lower() + '''.webm" dashMPD="world/maps/''' + name.lower() + '''/videoscoach/''' + name.lower() + '''.mpd" channelID="" />
                                </COMPONENTS>
                            </Actor>
                        </ACTORS>
                        <ACTORS NAME="Actor">
                            <Actor RELATIVEZ="0.000000" SCALE="3.941238 2.220000" xFLIPPED="0" USERFRIENDLY="VideoOutput" MARKER="" POS2D="0.000000 0.000000" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="world/_common/videoscreen/video_output_main.tpl">
                                <COMPONENTS NAME="PleoTextureGraphicComponent">
                                    <PleoTextureGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="4294967295" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000" channelID="">
                                        <PrimitiveParameters>
                                            <GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000">
                                                <ENUM NAME="gfxOccludeInfo" SEL="0" />
                                            </GFXPrimitiveParam>
                                        </PrimitiveParameters>
                                        <ENUM NAME="anchor" SEL="1" />
                                        <material>
                                            <GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/_common/matshader/pleofullscreen.msh" stencilTest="0" alphaTest="0" alphaRef="0">
                                                <textureSet>
                                                    <GFXMaterialTexturePathSet diffuse="" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4="" />
                                                </textureSet>
                                                <materialParams>
                                                    <GFXMaterialSerializableParam Reflector_factor="0.000000" />
                                                </materialParams>
                                            </GFXMaterialSerializable>
                                        </material>
                                        <ENUM NAME="oldAnchor" SEL="1" />
                                    </PleoTextureGraphicComponent>
                                </COMPONENTS>
                            </Actor>
                        </ACTORS>
                        <sceneConfigs>
                            <SceneConfigs activeSceneConfig="0" />
                        </sceneConfigs>
                    </Scene>
                </SCENE>
            </SubSceneActor>
        </ACTORS>
        <ACTORS NAME="Actor">
            <Actor RELATIVEZ="0.000000" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="''' + name + ''' : Template Artist - Template Title&#10;JDVer = 5, ID = 842776738, Type = 1 (Flags 0x00000000), NbCoach = 2, Difficulty = 2" MARKER="" POS2D="-3.531976 -1.485322" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="world/maps/''' + name.lower() + '''/songdesc.tpl">
                <COMPONENTS NAME="JD_SongDescComponent">
                    <JD_SongDescComponent />
                </COMPONENTS>
            </Actor>
        </ACTORS>
        <ACTORS NAME="SubSceneActor">
            <SubSceneActor RELATIVEZ="0.000000" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="''' + name + '''_menuart" MARKER="" POS2D="0.000000 0.000000" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/subscene.tpl" RELATIVEPATH="world/maps/''' + name.lower() + '''/menuart/''' + name.lower() + '''_menuart.isc" EMBED_SCENE="1" IS_SINGLE_PIECE="0" ZFORCED="1" DIRECT_PICKING="1" IGNORE_SAVE="0">
                <ENUM NAME="viewType" SEL="3" />
                <SCENE>
                    <Scene ENGINE_VERSION="253653" GRIDUNIT="0.500000" DEPTH_SEPARATOR="0" NEAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" FAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" viewFamily="1">
                        <ACTORS NAME="Actor">
                            <Actor RELATIVEZ="0.000000" SCALE="0.300000 0.300000" xFLIPPED="0" USERFRIENDLY="''' + name + '''_cover_generic" MARKER="" POS2D="266.087555 197.629959" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
                                <COMPONENTS NAME="MaterialGraphicComponent">
                                    <MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="4294967295" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
                                        <PrimitiveParameters>
                                            <GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000">
                                                <ENUM NAME="gfxOccludeInfo" SEL="0" />
                                            </GFXPrimitiveParam>
                                        </PrimitiveParameters>
                                        <ENUM NAME="anchor" SEL="1" />
                                        <material>
                                            <GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/ui/materials/alpha_mul_b.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
                                                <textureSet>
                                                    <GFXMaterialTexturePathSet diffuse="world/maps/''' + name.lower() + '''/menuart/textures/''' + name.lower() + '''_cover_generic.tga" back_light="" normal="" separateAlpha="" diffuse_2="world/ui/textures/mask_square.tga" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4="" />
                                                </textureSet>
                                                <materialParams>
                                                    <GFXMaterialSerializableParam Reflector_factor="0.000000" />
                                                </materialParams>
                                            </GFXMaterialSerializable>
                                        </material>
                                        <ENUM NAME="oldAnchor" SEL="1" />
                                    </MaterialGraphicComponent>
                                </COMPONENTS>
                            </Actor>
                        </ACTORS>
                        <ACTORS NAME="Actor">
                            <Actor RELATIVEZ="0.000000" SCALE="0.300000 0.300000" xFLIPPED="0" USERFRIENDLY="''' + name + '''_cover_online" MARKER="" POS2D="-150.000000 0.000000" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
                                <COMPONENTS NAME="MaterialGraphicComponent">
                                    <MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="4294967295" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
                                        <PrimitiveParameters>
                                            <GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000">
                                                <ENUM NAME="gfxOccludeInfo" SEL="0" />
                                            </GFXPrimitiveParam>
                                        </PrimitiveParameters>
                                        <ENUM NAME="anchor" SEL="1" />
                                        <material>
                                            <GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/ui/materials/alpha_mul_b.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
                                                <textureSet>
                                                    <GFXMaterialTexturePathSet diffuse="world/maps/''' + name.lower() + '''/menuart/textures/''' + name.lower() + '''_cover_online.tga" back_light="" normal="" separateAlpha="" diffuse_2="world/ui/textures/mask_square.tga" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4="" />
                                                </textureSet>
                                                <materialParams>
                                                    <GFXMaterialSerializableParam Reflector_factor="0.000000" />
                                                </materialParams>
                                            </GFXMaterialSerializable>
                                        </material>
                                        <ENUM NAME="oldAnchor" SEL="1" />
                                    </MaterialGraphicComponent>
                                </COMPONENTS>
                            </Actor>
                        </ACTORS>
                        <ACTORS NAME="Actor">
                            <Actor RELATIVEZ="0.000000" SCALE="0.300000 0.300000" xFLIPPED="0" USERFRIENDLY="''' + name + '''_cover_albumcoach" MARKER="" POS2D="738.106323 359.612030" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
                                <COMPONENTS NAME="MaterialGraphicComponent">
                                    <MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="4294967295" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
                                        <PrimitiveParameters>
                                            <GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000">
                                                <ENUM NAME="gfxOccludeInfo" SEL="0" />
                                            </GFXPrimitiveParam>
                                        </PrimitiveParameters>
                                        <ENUM NAME="anchor" SEL="6" />
                                        <material>
                                            <GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/ui/materials/alpha.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
                                                <textureSet>
                                                    <GFXMaterialTexturePathSet diffuse="world/maps/''' + name.lower() + '''/menuart/textures/''' + name.lower() + '''_cover_albumcoach.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4="" />
                                                </textureSet>
                                                <materialParams>
                                                    <GFXMaterialSerializableParam Reflector_factor="0.000000" />
                                                </materialParams>
                                            </GFXMaterialSerializable>
                                        </material>
                                        <ENUM NAME="oldAnchor" SEL="6" />
                                    </MaterialGraphicComponent>
                                </COMPONENTS>
                            </Actor>
                        </ACTORS>
                        <ACTORS NAME="Actor">
                            <Actor RELATIVEZ="0.000000" SCALE="0.300000 0.300000" xFLIPPED="0" USERFRIENDLY="''' + name + '''_cover_albumbkg" MARKER="" POS2D="1067.972168 201.986328" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
                                <COMPONENTS NAME="MaterialGraphicComponent">
                                    <MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="4294967295" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
                                        <PrimitiveParameters>
                                            <GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000">
                                                <ENUM NAME="gfxOccludeInfo" SEL="0" />
                                            </GFXPrimitiveParam>
                                        </PrimitiveParameters>
                                        <ENUM NAME="anchor" SEL="1" />
                                        <material>
                                            <GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/ui/materials/alpha_mul_b.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
                                                <textureSet>
                                                    <GFXMaterialTexturePathSet diffuse="world/maps/''' + name.lower() + '''/menuart/textures/''' + name.lower() + '''_cover_albumbkg.tga" back_light="" normal="" separateAlpha="" diffuse_2="world/ui/textures/mask_square.tga" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4="" />
                                                </textureSet>
                                                <materialParams>
                                                    <GFXMaterialSerializableParam Reflector_factor="0.000000" />
                                                </materialParams>
                                            </GFXMaterialSerializable>
                                        </material>
                                        <ENUM NAME="oldAnchor" SEL="1" />
                                    </MaterialGraphicComponent>
                                </COMPONENTS>
                            </Actor>
                        </ACTORS>
                        <ACTORS NAME="Actor">
                            <Actor RELATIVEZ="0.000000" SCALE="0.290211 0.290211" xFLIPPED="0" USERFRIENDLY="''' + name + '''_coach_1" MARKER="" POS2D="212.784500 663.680176" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
                                <COMPONENTS NAME="MaterialGraphicComponent">
                                    <MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="4294967295" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
                                        <PrimitiveParameters>
                                            <GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000">
                                                <ENUM NAME="gfxOccludeInfo" SEL="0" />
                                            </GFXPrimitiveParam>
                                        </PrimitiveParameters>
                                        <ENUM NAME="anchor" SEL="6" />
                                        <material>
                                            <GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/ui/materials/alpha.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
                                                <textureSet>
                                                    <GFXMaterialTexturePathSet diffuse="world/maps/''' + name.lower() + '''/menuart/textures/''' + name.lower() + '''_coach_1.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4="" />
                                                </textureSet>
                                                <materialParams>
                                                    <GFXMaterialSerializableParam Reflector_factor="0.000000" />
                                                </materialParams>
                                            </GFXMaterialSerializable>
                                        </material>
                                        <ENUM NAME="oldAnchor" SEL="6" />
                                    </MaterialGraphicComponent>
                                </COMPONENTS>
                            </Actor>
                        </ACTORS>
                        <ACTORS NAME="Actor">
                            <Actor RELATIVEZ="0.000000" SCALE="0.290211 0.290211" xFLIPPED="0" USERFRIENDLY="''' + name + '''_coach_2" MARKER="" POS2D="524.381104 670.829834" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
                                <COMPONENTS NAME="MaterialGraphicComponent">
                                    <MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="4294967295" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
                                        <PrimitiveParameters>
                                            <GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000">
                                                <ENUM NAME="gfxOccludeInfo" SEL="0" />
                                            </GFXPrimitiveParam>
                                        </PrimitiveParameters>
                                        <ENUM NAME="anchor" SEL="6" />
                                        <material>
                                            <GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/ui/materials/alpha.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
                                                <textureSet>
                                                    <GFXMaterialTexturePathSet diffuse="world/maps/''' + name.lower() + '''/menuart/textures/''' + name.lower() + '''_coach_2.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4="" />
                                                </textureSet>
                                                <materialParams>
                                                    <GFXMaterialSerializableParam Reflector_factor="0.000000" />
                                                </materialParams>
                                            </GFXMaterialSerializable>
                                        </material>
                                        <ENUM NAME="oldAnchor" SEL="6" />
                                    </MaterialGraphicComponent>
                                </COMPONENTS>
                            </Actor>
                        </ACTORS>
                        <ACTORS NAME="Actor">
                            <Actor RELATIVEZ="0.000000" SCALE="0.290211 0.290211" xFLIPPED="0" USERFRIENDLY="''' + name + '''_coach_3" MARKER="" POS2D="524.381104 670.829834" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
                                <COMPONENTS NAME="MaterialGraphicComponent">
                                    <MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="4294967295" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
                                        <PrimitiveParameters>
                                            <GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000">
                                                <ENUM NAME="gfxOccludeInfo" SEL="0" />
                                            </GFXPrimitiveParam>
                                        </PrimitiveParameters>
                                        <ENUM NAME="anchor" SEL="6" />
                                        <material>
                                            <GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/ui/materials/alpha.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
                                                <textureSet>
                                                    <GFXMaterialTexturePathSet diffuse="world/maps/''' + name.lower() + '''/menuart/textures/''' + name.lower() + '''_coach_3.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4="" />
                                                </textureSet>
                                                <materialParams>
                                                    <GFXMaterialSerializableParam Reflector_factor="0.000000" />
                                                </materialParams>
                                            </GFXMaterialSerializable>
                                        </material>
                                        <ENUM NAME="oldAnchor" SEL="6" />
                                    </MaterialGraphicComponent>
                                </COMPONENTS>
                            </Actor>
                        </ACTORS>
                        <ACTORS NAME="Actor">
                            <Actor RELATIVEZ="0.000000" SCALE="0.290211 0.290211" xFLIPPED="0" USERFRIENDLY="''' + name + '''_coach_4" MARKER="" POS2D="524.381104 670.829834" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
                                <COMPONENTS NAME="MaterialGraphicComponent">
                                    <MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="4294967295" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
                                        <PrimitiveParameters>
                                            <GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000">
                                                <ENUM NAME="gfxOccludeInfo" SEL="0" />
                                            </GFXPrimitiveParam>
                                        </PrimitiveParameters>
                                        <ENUM NAME="anchor" SEL="6" />
                                        <material>
                                            <GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/ui/materials/alpha.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
                                                <textureSet>
                                                    <GFXMaterialTexturePathSet diffuse="world/maps/''' + name.lower() + '''/menuart/textures/''' + name.lower() + '''_coach_4.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4="" />
                                                </textureSet>
                                                <materialParams>
                                                    <GFXMaterialSerializableParam Reflector_factor="0.000000" />
                                                </materialParams>
                                            </GFXMaterialSerializable>
                                        </material>
                                        <ENUM NAME="oldAnchor" SEL="6" />
                                    </MaterialGraphicComponent>
                                </COMPONENTS>
                            </Actor>
                        </ACTORS>
                        <ACTORS NAME="Actor">
                            <Actor RELATIVEZ="0.000000" SCALE="256.000000 128.000000" xFLIPPED="0" USERFRIENDLY="''' + name + '''_map_bkg" MARKER="" POS2D="1487.410156 -32.732918" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
                                <COMPONENTS NAME="MaterialGraphicComponent">
                                    <MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="1" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
                                        <PrimitiveParameters>
                                            <GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000">
                                                <ENUM NAME="gfxOccludeInfo" SEL="0" />
                                            </GFXPrimitiveParam>
                                        </PrimitiveParameters>
                                        <ENUM NAME="anchor" SEL="1" />
                                        <material>
                                            <GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/_common/matshader/multitexture_1layer.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
                                                <textureSet>
                                                    <GFXMaterialTexturePathSet diffuse="world/maps/''' + name.lower() + '''/menuart/textures/''' + name.lower() + '''_map_bkg.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4="" />
                                                </textureSet>
                                                <materialParams>
                                                    <GFXMaterialSerializableParam Reflector_factor="0.000000" />
                                                </materialParams>
                                            </GFXMaterialSerializable>
                                        </material>
                                        <ENUM NAME="oldAnchor" SEL="1" />
                                    </MaterialGraphicComponent>
                                </COMPONENTS>
                            </Actor>
                        </ACTORS>
                        <sceneConfigs>
                            <SceneConfigs activeSceneConfig="0" />
                        </sceneConfigs>
                    </Scene>
                </SCENE>
            </SubSceneActor>
        </ACTORS>
        <ACTORS NAME="SubSceneActor">
            <SubSceneActor RELATIVEZ="0.000000" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="''' + name + '''_AUTODANCE" MARKER="" POS2D="0.000000 -0.033823" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/subscene.tpl" RELATIVEPATH="world/maps/''' + name.lower() + '''/autodance/''' + name.lower() + '''_autodance.isc" EMBED_SCENE="1" IS_SINGLE_PIECE="0" ZFORCED="1" DIRECT_PICKING="1" IGNORE_SAVE="0">
                <ENUM NAME="viewType" SEL="2" />
                <SCENE>
                    <Scene ENGINE_VERSION="253653" GRIDUNIT="0.500000" DEPTH_SEPARATOR="0" NEAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" FAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" viewFamily="0">
                        <ACTORS NAME="Actor">
                            <Actor RELATIVEZ="0.000000" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="''' + name + '''_autodance" MARKER="" POS2D="-0.006150 -0.003075" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="world/maps/''' + name.lower() + '''/autodance/''' + name.lower() + '''_autodance.tpl">
                                <COMPONENTS NAME="JD_AutodanceComponent">
                                    <JD_AutodanceComponent />
                                </COMPONENTS>
                            </Actor>
                        </ACTORS>
                        <sceneConfigs>
                            <SceneConfigs activeSceneConfig="0" />
                        </sceneConfigs>
                    </Scene>
                </SCENE>
            </SubSceneActor>
        </ACTORS>
        <sceneConfigs>
            <SceneConfigs activeSceneConfig="0">
                <sceneConfigs NAME="JD_MapSceneConfig">
                    <JD_MapSceneConfig name="" soundContext="" hud="0" phoneTitleLocId="4294967295" phoneImage="">
                        <ENUM NAME="Pause_Level" SEL="6" />
                        <ENUM NAME="type" SEL="1" />
                        <ENUM NAME="musicscore" SEL="2" />
                    </JD_MapSceneConfig>
                </sceneConfigs>
            </SceneConfigs>
        </sceneConfigs>
    </Scene>
</root>''')
    mainsceneisc.write(mainsceneisc_content)
    mainsceneisc.close()
    #MAINSCENE ISC
    #MAINSCENE ISC
    #MAINSCENE ISC

    #MAINSCENE SGS
    #MAINSCENE SGS
    #MAINSCENE SGS
    mainscenesgs = open(cache_path + name.lower() + "_main_scene.sgs.ckd", "w", encoding="utf-8")
    mainscenesgs.write('S{"settings":{"__class":"JD_MapSceneConfig","Pause_Level":6,"name":"","type":1,"musicscore":2,"soundContext":"","hud":0,"phoneTitleLocId":4294967295,"phoneImage":""}}')
    mainscenesgs.close()
    #MAINSCENE SGS
    #MAINSCENE SGS
    #MAINSCENE SGS

    #AutoDance Files
    ##
    autodancetpl = open(cache_autodance + name.lower() + "_autodance.tpl.ckd", "w", encoding="utf-8")
    autodancetpl.write('{"__class":"Actor_Template","WIP":0,"LOWUPDATE":0,"UPDATE_LAYER":0,"PROCEDURAL":0,"STARTPAUSED":0,"FORCEISENVIRONMENT":0,"COMPONENTS":[{"__class":"JD_AutodanceComponent_Template","song":"' + name + '","autodanceData":{"__class":"JD_AutodanceData","recording_structure":{"__class":"JD_AutodanceRecordingStructure","records":[{"__class":"Record","Start":88,"Duration":16},{"__class":"Record","Start":136,"Duration":8},{"__class":"Record","Start":188,"Duration":8},{"__class":"Record","Start":252,"Duration":16}]},"video_structure":{"__class":"JD_AutodanceVideoStructure","SongStartPosition":244,"Duration":32,"ThumbnailTime":0,"FadeOutDuration":3,"GroundPlanePath":"invalid ","FirstLayerTripleBackgroundPath":"invalid ","SecondLayerTripleBackgroundPath":"invalid ","ThirdLayerTripleBackgroundPath":"invalid ","playback_events":[{"__class":"PlaybackEvent","ClipNumber":0,"StartClip":0,"StartTime":244,"Duration":1,"Speed":1},{"__class":"PlaybackEvent","ClipNumber":0,"StartClip":0,"StartTime":245,"Duration":1,"Speed":1},{"__class":"PlaybackEvent","ClipNumber":0,"StartClip":0,"StartTime":246,"Duration":1,"Speed":1},{"__class":"PlaybackEvent","ClipNumber":0,"StartClip":0,"StartTime":247,"Duration":1,"Speed":1},{"__class":"PlaybackEvent","ClipNumber":0,"StartClip":3,"StartTime":248,"Duration":0.500000,"Speed":2},{"__class":"PlaybackEvent","ClipNumber":0,"StartClip":3,"StartTime":248.500000,"Duration":0.500000,"Speed":2},{"__class":"PlaybackEvent","ClipNumber":0,"StartClip":3,"StartTime":249,"Duration":0.500000,"Speed":2},{"__class":"PlaybackEvent","ClipNumber":0,"StartClip":3,"StartTime":249.500000,"Duration":0.500000,"Speed":2},{"__class":"PlaybackEvent","ClipNumber":1,"StartClip":0,"StartTime":250,"Duration":1,"Speed":2},{"__class":"PlaybackEvent","ClipNumber":1,"StartClip":1,"StartTime":251,"Duration":1,"Speed":4},{"__class":"PlaybackEvent","ClipNumber":0,"StartClip":5,"StartTime":252,"Duration":1,"Speed":1.500000},{"__class":"PlaybackEvent","ClipNumber":0,"StartClip":5,"StartTime":253,"Duration":1,"Speed":1.500000},{"__class":"PlaybackEvent","ClipNumber":0,"StartClip":6,"StartTime":254,"Duration":2,"Speed":1.800000},{"__class":"PlaybackEvent","ClipNumber":0,"StartClip":6,"StartTime":256,"Duration":0.500000,"Speed":2},{"__class":"PlaybackEvent","ClipNumber":0,"StartClip":6,"StartTime":256.500000,"Duration":0.500000,"Speed":2},{"__class":"PlaybackEvent","ClipNumber":0,"StartClip":6,"StartTime":257,"Duration":0.500000,"Speed":2},{"__class":"PlaybackEvent","ClipNumber":0,"StartClip":6,"StartTime":257.500000,"Duration":0.500000,"Speed":2},{"__class":"PlaybackEvent","ClipNumber":0,"StartClip":6,"StartTime":258,"Duration":0.500000,"Speed":2},{"__class":"PlaybackEvent","ClipNumber":0,"StartClip":7,"StartTime":258.500000,"Duration":1.500000,"Speed":1.500000},{"__class":"PlaybackEvent","ClipNumber":2,"StartClip":0,"StartTime":260,"Duration":1,"Speed":2},{"__class":"PlaybackEvent","ClipNumber":1,"StartClip":2,"StartTime":261,"Duration":1,"Speed":2},{"__class":"PlaybackEvent","ClipNumber":1,"StartClip":2,"StartTime":262,"Duration":1,"Speed":2},{"__class":"PlaybackEvent","ClipNumber":1,"StartClip":2,"StartTime":263,"Duration":1,"Speed":2},{"__class":"PlaybackEvent","ClipNumber":3,"StartClip":0,"StartTime":264,"Duration":1.500000,"Speed":3},{"__class":"PlaybackEvent","ClipNumber":3,"StartClip":3,"StartTime":265.500000,"Duration":1.500000,"Speed":-3},{"__class":"PlaybackEvent","ClipNumber":3,"StartClip":1.500000,"StartTime":267,"Duration":1,"Speed":2},{"__class":"PlaybackEvent","ClipNumber":3,"StartClip":2.200000,"StartTime":268,"Duration":1,"Speed":3},{"__class":"PlaybackEvent","ClipNumber":2,"StartClip":0,"StartTime":269,"Duration":2,"Speed":3},{"__class":"PlaybackEvent","ClipNumber":0,"StartClip":0,"StartTime":271,"Duration":1,"Speed":1},{"__class":"PlaybackEvent","ClipNumber":3,"StartClip":4,"StartTime":272,"Duration":2,"Speed":2},{"__class":"PlaybackEvent","ClipNumber":0,"StartClip":0,"StartTime":274,"Duration":1,"Speed":1},{"__class":"PlaybackEvent","ClipNumber":3,"StartClip":3,"StartTime":275,"Duration":1,"Speed":5}],"background_effect":{"__class":"AutoDanceFxDesc","Opacity":1,"ColorLow":{"__class":"GFX_Vector4","x":0,"y":0,"z":0,"w":1},"ColorMid":{"__class":"GFX_Vector4","x":0,"y":0,"z":0,"w":1},"ColorHigh":{"__class":"GFX_Vector4","x":0,"y":0,"z":0,"w":1},"LowToMid":0.333000,"LowToMidWidth":0.150000,"MidToHigh":0.666000,"MidToHighWidth":0.150000,"SobColor":{"__class":"GFX_Vector4","x":0,"y":0,"z":0,"w":1},"OutColor":{"__class":"GFX_Vector4","x":0,"y":0,"z":0,"w":0},"ThickMiddle":0.400000,"ThickInner":0.100000,"ThickSmooth":0.100000,"ShvNbFrames":0,"PartsScale":[0,0,0,0,0],"HalftoneFactor":0,"HalftoneCutoutLevels":256,"UVBlackoutFactor":0,"UVBlackoutDesaturation":0.200000,"UVBlackoutContrast":4,"UVBlackoutBrightness":0,"UVBlackoutColor":{"__class":"GFX_Vector4","x":0.549020,"y":0.549020,"z":1,"w":1},"ToonFactor":0,"ToonCutoutLevels":8,"RefractionFactor":0,"RefractionTint":{"__class":"GFX_Vector4","x":1,"y":1,"z":1,"w":1},"RefractionScale":{"__class":"GFX_Vector4","x":0.030000,"y":0.030000,"z":0.030000,"w":0.030000},"RefractionOpacity":0.200000,"ColoredShivaThresholds":{"__class":"GFX_Vector4","x":0.100000,"y":0.300000,"z":0.600000,"w":0.950000},"ColoredShivaColor0":{"__class":"GFX_Vector4","x":1,"y":1,"z":1,"w":1},"ColoredShivaColor1":{"__class":"GFX_Vector4","x":1,"y":1,"z":1,"w":1},"ColoredShivaColor2":{"__class":"GFX_Vector4","x":1,"y":1,"z":1,"w":1},"SaturationModifier":0,"SlimeFactor":0,"SlimeColor":{"__class":"GFX_Vector4","x":0.499020,"y":0.629176,"z":0.136039,"w":1},"SlimeOpacity":0.200000,"SlimeAmbient":0.200000,"SlimeNormalTiling":7,"SlimeLightAngle":0,"SlimeRefraction":0.091300,"SlimeRefractionIndex":1.083700,"SlimeSpecular":1,"SlimeSpecularPower":10,"OverlayBlendFactor":0,"OverlayBlendColor":{"__class":"GFX_Vector4","x":0.721569,"y":0.639216,"z":0.756863,"w":1},"BackgroundSobelFactor":0,"BackgroundSobelColor":{"__class":"GFX_Vector4","x":0,"y":1,"z":1,"w":1},"PlayerGlowFactor":0,"PlayerGlowColor":{"__class":"GFX_Vector4","x":0,"y":1,"z":1,"w":1},"SwapHeadWithPlayer":[0,1,2,3,4,5],"AnimatePlayerHead":[0,0,0,0,0,0],"AnimatedHeadTotalTime":20,"AnimatedHeadRestTime":16,"AnimatedHeadFrameTime":0.600000,"AnimatedHeadMaxDistance":1.250000,"AnimatedHeadMaxAngle":1.200000,"ScreenBlendInverseAlphaFactor":0,"ScreenBlendInverseAlphaScaleX":0,"ScreenBlendInverseAlphaScaleY":0,"ScreenBlendInverseAlphaTransX":0,"ScreenBlendInverseAlphaTransY":0,"TintMulColorFactor":0,"TintMulColor":{"__class":"GFX_Vector4","x":0,"y":0,"z":0,"w":1},"FloorPlaneFactor":0,"FloorPlaneTiles":{"__class":"GFX_Vector4","x":8,"y":8,"z":0,"w":0},"FloorSpeedX":0,"FloorSpeedY":0,"FloorWaveSpeed":0,"FloorBlendMode":0,"FloorPlaneImageID":0,"StartRadius":3,"EndRadius":2,"RadiusVariance":0.500000,"RadiusNoiseRate":0,"RadiusNoiseAmp":0,"MinSpin":-4,"MaxSpin":4,"DirAngle":0,"MinWanderRate":2,"MaxWanderRate":3,"MinWanderAmp":0.100000,"MaxWanderAmp":0.200000,"MinSpeed":0.200000,"MaxSpeed":0.400000,"MotionPower":1.500000,"Amount":0,"ImageID":7,"StartR":1,"StartG":0.100000,"StartB":0.100000,"EndR":0.100000,"EndG":0.200000,"EndB":1,"StartAlpha":1,"EndAlpha":1,"TexturedOutlineFactor":0,"TexturedOutlineTiling":1,"TripleLayerBackgroundFactor":0,"TripleLayerBackgroundTintColor":{"__class":"GFX_Vector4","x":0,"y":0,"z":0,"w":0},"TripleLayerBackgroundSpeedX":0,"TripleLayerBackgroundSpeedY":0,"TrailEffectId":0},"player_effect":{"__class":"AutoDanceFxDesc","Opacity":1,"ColorLow":{"__class":"GFX_Vector4","x":0,"y":0,"z":0,"w":1},"ColorMid":{"__class":"GFX_Vector4","x":0,"y":0,"z":0,"w":1},"ColorHigh":{"__class":"GFX_Vector4","x":0,"y":0,"z":0,"w":1},"LowToMid":0.333000,"LowToMidWidth":0.150000,"MidToHigh":0.666000,"MidToHighWidth":0.150000,"SobColor":{"__class":"GFX_Vector4","x":0,"y":0,"z":0,"w":1},"OutColor":{"__class":"GFX_Vector4","x":1,"y":1,"z":1,"w":0},"ThickMiddle":0.400000,"ThickInner":0.100000,"ThickSmooth":0.100000,"ShvNbFrames":0,"PartsScale":[0,0,0,0,0],"HalftoneFactor":0,"HalftoneCutoutLevels":256,"UVBlackoutFactor":0,"UVBlackoutDesaturation":0.200000,"UVBlackoutContrast":4,"UVBlackoutBrightness":0,"UVBlackoutColor":{"__class":"GFX_Vector4","x":0.549020,"y":0.549020,"z":1,"w":1},"ToonFactor":0,"ToonCutoutLevels":256,"RefractionFactor":0,"RefractionTint":{"__class":"GFX_Vector4","x":1,"y":1,"z":1,"w":1},"RefractionScale":{"__class":"GFX_Vector4","x":0.030000,"y":0.030000,"z":0.030000,"w":0.030000},"RefractionOpacity":0.200000,"ColoredShivaThresholds":{"__class":"GFX_Vector4","x":0.100000,"y":0.300000,"z":0.600000,"w":0.950000},"ColoredShivaColor0":{"__class":"GFX_Vector4","x":1,"y":1,"z":1,"w":1},"ColoredShivaColor1":{"__class":"GFX_Vector4","x":1,"y":1,"z":1,"w":1},"ColoredShivaColor2":{"__class":"GFX_Vector4","x":1,"y":1,"z":1,"w":1},"SaturationModifier":0,"SlimeFactor":0,"SlimeColor":{"__class":"GFX_Vector4","x":0.894118,"y":0.294118,"z":1,"w":0.549020},"SlimeOpacity":0.200000,"SlimeAmbient":0.200000,"SlimeNormalTiling":7,"SlimeLightAngle":0,"SlimeRefraction":0.100000,"SlimeRefractionIndex":1.100000,"SlimeSpecular":1.100000,"SlimeSpecularPower":2,"OverlayBlendFactor":0,"OverlayBlendColor":{"__class":"GFX_Vector4","x":0.721569,"y":0.639216,"z":0.756863,"w":1},"BackgroundSobelFactor":0,"BackgroundSobelColor":{"__class":"GFX_Vector4","x":0,"y":1,"z":1,"w":1},"PlayerGlowFactor":0,"PlayerGlowColor":{"__class":"GFX_Vector4","x":0,"y":1,"z":1,"w":1},"SwapHeadWithPlayer":[0,1,2,3,4,5],"AnimatePlayerHead":[0,0,0,0,0,0],"AnimatedHeadTotalTime":20,"AnimatedHeadRestTime":16,"AnimatedHeadFrameTime":0.600000,"AnimatedHeadMaxDistance":1.250000,"AnimatedHeadMaxAngle":1.200000,"ScreenBlendInverseAlphaFactor":0,"ScreenBlendInverseAlphaScaleX":0,"ScreenBlendInverseAlphaScaleY":0,"ScreenBlendInverseAlphaTransX":0,"ScreenBlendInverseAlphaTransY":0,"TintMulColorFactor":0,"TintMulColor":{"__class":"GFX_Vector4","x":0,"y":0,"z":0,"w":1},"FloorPlaneFactor":0,"FloorPlaneTiles":{"__class":"GFX_Vector4","x":8,"y":8,"z":0,"w":0},"FloorSpeedX":0,"FloorSpeedY":0,"FloorWaveSpeed":0,"FloorBlendMode":0,"FloorPlaneImageID":0,"StartRadius":0,"EndRadius":2,"RadiusVariance":0,"RadiusNoiseRate":0,"RadiusNoiseAmp":0,"MinSpin":0,"MaxSpin":0,"DirAngle":0,"MinWanderRate":0,"MaxWanderRate":0,"MinWanderAmp":0,"MaxWanderAmp":0,"MinSpeed":2,"MaxSpeed":4,"MotionPower":1,"Amount":0,"ImageID":0,"StartR":0,"StartG":0,"StartB":0,"EndR":1,"EndG":1,"EndB":1,"StartAlpha":1,"EndAlpha":1,"TexturedOutlineFactor":0,"TexturedOutlineTiling":0,"TripleLayerBackgroundFactor":0,"TripleLayerBackgroundTintColor":{"__class":"GFX_Vector4","x":0,"y":0,"z":0,"w":0},"TripleLayerBackgroundSpeedX":0,"TripleLayerBackgroundSpeedY":0,"TrailEffectId":0}},"autodanceSoundPath":"world/maps/' + name.lower() + '/autodance/' + name.lower() + '.ogg"}}]}')
    autodancetpl.close()
    ##

    ##
    autodanceisc = open(cache_autodance + name.lower() + "_autodance.isc.ckd", "w", encoding="utf-8")
    autodanceisc.write('''<?xml version="1.0" encoding="ISO-8859-1"?>
<root>
    <Scene ENGINE_VERSION="253653" GRIDUNIT="0.500000" DEPTH_SEPARATOR="0" NEAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" FAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" viewFamily="0">
        <ACTORS NAME="Actor">
            <Actor RELATIVEZ="0.000000" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="''' + name + '''_autodance" MARKER="" POS2D="-0.006150 -0.003075" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="world/maps/''' + name.lower() + '''/autodance/''' + name.lower() + '''_autodance.tpl">
                <COMPONENTS NAME="JD_AutodanceComponent">
                    <JD_AutodanceComponent />
                </COMPONENTS>
            </Actor>
        </ACTORS>
        <sceneConfigs>
            <SceneConfigs activeSceneConfig="0" />
        </sceneConfigs>
    </Scene>
</root>''')
    autodanceisc.close()
    ##
    #AutoDance Files

    #ACT FILES
    #ACT FILES
    #ACT FILES
    autodanceact = open(cache_autodance + name.lower() + "_autodance.act.ckd", "wb")
    ByteFileName = (name.lower() + "_autodance.tpl").encode()
    ByteFileName_Length = (len(ByteFileName).to_bytes(4, 'big'))
    BytePathFile = ("world/maps/" + name.lower() + "/autodance/").encode()
    BytePathFile_Length = (len(BytePathFile).to_bytes(4, 'big'))
    fileHash = (randint(1000000000, 4000000000).to_bytes(4, 'big'))
    autodanceact.write(b'\x00\x00\x00\x01\x00\x00\x00\x00\x3F\x80\x00\x00\x3F\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\xFF\xFF\x00\x00\x00\x00')
    autodanceact.write(ByteFileName_Length)
    autodanceact.write(ByteFileName)
    autodanceact.write(BytePathFile_Length)
    autodanceact.write(BytePathFile)
    autodanceact.write(fileHash)
    autodanceact.write(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x67\xB8\xBB\x77')
    autodanceact.close()

    def makeTexAct(texturename, output):
        file = open(output, 'wb')
        SongTextureName = (texturename).encode()
        SongTextureName_Length = (len(SongTextureName).to_bytes(4, 'big'))
        PathToSongTexture = ("world/maps/" + name.lower() + "/menuart/textures/").encode()
        PathToSongTexture_Length = (len(PathToSongTexture).to_bytes(4, 'big'))
        fileHash = (randint(1000000000, 4000000000).to_bytes(4, 'big'))
        file.write(b'\x00\x00\x00\x01\x00\x00\x00\x00\x3F\x80\x00\x00\x3F\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x22\x74\x70\x6C\x5F\x6D\x61\x74\x65\x72\x69\x61\x6C\x67\x72\x61\x70\x68\x69\x63\x63\x6F\x6D\x70\x6F\x6E\x65\x6E\x74\x32\x64\x2E\x74\x70\x6C\x00\x00\x00\x1A\x65\x6E\x67\x69\x6E\x65\x64\x61\x74\x61\x2F\x61\x63\x74\x6F\x72\x74\x65\x6D\x70\x6C\x61\x74\x65\x73\x2F\xB4\xA8\x17\xA8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x72\xB6\x1F\xC5\x3F\x80\x00\x00\x3F\x80\x00\x00\x3F\x80\x00\x00\x3F\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x06\x00\x00\x00\x00\x00\x00\x00\x00')
        file.write(SongTextureName_Length)
        file.write(SongTextureName)
        file.write(PathToSongTexture_Length)
        file.write(PathToSongTexture)
        file.write(fileHash)
        file.write(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x17\x6D\x75\x6C\x74\x69\x74\x65\x78\x74\x75\x72\x65\x5F\x31\x6C\x61\x79\x65\x72\x2E\x6D\x73\x68\x00\x00\x00\x18\x77\x6F\x72\x6C\x64\x2F\x5F\x63\x6F\x6D\x6D\x6F\x6E\x2F\x6D\x61\x74\x73\x68\x61\x64\x65\x72\x2F\xD7\xE7\xD9\xC7\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x3F\x80\x00\x00\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x3F\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01')
        file.close()
        
    abname = (name.lower() + "_cover_albumcoach")
    makeTexAct(abname + ".tga", cache_act_menuart + abname + ".act.ckd")

    bannername = (name.lower() + "_map_bkg")
    makeTexAct(bannername + ".tga", cache_act_menuart + bannername + ".act.ckd")

    covergenericname = (name.lower() + "_cover_generic")
    makeTexAct(covergenericname + ".tga", cache_act_menuart + covergenericname + ".act.ckd")

    coveronlinename = (name.lower() + "_cover_online")
    makeTexAct(coveronlinename + ".tga", cache_act_menuart + coveronlinename + ".act.ckd")

    if(coachnum >= 1):
        c1name = (name.lower() + "_coach_1")
        makeTexAct(c1name + ".tga", cache_act_menuart + c1name + ".act.ckd")
        
    if(coachnum >= 2):
        c2name = (name.lower() + "_coach_2")
        makeTexAct(c2name + ".tga", cache_act_menuart + c2name + ".act.ckd")

    if(coachnum >= 3):
        c3name = (name.lower() + "_coach_3")
        makeTexAct(c3name + ".tga", cache_act_menuart + c3name + ".act.ckd")

    if(coachnum >= 4):
        c4name = (name.lower() + "_coach_4")
        makeTexAct(c4name + ".tga", cache_act_menuart + c4name + ".act.ckd")

    danceact = open(cache_timeline + name.lower() + "_tml_dance.act.ckd", "wb")
    ByteFileName = (name.lower() + "_tml_dance.tpl").encode()
    ByteFileName_Length = (len(ByteFileName).to_bytes(4, 'big'))
    BytePathFile = ("world/maps/" + name.lower() + "/timeline/").encode()
    BytePathFile_Length = (len(BytePathFile).to_bytes(4, 'big'))
    fileHash = (randint(1000000000, 4000000000).to_bytes(4, 'big'))
    danceact.write(b'\x00\x00\x00\x01\x00\x00\x00\x00\x3F\x80\x00\x00\x3F\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\xFF\xFF\x00\x00\x00\x00')
    danceact.write(ByteFileName_Length)
    danceact.write(ByteFileName)
    danceact.write(BytePathFile_Length)
    danceact.write(BytePathFile)
    danceact.write(fileHash)
    danceact.write(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x23\x1F\x27\xDE')
    danceact.close()

    karaokeact = open(cache_timeline + name.lower() + "_tml_karaoke.act.ckd", "wb")
    ByteFileName = (name.lower() + "_tml_karaoke.tpl").encode()
    ByteFileName_Length = (len(ByteFileName).to_bytes(4, 'big'))
    BytePathFile = ("world/maps/" + name.lower() + "/timeline/").encode()
    BytePathFile_Length = (len(BytePathFile).to_bytes(4, 'big'))
    fileHash = (randint(1000000000, 4000000000).to_bytes(4, 'big'))
    karaokeact.write(b'\x00\x00\x00\x01\x00\x00\x00\x00\x3F\x80\x00\x00\x3F\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\xFF\xFF\x00\x00\x00\x00')
    karaokeact.write(ByteFileName_Length)
    karaokeact.write(ByteFileName)
    karaokeact.write(BytePathFile_Length)
    karaokeact.write(BytePathFile)
    karaokeact.write(fileHash)
    karaokeact.write(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x23\x1F\x27\xDE')
    karaokeact.close()

    songdescact = open(cache_path + "songdesc.act.ckd", "wb")
    BytePathFile = ("world/maps/" + name.lower() + "/").encode()
    BytePathFile_Length = (len(BytePathFile).to_bytes(4, 'big'))
    fileHash = (randint(1000000000, 4000000000).to_bytes(4, 'big'))
    songdescact.write(b'\x00\x00\x00\x01\x00\x00\x00\x00\x3F\x80\x00\x00\x3F\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x0C\x73\x6F\x6E\x67\x64\x65\x73\x63\x2E\x74\x70\x6C')
    songdescact.write(BytePathFile_Length)
    songdescact.write(BytePathFile)
    songdescact.write(fileHash)
    songdescact.write(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\xE0\x7F\xCC\x3F')
    songdescact.close()

    videoscoachact = open(cache_videoscoach + "video_player_main.act.ckd", "wb")
    ByteFileName = (name.lower() + ".webm").encode()
    ByteFileName_Length = (len(ByteFileName).to_bytes(4, 'big'))
    ByteMpdFileName = (name.lower() + ".mpd").encode()
    ByteMpdFileName_Length = (len(ByteMpdFileName).to_bytes(4, 'big'))
    fileHash1 = (randint(1000000000, 4000000000).to_bytes(4, 'big'))
    BytePathFile = ("world/maps/" + name.lower() + "/videoscoach/").encode()
    BytePathFile_Length = (len(BytePathFile).to_bytes(4, 'big'))
    fileHash2 = (randint(1000000000, 4000000000).to_bytes(4, 'big'))
    videoscoachact.write(b'\x00\x00\x00\x01\x00\x00\x00\x00\x3F\x80\x00\x00\x3F\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x15\x76\x69\x64\x65\x6F\x5F\x70\x6C\x61\x79\x65\x72\x5F\x6D\x61\x69\x6E\x2E\x74\x70\x6C\x00\x00\x00\x1A\x77\x6F\x72\x6C\x64\x2F\x5F\x63\x6F\x6D\x6D\x6F\x6E\x2F\x76\x69\x64\x65\x6F\x73\x63\x72\x65\x65\x6E\x2F\xF5\xD5\xE8\xF2\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x12\x63\xDA\xD9')
    videoscoachact.write(ByteFileName_Length)
    videoscoachact.write(ByteFileName)
    videoscoachact.write(BytePathFile_Length)
    videoscoachact.write(BytePathFile)
    videoscoachact.write(fileHash1)
    videoscoachact.write(b'\x00\x00\x00\x00')
    videoscoachact.write(ByteMpdFileName_Length)
    videoscoachact.write(ByteMpdFileName)
    videoscoachact.write(BytePathFile_Length)
    videoscoachact.write(BytePathFile)
    videoscoachact.write(fileHash2)
    videoscoachact.write(b'\x00\x00\x00\x00\x00\x00\x00\x00')
    videoscoachact.close()

    def getVideoInf(qualidade):
        nome = ("jmcs://jd-contents/" + name + "/" + name + "_" + qualidade + ".webm").encode()
        tamanho = (len(nome).to_bytes(4, 'big'))
        return tamanho, nome
    
    videoscoachmpd = open(cache_videoscoach + name.lower() + ".mpd.ckd", "wb")
    videoscoachmpd.write(b'\x00\x00\x00\x01\x00\x43\x6C\x33\x33\x3F\x80\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x43\x6C\x33\x33\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x0A\x76\x69\x64\x65\x6F\x2F\x77\x65\x62\x6D\x00\x00\x00\x03\x76\x70\x38\x00\x00\x04\xC0\x00\x00\x02\xD0\x00\x00\x00\x00\x00\x00\x00\x01\x01\x01\x00\x00\x00\x04\x00\x00\x00\x00\x00\x07\x4B\xA6')
    LowWebm = getVideoInf("LOW")
    MidWebm = getVideoInf("MID")
    HighWebm = getVideoInf("HIGH")
    UltraWebm = getVideoInf("ULTRA")
    videoscoachmpd.write(LowWebm[0])
    videoscoachmpd.write(LowWebm[1])
    videoscoachmpd.write(b'\x00\x00\x00\x00\x00\x00\x02\x58\x00\x00\x02\x58\x00\x00\x11\xDB\x00\x00\x00\x01\x00\x1C\x38\xD4')
    videoscoachmpd.write(MidWebm[0])
    videoscoachmpd.write(MidWebm[1])
    videoscoachmpd.write(b'\x00\x00\x00\x00\x00\x00\x02\x58\x00\x00\x02\x58\x00\x00\x12\x7E\x00\x00\x00\x02\x00\x38\x83\xCD')
    videoscoachmpd.write(HighWebm[0])
    videoscoachmpd.write(HighWebm[1])
    videoscoachmpd.write(b'\x00\x00\x00\x00\x00\x00\x02\x58\x00\x00\x02\x58\x00\x00\x12\xA1\x00\x00\x00\x03\x00\x74\xB3')
    videoscoachmpd.write(UltraWebm[0])
    videoscoachmpd.write(UltraWebm[1])
    videoscoachmpd.write(b'\x00\x00\x00\x00\x00\x00\x02\x58\x00\x00\x02\x58\x00\x00\x12\xB7')
    videoscoachmpd.close()

    videoscoachpreviewact = open(cache_videoscoach + "video_player_map_preview.act.ckd", "wb")
    ByteFileName = (name.lower() + ".webm").encode()
    ByteFileName_Length = (len(ByteFileName).to_bytes(4, 'big'))
    ByteMpdFileName = (name.lower() + ".mpd").encode()
    ByteMpdFileName_Length = (len(ByteMpdFileName).to_bytes(4, 'big'))
    fileHash1 = (randint(1000000000, 4000000000).to_bytes(4, 'big'))
    BytePathFile = ("world/maps/" + name.lower() + "/videoscoach/").encode()
    BytePathFile_Length = (len(BytePathFile).to_bytes(4, 'big'))
    fileHash2 = (randint(1000000000, 4000000000).to_bytes(4, 'big'))
    videoscoachpreviewact.write(b'\x00\x00\x00\x01\x00\x00\x00\x00\x3F\x80\x00\x00\x3F\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x1C\x76\x69\x64\x65\x6F\x5F\x70\x6C\x61\x79\x65\x72\x5F\x6D\x61\x70\x5F\x70\x72\x65\x76\x69\x65\x77\x2E\x74\x70\x6C\x00\x00\x00\x1A\x77\x6F\x72\x6C\x64\x2F\x5F\x63\x6F\x6D\x6D\x6F\x6E\x2F\x76\x69\x64\x65\x6F\x73\x63\x72\x65\x65\x6E\x2F\xD3\x94\x54\x28\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x12\x63\xDA\xD9')
    videoscoachpreviewact.write(ByteFileName_Length)
    videoscoachpreviewact.write(ByteFileName)
    videoscoachpreviewact.write(BytePathFile_Length)
    videoscoachpreviewact.write(BytePathFile)
    videoscoachpreviewact.write(fileHash1)
    videoscoachpreviewact.write(b'\x00\x00\x00\x00')
    videoscoachpreviewact.write(ByteMpdFileName_Length)
    videoscoachpreviewact.write(ByteMpdFileName)
    videoscoachpreviewact.write(BytePathFile_Length)
    videoscoachpreviewact.write(BytePathFile)
    videoscoachpreviewact.write(fileHash2)
    videoscoachpreviewact.write(b'\x00\x00\x00\x00\x00\x00\x00\x00')
    videoscoachpreviewact.write(BytePathFile = " + name.lower() + ")
    videoscoachpreviewact.close()
    #ACT FILES
    #ACT FILES
    #ACT FILES
    

    print("Done!")
except:
    print("An error occured with mainscene gen. This typically shows up- so nothing to worry about.")


def tryorpass(content):
    try:
        content
    except:
        pass

def beat48(value):
    return value*48

def beat24(value):
    return value*24

def zerox(mapjson):
    return mapjson.replace("0x","")

def fixjson(mapjson):
    return mapjson.replace(name+"(","").replace("})","}")

def fixmoves0(mapjson):
    return mapjson.replace(name+"0(","").replace("])","]")

def fixmoves1(mapjson):
    return mapjson.replace(name+"1(","").replace("])","]")

def fixmoves2(mapjson):
    return mapjson.replace(name+"2(","").replace("])","]")

def fixmoves3(mapjson):
    return mapjson.replace(name+"3(","").replace("])","]")

def hex_to_rgb(value): 
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

def removeduplicate(it):
    seen = []
    for x in it:
        if x not in seen:
            yield x
            seen.append(x)

def downloadMSM(server, name, moves_json):
    for move in moves_json:
        movename=move["name"]
        if server=='new':
            classifierdata=requests.get(mapurl+'/data/classifiers_WIIU/'+movename+'.msm',allow_redirects=True)
        elif server=='old':
            classifierdata=requests.get(mapurl+'/data/classifiers/'+movename+'.msm',allow_redirects=True)
        os.makedirs('temp/classifiers', exist_ok=True)
        open('temp/classifiers/'+movename+'.msm','wb').write(classifierdata.content)

def OLD_PictoCut(name, numcoach):
    mapurl='http://jdnowweb-s.cdn.ubi.com/uat/release_tu2/20150928_1740/songs/'+name
    pictopng=Image.open(BytesIO(urlopen(mapurl+'/assets/web/pictos-sprite.png').read()))
    pictocss=urlopen(mapurl+'/assets/web/pictos-sprite.css').read().decode('utf-8').split('\n')
    if numcoach == 2 or numcoach == 3 or numcoach == 4 or numcoach == "Duet" or numcoach == "Trio" or numcoach == "Quarto":
        top=40
        bottom=217
    elif numcoach == 1 or numcoach == "Solo":
        top=0
        bottom=256
    left=0
    right=left+256
    for picto in pictocss:
        pictoname=picto.split('-')
        pictoname=pictoname[1].split('{')
        pictoname=pictoname[0]
        picto=pictopng.crop((left,top,right,bottom))
        left+=256
        right+=256
        if numcoach == 2 or numcoach == 3 or numcoach == 4 or numcoach == "Duet" or numcoach == "Trio" or numcoach == "Quarto":
            picto=picto.resize((256,256))
        os.makedirs('temp/pictos/png', exist_ok=True)
        picto.save('temp/pictos/png/'+pictoname+'.png')

def NEW_PictoCut(name, mapurl):
    pictopng=mapurl+"/assets/web/pictos-atlas.png"
    pictojson=mapurl+"/assets/web/pictos-atlas.json"
    pictopng=Image.open(BytesIO(urlopen(mapurl+"/assets/web/pictos-atlas.png").read()))
    pictojson=json.loads(urlopen(pictojson).read().decode("utf-8"))
    width=pictojson['imageSize']['width']
    height=pictojson['imageSize']['height']
    pictos=pictojson['images']
    pictonames=list(pictos)
    count=0
    while count<len(pictonames):
        pictoname=pictonames[count]
        left,top=pictos[pictoname]
        right=left+width
        bottom=top+height
        pictocut=pictopng.crop((left, top, right, bottom))
        pictorender=pictocut.resize((256,256))
        pictorender.save('temp/pictos/'+pictoname+'.png')
        count+=1

jdnserver=input('Which jdnow server are you finding files? (old/new): ')



backup_stuff={}

moves0json=[]
moves1json=[]
moves2json=[]
moves3json=[]

mapjson={
    "name": "",
    "JDVersion": 0,
    "Artist": "",
    "Title": "",
    "NumCoach": 1,
    "Mode": 0,
    "AudioPreviewFadeTime": 0.5,
    "AudioPreview": {
        "coverflow": {
            "startbeat": 0
        },
        "prelobby": {
            "startbeat": 0
        }
    },
    "DefaultColors": {
        "lyrics": "0xFFFFFFFF",
        "theme": "0xFFFFFFFF"
    },
    "lyricsColor": "#FFFFFF",
    "videoOffset": 0,
    "beats": [],
    "lyrics": [],
    "pictos": []
}

if jdnserver=="new" or jdnserver=="New" or jdnserver=="NEW":
    nowurl=urlopen("https://ire-prod-api.justdancenow.com/v1/songs/published")
    db=json.loads(nowurl.read())
    for name in db:
        if name["id"]==name:
            print('getting '+name+' database')
            mapurl=name["base"]
            jsonfile=fixjson(urlopen(mapurl+'/'+name+'.json').read().decode("utf-8"))
            mapjson=json.loads(jsonfile)
            backup_stuff['jdnowurl']=mapurl

            try:
                coachcount=mapjson["NumCoach"]
            except:
                coachcount=1
                    
            print('cutting pictos...')
            NEW_PictoCut(name, mapurl)

            #moves0
            try:
                moves0file=fixmoves0(urlopen(mapurl+'/data/moves/'+name+'_moves0.json').read().decode("utf-8"))
                moves0json=json.loads(moves0file)
            except:
                pass

            #moves1
            try:
                moves1file=fixmoves1(urlopen(mapurl+'/data/moves/'+name+'_moves1.json').read().decode("utf-8"))
                moves1json=json.loads(moves1file)
            except:
                pass

            #moves2
            try:
                moves2file=fixmoves2(urlopen(mapurl+'/data/moves/'+name+'_moves2.json').read().decode("utf-8"))
                moves2json=json.loads(moves2file)
            except:
                pass

            #moves3
            try:
                moves3file=fixmoves3(urlopen(mapurl+'/data/moves/'+name+'_moves3.json').read().decode("utf-8"))
                moves3json=json.loads(moves3file)
            except:
                pass

            print('download msms...')
            tryorpass(downloadMSM('new', name, moves0json))
            tryorpass(downloadMSM('new', name, moves1json))
            tryorpass(downloadMSM('new', name, moves2json))
            tryorpass(downloadMSM('new', name, moves3json))
                
elif jdnserver=="old" or jdnserver=="Old" or jdnserver=="OLD":
    try:
        mapurl='http://jdnowweb-s.cdn.ubi.com/uat/release_tu2/20150928_1740/songs/'+name
        jsonfile=fixjson(urlopen(mapurl+'/'+name+'.json').read().decode("utf-8"))
        mapjson=json.loads(jsonfile)
        backup_stuff['jdnowurl']=mapurl

        try:
            coachcount=mapjson["NumCoach"]
        except:
            coachcount=1

        print('cutting pictos...')
        OLD_PictoCut(name, coachcount)

        #moves0
        try:
            moves0file=fixmoves0(urlopen(mapurl+'/data/moves/'+name+'_moves0.json').read().decode("utf-8"))
            moves0json=json.loads(moves0file)
        except:
            pass

        #moves1
        try:
            moves1file=fixmoves1(urlopen(mapurl+'/data/moves/'+name+'_moves1.json').read().decode("utf-8"))
            moves1json=json.loads(moves1file)
        except:
            pass

        #moves2
        try:
            moves2file=fixmoves2(urlopen(mapurl+'/data/moves/'+name+'_moves2.json').read().decode("utf-8"))
            moves2json=json.loads(moves2file)
        except:
            pass

        #moves3
        try:
            moves3file=fixmoves3(urlopen(mapurl+'/data/moves/'+name+'_moves3.json').read().decode("utf-8"))
            moves3json=json.loads(moves3file)
        except:
            pass

        print('download msms...')
        tryorpass(downloadMSM('old', name, moves0json))
        tryorpass(downloadMSM('old', name, moves1json))
        tryorpass(downloadMSM('old', name, moves2json))
        tryorpass(downloadMSM('old', name, moves3json))

    except KeyError:
        input(name+" does not exist. " + KeyError)

else:
    input('You need to pick between new or old server.')

def j2d(): #jdnow timelines to ubiart timelines

    print('converting '+name+'...')
    beats_24=[]
    index24=0
    beatrange=0
    #for markers that doesn't start at 0
    if mapjson['beats'][0]!=0:
        firstbeat=mapjson['beats'][0]
        extrabeats=mapjson['beats'][0:beatrange]
        for addbeat in range(beatrange):
            mapjson['beats'].insert(addbeat,extrabeats[addbeat]-firstbeat)

    for beat in mapjson['beats']:
        beats_24.append(index24) #added 24 for each beat.
        index24+=24

    lyricjson=zerox(mapjson['DefaultColors']['lyrics'])

    songdesc={}
    songdesc["__class"]="Actor_Template"
    songdesc["WIP"]=0
    songdesc["LOWUPDATE"]=0
    songdesc["UPDATE_LAYER"]=0
    songdesc["PROCEDURAL"]=0
    songdesc["STARTPAUSED"]=0
    songdesc["FORCEISENVIRONMENT"]=0
    songdesctemplate={}
    coverphone="world/maps/"+namelower+"/menuart/textures/"+namelower+"_cover_phone.jpg"
    coach1phone="world/maps/"+namelower+"/menuart/textures/"+namelower+"_coach_1_phone.png"
    coach2phone="world/maps/"+namelower+"/menuart/textures/"+namelower+"_coach_2_phone.png"
    coach3phone="world/maps/"+namelower+"/menuart/textures/"+namelower+"_coach_3_phone.png"
    coach4phone="world/maps/"+namelower+"/menuart/textures/"+namelower+"_coach_4_phone.png"
    phoneimages={}
    phoneimages["cover"]=coverphone
    try:
        if mapjson["NumCoach"] == 1 or mapjson["NumCoach"] == 'Solo':
            phoneimages["coach1"]=coach1phone
        elif mapjson["NumCoach"] == 2 or mapjson["NumCoach"] == 'Duet':
            phoneimages["coach1"]=coach1phone
            phoneimages["coach2"]=coach2phone
        elif mapjson["NumCoach"] == 3 or mapjson["NumCoach"] == 'Trio':
            phoneimages["coach1"]=coach1phone
            phoneimages["coach2"]=coach2phone
            phoneimages["coach3"]=coach3phone
        elif mapjson["NumCoach"] == 4 or mapjson["NumCoach"] == 'Quatro':
            phoneimages["coach1"]=coach1phone
            phoneimages["coach2"]=coach2phone
            phoneimages["coach3"]=coach3phone
            phoneimages["coach4"]=coach4phone
    except:
        phoneimages["coach1"]=coach1phone
    songdesctemplate["__class"]="JD_SongDescTemplate"
    songdesctemplate["MapName"]=name
    songdesctemplate["JDVersion"]=2016
    try:
        songdesctemplate["OriginalJDVersion"]=mapjson["OriginalJDVersion"]
    except:
        songdesctemplate["OriginalJDVersion"]=2016
    songdesctemplate["Artist"]=mapjson["Artist"]
    songdesctemplate["DancerName"]="Unknown Dancer"
    songdesctemplate["Title"]=mapjson["Title"]
    try:
        songdesctemplate["Credits"]=mapjson["Credits"]
    except:
        songdesctemplate["Credits"]="Empty Credits"
    songdesctemplate["PhoneImages"]=phoneimages
    try:
        if mapjson["NumCoach"] == "Solo" or mapjson["NumCoach"]  == 1:
            songdesctemplate["NumCoach"]=1
        elif mapjson["NumCoach"] == "Duet" or mapjson["NumCoach"]  == 2:
             songdesctemplate["NumCoach"]=2
        elif numcoach == "Trio" or numcoach == 3:
             songdesctemplate["NumCoach"]=3
        elif numcoach == "Quatro" or numcoach == 4:
             songdesctemplate["NumCoach"]=4
    except:
        songdesctemplate["NumCoach"]=1
    songdesctemplate["MainCoach"]=-1
    try:
        songdesctemplate["Difficulty"]=mapjson["Difficulty"]
    except:
        songdesctemplate["Difficulty"]=2
    songdesctemplate["SweatDifficulty"]=2
    songdesctemplate["backgroundType"]=0
    songdesctemplate["LyricsType"]=0
    songdesctemplate["Energy"]=1
    songdesctemplate["Tags"]=["main"]
    songdesctemplate["Status"]=3
    try:
        songdesctemplate["LocaleID"]=mapjson["LocaleID"]
    except:
        songdesctemplate["LocaleID"]=4294967295
    songdesctemplate["MojoValue"]=0
    songdesctemplate["CountInProgression"]=1
    defaultcolors={}
    defaultcolors["lyrics"]=[hex_to_rgb(lyricjson)[0]/255,hex_to_rgb(lyricjson)[1]/255,hex_to_rgb(lyricjson)[2]/255,hex_to_rgb(lyricjson)[3]/255]
    defaultcolors["theme"]=[1,1,1,1]
    songdesctemplate["DefaultColors"]=defaultcolors
    songdesctemplate["VideoPreviewPath"]=""
    components=[songdesctemplate]
    songdesc["COMPONENTS"]=components

    musictrack={}
    musictrack["__class"]="Actor_Template"
    musictrack["WIP"]=0
    musictrack["LOWUPDATE"]=0
    musictrack["UPDATE_LAYER"]=0
    musictrack["PROCEDURAL"]=0
    musictrack["STARTPAUSED"]=0
    musictrack["FORCEISENVIRONMENT"]=0
    beats=list(map(beat48, mapjson['beats']))
    signaturetape={
    "__class": "MusicSignature",
    "marker": 8,
    "beats": 4}
    sectiontape={
    "__class": "MusicSection",
    "marker": 16,
    "sectionType": 8,
    "comment": ""
    }
    signatureclip=[signaturetape]
    sectionclip=[sectiontape]
    structure={}
    structure["__class"]="MusicTrackStructure"
    structure["markers"]=beats
    structure["signatures"]=signatureclip
    structure["sections"]=sectionclip
    structure["startBeat"]=0
    structure["endBeat"]=len(beats)
    structure["videoStartTime"]=0
    try:
        structure["previewEntry"]=mapjson['AudioPreview']['coverflow']['startBeat']
    except:
        structure["previewEntry"]=round(len(beats)/4)
    structure["previewLoopStart"]=round(len(beats)/3)
    structure["previewLoopEnd"]=round(len(beats)/2)
    structure["volume"]=0
    mtdata={}
    mtdata["__class"]="MusicTrackData"
    mtdata["structure"]=structure
    mtdata["path"]="world/maps/"+namelower+"/audio/"+namelower+".ogg"
    mtdata["url"]="jmcs://jd-contents/"+name+"/"+name+".ogg"
    mttemplate={}
    mttemplate["__class"]="MusicTrackComponent_Template"
    mttemplate["trackData"]=mtdata
    components=[mttemplate]
    musictrack["COMPONENTS"]=components

    ktape={
    "__class": "Tape",
    "Clips": [],
    "TapeClock": 0,
    "TapeBarCount": 1,
    "FreeResourcesAfterPlay": 0,
    "MapName": name,
    "SoundwichEvent": ""
    }

    dtape={
    "__class": "Tape",
    "Clips": [],
    "TapeClock": 0,
    "TapeBarCount": 1,
    "FreeResourcesAfterPlay": 0,
    "MapName": name,
    "SoundwichEvent": ""
    }
    
    def ubiarttime(time): #credits to planedec for this script to make synced times for ubiart
        return int(np.interp(time+48,mapjson['beats'],beats_24)-2)

    goldmoveframes=[]

    #pictos
    for picto in mapjson['pictos']:
        picto_id=randint(10000000, 99999999)
        picto_trackid=randint(10000000, 99999999)
        picto_clip={}
        picto_clip["__class"]="PictogramClip"
        picto_clip["Id"]=picto_id
        picto_clip["TrackId"]=picto_trackid
        picto_clip["IsActive"]=1
        picto_clip["StartTime"]=ubiarttime(picto['time'])
        picto_clip["Duration"]=ubiarttime(picto['duration'])
        picto_clip["PictoPath"]="world/maps/"+namelower+"/timeline/pictos/"+picto["name"]+".png"
        picto_clip["CoachCount"]=4294967295
        dtape["Clips"].append(picto_clip)
        picto_id+=1

    #lyrics
    for lyric in mapjson['lyrics']:
        lyric_id=randint(10000000, 99999999)
        lyric_trackid=randint(10000000, 99999999)
        lyric_clip={}
        lyric_clip["__class"]="KaraokeClip"
        lyric_clip["Id"]=lyric_id
        lyric_clip["TrackId"]=lyric_trackid
        lyric_clip["IsActive"]=1
        lyric_clip["StartTime"]=ubiarttime(lyric['time'])
        lyric_clip["Duration"]=ubiarttime(lyric['duration'])
        lyric_clip["Pitch"]=8.661958
        lyric_clip["Lyrics"]=lyric["text"]
        lyric_clip["IsEndOfLine"]=lyric["isLineEnding"]
        lyric_clip["ContentType"]=1
        lyric_clip["StartTimeTolerance"]=4
        lyric_clip["EndTimeTolerance"]=4
        lyric_clip["SemitoneTolerance"]=5
        ktape["Clips"].append(lyric_clip)
        lyric_id+=1
        
    #moves0
    try:
        for move0 in moves0json:
            try:
                goldmove=move0["goldMove"]
            except:
                goldmove=0
            moves0_id=randint(10000000, 99999999)
            moves0_trackid=randint(10000000, 99999999)
            moves0_clip={}
            moves0_clip["__class"]="MotionClip"
            moves0_clip["Id"]=moves0_id
            moves0_clip["TrackId"]=moves0_trackid
            moves0_clip["IsActive"]=1
            moves0_clip["StartTime"]=ubiarttime(move0['time'])
            moves0_clip["Duration"]=ubiarttime(move0['duration'])
            moves0_clip["ClassifierPath"]="world/maps/"+namelower+"/timeline/moves/"+move0["name"]+".msm"
            moves0_clip["GoldMove"]=goldmove
            moves0_clip["CoachId"]=0
            moves0_clip["MoveType"]=0
            moves0_clip["Color"]=[1,1,1,1]
            motionplatformspecific={}
            motionplatformspecifics={}
            motionplatformspecific["ScoreScale"]=1
            motionplatformspecific["ScoreSmoothing"]=0
            motionplatformspecific["ScoringMode"]=0
            motionplatformspecifics["X360"]=motionplatformspecific
            motionplatformspecifics["ORBIS"]=motionplatformspecific
            motionplatformspecifics["DURANGO"]=motionplatformspecific
            moves0_clip["MotionPlatformSpecifics"]=motionplatformspecifics
            dtape["Clips"].append(moves0_clip)
            moves0_id+=1
            if goldmove==1:
                goldmoveframes.append(ubiarttime(move0['time']))
    except:
        pass

    #moves1
    try:
        for move1 in moves1json:
            try:
                goldmove=move1["goldMove"]
            except:
                goldmove=0
            moves1_id=randint(10000000, 99999999)
            moves1_trackid=randint(10000000, 99999999)
            moves1_clip={}
            moves1_clip["__class"]="MotionClip"
            moves1_clip["Id"]=moves1_id
            moves1_clip["TrackId"]=moves1_trackid
            moves1_clip["IsActive"]=1
            moves1_clip["StartTime"]=ubiarttime(move1['time'])
            moves1_clip["Duration"]=ubiarttime(move1['duration'])
            moves1_clip["ClassifierPath"]="world/maps/"+namelower+"/timeline/moves/"+move1["name"]+".msm"
            moves1_clip["GoldMove"]=goldmove
            moves1_clip["CoachId"]=1
            moves1_clip["MoveType"]=0
            moves1_clip["Color"]=[1,1,1,1]
            motionplatformspecific={}
            motionplatformspecifics={}
            motionplatformspecific["ScoreScale"]=1
            motionplatformspecific["ScoreSmoothing"]=0
            motionplatformspecific["ScoringMode"]=0
            motionplatformspecifics["X360"]=motionplatformspecific
            motionplatformspecifics["ORBIS"]=motionplatformspecific
            motionplatformspecifics["DURANGO"]=motionplatformspecific
            moves1_clip["MotionPlatformSpecifics"]=motionplatformspecifics
            dtape["Clips"].append(moves1_clip)
            moves1_id+=1
            if goldmove==1:
                goldmoveframes.append(ubiarttime(move1['time']))
    except:
        pass
    
    #moves2
    try:
        for move2 in moves2json:
            try:
                goldmove=move2["goldMove"]
            except:
                goldmove=0
            moves2_id=randint(10000000, 99999999)
            moves2_trackid=randint(10000000, 99999999)
            moves2_clip={}
            moves2_clip["__class"]="MotionClip"
            moves2_clip["Id"]=moves2_id
            moves2_clip["TrackId"]=moves2_trackid
            moves2_clip["IsActive"]=1
            moves2_clip["StartTime"]=ubiarttime(move2['time'])
            moves2_clip["Duration"]=ubiarttime(move2['duration'])
            moves2_clip["ClassifierPath"]="world/maps/"+namelower+"/timeline/moves/"+move2["name"]+".msm"
            moves2_clip["GoldMove"]=goldmove
            moves2_clip["CoachId"]=2
            moves2_clip["MoveType"]=0
            moves2_clip["Color"]=[1,1,1,1]
            motionplatformspecific={}
            motionplatformspecifics={}
            motionplatformspecific["ScoreScale"]=1
            motionplatformspecific["ScoreSmoothing"]=0
            motionplatformspecific["ScoringMode"]=0
            motionplatformspecifics["X360"]=motionplatformspecific
            motionplatformspecifics["ORBIS"]=motionplatformspecific
            motionplatformspecifics["DURANGO"]=motionplatformspecific
            moves2_clip["MotionPlatformSpecifics"]=motionplatformspecifics
            dtape["Clips"].append(moves2_clip)
            moves2_id+=1
            if goldmove==1:
                goldmoveframes.append(ubiarttime(move2['time']))
    except:
        pass

    #moves3
    try:
        for move3 in moves3json:
            try:
                goldmove=move3["goldMove"]
            except:
                goldmove=0
            moves3_id=randint(10000000, 99999999)
            moves3_trackid=randint(10000000, 99999999)
            moves3_clip={}
            moves3_clip["__class"]="MotionClip"
            moves3_clip["Id"]=moves3_id
            moves3_clip["TrackId"]=moves3_trackid
            moves3_clip["IsActive"]=1
            moves3_clip["StartTime"]=ubiarttime(move3['time'])
            moves3_clip["Duration"]=ubiarttime(move3['duration'])
            moves3_clip["ClassifierPath"]="world/maps/"+namelower+"/timeline/moves/"+move3["name"]+".msm"
            moves3_clip["GoldMove"]=goldmove
            moves3_clip["CoachId"]=3
            moves3_clip["MoveType"]=0
            moves3_clip["Color"]=[1,1,1,1]
            motionplatformspecific={}
            motionplatformspecifics={}
            motionplatformspecific["ScoreScale"]=1
            motionplatformspecific["ScoreSmoothing"]=0
            motionplatformspecific["ScoringMode"]=0
            motionplatformspecifics["X360"]=motionplatformspecific
            motionplatformspecifics["ORBIS"]=motionplatformspecific
            motionplatformspecifics["DURANGO"]=motionplatformspecific
            moves3_clip["MotionPlatformSpecifics"]=motionplatformspecifics
            dtape["Clips"].append(moves3_clip)
            moves3_id+=1
            if goldmove==1:
                goldmoveframes.append(ubiarttime(move3['time']))
    except:
        pass

    #adding goldeffect clips
    for goldeffecttime in removeduplicate(goldmoveframes):
        goldeffect_id=randint(10000000, 99999999)
        goldeffect_trackid=randint(10000000, 99999999)
        goldeffect_clip={}
        goldeffect_clip["__class"]="GoldEffectClip"
        goldeffect_clip["Id"]=goldeffect_id
        goldeffect_clip["TrackId"]=goldeffect_trackid
        goldeffect_clip["IsActive"]=1
        goldeffect_clip["StartTime"]=goldeffecttime+24 #
        goldeffect_clip["Duration"]=24
        goldeffect_clip["EffectType"]=0

        dtape["Clips"].append(goldeffect_clip)
        goldeffect_id+=1

    json.dump(songdesc,open(fr'temp/{namelower}_nx/cache/itf_cooked/nx/world/maps/{namelower}/songdesc.tpl.ckd',"w"))
    json.dump(musictrack,open(fr'temp/{namelower}_nx/cache/itf_cooked/nx/world/maps/{namelower}/audio/{namelower}_musictrack.tpl.ckd',"w"))
    json.dump(ktape,open(fr'temp/{namelower}_nx/cache/itf_cooked/nx/world/maps/{namelower}/timeline/{namelower}_tml_karaoke.ktape.ckd',"w"))
    json.dump(dtape,open(fr'temp/{namelower}_nx/cache/itf_cooked/nx/world/maps/{namelower}/timeline/{namelower}_tml_dance.dtape.ckd',"w"))
print("Converting JDNOW to UBIART...")
j2d()

outputpath = fr'temp/'
outputpathwithmapname = fr'temp/' + name

def nxpicto(name):
    try:
        os.makedirs('temp/pictos/nx')
        os.makedirs('temp/pictos/xtx')
        os.makedirs('temp/pictos/dds')
    except:
        pass
    for png in os.listdir(outputpath+'/pictos/png'):
        file_name=png.split('.')[0]
        dds=image.Image(filename='temp/pictos/png/' + png)
        dds.compression='dxt5'
        dds.save(filename='temp/pictos/dds/'+file_name+'.dds')

    for dds in os.listdir(outputpath+'/pictos/dds'):
        print(dds)
        subprocess.check_call(['bin/xtxextract.exe','-o',outputpath+'/pictos/xtx/'+dds.replace('.dds','.xtx'),outputpath+'/pictos/dds/'+dds])

    for xtx in os.listdir(outputpath+'/pictos/xtx'):
        with open(outputpath+'/pictos/xtx/'+xtx, "rb") as f:
            xtxdata=f.read()

        ckdoutput=open(outputpath+'/pictos/nx/'+xtx.replace(".xtx",".png.ckd"),"wb")
        ckdoutput.write(b'\x00\x00\x00\x09\x54\x45\x58\x00\x00\x00\x00\x2C\x00\x00\x20\x80\x01\x00\x01\x00\x00\x01\x18\x00\x00\x00\x20\x80\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\xCC\xCC')

        ckdoutput.write(xtxdata)
        ckdoutput.close()

    #moving picto files into the correct directory
    for picto in os.listdir('temp/pictos/nx'):
        shutil.move('temp/pictos/nx/'+picto,outputpathwithmapname + '_nx' + '/cache/itf_cooked/nx/world/maps/' + namelower + '/timeline/pictos/' + picto)
    os.rmdir('temp/pictos/nx')
    for xtx in os.listdir(outputpath+'/pictos/xtx'):
        os.remove(outputpath+'/pictos/xtx/'+xtx)
    os.rmdir('temp/pictos/xtx')

print('''



____  __________________  ___ _________  ____  __.________   
\   \/  /\__    ___/\   \/  / \_   ___ \|    |/ _|\______ \  
 \     /   |    |    \     /  /    \  \/|      <   |    |  \ 
 /     \   |    |    /     \  \     \___|    |  \  |    `   \
/___/\  \  |____|   /___/\  \  \______  /____|__ \/_______  /
      \_/                 \_/         \/        \/        \/ 

                                                 
By JackLSummer15

''')

print('Making pictos #slay')
nxpicto(name)

videoscoachpath = fr'temp/{name.lower()}_nx/world/maps/{name.lower()}/videoscoach'
#examplepath = fr'temp/{namelower}_nx/cache/itf_cooked/nx/world/maps/{namelower}/menuart/textures/'
msmpath = fr'temp/{namelower}_nx/world/maps/{namelower}/timeline/moves/wiiu'

#Copy classifiers
try:
    shutil.copytree('temp/classifiers/', msmpath, dirs_exist_ok=True)
except KeyError:
    print("You flopped. Here's your fucking error: " + KeyError)

# Copy the videoscoach
try:
    shutil.copy('input/' + name.lower() + '.vp9.720.webm', videoscoachpath)
except KeyError:
    print("You flopped. KeyError: " + KeyError)

## MenuArt
menuartpath = fr'temp/{namelower}_nx/cache/itf_cooked/nx/world/maps/{namelower}/menuart/textures/'

try:
    shutil.copytree('input/menuart/', menuartpath, dirs_exist_ok=True)
except KeyError:
    print("You flopped. Here's your fucking error: " + KeyError)

## OGG 
audiopath = fr'temp/{name.lower()}_nx/world/maps/{name.lower()}/audio/'
shutil.copy('input/' + name.lower() + '.ogg', audiopath)

## Write code above this line

# Pack to the directory

thefuckingpathorsomeshit = fr'temp/{name.lower()}_nx/'


try:
    shutil.copytree(thefuckingpathorsomeshit, 'output\\' + name.lower() + '_nx', dirs_exist_ok=True)
except KeyError:
    print("IPK could not pack! KeyError: " + KeyError)

print("YASS You automodded a map! slay!")
