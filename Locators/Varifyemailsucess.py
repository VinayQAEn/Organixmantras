from selenium.webdriver.common.by import By

class Verifyemailmsg:
    txt_emailmsg_Xpath = "//p[contains(text(),'Please check We’ve sent a verification Link to you')]"

    def __init__(self, driver):
        self.driver = driver

    def get_email_successmsg(self):
        """Verifies if the success message is displayed after entering an email."""
        email_field = self.driver.find_element(By.XPATH, "//input[@placeholder='Email']")
        entered_email = email_field.get_attribute("value")  # Get the email entered
        
        try:
            success_msg_element = self.driver.find_element(By.XPATH, self.txt_emailmsg_Xpath)
            success_msg = success_msg_element.text
            assert "Please check We’ve sent a verification Link to you" in success_msg
            print(f"✅ Success message displayed: {success_msg}")
            return True
        except Exception:
            print("❌ Verification message not found!")
            return False



    