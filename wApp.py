from time import sleep

class wApp:
    def __init__(self,driver) -> None:
        self.driver = driver
    
    def search_for(self,text):
        text_area = self.driver.find_element(by="xpath", value='//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]')
        text_area.send_keys(text)
        print("sleeping for 20S")
        sleep(5)
        click_area = self.driver.find_element(by="xpath",value = '//*[@id="pane-side"]/div[1]/div/div/div[1]/div/div/div/div[2]/div[1]/div[1]/span')
        click_area.click()
        sleep(5)
        click_area = self.driver.find_element(by="xpath",value = '//*[@id="pane-side"]/div[1]/div/div/div[1]/div/div/div/div[2]/div[1]/div[1]/span')
        click_area.click()

    def send_menssage(self,menssage):
        text_message = self.driver.find_element(by = 'xpath',value = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]')
        text_message.send_keys(menssage)
        sleep(5)

        send_it = self.driver.find_element(by = 'xpath', value = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]')
        send_it.click()
    
    def get_last_menssage(self):
        message = self.driver.find_element(by = 'xpath', value = '//*[@id="pane-side"]/div[1]/div/div/div[15]/div/div/div/div[2]/div[2]/div[1]/span/span[3]')
        return message.get_attribute("innerHTML")


