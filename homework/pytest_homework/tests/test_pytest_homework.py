import pytest


class TestHomework:
    @pytest.mark.wizard
    @pytest.mark.parametrize("first_name", ["John", "Harry", "Ron"])
    @pytest.mark.parametrize("last_name", ["Smith", "Potter", "Weasley"])
    def test_fail_if_john_smith(self, age, first_name, last_name):
        if first_name == "John" and last_name == "Smith":
            print("John Smith? Seriously?")
            pytest.xfail("Who the hell is John Smith!?")
        else:
            print(f"Hello {first_name} {last_name}! Your age is {age}")







