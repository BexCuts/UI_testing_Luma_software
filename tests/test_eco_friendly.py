def test_change_table_to_list(eco_friendly_page):
    eco_friendly_page.open_page()
    eco_friendly_page.change_table_to_list('Add Your Review')


def test_len_of_elements(eco_friendly_page):
    eco_friendly_page.open_page()
    eco_friendly_page.len_of_elements()


def test_add_to_card(eco_friendly_page):
    eco_friendly_page.open_page()
    eco_friendly_page.adding_to_card('You added Ana Running Short to your shopping cart.')
