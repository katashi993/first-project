import time
from selenium.webdriver.common.by import By


def test_add_to_basket_button_is_present(browser):
    """Test that product page contains add to basket button."""
    # Открываем страницу товара
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)

    # Пауза для визуальной проверки языка (можно убрать после тестирования)
    time.sleep(5)  # уменьшил время для тестирования

    # Проверяем наличие кнопки добавления в корзину
    add_to_basket_button = browser.find_elements(
        By.CSS_SELECTOR, "button.btn-add-to-basket"
    )

    # Убеждаемся, что кнопка существует
    assert len(add_to_basket_button) > 0, "Add to basket button is not present on the page"

    # Дополнительная проверка: кнопка должна быть видимой
    assert add_to_basket_button[0].is_displayed(), "Add to basket button is not visible"
