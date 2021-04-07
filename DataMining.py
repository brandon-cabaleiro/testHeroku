'''
# information to Retrieve:
    Recording location on RAID
    Recording date
    ...
    

'''

'''
Connection to RAID:
    Method: MacOS terminal?
    RAID location: "Herbie's Macbook Pro (4728)
    Structure: HHMusic -> incoming Drives -> Drobo 5D3  
'''

'''
Connection to DataBase, Django:
    ...
'''

class Recordings:
    # constructor
    def __init__(self, loc, date, name):  
        self.loc = loc
        self.date = date
        self.artistName = name
        
    # viewer
    def getLocation (self):
        return self.loc
    
    def getDate (self):
        return self.date
    
    
def main():
    all_information = []
    
    
if __name__ == "__main__":
    main()


