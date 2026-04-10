import random 
# class Player:
#     def __init__(self):
#         self.role = "villager"
#         self.status = "alive"
#         self.awake = "no"

players = [ "Mykha",
           "Aishani",
           "Akshay",
           "Andrew",
           "Aric",
           "Testudo"]


def make_game(players):
    """ This method will randomly assign roles to each player depending on how 
    many people are playing. There are four roles: villager, mafia, doctor, and 
    detective. 
    5-7 players: 2 mafia, 1 detective, 1 doctor, 0-3 civilians
    8-11: 3 mafia, 1 detective, 1 doctor, 2-5 civilians
    12-15: 4 mafia, 1 detectives, 1 doctor, 4-7 civilians.

    Args:
        players (list): The list of players that are participating in 
        the game

    Returns:
        Assigned (list): A list of player instances and their assigned roles and status

    Side effects: 
        Instances of players will be updated to now have a role. This will be done 
        through either classes or interfaces."""
   
    #Amounts of Mafia
    mafia_num = 0
    if len(players) < 5:
        mafia_num = 1
    elif len(players) < 8:
        mafia_num = 2
    elif len(players) < 12:
        mafia_num = 3
    else:
        mafia_num = 4
    
    #Non updated player list
    no_roles =list(players)
    
    #Players with Roles
    assigned = {}
    
    #assign random to nurse
    nurse = random.choice(no_roles)
    assigned[nurse] = {"alive", "nurse"}
    no_roles.remove(nurse)
    
    #assign random to detective
    detective = random.choice(no_roles)
    assigned[detective] = {"alive", "detective"}
    no_roles.remove(detective)
    
    #assign random to mafia 
    for x in range(mafia_num):
        mafia = random.choice(no_roles)
        assigned[mafia] = {"alive", "mafia"}
        no_roles.remove(mafia)
    #assign rest to villager
    for j in no_roles:
        assigned[j] = {"alive", "villager"}
    
    print(assigned)
    
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
    """This method will be in charge of the day cycle. This includes 
    giving the information gathered overnight (i.e. deaths and saves)
    and giving the players time/a way to vote to eliminate. 
     Args:
        players(list): a list of Player instances
     Returns:
         (bool): if the players voted out a member of the mafia

     Side effects:
        The information and the voting process will printed to	stdout"""
        
def vote(self):
    pass

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
    make_game(players)

if __name__ == "__main__": 
    main()