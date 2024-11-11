import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
@pytest.mark.usefixtures("driver")
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_register_valid(driver):
    driver.get("https://demo.opencart.com/index.php?route=account/register&language=en-gb")
    time.sleep(3)
    driver.find_element(By.ID, "input-firstname").send_keys("Le Tan")
    driver.find_element(By.ID, "input-lastname").send_keys("Phat")
    driver.find_element(By.ID, "input-email").send_keys("tanphatrey130@gmail.com")
    driver.find_element(By.ID, "input-password").send_keys("123456789")
    time.sleep(3)

    # Agree to the Privacy Policy
    privacy_policy_checkbox = driver.find_element(By.NAME, "agree")
    driver.execute_script("arguments[0].click();", privacy_policy_checkbox)
    time.sleep(3)

    # Submit the form
    continue_button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
    continue_button.click()
    time.sleep(3)

    try:
        success_message = driver.find_element(By.XPATH, "//div[contains(text(), 'Your Account Has Been Created!')]")
        assert success_message.is_displayed()
    except Exception as e:
        print("Registration failed: Success message not found.")
        print(e)


def test_register_blank_valid(driver):
    driver.get("https://demo.opencart.com/index.php?route=account/register&language=en-gb")
    time.sleep(3)
    continue_button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
    continue_button.click()
    time.sleep(3)
    # Check for required field error messages
    try:
        # Verify error message for first name
        first_name_error = driver.find_element(By.XPATH,
                                               "//input[@id='input-firstname']/following-sibling::div[@class='text-danger']")
        assert first_name_error.is_displayed(), "First name error message not displayed."
        assert "First Name must be between 1 and 32 characters!" in first_name_error.text, "First name error message text is incorrect."

        # Verify error message for last name
        last_name_error = driver.find_element(By.XPATH,
                                              "//input[@id='input-lastname']/following-sibling::div[@class='text-danger']")
        assert last_name_error.is_displayed(), "Last name error message not displayed."
        assert "Last Name must be between 1 and 32 characters!" in last_name_error.text, "Last name error message text is incorrect."

        # Verify error message for email
        email_error = driver.find_element(By.XPATH,
                                          "//input[@id='input-email']/following-sibling::div[@class='text-danger']")
        assert email_error.is_displayed(), "Email error message not displayed."
        assert "E-Mail Address does not appear to be valid!" in email_error.text or "E-Mail Address must be between 1 and 96 characters!" in email_error.text, "Email error message text is incorrect."

        # Verify error message for password
        password_error = driver.find_element(By.XPATH,
                                             "//input[@id='input-password']/following-sibling::div[@class='text-danger']")
        assert password_error.is_displayed(), "Password error message not displayed."
        assert "Password must be between 4 and 20 characters!" in password_error.text, "Password error message text is incorrect."


    except Exception as e:
        print("Error or assertion failed:", e)
        # print("Current page source:", driver.page_source)

def test_register_invalid_email(driver):
    driver.get("https://demo.opencart.com/index.php?route=account/register&language=en-gb")
    time.sleep(3)
    driver.find_element(By.ID, "input-firstname").send_keys("Le Tan")
    driver.find_element(By.ID, "input-lastname").send_keys("Phat")
    driver.find_element(By.ID, "input-email").send_keys("tanphatreygmail.com")
    driver.find_element(By.ID, "input-password").send_keys("123456789")
    time.sleep(3)
    # Agree to the Privacy Policy
    privacy_policy_checkbox = driver.find_element(By.NAME, "agree")
    driver.execute_script("arguments[0].click();", privacy_policy_checkbox)
    time.sleep(10)
    # Gửi biểu mẫu
    continue_button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
    continue_button.click()
    time.sleep(3)
    # Check for email error message
    try:
        email_error = driver.find_element(By.XPATH,
                                          "//input[@id='input-email']/following-sibling::div[@class='text-danger']")
        assert email_error.is_displayed(), "Email error message not displayed."
        assert "E-Mail Address does not appear to be valid!" in email_error.text, "Email error message text is incorrect."
    except Exception as e:
        print("Error or assertion failed:", e)
        print("Current page source:", driver.page_source)


