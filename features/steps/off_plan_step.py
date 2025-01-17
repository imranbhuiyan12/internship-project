from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep




@when ('Click on “off plan” at the left side menu')
def click_off_plan_menu(context):
    context.app.off_plan.click_off_plan_button()

@then ('Verify the right page opens')
def verify_right_page(context):
    # expected = 'Off-plan'
    # actual = context.driver.find_element(By.XPATH, "//a[text()='Off-plan']").text
    # assert expected == actual, f"{expected} is not in {actual}"
    # print("Verified")
    context.app.off_plan.verify_right_page()


@when ('Click on Filters and Filter by sale status of “Out of Stocks”')
def click_filters(context):
    context.app.off_plan.select_filter()



@then ('Verify each product contains the Out of Stocks tag')
def verify_each_product_contains(context):
    # context.driver.execute_script("window.scrollBy(0,2000)", "")
    # sleep(4)
    # context.driver.execute_script("window.scrollBy(0,2000)", "")
    # all_product = context.driver.find_elements(By.CSS_SELECTOR, "[wized='cardOfProperty']")
    # print(all_product)
    # for OutOfStock in all_product:
    #     tag_oos = OutOfStock.find_elements(By.CSS_SELECTOR,"[wized='projectStatus']")
    #     assert tag_oos != '', f"product not shown"

    context.app.off_plan.verify_each_listing()








