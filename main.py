
from user import User

my_user = User( "svenska", "Matz", "123" )

print( my_user )
print( my_user.preferred_language )

my_user.preferred_language = "norska"
print( my_user )

print( my_user.get_password() )

my_user.is_correct_login( "Kajsa", "060606" )

print( my_user.password )