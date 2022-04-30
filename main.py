from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
PATH = '/Users/jonathantan/Documents/Python Project/chromedriver'
driver = webdriver.Chrome(PATH)

driver.get("online.enablelc.org/")
time.sleep(1)

input_month = 1;
input_date = 29;
#dateselection
#take input month and date; then take (input month) - (Current Month) and click the ">" button

Next_month_button = driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[1]/xn-bookinglist-component/xn-calendar-popup/div/div/div/div/div[1]/div/span[3]")
Next_month_button.click()

date_button = driver.find_elements_by_xpath("//td[contains(text(), '"+input_date+"')]").click();
#or //* not sure if td is considered tag name I think it is; good explanations can be found by googling xpath tutorials
#activityselection
slot_button = driver.find_elements_by_xpath("//article [.//a[.='Tennis']]//a[.='"+input_time+"']")
# Really really good explanation of multiple levels of search https://stackoverflow.com/questions/53642438/find-by-xpath-with-multiple-elements-seperate-lines

#slotselection






#login screen
input_email = driver.find_element_by_id("email")
input_password = driver.find_element_by_id("password")

input_email.send_keys("Jonathanhktan@gmail.com")
input_password.send_keys("Iam110%sexy")

login_button = driver.find_element_by_xpath("/html/body/div[3]/div/div/div[1]/form/div[3]/div[2]/div/button")
login_button.click()

time.sleep(1)

#donation form input
for x in range(11):
    input_cause_id = Select(driver.find_element_by_id("cause_id"))
    input_donation = driver.find_element_by_id("amount")
    input_reference = driver.find_element_by_id("payment_reference")

    input_cause_id.select_by_value("176")
    input_donation.send_keys("10")
    input_reference.send_keys("Correction")

    save_button = driver.find_element_by_xpath("/html/body/div[3]/div/div/form/div/div/div/div/div[4]/div/button")
    save_button.click()

    time.sleep(1)

    add_another_button = driver.find_element_by_xpath("/html/body/div[3]/div/div/form/div/div/div[2]/div/div[4]/div/a[2]")
    add_another_button.click()
    x+=1

else:
    print("Function was looped for "+str(x)+" times")