def test_new_tab_and_check(sale_page):
    sale_page.open_page()
    sale_page.new_tab_and_check_header('Tees')


def test_select_women_jacket(sale_page):
    sale_page.open_page()
    sale_page.select_women('Jackets')


def test_go_to_logo(sale_page):
    sale_page.open_page()
    sale_page.go_to_logo('New Luma Yoga Collection')
