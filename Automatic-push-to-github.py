import os

name_project = str(input("Please enter your name of name project:"))

os.system("git add -A")

get_commit = str(input("Please enter a commit for project:"))
os.system(f'git commit -m "{get_commit}"')

get_branch = os.system("git branch")

os.system(f"git push origin {get_branch} {name_project}")