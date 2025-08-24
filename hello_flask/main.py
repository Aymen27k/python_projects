# This is a practice session for Decorator functions

IS_ADMIN = True

def requires_admin(function):
    def wrapper(*args, **kwargs):
        if IS_ADMIN:
            return function(*args, **kwargs)
        else:
            print(f"Access Denied: You must be an administrator to perform this action.")
            return None
    return wrapper

@requires_admin
def view_dashboard():
    print("Viewing the administrative dashboard.")

@requires_admin
def delete_database():
    print("Deleting all data from the database!")

@requires_admin
def view_user_profile(user_id):
    print(f"Viewing profile for user ID: {user_id}")

@requires_admin
def update_settings(user_id, setting, value):
    print(f"Updating setting '{setting}' for user {user_id} to '{value}'.")

@requires_admin
def add_two_numbers(a, b):
    print(f"Inside the function, adding {a} and {b}")
    return a + b

# The test case that will cause an error.
print("Calling the decorated function...")
result = add_two_numbers(5, 3)

# This is where the code will break.
# It tries to add 10 to what the decorator returned.
print("Trying to use the returned value...")
print(f"Result + 10 = {result + 10}")
