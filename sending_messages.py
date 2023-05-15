texts = ['Hello there', 'today is Thursday', 'L is for love']
sent_messages = []

def send_messages(messages):
	while messages:
		sent_message = messages.pop()
		print(f"The current message is {sent_message.title()}")
		sent_messages.append(sent_message)

send_messages(texts)
print(sent_messages)
print(texts)