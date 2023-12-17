import re
from playwright.sync_api import expect


class TestHomeWork:
    def test_homework(self, page):
        page.goto("https://blizko.by/")
        page.get_by_role("link", name="Каталог").click()
        page.locator("xpath=//a[text()='Дом']").click()
        page.locator("xpath=//a[text()='Товары для дома']").click()
        page.locator("xpath=//a[text()='Телефоны']").first.click()

        title = page.locator("xpath=//*[@id='modalSet']//*[contains(text(), 'Салон штор «Виджи дизайн» ')]")
        address = page.locator("//*[@id='modalSet']//*[contains(text(), 'ул. Шафарнянская, 18-19')]")
        tel_1 = page.get_by_role("link", name="8 (017) 270-60-12")
        tel_2 = page.get_by_role("link", name="8 (029) 619-43-16")
        tel_3 = page.get_by_role("link", name="8 (029) 123-88-33")
        footer_msg = page.locator("xpath=(//*[@class='pmi__footer'])[5]")

        # Basic assertions
        expect(title).to_be_visible()
        expect(address).to_be_visible()
        expect(tel_1).to_be_visible()
        expect(tel_2).to_be_visible()
        expect(tel_3).to_be_visible()
        expect(footer_msg).to_be_visible()

        # Assert title is bold
        is_bold = int(title.evaluate(
            "(e) => {return"
            " window.getComputedStyle(e).getPropertyValue('font-weight');"
            "}")
        )
        assert is_bold >= 700

        # Assert phone number matches the pattern
        phone_regex = re.compile(r'8 \(\d{3}\) \d{3}-\d{2}-\d{2}')
        assert phone_regex.match(tel_1.text_content())
        assert phone_regex.match(tel_2.text_content())
        assert phone_regex.match(tel_3.text_content())

        # Assert phone number is a link
        assert tel_1.get_attribute('href')
        assert tel_2.get_attribute('href')
        assert tel_3.get_attribute('href')
