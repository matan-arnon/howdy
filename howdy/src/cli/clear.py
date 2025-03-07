# Clear all models by deleting the whole file

# Import required modules
import os
import sys
import builtins

from i18n import _

# Get the full path to this file
path = os.path.dirname(os.path.abspath(__file__))
# Get the passed user
user = builtins.howdy_user

# Check if the models folder is there
if not os.path.exists(path + "/../models"):
	print(_("No models created yet, can't clear them if they don't exist"))
	sys.exit(1)

# Check if the user has a models file to delete
if not os.path.isfile(path + "/../models/" + user + ".dat"):
	print(_("{} has no models or they have been cleared already").format(user))
	sys.exit(1)

# Only ask the user if there's no -y flag
if not builtins.howdy_args.y:
	# Double check with the user
	print(_("This will clear all models for ") + user)
	ans = input(_("Do you want to continue [y/N]: "))

	# Abort if they don't answer y or Y
	if (ans.lower() != "y"):
		print(_('\nInerpeting as a "NO", aborting'))
		sys.exit(1)

# Delete otherwise
os.remove(path + "/../models/" + user + ".dat")
print(_("\nModels cleared"))
