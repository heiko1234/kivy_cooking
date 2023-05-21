

# https://github.com/kivymd/KivyMD/blob/master/kivymd/icon_definitions.py
# Kivy MD
# https://www.youtube.com/watch?v=LRXo0juuTrw&list=PLhTjy8cBISEoQQLZ9IBlVlr4WjVoStmy-

# from kivy.config import Config
# Config.set('kivy','keyboard_mode','systemanddock')


from kivymd.app import MDApp

from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivymd.toast.kivytoast.kivytoast import toast

# from sail_class import sail_infos, sail_scenario


# Properties
from kivy.properties import ObjectProperty

# Clock
from kivy.clock import Clock

# background Threading
from threading import Thread

# partial: funktions reverenz + parameter übergabe
from functools import partial

from kivy.storage.jsonstore import JsonStore




# Define our differeent screens
class WelcomeWindow(Screen):

    # def on_enter(self, *args):
    #     # on_enter works automatically, while keyword
    #     Clock.schedule_once(self.switch_to_second_view, 3)

    def entrance_button_behavior(self, *args):
        Clock.schedule_once(self.switch_to_second_view, 1)

    def switch_to_second_view(self, *args):
        self.manager.current = "setupwindow"
        self.manager.transition.direction="left"

        # boat_questions.start(number_questions = 10)


class SetupWindow(Screen):

    # number_of_questions = ObjectProperty()

    def any_function(self, *args):
        pass

    def switch_to_Stammdaten(self, *args):
        self.manager.current = "stammdatenwindow"
        self.manager.transition.direction="left"

    def switch_to_Bootskasse(self, *args):
        self.manager.current = "bootskassewindow"
        self.manager.transition.direction="left"

    def switch_to_Bestand(self, *args):
        self.manager.current = "bestandwindow"
        self.manager.transition.direction="left"

    def switch_to_Produkts(self, *args):
        self.manager.current = "productswindow"
        self.manager.transition.direction="left"


class ProduktWindow(Screen):

    def any_function(self, *args):
        pass


class ProdukteWindow(Screen):

    def switch_to_product(self, *args):
        self.manager.current = "productwindow"
        self.manager.transition.direction="left"


class BestandWindow(Screen):

    def any_function(self, *args):
        pass


class StammdatenWindow(Screen):

    def any_function(self, *args):
        pass


class BootskasseWindow(Screen):

    def any_function(self, *args):
        pass



# https://github.com/kivymd/KivyMD/wiki/Modules-Material-App#exceptions
class SailApp(MDApp):
    def __init__(self, **kwargs):
        self.title = "Sail Cook and Storage"
        super().__init__(**kwargs)

    def build(self):
        # Load file function musst be in build and not before
        kv = Builder.load_file("Sail_cookandstorage.kv")
        self.root = kv


if __name__ == "__main__":
    SailApp().run()









