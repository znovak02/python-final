from pyautogui import locateOnScreen, moveTo, click, scroll, typewrite
import pyautogui
import time
import keyboard
import win32api, win32con
from typing import Tuple
#This is a cyber-security based project that I did over the summer, I wrote over what I did over the summer
#I hope that it makes some sense, it is a survey taking robot I was inspired to make after learning about
#Selenium a couple years ago, but many websites have selenium blocked, while system based services like pyautogui are not
#This code is very specific to my sytem and configured to fit my resolution size on my monitor, so sorry.
#It is for the website college pulse

class BaseBot:
    def __init__(self, root): #Set root
        self._root = root

    def click(self, x: int, y: int) -> None:
        win32api.SetCursorPos((x, y))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
        #Coordinate mouse to click

class SurveyBot(BaseBot):
    def run(self) -> None:
        time.sleep(5)
        #Delay to prevent users from interfering with bot process

        try:
            while not keyboard.is_pressed('q'):
                self._process_newly_added()
                self._process_inside_survey()
                self._submit_and_return()
        except Exception as e:
            print(f"An error occurred: {e}")

    def _process_newly_added(self) -> None:
        if locateOnScreen("Newlyadded.png", grayscale=False, confidence=0.8):
            moveTo(*locateOnScreen("Newlyadded.png", grayscale=False, confidence=0.8))
            click()
            time.sleep(0.5)
            #Newly added allows a user (or a bot) to access surveys with higher points

    def _process_inside_survey(self) -> None:
        while pyautogui.locateOnScreen("Insidethesurvey.png", grayscale=False, confidence= 0.8) == None:
            
            if pyautogui.locateOnScreen("Fiftypointsbetter.png", grayscale=False, confidence= 0.8) != None:
                pyautogui.moveTo(pyautogui.locateOnScreen("Fiftypointsbetter.png", grayscale=False, confidence= 0.8))
                pyautogui.click()
                time.sleep(0.5)
                #Point priorotization for the bot
            
            elif pyautogui.locateOnScreen("Frontpagenext.png", grayscale=False, confidence= 0.8) != None:
                pyautogui.moveTo(pyautogui.locateOnScreen("Frontpagenext.png", grayscale=False, confidence= 0.8))
                pyautogui.click()
                time.sleep(0.5)
                #Page navigation
            
            else:
                pyautogui.scroll(1)
                time.sleep(0.5)
                #Adding sleep time is also great for preventing perma banning of bot/user accounts

    def answering_questions(self) -> None:      
        while pyautogui.locateOnScreen("Submit.png", grayscale=False, confidence= 0.8) == None:
            
            if pyautogui.locateOnScreen("Bubble.png", grayscale=False, confidence= 0.8) != None:
                pyautogui.moveTo(pyautogui.locateOnScreen("Bubble.png", grayscale=False, confidence= 0.8))
                pyautogui.click()
                time.sleep(0.5)
                #Most surveys have a different layout for selectable icons and even text boxes
                    
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

                    
    def _submit_and_return(self) -> None:    
        pyautogui.moveTo(pyautogui.locateOnScreen("Submit.png", grayscale=False, confidence= 0.8))
        pyautogui.click()
        time.sleep(0.5)
        #After every completed survey, submit

        pyautogui.moveTo(pyautogui.locateOnScreen("Returnpulselogo.png", grayscale=False, confidence= 0.8))
        pyautogui.click()
        time.sleep(0.5)


def main():
    bot = SurveyBot(None)
    bot.run()


if __name__ == "__main__":
    main()

#Lamo main stuff...
