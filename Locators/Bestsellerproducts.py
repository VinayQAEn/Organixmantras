from selenium.webdriver.common.by import By
import time

class BestSEllerPRoduct:
    def __init__(self,driver):
        self.driver = driver
    Addtocart_btn_Xpath = "/html/body/app-root/app-home-page/div[2]/app-product-slider/div/div/div/div[2]/ngx-slick-carousel/div/div/div[1]/app-product-card/div/div/div/div[2]/div/div/div/div/button"
    Addproductquantity_Xpath = "//div[@class='quantitt-box ng-star-inserted']//span[@class='pi pi-plus']"
    item_cart_btn = "//div[@class='quantitt-box ng-star-inserted']//span[@class='pi pi-plus']"
    cat_btn_xpath = "//span[normalize-space()='Proceed']"
    Delevery_dateBTN_xpath = "//chevrondownicon[@class='p-element p-icon-wrapper ng-star-inserted']//*[name()='svg']"
    Dates_Xpath = "//div[@class='p-dropdown-items-wrapper']"
    Checkout_btn_xpath = "//span[normalize-space()='Checkout']"
    def add_tocart(self):
        self.driver.find_element(By.XPATH,self.Addtocart_btn_Xpath).click()
        time.sleep(8)
    def add_product_quantity(self):
        self.driver.find_element(By.XPATH,self.Addproductquantity_Xpath).click()
