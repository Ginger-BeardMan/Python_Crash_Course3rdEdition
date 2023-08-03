from users_module import Users
from admin_privileges_module import Admin, Privileges

ultimate_admin = Admin('Lord', 'Ruler', 'Interwebs', 'iamyourruler@mysite.com', 'January 1, 0000')
print(ultimate_admin.describe_user())
print(ultimate_admin.privileges.show_privileges())