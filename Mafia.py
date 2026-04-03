def make_game(self, num_of_players):
    """ This method will randomly assign roles to each player depending on how 
    many people are playing. There are four roles: villager, mafia, doctor, and 
    detective. 
    5-7 players: 2 mafia, 1 detective, 1 doctor, 0-3 civilians
    8-11: 3 mafia, 2 detective, 1 doctor, 2-5 civilians
    12-15: 4 mafia, 3 detectives, 1 doctor, 4-7 civilians.

    Args:
        num_of_players (int): The numbers of players that are participating in 
        the game

    Returns:
        Players (list): A list of player instances.

    Side effects: 
        Instances of players will be updated to now have a role. This will be done 
        through either classes or interfaces."""
def night_time(self, players):
    """This method will be in charge of the night time cycle. This includes
    actions from the Doctor (protect someone from elimination), the Mafia 
    (eliminate someone), and the Detective(s) (learn someone’s role).

    Args: 
        players (list) : a list of player instances

    Returns:
        (list) : list of actions from players

    Side effects:
    Detective action will print someone’s role if selected. Mafia action will 
    print who is eliminated and will potentially reduce the list of players
    by 1."""

 def day_time(self, players):
     #add voting function with iteration 
     
    """This method will be in charge of the day cycle. This includes 
    giving the information gathered overnight (i.e. deaths and saves)
    and giving the players time/a way to vote to eliminate. 
     Args:
        players(list): a list of Player instances
     Returns:
         (bool): if the players voted out a member of the mafia

     Side effects:
        The information and the voting process will printed to	stdout"""

def check_win_condition(self, player):
    """This method checks if the game has reached a win condition. The game
    ends when either all mafia members have been eliminated (villagers win) or
    when the number of mafia players is equal to or greater than the number of
    non-mafia players (mafia wins).

    Args:
    players(list) : a list of player instances who are still in the game

    Return:
        str: A string indicating the result of the game:
    “Mafia” if the mafia has won
    “Villagers” if the villagers have one
    None if neither condition has been met

    Side effects: 
        None. """
    pass

def main():
    pass

if __name__ == "__main__": 
    pass