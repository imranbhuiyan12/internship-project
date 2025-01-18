from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep




@when ('Click on “off plan” at the left side menu')
def click_off_plan_menu(context):
    context.app.off_plan.click_off_plan_button()

@then ('Verify the right page opens')
def verify_right_page(context):
    context.app.off_plan.verify_right_page()


@when ('Click on Filters and Filter by sale status of “Out of Stocks”')
def click_filters(context):
    context.app.off_plan.select_filter()



@then ('Verify each product contains the Out of Stocks tag')
def verify_each_product_contains(context):
    context.app.off_plan.verify_each_listing()








