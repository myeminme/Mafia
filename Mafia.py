import random 
from argparse import ArgumentParser
from sys import argv

class Player:
    """Class for the player objects
    
    Attributes:
        name (str): the players name
        role (str): the role of the player (villager, mafia, doctor, or 
            detective)
        status (str): either alive or eliminated if the player is still playing
    """
    def __init__(self, name, role, status = "alive"):
        """Sets the attriubtes

        Args:
            name (str): name of the player
            role (str): role of the player
            status (str, optional): if the player is alive or dead.
                Defaults to "alive".
        """
        self.name = name
        self.role = role
        self.status = status

def make_game_with_objects(players): #
    """ This function will randomly assign roles to each player depending on how 
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
    assigned = []
    
    #assign random to nurse
    nurse = random.choice(no_roles)
    assigned.append(Player(nurse, "nurse"))
    no_roles.remove(nurse)
    
    #assign random to detective
    detective = random.choice(no_roles)
    assigned.append(Player(detective, "detective"))
    no_roles.remove(detective)
    
    #assign random to mafia 
    while mafia_num:
        mafia = random.choice(no_roles)
        assigned.append(Player(mafia, "mafia"))
        no_roles.remove(mafia)
        mafia_num-=1
    #assign rest to villager
    for j in no_roles:
        assigned.append(Player(j, "villager"))
    
    return(assigned)
    
    
def make_game(players): # Not sure we use this anymore...
    """ This function will randomly assign roles to each player depending on how 
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
    
    return(assigned)

def get_choice(prompt, options):
    """Displays a list of players and returns the selected player object.

    Args: 
        prompt (String) : prompt for specific player
        options (list) : list of alive players

    Returns:
        (int) : returns choice of specific player

    Side Effects:
        Prints options of players, and takes in input for a number until valid input.

    Raises:
        ValueError: If input is not a number, it will try again.
    """
    print(f"\n--- {prompt} ---")
    for i, player in enumerate(options):
        print(f"{i + 1}) {player.name}")
    
    while True:
        try:
            choice = int(input("Select a number: ")) - 1
            if 0 <= choice < len(options):
                return options[choice]
            print("Invalid number. Try again.")
        except ValueError:
            print("Please enter a valid number.")

from collections import Counter

def night_time(players):
    """This function will be in charge of the night time cycle. This includes
    actions from the Doctor (protect someone from elimination), the Mafia 
    (eliminate someone), and the Detective(s) (learn someone's role).

    Args: 
        players (list) : a list of player instances

    Returns:
        (list) : list of actions from players

    Side effects:
    Detective action will print someone's role if selected. Mafia action will 
    print who is eliminated and will potentially reduce the list of players
    by 1."""
    # Filter for players who are still in the game
    alive_players = get_alive_players(players)

    input("----NIGHT TIME----\nPress Enter to continue:")
    print("\n" * 50)
    # 1. Nurse's turn
    nurse = next((p for p in alive_players if p.role == "nurse"), None)
    protected_target = None
    if nurse:
        print("\nNurse, It's your turn!!")
        protected_target = get_choice("Who do you want to save?", alive_players)
    print("\n" * 50)           

    # 2. Mafia's turn
    mafia_members = [p for p in alive_players if p.role == "mafia"]
    kill_target = None
    
    if mafia_members:
        input(f"\n---- MAFIA VOTING PHASE ----\nPress Enter to start phase:")
        print("\n" * 50)
        votes = []
        kill_options = [p for p in alive_players if p.role != "mafia"]
        
        for i in mafia_members:
            input(f"Mafia, {i.name}, press Enter to cast your secret vote...")
            voted_for = get_choice(f" Mafia {i.name}, who should we eliminate?", kill_options)
            votes.append(voted_for)
            # clear_screen()

        # Determine the winner of the vote
        vote_counts = Counter(votes)
        # Get the player(s) with the highest number of votes
        top_votes = vote_counts.most_common(1) # Returns [(player_object, count)]
        
        if top_votes:
            kill_target = top_votes[0][0]
            print(f"Most Voted: The Mafia has decided to target {kill_target.name}")
        input("Press Enter to continue:")
        print("\n" * 50)   
    # 3. Detective's turn
    detective = next((p for p in alive_players if p.role == "detective"), None)
    if detective:
        print(f"\nDetective, It's your turn!!")
        investigation_options = [p for p in alive_players if p != detective]
        check_target = get_choice("Who do you want to investigate?", investigation_options)
        print(f"Investigation Conclusion: Player {check_target.name} is {check_target.role}")
        input("Press Enter to continue")
    # Resolution
    print("\n" * 50)
    if kill_target:
        if kill_target == protected_target:
            input(f"The Mafia attacked {kill_target.name}, but they were saved!")
        else:
            kill_target.status = "eliminated"
            input(f"The morning sun rises, but {kill_target.name} is nowhere to be found.")
    else:
        input("The night was quiet.")
    
