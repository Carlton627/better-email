from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

Window.clearcolor = (1, 1, 1, 1)
Window.maximize()

class HomeScreen(BoxLayout):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)


class HomeApp(App):
	def build(self):
		return HomeScreen()


if __name__ == '__main__':
	HomeApp().run()	