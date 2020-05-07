
How can I assign a keyboard shortcut for the script that I have created?

Didn't end up using this...
```
dnf search xbindkeys
sudo dnf install xbindkeys
```

Go to System Settings -> keyboard -> shortcuts.
Click on + to add a custom shortcut.Name it anything.
In the command box type gnome-terminal -e "path_of_script". Make sure your script has executable permissions

```
"Ctrl + Shift + s"
```

Script is here:

```
./home/davidkypuros/favoritecommands/up.sh
```

Home path is here:
```
echo $HOME
/home/davidkypuros

```

update home path
```
vim  /home/davidkypuros/.bashrc
~/favoritecommands
source ~/.bashrc
```

alias
```
alias gitpush='( cd "/home/davidkypuros/favoritecommands" && ./up.sh )'

( cd "/home/davidkypuros/favoritecommands" && ./up.sh )'
```
