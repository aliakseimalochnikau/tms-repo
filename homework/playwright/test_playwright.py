"""
pip install pytest-playwright
playwright install
"""

from playwright.sync_api import expect


class TestClass:
    def test_first(self, page):
        RED_COLOR = 'rgb(239, 49, 36)'

        page.goto("https://myfin.by/")
        cards_button = page.get_by_role("link", name="Карты", exact=True)
        cards_button.nth(0).hover()

        with page.context.expect_page() as second_tab:
            page.get_by_text("Красная карта").first.click()

        second_page = second_tab.value
        phone_input = second_page.get_by_label("Номер мобильного телефона")
        phone_input.fill("2912345678")

        confirm_button = second_page.get_by_role("button", name="Подтвердить")
        confirm_button.click()

        title = second_page.get_by_text("Пройдите идентификацию")
        expect(title).to_have_text("Пройдите идентификацию")

        red_button = second_page.get_by_role("button", name="Перейти в МСИ")
        color = red_button.evaluate(
            "(e) => {return"
            " window.getComputedStyle(e).getPropertyValue('background-color');"
            "}"
        )
        height = red_button.evaluate(
            "(e) => {return"
            " window.getComputedStyle(e).getPropertyValue('height');"
            "}"
        )

        assert color == RED_COLOR, "Color was not red"
