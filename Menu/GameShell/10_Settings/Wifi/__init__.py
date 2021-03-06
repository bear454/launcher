# -*- coding: utf-8 -*- 


## local UI import
import pages
import myvars
"""
try:
    from icons import preload
except:
    print("No icons package")
"""
from icons import preload

def Init(main_screen):
    
    preload.load_icons()
    pages.InitPasswordPage(main_screen)
    pages.InitScanPage(main_screen)

def API(main_screen):
    
    if main_screen != None:
        main_screen.PushCurPage()
        main_screen.SetCurPage(myvars.ScanPage)
        main_screen.Draw()
        main_screen.SwapAndShow()


