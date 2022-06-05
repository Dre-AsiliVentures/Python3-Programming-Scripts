#Formula 1 points award scheme
class awardpoints:
    def __init__(self,race_type,pos):
        self.race_type=race_type
        self.pos=pos
        #self.player==player
        print("Initializing..  ..")
        #race_type=int(input("Enter the race type:"))
        #print("1= Main Race.\n2= Sprint.")
        race=("main_race","Sprint")
    def player_points(race_type,pos):
        if race_type=='Main':
            print("Now assigning points for Main race")
            points=['25','18','15','12','10','8','6','4','2','1']
            return points[pos-1]
        elif race_type=='Sprint':
            print("Now assigning points for Sprint race")
            points=['8','7','6','5','4','3','2','1']
            print(points[int(pos)-1])
        else:
            print("Buda kuwa serious")

if __name__ == '__main__':
    awardpoints.player_points('Sprint','2')
    print(awardpoints.player_points('Main',2))