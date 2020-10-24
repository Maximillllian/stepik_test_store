def test_store_button():
  button = browser.find_elements_by_css_selector('button[type='submit'].btn-add-to-basket')
  assert button
