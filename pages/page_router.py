"""Screen Manager for Full Pages"""

# kivy
from kivy.uix.screenmanager import ScreenManager, ShaderTransition

# imports
from pages.splash_page import SplashScreen
from pages.settings import SettingsPage


# =================================================================

page_router = ScreenManager()
page_router.add_widget(SplashScreen(name="SplashScreen"))
page_router.add_widget(SettingsPage(name="SettingsPage"))

def change_screen(instance, value: str = "SplashScreen") -> None:
    page_router.current = value
