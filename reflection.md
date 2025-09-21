# Reflection

Setting up the Django environment was both challenging and rewarding. One of the first issues I encountered was making sure my Python version was compatible with Django. At first, I had an older version of Python installed, which caused errors when trying to install Django. I solved this by upgrading Python to the latest version and then reinstalling Django within my virtual environment.

Another challenge was activating the virtual environment correctly in VS Code. At first, I forgot to select the interpreter linked to my `venv`, which caused Django commands like `runserver` not to work. Once I switched the interpreter in VS Code to point to my virtual environment, everything started working as expected.

I also struggled with running the server for the first time. I encountered migration errors, but running `python manage.py migrate` solved the problem. Finally, connecting my project to GitHub was a bit confusing at first, especially when setting the remote origin. I solved this by carefully following the steps to initialize git, add the remote URL, and push my code.

Overall, these challenges helped me understand the importance of version control, virtual environments, and step-by-step debugging. Now I feel more confident in setting up Django projects and managing them properly in VS Code and GitHub.
