#OOPStructure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import pytest
import time

class ParaBank:
    def __init__(self):
        self.driver = webdriver.Firefox()

    def setup(self):
        self.driver.get("https://parabank.parasoft.com/parabank/index.htm;jsessionid=7CD8C959526F3B180A6E58C14625BF40")
        self.driver.maximize_window()
        print("Open URL")

    def register(self):
        self.driver.find_element(By.LINK_TEXT, "Register").click()
        print("Click Register")

    def login(self):
        self.driver.find_element(By.NAME, "username").send_keys("QA")
        self.driver.find_element(By.NAME,"password").send_keys("123456", Keys.ENTER)
        print ("Login Success")
        time.sleep(3)

    def account_overview(self):
        acc_number = self.driver.find_element(By.LINK_TEXT, "16563").text
        acc_balance = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[2]/div/div[1]/table/tbody/tr[1]/td[2]").text
        acc_amount = self.driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[2]/div/div[1]/table/tbody/tr[1]/td[3]").text
        print("Account Number: ",acc_number)
        print("Account Balance: ",acc_balance)
        print("Account Amount: ",acc_amount)
        print("Account Over View Success")
        to_before_acc = self.driver.find_element(By.LINK_TEXT,"17118").text
        to_before_balance = self.driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[2]/div/div[1]/table/tbody/tr[2]/td[2]").text
        print("To Before Account: ",to_before_acc)
        print("To Before Balance: ",to_before_balance)
        time.sleep(4)

    def open_new_account(self):
        self.driver.find_element(By.LINK_TEXT,"Open New Account").click()
        self.driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[2]/div/div[1]/form/select[1]/option[2]")
        self.driver.find_element(By.CLASS_NAME, "button").click()
        print("Open New Account")

    def transfer(self):
        self.driver.find_element(By.LINK_TEXT,"Transfer Funds").click()
        self.driver.find_element(By.ID, "amount").send_keys("10")
        time.sleep(3)
        select = Select(self.driver.find_element(By.ID, "fromAccountId"))
        select.select_by_visible_text("16563")
        time.sleep(3)
        select = Select(self.driver.find_element(By.ID, "toAccountId"))
        select.select_by_value("17118")
        time.sleep(3)
        self.driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[2]/div/div[1]/form/div[2]/input").click()
        time.sleep(10)
        print("Transfer Success")

    def verify_amount(self):
        self.driver.find_element(By.LINK_TEXT,"Accounts Overview").click()
        time.sleep(5)
        from_account = self.driver.find_element(By.LINK_TEXT, "16563").text
        time.sleep(5)
        from_acc_balance = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[2]/div/div[1]/table/tbody/tr[1]/td[2]").text
        from_acc_amount = self.driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[2]/div/div[1]/table/tbody/tr[1]/td[3]").text
        to_after_balance = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[2]/div/div[1]/table/tbody/tr[2]/td[2]").text
        print("From Account Number: ",from_account)
        print("From Account Balance: ",from_acc_balance)
        print("From Account Amount: ",from_acc_amount)
        print("To After Balance: ",to_after_balance)
        print("Account Verify Success")
        time.sleep(4)

    def main(self):
        self.setup()
        self.register()
        self.login()
        self.account_overview()
        #self.open_new_account()
        self.transfer()
        self.verify_amount()
        self.driver.quit()

ParaBank().main()