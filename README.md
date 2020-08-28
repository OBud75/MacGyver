# MacGyver

## MacGyver is trapped in a maze
Help him to escape using directional keys

Items on your way could help you to defeat the guardian

### Openclassrooms project 3
There is only 1 level.

The structure (start, walls, arrive) must be registered in a file so that it can be changed easily if needed.

MacGyver will be controlled with a directional keyboard.

Objects will be displayed randomly in the maze and will change location if the user reloads the game.

The game window will be a square that displays 15 blocks vertically and horizontally.

MacGyver will have to move block to block.

He will collect the items when the player correctly chooses the path to each of them.

The program will stop only if MacGyver collects all the items and has found the arriving point.

If he doesn't collect all the items and he arrives at the guard, he dies (life is hard for heroes).

The game will be standalone, meaning it can be executed on any computer.

#### Download files
'https://github.com/OBud75/MacGyver', code, download zip and extract all

Or from terminal: 'git clone https://github.com/OBud75/MacGyver.git'

##### How to start game
Install python3 (https://www.python.org/downloads)

Open terminal in MacGyver directory

'python3 -m venv env'

'source env/Scripts/activate' (Window)

'source env/bin/activate' (Unix)

'pip install -r requirements.txt'

'python launcher.py'