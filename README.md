# TV CONTROL

[![WTFPL](http://www.wtfpl.net/wp-content/uploads/2012/12/wtfpl-badge-1.png)](http://www.wtfpl.net)

This is a basic application for run a web api who can control a SHARP Tv controlled by RS232.

## Requirements

- Python 3

- PIP 3

- Requirements file

## Usage

### Run server

``` Bash
python3 main.py
```

### Command call

Open the url related to the command you want to run.

Will return the command execution status. (OK / ERR / TIMEOUT / BAD REQUEST)

### Command list

> Commands imported from [here](http://siica.sharpusa.com/portals/0/downloads/Manuals/mon_man_PNE471R.pdf).

| Name      | URL     | Description               |
|-----------|---------|---------------------------|
| Power On  | /on     | Will power on the Tv      |
| Power Off | /off    | Will power off the Tv     |
| Mute      | /mute   | Will disable the Tv audio |
| Unmute    | /unmute | Will enable the Tv audio  |
