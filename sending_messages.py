texts = ['Hello there', 'today is Thursday', 'L is for love']
sent_messages = []

def show_messages(messages):
	for message in messages:
		print(message.title())

def send_messages(messages):
	for message in messages:
		print(message.title())
		sent_message = messages.pop(message)
		sent_messages.append(message)
	print(sent_messages)

send_messages(texts)
print(texts)