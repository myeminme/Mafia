import random 
from argparse import ArgumentParser
from sys import argv
from collections import Counter

class Player:
    """Class for the player objects
    
    Attributes:
        name (str): the players name
        role (str): the role of the player (villager, mafia, doctor, or 
            detective)
    """
    def __init__(self, name, role):
        """Sets the attriubtes

        Args:
            name (str): name of the player
            role (str): role of the player
            status (str, optional): if the player is alive or dead.
                Defaults to "alive".
        """
        self.name = name
        self.role = role
    
    def __str__(self):
        return (f"The player {self.name}'s role is {self.role.name}.")

#parent class
class Role():
    def __init__(self,name):
        self.name = name
        
    def action(self, game):
        pass
        
    
class Mafia(Role):
    def __init__(self):
        super().__init__("mafia")
        
    def action(self, game, player):
        input(f"Mafia press Enter to cast your secret vote...")
        voted_for = game.get_choice(f"Mafia {player.name}, who should we eliminate?", game.kill_options)
        game.votes.append(voted_for)
        print("\n" * 50)
        
class Nurse(Role):
    def __init__(self):
        super().__init__("nurse")
        
    def action(self, game, player):
        print("\nNurse, It's your turn!!")
        game.protect_target = game.get_choice(f"{player.name}, Who do you want to save?", game.alive_players )
        print("\n" * 50)  
    
class Detective(Role):
    def __init__(self):
        super().__init__("detective")
        
    def action(self, game, player):
        print(f"\nDetective, It's your turn!!")
        investigation_options = [p for p in game.alive_players if p != player]
        check_target = game.get_choice("Who do you want to investigate?", investigation_options)
        print(f"Investigation Conclusion: Player {check_target.name} is a {check_target.role.name}")
        input("Press Enter to continue")
        print("\n" * 50)
        
class Villager(Role):
    def __init__(self):
        super().__init__("villager")
        
    def action(self, game, player):
        pass
    
