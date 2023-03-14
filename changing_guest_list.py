guest_list = ['Dave Weckl', 'Chuck Shuldiner', 'Neil Peart']

print(f"You are formally invited to dinner {guest_list[0]}, you are such a big influence, it'd be an honor to have you here.")

print(f"{guest_list[1]} you went too soon. Your music is still as influencial today as it was when you first wrote it and I would be grateful if you joined me for dinner.")

print(f"I wish I took an opportunity to see you live {guest_list[-1]}, you have also greatly influenced me as a drummer. The dinner would not be complete without you there.")

cancelled_guest = guest_list.pop()

print(cancelled_guest + " had to cancel tonight.")

guest_list.append('Bill Hader')

print("The new guest list is " + guest_list[0] + ", " + guest_list[1] + ", and " + guest_list[2])