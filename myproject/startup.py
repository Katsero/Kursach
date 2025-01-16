import os
import subprocess
import platform


def run_django_server():
    try:
        # Construct the command to run the Django server
        command = "python manage.py runserver"

        # Check the operating system and modify command if needed
        if platform.system() == "Windows":
            command = "cmd /c " + command
        
        #Execute the command in terminal
        os.system(command)


    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    run_django_server()
