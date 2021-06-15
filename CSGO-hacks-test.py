import pymem
import pymem.process
import keyboard
import pyautogui
import pydirectinput
import time
from math import sqrt,pi,atan
import math

m_vecViewOffset = (0x108)
m_iHealth =(0x100)
m_vecOrigin = (0x138)
dwClientState = (0x588FEC)
dwClientState_ViewAngles = (0x4D90)
dwEntitityList = (0x4DA215C)
dwLocalPlayer = (0xD892CC)
m_iTeamNum = (0xF4)
dwGlowObjectManager = (0x52EA5D0)
m_iGlowIndex =(0xA438)
m_iObserverMode = (0x3378)
m_dwBoneMatrix = (0x26A8)
m_bDormant = (0xED)
m_iFOV = (0x31E4)
dwForceJump = (0x524BF4C)
m_fFlags = (0x104)
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