class Game:
    
    def __init__(self):
        self.kill_target = None
        self.kill_options = []
        self.protect_target = None
        self.alive_players = []
        self.eliminated = []
        self.votes = []
    
    def make_game(self, players): #
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
        if len(players) < 4:
            mafia_num = 1
        elif len(players) < 7:
            mafia_num = 2
        elif len(players) < 10:
            mafia_num = 3
        else:
            mafia_num = 4
            
        #Non updated player list
        no_roles =list(players)
        
        #Players with Roles
        assigned = []
        
        #assign random to nurse
        nurse = random.choice(no_roles)
        assigned.append(Player(nurse, Nurse()))
        no_roles.remove(nurse)
        
        #assign random to detective
        detective = random.choice(no_roles)
        assigned.append(Player(detective, Detective()))
        no_roles.remove(detective)
        
        #assign random to mafia 
        while mafia_num:
            mafia = random.choice(no_roles)
            assigned.append(Player(mafia, Mafia()))
            no_roles.remove(mafia)
            mafia_num-=1
        #assign rest to villager
        for j in no_roles:
            assigned.append(Player(j, Villager()))
        
        return(assigned)       

    def get_choice(self, prompt, options):
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

    def night_time(self):
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
        
        #reset attributes
        self.kill_target = None
        self.kill_options = []
        self.protect_target = None
        self.votes = []
        self.kill_options = []

        input("----NIGHT TIME----\nPress Enter to continue:")
        print("\n" * 50)
        
        self.kill_options = [p for p in self.alive_players if not isinstance(p.role, Mafia)]
        # Players turns
        for person in self.alive_players:
            input(f"\n---- PASS THE DEVICE TO {person.name} ----\nPress Enter to start turn:")
            print("\n" * 50)
            person.role.action(self, person)
         # Determine the winner of the vote
        vote_counts = Counter(self.votes)
        
        # Get the player(s) with the highest number of votes
        top_votes = vote_counts.most_common(1) # Returns [(player_object, count)] 
            
        if top_votes:
            self.kill_target = top_votes[0][0]
            print(f"Most Voted: The Mafia has decided to target {self.kill_target.name}")
        input("Press Enter to continue:")
        print("\n" * 50)   
        self.votes.clear()
        
        # Resolution
        print("\n" * 50)
        if self.kill_target:
            if self.kill_target == self.protect_target:
                input(f"The Mafia attacked {self.kill_target.name}, but they were saved!")
            else:
                self.alive_players.remove(self.kill_target)
                self.eliminated.append(self.kill_target)
                input(f"The morning sun rises, but {self.kill_target.name} is nowhere to be found.")
        else:
            input("The night was quiet.")
        
    def reveal_roles_privately(self, players):
        """This function reveals roles privately, so other players do not know.

        Args:
            players (list) : list of Player instances

        Side Effects:
            Takes in input and prints role of specific player. 
        """       
        for p in players:
            input(f"Is {p.name} at the computer? Press Enter to see your secret role...")
            print(f"Your role is: {p.role.name}")
            input("Press Enter to clear the screen for the next player...")
            print("\n" * 50) # Hide the role

    def check_win(self):
        """Checks to see if there are more mafia players than villagers (i.e. mafia
            wins)

        Args:
            players(list): a list of Player instances

        Returns:
            string: if there is a winner, it returns which team won, otherwise 
            returns none
        """
        mafia_count = sum(1 for p in self.alive_players if isinstance(p.role, Mafia))
        villager_count = sum(1 for p in self.alive_players if not isinstance(p.role, Mafia))
        if mafia_count == 0:
            return "Villagers"
        elif mafia_count >= villager_count:
            return "Mafia"
        else: 
            return None
            
    def vote(self, players=None): # Andrew Gerhardt
        """This function is how the players in the game will vote. Each player will
            vote for another player and votes will be counted before sorted and 
            returning the winner (or technically loser).
            
        Args: players(list): a list of Player instances
        
        Returns: The name of the winner and what role they had
        
        Side effects: Prints and reads from the stdout
        
        """
        if players is None:
            players = self.alive_players
        votes = {p.name: 0 for p in players}
        
        for p in self.alive_players:
            voted_for = self.get_choice(f"{p.name}, please vote for a player ?", players).name
            #voted_for = input(f"{p.name} please vote for a player ").lower()
            #while voted_for not in votes.keys():
                #voted_for = input("""That player was not found. 
                                #Please try again """).lower()
            votes[voted_for] += 1
        sorted_votes = dict(sorted(votes.items(), key=lambda item: item[1], 
                                reverse=True)) # claming use of a key function
        
        tied_names = self.tie(sorted_votes)
        if isinstance(tied_names, list):
            print("It's a tie. Lets do it again!")
            tied_players= [p for p in self.alive_players if p.name in tied_names]
            return self.vote(tied_players)
        winner = next(p for p in self.alive_players if p.name == list(sorted_votes)[0])
        self.alive_players.remove(winner)
        self.eliminated.append(winner)
        return f"{winner.name}, was voted out. They were a {winner.role}!"

    def tie(self, votes): # Andrew Gerhardt
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

    def reveal_all_roles(self, players):
        """Reveals the roles of all players
        
        Args:
            players(list): A list of player instances
            
        Returns:
            None
            
        Side effects:
            Prints each player's name along with their role"""
        for p in players:
            print(str(p))

    def game_loop(self, players):
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
        winner = None
        self.alive_players = players
        while winner is None:
            self.night_time()
            winner = self.check_win()
            #reveal_all_roles(players)
            if winner:
                break
            print("\n --- DAY TIME ---")
            print(self.vote())
            winner = self.check_win()

        print(f"{winner} won!")
        
        self.reveal_all_roles(players)
                
        

    def play_game(self, filepath): # Andrew Gerhardt and Akshay
        players = list()
        with open(filepath, "r", encoding= "utf-8") as f:
            for line in f:
                players.append(line.strip())
        the_players = self.make_game(players)
        self.reveal_roles_privately(the_players)
        self.game_loop(the_players) 

    def parse_args(self, arglist): # Andrew Gerhardt
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
    game = Game()
    args = game.parse_args(argv[1:])
    game.play_game(args.filepath)