# My Linux Dotfiles

My Linux dotfiles repository! This repository contains configuration files for various applications and tools that I use on my Linux system.

## Synchronizing Configuration Files

The `PushGithub.py` and `PullGithub.py` files are Python scripts designed to automate the process of synchronizing configuration files between your system and this repository. **PushGithub.py** copies configuration files from their respective locations on your system to the repository and pushes the updates to GitHub, Conversely, **PullGithub.py** pulls the latest changes from the GitHub repository and updates the configuration files on your system.

The `config_paths.json` file contains the paths of the configuration files and directories.

## Folders

- **i3wm:** Contains my configuration files for the i3 window manager.

  This folder includes configurations for keybindings, workspace layouts, and other settings related to i3wm.

- **lf:** Contains configuration files for the terminal file manager, lf.

  These files customize the appearance and behavior of lf according to my preferences.

- **shell:** Contains my shell configuration files, including `.zshrc` and `.bashrc`.

  These files contain aliases, environment variables, and other customizations for the Zsh and Bash shells.

- **others:** This folder will contain additional configuration files and dotfiles for other applications and tools that I use.

## Usage

Feel free to explore and use these dotfiles as a reference or starting point for your own configurations. However, be cautious when copying configurations directly, as they may contain settings specific to my system or preferences.

## Contributing

If you have suggestions or improvements for any of the configurations, feel free to open an issue or submit a pull request.
