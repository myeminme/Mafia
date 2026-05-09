Mafia.py - the main file with all of the code to make the game run

players.txt - a sample txt file that holds names of the players playing. Should have only first names of the players with a newline in between names 

Mafia.py takes one command line argument, the name of the txt file with players (i.e. players.txt)
You run the game using python Mafia.py players.txt - or whatever the name of your txt file is.

"Insert how the game works on a gameplay level here"

| Method/function| Primary author | Techniques demonstrated |
| -------------- | -------------- | ----------------------- |
| vote           | Andrew         | use of a key function   |
| play_game      | Andrew         | with statment           |
| parse_args     | Andrew         | ArgumentParser          |
| night_time     | Akshay         | conditional expressions |
| get_choice     | Akshay         | sequence unpacking      |
| reveal_roles_privately | Akshay | None                    |
| action for all classes | Mykha  | super()                 |
| __str__        | Mykha          | magic method            |
| make_game      | Mykha          | None                    |
| check_win      | Aishani        | Generator Expression    |
| get_alive_players| Aishani      | List Comprehension      |
| reveal_all_roles| Aishani       | F-strings               |
| game_loop      | Aishani        | F-strings               |

"# Mafia" 

- make_game function: This function will assign roles to a list of players. It does so dynamically deping on the amount playing.

- night_time function: This function will be in charge of the night time cycle. This includes actions from the Doctor (protect someone from elimination), the Mafia (eliminate someone), and the Detective(s) (learn someone’s role)

- reveal_roles_privately function: This function will reveal roles for each player privately, so others do not know their roles.

- get_choice function: This function displays a list of players and returns the selected player object. 

- check_win function: This function checks if the game has reached a win condition. The game ends when either all mafia members have been eliminated 		(villagers win) or when the number of mafia players is equal to or greater than the number of non-mafia players (mafia wins)

- vote function: This function is how the players in the game will vote. Each player will vote for another player and votes will be counted 
before sorted and returning the winner (or technically loser).

- tie fucntion: This function checks if there is a tie in the voting process

- day_time function: This function will be in charge of the day cycle. This includes  	giving the information gathered overnight (i.e. deaths and saves)
and giving the players time/a way to vote to eliminate

- Reveal_all_roles: This functioneveals the roles of each player at the end.

- Game_loop : This function is how the game knows when to stop the game and when 
to keep going. Itll stop when either the mfia kills everyone or the other characters
quess the mafia

- Get_alive_players: Shows a lit of all of they players who are still alive at any
given point in time
