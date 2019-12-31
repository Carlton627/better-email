from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label

Window.clearcolor = (1, 1, 1, 1)
Window.maximize() 	
# TODO: change initial window position


class LoginScreen(BoxLayout):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

	def validate_user(self):
		popup = Popup(title='Login Alerts', content=Label(text='Get this Bitch'), 
			size_hint=(None, None), size=(500, 500))

		email = self.ids.email_field.text
		password = self.ids.pass_field.text
		info = self.ids.info_text

		if email == "" and password == "":
			popup.open()
		else:
			info.text = "[color=#FF0000]email = {}, pass = {}[/color]".format(email, password)

		
class LoginApp(App):
	"""docstring for BetterEmailApp"""
	def build(self):
		return LoginScreen()

if __name__ == '__main__':
	LoginApp().run()
