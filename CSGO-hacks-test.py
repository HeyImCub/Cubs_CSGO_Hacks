import pymem
import pymem.process
import keyboard
import pyautogui
import pydirectinput
import time
from math import sqrt,pi,atan
import math
import requests



offsets = 'https://raw.githubusercontent.com/kadeeq/ProjectX/main/offsets/offsets.json'
response = requests.get( offsets ).json()

m_vecViewOffset = int( response["netvars"]["m_vecViewOffset"] )
m_iHealth =int( response["netvars"]["m_iHealth"] )
m_vecOrigin = int( response["netvars"]["m_vecOrigin"] )
dwClientState = int( response["signatures"]["dwClientState"] )
dwClientState_ViewAngles = int( response["signatures"]["dwClientState_ViewAngles"] )
dwEntitityList = int( response["signatures"]["dwEntityList"] )
dwLocalPlayer = int( response["signatures"]["dwLocalPlayer"] )
m_iTeamNum = (int( response["netvars"]["m_iTeamNum"] )
dwGlowObjectManager = int( response["signatures"]["dwGlowObjectManager"] )
m_iGlowIndex =int( response["netvars"]["m_iGlowIndex"] )
m_iFOV = int(respone["netvars"]["m_iFOV"])
dwForceJump = int( response["signatures"]["dwForceJump"] )
m_fFlags = int( response["netvars"]["m_fFlags"] )
switch = 0
pm = pymem.Pymem("csgo.exe")
client = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll
engine = pymem.process.module_from_name(pm.process_handle, "engine.dll").lpBaseOfDll


aimfov = 120




def main():
    
    
    entity_team_id = None
    player = pm.read_int(client + dwLocalPlayer)
    
    choice = 0
    
    while True:
        iFOV = pm.read_int(player + m_iFOV)
        
        if keyboard.is_pressed("space"):
            force_jump = client + dwForceJump
            on_ground = pm.read_int(player + m_fFlags)
            if player and on_ground and on_ground == 257:
                pm.write_int(force_jump,5)
                time.sleep(0.08)
                pm.write_int(force_jump,4)
        
        if keyboard.is_pressed("end"):
                pm.write_int(player + m_iFOV,100)
                exit(0)

        if keyboard.is_pressed("page up"):
                pm.write_int(player + m_iFOV,140)
        if keyboard.is_pressed("page down"):
                pm.write_int(player + m_iFOV,100)
        localplayer = pm.read_int(client + dwLocalPlayer)
       
        glow_manager = pm.read_int(client + dwGlowObjectManager)

        for i in range(1,32):
                entity = pm.read_int(client +dwEntitityList+i * 0x10)


                if entity:
                    entity_team_id = pm.read_int(entity + m_iTeamNum)
                    entity_glow = pm.read_int(entity + m_iGlowIndex)

                
                
                    if entity_team_id == 2:
                        pm.write_float(glow_manager + entity_glow * 0x38 + 0x4,float(1))
                        pm.write_float(glow_manager + entity_glow * 0x38 + 0x8,float(0))
                        pm.write_float(glow_manager + entity_glow * 0x38 + 0xC,float(0))
                        pm.write_float(glow_manager + entity_glow * 0x38 + 0x10,float(1))
                        pm.write_int(glow_manager + entity_glow * 0x38 + 0x24,1)

                    elif entity_team_id == 3:
                        pm.write_float(glow_manager + entity_glow * 0x38 + 0x4,float(0))
                        pm.write_float(glow_manager + entity_glow * 0x38 + 0x8,float(0))
                        pm.write_float(glow_manager + entity_glow * 0x38 + 0xC,float(1))
                        pm.write_float(glow_manager + entity_glow * 0x38 + 0x10,float(1))
                        pm.write_int(glow_manager + entity_glow * 0x38 + 0x24,1)
                    
                    
                

                    

if __name__ == '__main__':
    main()
