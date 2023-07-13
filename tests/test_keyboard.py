from src.keyboard import Keyboard

def test_keyboard():
    kb1 = Keyboard("BTC", 3000, 5)
    assert str(kb1) == "BTC"
    assert str(kb1.language) == "EN"

    kb1.change_lang()
    assert str(kb1.language) == "RU"

    kb1.change_lang().change_lang()
    assert str(kb1.language) == "RU"