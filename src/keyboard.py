from src.item import Item

class KeyboardLangMixin:
    _langs = {'EN': 'EN', 'RU': 'RU'}

    def __init__(self):
        self._current_lang = 'EN'

    def change_lang(self):
        if self._current_lang == 'EN':
            self._current_lang = 'RU'
        else:
            self._current_lang = 'EN'
        return self

    @property
    def language(self):
        return self._langs[self._current_lang]

    @language.setter
    def language(self, value):
        for lang_code, lang_name in self._langs.items():
            if value == lang_code:
                self._current_lang = value
                return
        raise ValueError(f"AttributeError: property 'language' of 'Keyboard' object has no setter")


class Keyboard(Item, KeyboardLangMixin):
    def __init__(self,name: str, price: float, quantity: int, language: str = 'EN'):
        super().__init__(name, price, quantity)
        self.language = language