
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from deep_translator import GoogleTranslator, PonsTranslator, LingueeTranslator, MyMemoryTranslator

__version__ = "1.0.0"


class MainLayout(BoxLayout):

    auto_inserted = False

    @staticmethod
    def get_supported_languages(translator='Google Translate', auto_included=False, *args):

        if translator == 'Google Translate' or translator == 'My Memory':
            supported_languages = GoogleTranslator.supported_languages
            if auto_included and not MainLayout.auto_inserted:
                supported_languages.insert(0, 'auto')
                MainLayout.auto_inserted = True

        elif translator == 'Pons':
            supported_languages = PonsTranslator.supported_languages

        elif translator == 'Linguee':
            supported_languages = LingueeTranslator.supported_languages

        else:
            return ""
            # raise Exception("You need to choose a translator")

        return supported_languages

    @staticmethod
    def translate(translator, source, target, text, *args):

        if not text:
            return 'provide a text to translate'

        try:
            if translator == 'Google Translate':
                res = GoogleTranslator(source=source, target=target).translate(text=text)
                # if target == 'arabic':
                #     res = get_display(arabic_reshaper.reshape(res))

            elif translator == 'My Memory':
                res = MyMemoryTranslator(source=source, target=target).translate(text=text)
                # if target == 'arabic':
                #     res = get_display(arabic_reshaper.reshape(res))

            elif translator == 'Pons':
                res = PonsTranslator(source=source, target=target).translate(word=text)
                # if target == 'arabic':
                #     res = get_display(arabic_reshaper.reshape(res))

            elif translator == 'Linguee':
                res = LingueeTranslator(source=source, target=target).translate(word=text)

            else:
                return "you need to choose a translator"

            return "No translation is provided" if not res else res

        except Exception as e:
            print(e.args)
            return "No translation is provided"


class TranslatorApp(App):

    def build(self):
        return MainLayout()


if __name__ == '__main__':
    TranslatorApp().run()