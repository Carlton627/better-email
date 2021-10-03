import email

class EmailStructure:
	"""docstring for EmailStruct"""
	#divide email into from, content and other meta data
	def __init__(self, email):
		self.email = email

	def extractEmailSender(self, email):
		pass

	def extractEmailContent(self, email):
		pass

	def extractEmailAttachments(self, email):
		pass

	def extractOtherMetaData(self, email):
		pass
