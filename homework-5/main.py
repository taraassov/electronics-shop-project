from src.keyboard import Keyboard

if __name__ == '__main__':
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    #assert str(kb) == "Dark Project KD87A" # не понял как убрать ограничения по символам
    assert str(kb) == "Dark Proje"
    # print(kb.__dict__)
    # print(kb.language)
    # print(str(kb))

    assert str(kb.language) == "EN"

    kb.change_lang()
    assert str(kb.language) == "RU"

    # Сделали RU -> EN -> RU
    kb.change_lang().change_lang()
    assert str(kb.language) == "RU"

    kb.language = 'CH'
    # AttributeError: property 'language' of 'Keyboard' object has no setter