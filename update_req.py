import sys
import git

repo_name = sys.argv[1] # Ex. robotpy/robotpy-wpilib
repo_path = "https://github.com/" + repo_name + ".git"
package_name = sys.argv[2] # Ex. wpilib

tag = git.Repo.clone_from(repo_path, "./temp", branch="master").git.describe('--tags', '--abbrev=0')

lower_bound = tag

version = tag.split('.')

for i in range(len(version)):
    if i == 0:
        version[i] = str(int(version[i]) + 1)
    else:
        version[i] = "0"

upper_bound = '.'.join(version)

file_data = None
with open("requirements.txt", "r") as file:
    file_data = file.readlines()

for i in range(len(file_data)):
    if file_data[i].find(package_name + ">=") == 0:
        file_data[i] = "{}>={}, <{}\n".format(package_name, lower_bound, upper_bound)

with open("requirements.txt", "w") as file:
    file.writelines(file_data)