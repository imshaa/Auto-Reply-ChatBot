import pyautogui
import time
import pyperclip

def automate_text_selection_and_copy():
    
    pyautogui.click(520, 170)  # Adjust coordinates if needed
    time.sleep(1)  # Wait for user to manually select the text


    
    
    print("Please drag and select the text, then wait for the script to continue...")
    time.sleep(3)  
   
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.5)
    pyautogui.click(1284,655)  

   
    copied_text = pyperclip.paste()
    return copied_text


copied_text = automate_text_selection_and_copy()
print(f"Copied Text: {copied_text}")
