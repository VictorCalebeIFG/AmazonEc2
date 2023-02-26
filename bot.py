from get_driver import get_driver
from gsheets import get_all, get_hour
from wApp import wApp
from datetime import date,datetime
from time import sleep

def dayly_remember(time):
    text = ''
    #WHAT TIME IS IT?
    now = datetime.now()
    if time == now.strftime("%H:%M"):
        for bot_text in get_all("Every_Day"):
            if bot_text["OUTPUT"]:
                text += '[BOT]: '+bot_text["OUTPUT"]+'\n'
        
        return [True,text]
    
    return [False,False]


driver = get_driver()
driver.get("https://web.whatsapp.com/")


while True:
    ok = input("Want to screenshot?[y]or[n]")
    if ok == 'n':
        break
    else: driver.save_screenshot("screenshot.png"); print("check screenshot.png")

user = input("For who do you want to send?")
print('scheduled time: ',get_hour('Every_Day'))

W_app = wApp(driver)

while True:
    sleep(5)
    remeber = dayly_remember(get_hour('Every_Day'))
    if remeber[0]:
        W_app.search_for(user)
        sleep(1)
        W_app.send_menssage(remeber[1])
        sleep(60)




