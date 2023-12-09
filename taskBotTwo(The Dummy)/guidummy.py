from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

class bot:
    def __init__(self, root):
         self.root = root
         time.sleep(5) #Sleep to allow for a user to not interrupt bot process
         self.click()
         
    def click(x,y):
        win32api.SetCursorPos((x,y))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    #Clicks according to input values

    #Color of center: (255, 219, 195)

    while keyboard.is_pressed('q') == False:
        #Stops bot process
        if pyautogui.locateOnScreen("Newlyadded.png", grayscale=False, confidence= 0.8) != None:
            pyautogui.moveTo(pyautogui.locateOnScreen("Newlyadded.png", grayscale=False, confidence= 0.8))
            pyautogui.click()
            time.sleep(0.5)
            
        else:
            pass
    
        
        while pyautogui.locateOnScreen("Insidethesurvey.png", grayscale=False, confidence= 0.8) == None:
            
            if pyautogui.locateOnScreen("Fiftypointsbetter.png", grayscale=False, confidence= 0.8) != None:
                pyautogui.moveTo(pyautogui.locateOnScreen("Fiftypointsbetter.png", grayscale=False, confidence= 0.8))
                pyautogui.click()
                time.sleep(0.5)
            
            elif pyautogui.locateOnScreen("Frontpagenext.png", grayscale=False, confidence= 0.8) != None:
                pyautogui.moveTo(pyautogui.locateOnScreen("Frontpagenext.png", grayscale=False, confidence= 0.8))
                pyautogui.click()
                time.sleep(0.5)
            
            else:
                pyautogui.scroll(1)
                time.sleep(0.5)
                
        while pyautogui.locateOnScreen("Submit.png", grayscale=False, confidence= 0.8) == None:
            
            if pyautogui.locateOnScreen("Bubble.png", grayscale=False, confidence= 0.8) != None:
                pyautogui.moveTo(pyautogui.locateOnScreen("Bubble.png", grayscale=False, confidence= 0.8))
                pyautogui.click()
                time.sleep(0.5)
                    
                if pyautogui.locateOnScreen("Questionairenext.png", grayscale=False, confidence= 0.8) != None:
                    pyautogui.moveTo(pyautogui.locateOnScreen("Questionairenext.png", grayscale=False, confidence= 0.8))
                    pyautogui.click()
                    time.sleep(0.5)
                        
            
            elif pyautogui.locateOnScreen("Thetextbox.png", grayscale=False, confidence= 0.8) != None:
                    pyautogui.moveTo(pyautogui.locateOnScreen("Thetextbox.png", grayscale=False, confidence= 0.8))
                    pyautogui.click()
                    pyautogui.typewrite("n/a")
                    
                    if pyautogui.locateOnScreen("Questionairenext.png", grayscale=False, confidence= 0.8) != None:
                        pyautogui.moveTo(pyautogui.locateOnScreen("Questionairenext.png", grayscale=False, confidence= 0.8))
                        pyautogui.click()
                        time.sleep(0.5)
                        
            elif pyautogui.locateOnScreen("Square.png", grayscale=False, confidence= 0.8) != None:
                    pyautogui.moveTo(pyautogui.locateOnScreen("Square.png", grayscale=False, confidence= 0.8))
                    pyautogui.click()
                    
                    if pyautogui.locateOnScreen("Multisquare.png", grayscale=False, confidence= 0.8) != None:
                        pyautogui.moveTo(pyautogui.locateOnScreen("Square.png", grayscale=False, confidence= 0.8))
                        pyautogui.click()
                        pyautogui.scroll(1)
                        
                    elif pyautogui.locateOnScreen("Questionairenext.png", grayscale=False, confidence= 0.8) != None:
                        pyautogui.moveTo(pyautogui.locateOnScreen("Questionairenext.png", grayscale=False, confidence= 0.8))
                        pyautogui.click()
                        time.sleep(0.5)
                        
                        
            elif pyautogui.locateOnScreen("Questionairenext.png", grayscale=False, confidence= 0.8) != None:
                    pyautogui.moveTo(pyautogui.locateOnScreen("Questionairenext.png", grayscale=False, confidence= 0.8))
                    pyautogui.click()
                    time.sleep(0.5)
                    
            else:
                pass
                    
            
        pyautogui.moveTo(pyautogui.locateOnScreen("Submit.png", grayscale=False, confidence= 0.8))
        pyautogui.click()
        time.sleep(0.5)

        pyautogui.moveTo(pyautogui.locateOnScreen("Returnpulselogo.png", grayscale=False, confidence= 0.8))
        pyautogui.click()
        time.sleep(0.5)
                
            
    
        