def reveal_roles_privately(players):
    """This function reveals roles privately, so other players do not know.

    Args:
        players (list) : list of Player instances

    Side Effects:
        Takes in input and prints role of specific player. 
    """       
    for p in players:
        input(f"Is {p.name} at the computer? Press Enter to see your secret role...")
        print(f"Your role is: {p.role}")
        input("Press Enter to clear the screen for the next player...")
        print("\n" * 50) # Hide the role



def check_win(players):
    """Checks to see if there are more mafia players than villagers (i.e. mafia
        wins)

    Args:
        players(list): a list of Player instances

    Returns:
        string: if there is a winner, it returns which team won, otherwise 
        returns none
    """
    alive_players = [p for p in players if p.status == "alive"]
    mafia_count = sum(1 for p in alive_players if p.role == "mafia")
    villager_count = sum(1 for p in alive_players if p.role != "mafia")
    if mafia_count == 0:
        return "Villagers"
    elif mafia_count >= villager_count:
        return "Mafia"
    else: 
        return None
           
def get_alive_players(players):
    """Filters and returns players who are alive and still in the game

    Args:
        players(list): a list of Player instances

    Returns:
        A list of player instances who are still alive 
    
    Side effects: None
    """
    return [p for p in players if p.status == "alive"]

def vote(players): # Andrew Gerhardt
    """This function is how the players in the game will vote. Each player will
        vote for another player and votes will be counted before sorted and 
        returning the winner (or technically loser).
        
    Args: players(list): a list of Player instances
    
    Returns: The name of the winner and what role they had
    
    Side effects: Prints and reads from the stdout
    
    """
    alive_players = get_alive_players(players)
    votes = {p.name.lower(): 0 for p in alive_players}
    for p in alive_players:
        voted_for = input(f"{p.name} please vote for a player ").lower()
        while voted_for not in votes.keys():
            voted_for = input("""That player was not found. 
                              Please try again """).lower()
        votes[voted_for] += 1
    sorted_votes = dict(sorted(votes.items(), key=lambda item: item[1], 
                               reverse=True)) # claming use of a key function
    
    tied_names = tie(sorted_votes)
    if isinstance(tied_names, list):
        print("It's a tie. Lets do it again!")
        tied_players= [p for p in alive_players if p.name.lower() in tied_names]
        return vote(tied_players)
    winner = next(p for p in alive_players if p.name.lower() == 
                  list(sorted_votes)[0])
    winner.status = "eliminated"
    return f"{winner.name}, was voted out. They were a {winner.role}!"

def tie(votes): # Andrew Gerhardt
    """This function checks if there is a tie in the voting process

    Args: votes (dict): the pre sorted dict of player instances and
        and how many votes they got.
    
    Returns: a string if just one winner, a list of the winner if there is a tie
    """
    most_votes = max(votes.values())
    players_in_tie = [player for player, count in votes.items() 
                      if count == most_votes]
    if len(players_in_tie) > 1:
        return players_in_tie
    return players_in_tie[0]


def reveal_all_roles(players):
    """Reveals the roles of all players
    
    Args:
        players(list): A list of player instances
        
    Returns:
        None
        
    Side effects:
        Prints each player's name along with their role"""
    for p in players:
        print(f"{p.name}: {p.role}")

def game_loop(players):
    """Controls the main flow of the mafia game by running alternating night
    and day cycles until a win condition is met
    
    Args: 
        players (list): A list of player instances participating in the game
        
    Returns: 
        None
        
    Side effects:
        Calls night_time and vote to stimulate gameplay
        Prints updates about each phasing, including updates about
        eliminations and results
        Ends the game when a winner is determined and results are printed"""
    while True:
        night_time(players)
        winner = check_win(players)
        #reveal_all_roles(players)
        if winner:
            print(f"{winner} won!")
            reveal_all_roles(players) 
            break
        print("\n --- DAY TIME ---")
        print(vote(get_alive_players(players)))
        
        winner = check_win(players)
        if winner:
            print(f"{winner} won!")
            reveal_all_roles(players)
            break
    

def play_game(filepath): # Andrew Gerhardt and Akshay
    players = list()
    with open(filepath, "r", encoding= "utf-8") as f:
        for line in f:
            players.append(line.strip())
    the_players = make_game_with_objects(players)
    reveal_roles_privately(the_players)
    game_loop(the_players) 

def parse_args(arglist): # Andrew Gerhardt
    """Parse command-line arguments.
    
    Expect three mandatory arguments:
        - filepath: a path to a file containing the people playing mafia

    Args:
        arglist (list of str): arguments from the command line.

    Returns:
        namespace: the parsed arguments, as a namespace.
    """
    
    parser = ArgumentParser()
    parser.add_argument("filepath",help="Path to the file with the players")
    return parser.parse_args(arglist)

if __name__ == "__main__": 
    args = parse_args(argv[1:])
    play_game(args.filepath)
