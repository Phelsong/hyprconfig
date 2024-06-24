import os
import sys
import shutil
from pathlib import Path

from kivy.uix.button import Button
from kivy.uix.label import Label

# from kivy.uix.
from kivy.uix.boxlayout import BoxLayout
from typing import Self
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

# local imports

# =============================================================================


class SettingsPage(Screen):
    """Page"""

    layout = BoxLayout(orientation='vertical')

    home:str = os.getenv("HOME")
    config_dir = Path(f"{home}/.config").absolute()
    hypr_path:str = Path(f"{config_dir}/hypr").absolute()


    def __init__(self, **kwargs):
        super(SettingsPage, self).__init__(**kwargs)

        self.add_widget(widget=self.layout)

        with open(f"{self.hypr_path}/hyprland.conf") as f:
            for line in f.readlines():
                title = Label(text=line, font_size="18sp", size_hint=(1,1))
                self.layout.add_widget(widget=title)
