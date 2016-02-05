# BASH-Portal

In many situations, switching in between folders under the command line operation is a combersom task.
One needs to key-in many letters to go through the right path, and this is why I made the "BASH-Portal" for the Linux / Unix-like system.

> With BASH-Portal, you can easily mark your current place of a folder, and come back again by using the keyword that you marked in an early time.

# Example
Here is a example of using the "BASH-Portal":
```sh
 ~$ cd First_layer/Second_layer    # Go to some folder place
 ~/First_layer/Second_layer$ here  # Mark an empty keyword for this place
 ```
 Now you've marked a folder place with an empty keyword for the future usage.
 You can leave the folder and go to some where, such as:
 ```sh
 ~/First_layer/Second_layer$ cd    # Return to your home folder
 ```
And once if you want go back to the place that you marked, just do the following:
 ```sh
 ~$ there            # Directly go to the place that you just marked
 ~/First_ayer/Second_layer$   # Now, you are in the folder you want!
```
Here is the functions of the BASH-Portal:

 - Mark current folder with empty keyword
```sh
here <Enter>
```
 - Mark current folder with keyword "ddd"
```sh
here ddd <Enter>
```
 - Go to the place where with the empty keyword
```sh
there <Enter>
```
 - Go to the place where with the "ddd" keyword
```sh
there-ddd <Enter>
```
 - Check the portal list that you've made in the past (here -l):
```sh
$ here -l <Enter> # -l is the 'L' letter in lower case

alias there='cd /Users/username'; pwd;
alias there-ddd='cd /Users/username/path-to-ddd'; pwd;

$
```

# Installation
 1. Just download this repository and place the folder in someplace.
 2. Add the following script in your ~/.bashrc (Linux) or ~/.profile (OSX)
```sh
export PORTAL_PATH=~/path-to-the-bash-portal # Place your folder path for the "BASH-Portal" folder
source ${PORTAL_PATH}/here.source
```