def test_login_valid(driver):
    driver.get("https://demo.opencart.com/index.php?route=account/login&language=en-gb")
    time.sleep(3)
    driver.find_element(By.NAME, "email").send_keys("tanphatrey510@gmail.com")
    driver.find_element(By.NAME, "password").send_keys("147258369P")
    time.sleep(3)
    # Gửi biểu mẫu đăng nhập
    submit_button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
    submit_button.click()
    time.sleep(3)
    try:
        # Wait until the success element is present
        success_message = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//h2, 'My Account')]"))
        )

        # Assert that the success message is displayed
        assert success_message.is_displayed(), "Success message is not displayed."
        print("Login successful.")

    except Exception as e:
        print("Login failed: Success message not found.")
        print(e)

def test_login_invalid_password(driver):
    driver.get("https://demo.opencart.com/index.php?route=account/login&language=en-gb")
    time.sleep(3)
    driver.find_element(By.NAME, "email").send_keys("tanphatrey510@gmail.com")
    driver.find_element(By.NAME, "password").send_keys("123")
    time.sleep(3)
    # Gửi biểu mẫu đăng nhập
    submit_button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
    submit_button.click()
    time.sleep(3)
    error_message = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "alert-danger"))
    )

    # Assert that the error message is displayed and has the expected text
    assert error_message.is_displayed(), "Error message is not displayed."
    assert "Warning: No match for E-Mail Address and/or Password." in error_message.text.strip(), \
        "Unexpected error message content."


def test_login_invalid_email(driver):
    driver.get("https://demo.opencart.com/index.php?route=account/login&language=en-gb")
    time.sleep(3)
    driver.find_element(By.NAME, "email").send_keys("tanphat510@gmail.com")
    driver.find_element(By.NAME, "password").send_keys("147258369P")
    time.sleep(3)
    # Gửi biểu mẫu đăng nhập
    submit_button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
    submit_button.click()
    time.sleep(3)
    error_message = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "alert-danger"))
    )

    # Assert that the error message is displayed and has the expected text
    assert error_message.is_displayed(), "Error message is not displayed."
    assert "Warning: No match for E-Mail Address and/or Password." in error_message.text.strip(), \
        "Unexpected error message content."


def test_login_special_character(driver):
    driver.get("https://demo.opencart.com/index.php?route=account/login&language=en-gb")
    time.sleep(3)
    driver.find_element(By.NAME, "email").send_keys("tanphat510@gmail.com")
    driver.find_element(By.NAME, "password").send_keys("*&^%$#@!")
    time.sleep(3)
    # Gửi biểu mẫu đăng nhập
    submit_button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
    submit_button.click()
    time.sleep(3)
    error_message = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "alert-danger"))
    )

    # Assert that the error message is displayed and has the expected text
    assert error_message.is_displayed(), "Error message is not displayed."
    assert "Warning: No match for E-Mail Address and/or Password." in error_message.text.strip(), \
        "Unexpected error message content."

def test_logout(driver):
    driver.get("https://demo.opencart.com/index.php?route=account/login&language=en-gb")
    time.sleep(3)
    driver.find_element(By.NAME, "email").send_keys("tanphatrey510@gmail.com")
    driver.find_element(By.NAME, "password").send_keys("147258369P")
    time.sleep(3)
    # Gửi biểu mẫu đăng nhập
    submit_button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
    submit_button.click()
    time.sleep(5)
    driver.find_element(By.XPATH, "//*[@id='top']/div/div[2]/ul/li[2]/div/a").click()
    time.sleep(5)
    # Quá trình đăng xuất
    driver.find_element(By.CSS_SELECTOR, "a.dropdown-item[href*='route=account/logout']").click()


def test_form_submission(driver):
    driver.get("https://demo.opencart.com/en-gb?route=account/login")
    time.sleep(5)
    driver.find_element(By.NAME, "email").send_keys("tanphatrey510@gmail.com")
    driver.find_element(By.NAME, "password").send_keys("147")
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary").click()
    time.sleep(3)
    # Kiểm tra thông báo sau khi gửi biểu mẫu
    error_message = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "alert-danger"))
    )

    # Assert that the error message is displayed and has the expected text
    assert error_message.is_displayed(), "Error message is not displayed."
    assert "Warning: No match for E-Mail Address and/or Password." in error_message.text.strip(), \
        "Unexpected error message content."


def test_navigation(driver):
    driver.get("https://demo.opencart.com/en-gb?route=common/home")
    time.sleep(7)
    driver.find_element(By.LINK_TEXT, "Desktops").click()
    time.sleep(7)
    assert "Desktops" in driver.title
    time.sleep(7)
    driver.get("https://demo.opencart.com/en-gb?route=common/home")
    time.sleep(7)
    driver.find_element(By.LINK_TEXT, "MacBook").click()
    time.sleep(7)
    assert "MacBook" in driver.title
    time.sleep(7)

