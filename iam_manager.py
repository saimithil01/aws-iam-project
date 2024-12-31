import boto3

# Initialize the IAM client
iam_client = boto3.client('iam')

def create_user(user_name):
    """Create an IAM user."""
    try:
        response = iam_client.create_user(UserName=user_name)
        print(f"User '{user_name}' created successfully.")
        return response
    except Exception as e:
        print(f"Error creating user '{user_name}': {e}")


def list_users():
    """List all IAM users."""
    try:
        response = iam_client.list_users()
        users = response.get('Users', [])
        print("IAM Users:")
        for user in users:
            print(f"- {user['UserName']} (Created: {user['CreateDate']})")
        return users
    except Exception as e:
        print(f"Error listing users: {e}")


def delete_user(user_name):
    """Delete an IAM user."""
    try:
        iam_client.delete_user(UserName=user_name)
        print(f"User '{user_name}' deleted successfully.")
    except Exception as e:
        print(f"Error deleting user '{user_name}': {e}")

if __name__ == "__main__":
    print("AWS IAM User Management Script")
    print("1. Create User")
    print("2. List Users")
    print("3. Delete User")
    print("4. Exit")

    while True:
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                user_name = input("Enter the user name to create: ")
                create_user(user_name)
            elif choice == 2:
                list_users()
            elif choice == 3:
                user_name = input("Enter the user name to delete: ")
                delete_user(user_name)
            elif choice == 4:
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Please enter a valid number.")
