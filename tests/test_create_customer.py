def test_create_customer(customer_page):
    customer_page.open_page()
    customer_page.fill_create_form()
    customer_page.check_thank_you_text('Thank you for registering with Main Website Store.')


def test_check_pass_for_strong(customer_page):
    customer_page.open_page()
    customer_page.check_pass_for_strong('Strong')


def test_check_header_title(customer_page):
    customer_page.open_page()
    customer_page.check_header_title('Create New Customer Account')
