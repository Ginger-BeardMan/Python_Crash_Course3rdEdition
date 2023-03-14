guest_list = ['Dave Weckl', 'Chuck Shuldiner', 'Neil Peart']

print(f"You are formally invited to dinner {guest_list[0]}, you are such a big influence, it'd be an honor to have you here.")

print(f"{guest_list[1]} you went too soon. Your music is still as influencial today as it was when you first wrote it and I would be grateful if you joined me for dinner.")

print(f"I wish I took an opportunity to see you live {guest_list[-1]}, you have also greatly influenced me as a drummer. The dinner would not be complete without you there.")

cancelled_guest = guest_list.pop()

print(cancelled_guest + " had to cancel tonight and I found a bigger table so I invited a few more people.")

guest_list.append('Bill Hader')
guest_list.insert(0, 'Johnny Bravo')
guest_list.insert(2, 'Franco Franco')

print("The new guest list is " + guest_list[0] + ", " + guest_list[1] + ", " + guest_list[2] + ", " + guest_list[3] + ", and " + guest_list[4])

print("Curses! My table won't arrive in time and I have to uninvite 3 people.")

first_cancel = guest_list.pop()

print("Sorry " + first_cancel + ", but I won't be able to host you tonight.")

second_cancel = guest_list.pop()

print("This one really hurts. " + second_cancel + ", I'll make it up to you, I promise.")

third_cancel = guest_list.pop()

print("My apologies " + third_cancel + ", I wish I didn't have to retract my invitation, there just isn't room anymore.")

print("Only " + guest_list[0] + " and " + guest_list[1] + " are invited now.")