def test_data_validation(driver):
    # Tìm sản phẩm MacBook
    driver.get("https://demo.opencart.com/home")
    time.sleep(5)
    macbook_element = driver.find_element(By.XPATH, "//a[text()='MacBook']")
    time.sleep(3)
    # Kiểm tra tên sản phẩm
    assert macbook_element.text == "MacBook", "Tên sản phẩm không khớp!"
    time.sleep(3)
    # Kiểm tra giá của sản phẩm MacBook
    macbook_price_element = driver.find_element(By.XPATH, "//*[@id='content']/div[2]/div[1]/div/div[2]/div/div/span[1]")
    macbook_price = macbook_price_element.text.split("\n")[0]  # Lấy giá đầu tiên (không bao gồm thuế)
    assert macbook_price == "$602.00", "Giá của MacBook không khớp!"
    time.sleep(3)
    # Kiểm tra mô tả của sản phẩm MacBook
    macbook_description_element = driver.find_element(By.XPATH, "//*[@id='content']/div[2]/div[1]/div/div[2]/div/p")
    macbook_description = macbook_description_element.text

    expected_description = "Intel Core 2 Duo processor"
    time.sleep(3)

    assert expected_description in macbook_description, "Mô tả chứa thông tin mong đợi!"

    print("Tất cả dữ liệu sản phẩm MacBook đã được xác thực thành công!")

def search_products(driver, search_query):
        # Open the homepage
        driver.get("https://demo.opencart.com/en-gb?route=common/home")
        try:
            # Locate the search input box
            search_box = WebDriverWait(driver, 30).until(
                EC.visibility_of_element_located((By.NAME, "search"))
            )

            # Perform a search
            search_box.clear()
            search_box.send_keys(search_query + Keys.RETURN)  # Submit the search

            # Wait for the search results to load
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "content"))
            )

            # Locate product elements
            products = driver.find_elements(By.XPATH, "//div[@id='content']//div[@class='product-thumb']")

            # List to store product details
            product_details = []

            # Check if products were found
            if not products:
                print("No products found for the search query.")
                return product_details  # Return an empty list if no products found

            for product in products:
                # Extract product details
                product_name = product.find_element(By.XPATH, ".//h4/a").text
                product_price = product.find_element(By.XPATH, ".//span[@class='price-new']").text
                product_link = product.find_element(By.XPATH, ".//h4/a").get_attribute('href')

                # Store product details in a dictionary
                product_details.append({
                    "name": product_name,
                    "price": product_price,
                    "link": product_link
                })

                # Print product details (optional)
                print(f"Product Name: {product_name}")
                print(f"Price: {product_price}")
                print(f"Link: {product_link}")
                print("=" * 40)  # Separator for better readability

            return product_details  # Return the list of product details

        except Exception as e:
            print(f"An error occurred: {e}")
            return []  # Return an empty list if an error occurs


def test_search_products(driver):
    existent_keyword = "MacBook"  # Example keyword
    results = search_products(driver, existent_keyword)
    assert len(results) > 0, "No products found for 'MacBook'"
    time.sleep(3)

def test_search_with_nonexistent_keyword(driver):
    nonexistent_keyword = "NonExistentProduct123"  # Example nonexistent keyword
    results = search_products(driver, nonexistent_keyword)
    time.sleep(3)


def test_search_with_uppercase_keyword(driver):
        uppercase_keyword = "MACBOOK"  # Example uppercase keyword
        results = search_products(driver, uppercase_keyword)
        time.sleep(3)


def test_search_with_lowercase_keyword(driver):
    lowercase_keyword = "macbook"  # Example lowercase keyword
    results = search_products(driver, lowercase_keyword)
    time.sleep(3)

def test_search_with_keyword_containing_special_characters(driver):
        special_characters_keyword = "!@#$%^&*()"  # Example keyword with special characters
        results = search_products(driver, special_characters_keyword)
        time.sleep(3)

def test_search_blank_characters(driver):
    empty_search_query = ""  # Example of an empty search query
    results = search_products(driver, empty_search_query)
    # Verify that no products are found for an empty search
    assert len(results) == 0, f"Expected no products for an empty search, but found {len(results)} products."
    time.sleep(3)
