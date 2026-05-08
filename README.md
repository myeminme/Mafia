"# Mafia" 

- make_game function: This function will assign roles to a list of players. It does so dynamically deping on the amount playing.

- night_time function: Akshay Varma - This function will be in charge of the night time cycle. This includes actions from the Doctor (protect someone from elimination), the Mafia (eliminate someone), and the Detective(s) (learn someone’s role)

- reveal_roles_privately function: Akshay Varma - This function will reveal roles for each player privately, so others do not know their roles.

- get_choice function: Akshay Varma - This function displays a list of players and returns the selected player object.

- check_win function: This function checks if the game has reached a win condition. The game ends when either all mafia members have been eliminated 		(villagers win) or when the number of mafia players is equal to or greater than the number of non-mafia players (mafia wins)

- vote function: This function is how the players in the game will vote. Each player will vote for another player and votes will be counted 
before sorted and returning the winner (or technically loser).

- tie fucntion: This function checks if there is a tie in the voting process

- day_time function: This function will be in charge of the day cycle. This includes  	giving the information gathered overnight (i.e. deaths and saves)
and giving the players time/a way to vote to eliminate
