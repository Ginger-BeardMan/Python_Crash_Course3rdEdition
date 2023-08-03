from privileges_module import Users, Admin, Privileges

senior_admin = Admin('Lord', 'Ruler', 'Interwebs', 'iamyourruler@mysite.com', 'January 1, 0000')
print(senior_admin.describe_user())
print(senior_admin.privileges.show_privileges())