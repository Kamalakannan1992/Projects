from selenium.webdriver.common.by import By
class HomePage():

    def __init__(self, driver):
        self.driver = driver

        self.pim_button_xpath = "//a[@href='/web/index.php/pim/viewPimModule']"
        self.add_button_xpath = "//button[@class='oxd-button oxd-button--medium oxd-button--secondary']"
        self.firstname_textbox_xpath = "//input[@class='oxd-input oxd-input--active orangehrm-firstname']"
        self.lastname_textbox_xpath  = "//input[@class='oxd-input oxd-input--active orangehrm-lastname']"
        self.save_button_xpath = "//button[@type='submit']"
        self.edit_button_xpath = "//*[contains(text(),'0261')]"
        self.editlastname_textbox_xpath = "//input[@class='oxd-input oxd-input--active orangehrm-lastname']"
        self.edit_save_button_xpath = "//button[@class='oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space']"

    def click_pim(self):
        self.driver.find_element(By.XPATH, self.pim_button_xpath).click()

    def click_add(self):
        self.driver.find_element(By.XPATH, self.add_button_xpath).click()

    def enter_firstname(self, firstname):
        self.driver.find_element(By.XPATH, self.firstname_textbox_xpath).clear()
        self.driver.find_element(By.XPATH, self.firstname_textbox_xpath).send_keys(firstname)

    def enter_lastname(self, lastname):
        self.driver.find_element(By.XPATH, self.lastname_textbox_xpath).clear()
        self.driver.find_element(By.XPATH, self.lastname_textbox_xpath).send_keys(lastname)

    def click_save(self):
        self.driver.find_element(By.XPATH, self.save_button_xpath).click()

    def click_editname(self):
        self.driver.find_element(By.XPATH, self.edit_button_xpath).click()

    def edit_lastname(selfself, lastname):
        self.driver.find_element(By.XPATH, editlastname_textbox_xpath).clear()
        self.driver.find_element(By.XPATH, editlastname_textbox_xpath).send_keys(lastname)

    def click_editsave(self):
        self.driver.find_element(By.XPATH, edit_save_button_xpath).click()



