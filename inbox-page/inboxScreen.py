from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

Window.clearcolor = (1, 1, 1, 1)
Window.maximize()


class InboxScreen(BoxLayout):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)


class InboxApp(App):
	def build(self):
		return InboxScreen()


if __name__ == '__main__':
	InboxApp().run()