def test_add_to_cart(driver):
    driver.get("https://demo.opencart.com/")
    time.sleep(10)
    driver.find_element(By.XPATH, "//*[@id='content']/div[2]/div[1]/div/div[2]/form/div/button[1]").click()
    time.sleep(10)
    driver.find_element(By.LINK_TEXT, "Shopping Cart").click()
    time.sleep(5)


@pytest.mark.usefixtures("driver")  # Sử dụng fixture driver đã định nghĩa
def login_add_to_cart(driver):
    # Mở trang đăng nhập
    driver.get("https://demo.opencart.com/index.php?route=account/login")

    # Khởi tạo WebDriverWait với thời gian chờ tối đa
    wait = WebDriverWait(driver, 10)  # Thay đổi 10 thành thời gian chờ tối đa bạn mong muốn

    # Chờ cho trường email có thể nhìn thấy và nhập email
    email_field = wait.until(EC.visibility_of_element_located((By.ID, "input-email")))
    email_field.send_keys("tanphatrey510@gmail.com")

    # Chờ cho trường mật khẩu có thể nhìn thấy và nhập mật khẩu
    password_field = wait.until(EC.visibility_of_element_located((By.ID, "input-password")))
    password_field.send_keys("147258369P")

    time.sleep(10)  # Chờ trang tải xong

    # Chờ cho nút đăng nhập có thể nhấp được và nhấn
    login_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-primary")))
    login_button.click()

    # Chờ cho việc đăng nhập hoàn tất (kiểm tra tiêu đề trang hoặc một phần tử nào đó)
    wait.until(EC.title_contains("My Account"))  # Kiểm tra tiêu đề trang nếu đăng nhập thành công
    driver.get(
        "https://demo.opencart.com/index.php?route=product/product&product_id=44")  # Cập nhật với ID sản phẩm hợp lệ
    wait = WebDriverWait(driver, 10)

    time.sleep(10)  # Chờ trang tải xong
    # Thêm sản phẩm vào giỏ hàng
    add_to_cart_button = wait.until(EC.element_to_be_clickable((By.ID, "button-cart")))
    add_to_cart_button.click()
    time.sleep(10)  # Chờ trang tải xong

    # Đi đến giỏ hàng
    driver.get("https://demo.opencart.com/index.php?route=checkout/cart")

    time.sleep(10)  # Chờ giỏ hàng cập nhật

    # Chọn nút thanh toán
    checkout_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Checkout")))
    checkout_button.click()

    time.sleep(10)  # Chờ trang thanh toán tải xong

def test_checkout_valid_info(driver):
    login_add_to_cart(driver)
    select_element = driver.find_element(By.NAME, "address_id")
    # Tạo đối tượng Select
    select = Select(select_element)

    # Chọn theo giá trị (value)
    select.select_by_value("1034")
    time.sleep(5)


    button_choose_payment = driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div/div[2]/div[1]/fieldset/div[1]/button")
    button_choose_payment.click()
    time.sleep(5)
    button_option = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/form/div[1]/label")
    button_option.click()
    time.sleep(5)
    button_submit = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/form/div[2]/button")
    button_submit.click()
    time.sleep(5)

    button_choose_shipment = driver.find_element(By.XPATH,
                                                "/html/body/main/div[2]/div/div/div/div[2]/div[2]/fieldset/div[1]/button")
    button_choose_shipment.click()
    time.sleep(5)
    button_option = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/form/div[1]/label")
    button_option.click()
    time.sleep(5)
    button_submit = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/form/div[2]/button")
    button_submit.click()
    time.sleep(5)

    button_confirm = driver.find_element(By.XPATH,
                                                "/html/body/main/div[2]/div/div/div/div[2]/div[3]/div[2]/div/button")
    button_confirm.click()

    # Kiểm tra thông báo thành công
    try:
        success_message = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/main/div[2]/div/div/h1, 'Your order has been placed!')]"))
        )
        assert success_message.is_displayed(), "Success message not displayed."
        print("Đơn hàng đã được đặt thành công.")
    except Exception as e:
        print("Đặt hàng không thành công.")
        print(e)


@pytest.mark.parametrize("size", [(800, 600), (1024, 768), (1920, 1080)])
def test_responsive_design(driver, size):
    driver.set_window_size(*size)
    driver.get("https://demo.opencart.com/")
    time.sleep(5)
    # Kiểm tra bố cục hoặc các phần tử cụ thể cho tính năng phản hồi
    element = driver.find_element(By.ID, "logo")
    assert element.is_displayed()
