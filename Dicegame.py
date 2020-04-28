
from random import sample

class Dashboard:
    def __init__(self,players):
        self.players=dict.fromkeys(players,0)
        self.__winner=None
        
    def update_score(self,player):
            throw=Dice.throw()
            print('{} throw {}'.format(player,throw))
            self.players[player] += sum(throw)
            
    def get_winner(self):
        score=max(self.players.values())
        winner_list= filter(lambda player:self.players[player]==score,self.players)
        winner=[player for player in winner_list] 
        self.__winner='tie' if len(winner) > 1 else 'winner is {}'.format(''.join(winner))
        return self.__winner
        
class Player:
    #if complex data structure is needed then override this
    pass
    
class Dice:
    die=[1,2,3,4,5,6,1,2,3,4,5,6]
    def throw():
        return sample(Dice.die,2)
    
class Dicegame:  
     def __init__(self,rounds):
         self.numOfPlayer=0
         self.rounds=rounds
         self.board=None
         
     def register_players(self,players):
          self.numOfplayer=len(players)
          self.board=Dashboard(players)
         
     def start(self):
         for num in range(1,self.rounds+1):
             temp_board=self.board.players.copy()
             print('\nstarting round....',num)
             for player in self.board.players.keys():
                 print("\n{} it's your turn".format(player))
                 input('Enter T to throw - ')
                 self.board.update_score(player)
             for key,value in zip(temp_board.keys(),zip(self.board.players.values(),temp_board.values())):
                 temp_board[key]=value[0]-value[1]
    
             print('\nResult for rounds {0} = {1}'.format(num,temp_board))
         print('\nfinal result is = {0}'.format(self.board.players))
         print(self.board.get_winner())
             
      
      
      
         
if __name__=='__main__':
    test=input('[NOTE - Name should be seperated by comma]\nplayer names  - ')
    num=int(input('\nNo of Round - '))
    board=Dicegame(num)
    board.register_players(test.split(','))
    board.start()