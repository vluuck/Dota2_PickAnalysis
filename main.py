import json
import dltvparser

with open('heroes.json') as file:
    data = json.load(file)

class MainFunctions:
    "Class with all main functions"
      
    def __init__(self, teamRadiant: list, teamDire: list):
        "Function for initialising both team heroes, and all the function resulting values"

        self.teamRadiant = teamRadiant
        self.teamDire = teamDire

        self.tRadiantCounterpicksScore = 0
        self.tDireCounterpicksScore = 0

        self.tRadiantChemistryScore = 0
        self.tDireChemistryScore = 0


    def addPoints(self, team: list, path: str):
        "Function for summing needed value types in teams, returns int"
        scoretype = 0

        for hero in team:
            scoretype += data['heroes'][hero][path]

        scoretype /= 5
        return scoretype


    def checkHeroSpelling(self):
        "Function was created to valid hero names in teams, returns boolean"

        hero_list = [
        'Abaddon', 'Alchemist', 'Ancient_Apparition', 'Anti_Mage', 'Arc_Warden', 'Axe', 'Bane', 'Batrider', 'Beastmaster', 'Bloodseeker', 'Bounty_Hunter', 'Brewmaster', 'Bristleback', 'Broodmother', 'Centaur_Warrunner', 'Chaos_Knight', 'Chen', 'Clinkz', 'Clockwerk', 'Crystal_Maiden', 'Dark_Seer', 'Dark_Willow', 'Dawnbreaker', 'Dazzle', 'Death_Prophet', 'Disruptor', 'Doom', 'Dragon_Knight', 'Drow_Ranger', 'Earth_Spirit', 'Earthshaker', 'Elder_Titan', 'Ember_Spirit', 'Enchantress', 'Enigma', 'Faceless_Void', 'Grimstroke', 'Gyrocopter', 'Hoodwink', 'Huskar', 'Invoker', 'Io', 'Jakiro', 'Juggernaut', 'Keeper_of_the_Light', 'Kunkka', 'Legion_Commander', 'Leshrac', 'Lich', 'Lifestealer', 'Lina', 'Lion', 'Lone_Druid', 'Luna', 'Lycan', 'Magnus', 'Marci', 'Mars', 'Medusa', 'Meepo', 'Mirana', 'Monkey_King', 'Morphling', 'Muerta', 'Naga_Siren', "Nature's_Prophet", 'Necrophos', 'Night_Stalker', 'Nyx_Assassin', 'Ogre_Magi', 'Omniknight', 'Oracle', 'Outworld_Destroyer', 'Outworld_Devourer', 'Pangolier', 'Phantom_Assassin', 'Phantom_Lancer', 'Phoenix', 'Primal_Beast', 'Puck', 'Pudge', 'Pugna', 'Queen_of_Pain', 'Razor', 'Riki', 'Rubick', 'Sand_King', 'Shadow_Demon', 'Shadow_Fiend', 'Shadow_Shaman', 'Silencer', 'Skywrath_Mage', 'Slardar', 'Slark', 'Snapfire', 'Sniper', 'Spectre', 'Spirit_Breaker', 'Storm_Spirit', 'Sven', 'Techies', 'Templar_Assassin', 'Terrorblade', 'Tidehunter', 'Timbersaw', 'Tinker', 'Tiny', 'Treant_Protector', 'Troll_Warlord', 'Tusk', 'Underlord', 'Undying', 'Ursa', 'Vengeful_Spirit', 'Venomancer', 'Viper', 'Visage', 'Void_Spirit', 'Warlock', 'Weaver', 'Windranger', 'Winter_Wyvern', 'Witch_Doctor', 'Wraith_King', 'Zeus'
        ]

        for hero in self.teamRadiant:
            if hero not in hero_list:
                print("Hero name in team Radiant is not valid =", hero)
                return False
        
        for hero in self.teamDire:
            if hero not in hero_list:
                print("Hero name in team Dire is not valid =", hero)
                return False 

        return True
    
    
    def checkCounterpicks(self):
        "Function to measure counterpicks score in both teams, it change counterpicks values in class specimen, returns nothing"
        self.radiantCounterpicksInfo = []
        self.direCounterpicksInfo = []

        for hero in self.teamRadiant:
            for i in range(0, 5):
                if self.teamDire[i] in data['heroes'][hero]['counters']['good_against']:
                    self.radiantCounterpicksInfo.append(f'{hero} counters {self.teamDire[i]} |')
                    self.tRadiantCounterpicksScore += 20

        for hero in self.teamDire:
            for i in range(0, 5):
                if self.teamRadiant[i] in data['heroes'][hero]['counters']['good_against']:
                    self.direCounterpicksInfo.append(f'{hero} counters {self.teamRadiant[i]} |')
                    self.tDireCounterpicksScore += 20
        

    def checkChemistry(self):
        "Function to measure chemistry score in both teams, it change chemistry values in class specimen, returns nothing"

        for hero in self.teamRadiant:
            for i in range(0, 4):
                if self.teamRadiant[i] in data['heroes'][hero]['counters']['works_well_with']:
                    self.tRadiantChemistryScore += 15

        for hero in self.teamDire:
            for i in range(0, 4):
                if self.teamDire[i] in data['heroes'][hero]['counters']['works_well_with']:
                    self.tDireChemistryScore += 15


    def checkTeamControl(self):
        "Function to measure control score in both teams, it change control values in class specimen, returns nothing"
        self.tRadiantControlScore = self.addPoints(self.teamRadiant, 'control')
        self.tDireControlScore = self.addPoints(self.teamDire, 'control')


    def checkTeamEscapability(self):
        "Function to measure escapability score in both teams, it change escapability values in class specimen, returns nothing"

        self.tRadiantEscapabilityScore = self.addPoints(self.teamRadiant, 'escape')
        self.tDireEscapabilityScore = self.addPoints(self.teamDire, 'escape')


    def checkTeamDurability(self):
        "Function to measure durability score in both teams, it change durability values in class specimen, returns nothing"

        self.tRadiantDurabilityScore = self.addPoints(self.teamRadiant, 'durability')
        self.tDireDurabilityScore = self.addPoints(self.teamDire, 'durability')


    def checkTeamInitiation(self):
        "Function to measure initiation score in both teams, it change initiation values in class specimen, returns nothing"

        self.tRadiantInitiationScore = self.addPoints(self.teamRadiant, 'initiation')
        self.tDireInitiationScore = self.addPoints(self.teamDire, 'initiation')


    def checkTeamLaning(self):
        "Function to measure laning score in both teams, it change laning values in class specimen, returns nothing"

        self.tRadiantLaningScore = self.addPoints(self.teamRadiant, 'laning')
        self.tDireLaningScore = self.addPoints(self.teamDire, 'laning')


    def checkTeamEarlygame(self):
        "Function to measure earlygame score in both teams, it change earlygame values in class specimen, returns nothing"

        self.tRadiantEarlygameScore = self.addPoints(self.teamRadiant, 'earlygame')
        self.tDireEarlygameScore = self.addPoints(self.teamDire, 'earlygame')


    def checkTeamMidgame(self):
        "Function to measure midgame score in both teams, it change midgame values in class specimen, returns nothing"

        self.tRadiantMidgameScore = self.addPoints(self.teamRadiant, 'midgame')
        self.tDireMidgameScore = self.addPoints(self.teamDire, 'midgame')

    
    def checkTeamLategame(self):
        "Function to measure lategame score in both teams, it change midgame values in class specimen, returns nothing"

        self.tRadiantLategameScore = self.addPoints(self.teamRadiant, 'lategame')
        self.tDireLategameScore = self.addPoints(self.teamDire, 'lategame')


    def checkTeamMeta(self):
        "Function to measure meta(OP) score in both teams, it change average score values in class specimen, returns nothing"

        self.tRadiantMetaScore = self.addPoints(self.teamRadiant, 'meta')
        self.tDireMetaScore = self.addPoints(self.teamDire, 'meta')


    def averageResultValue(self):
        "Function to measure average score in both teams, it change average score values in class specimen, returns nothing"

        self.tRadiantAverageScore = ((self.tRadiantCounterpicksScore)+(self.tRadiantChemistryScore)+(self.tRadiantControlScore)+(self.tRadiantEscapabilityScore)+(self.tRadiantDurabilityScore)+(self.tRadiantInitiationScore)+(self.tRadiantLaningScore)+(self.tRadiantEarlygameScore)+(self.tRadiantMidgameScore)+(self.tRadiantLategameScore)) / 10
        self.tDireAverageScore =    ((self.tDireCounterpicksScore)+(self.tDireChemistryScore)+(self.tDireControlScore)+(self.tDireEscapabilityScore)+(self.tDireDurabilityScore)+(self.tDireInitiationScore)+(self.tDireLaningScore)+(self.tDireEarlygameScore)+(self.tDireMidgameScore)+(self.tDireLategameScore)) / 10


    def allFuncResults(self, tRadiantTag = "empty", tDireTag = "empty"):
        "This function takes the results of other class functions together, and returns them"

        if self.tRadiantCounterpicksScore != None:
            res = """
░░░░░╔╗░░╔╗░░░░░░░░░░░╔╗░░░░░░░░░░░░░░╔╗░░░░░░░░░░░░░╔╗░╔═══╗░░░
░░░░░║║░╔╝╚╗░░░░░░░░░░║║░░░░░░░░░░░░░░║║░░░░░░░░░░░░╔╝║░║╔═╗║░░░
░░░╔═╝╠═╩╗╔╬══╗╔══╦╦══╣║╔╦══╗╔══╦═╗╔══╣║╔╗░╔╦═══╦══╦╩╗║░║║║║║░░░
░░░║╔╗║╔╗║║║╔╗║║╔╗╠╣╔═╣╚╝╣══╣║╔╗║╔╗╣╔╗║║║║░║╠══║║║═╣╔╣║░║║║║║░░░
░░░║╚╝║╚╝║╚╣╔╗║║╚╝║║╚═╣╔╗╬══║║╔╗║║║║╔╗║╚╣╚═╝║║══╣║═╣╠╝╚╦╣╚═╝║░░░
░░░╚══╩══╩═╩╝╚╝║╔═╩╩══╩╝╚╩══╝╚╝╚╩╝╚╩╝╚╩═╩═╗╔╩═══╩══╩╩══╩╩═══╝░░░
░░░░░░░░░░░░░░░║║░░░░░░░░░░░░░░░░░░░░░░░╔═╝║░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░╚╝░░░░░░░░░░░░░░░░░░░░░░░╚══╝░░░░░░░░░░░░░░░░░░░░

"""
            res += ("(" + tRadiantTag + ") ").ljust(21, ' ') + "Radiant:  " + " ".join(self.teamRadiant) +"\n"
            res += ("(" + tDireTag +  ") ").ljust(21, ' ') + "Dire:     " + " ".join(self.teamDire)  + "\n" + "\n"
            res += "               Team Radiant" + "           " + "  Team Dire \n \n"
            res += ("                    " + str(round(self.tRadiantCounterpicksScore)).rjust(2, " ") + "     counterpicks     " + str(round(self.tDireCounterpicksScore)).rjust(2, " ") + "\n") 
            res += ("                    " + str(round(self.tRadiantChemistryScore)).rjust(2, " ") + "     chemistry        " +    str(round(self.tDireChemistryScore)).rjust(2, " ") + "\n")
            res += ("                    " + str(round(self.tRadiantControlScore)).rjust(2, " ") + "     control          " +      str(round(self.tDireControlScore)).rjust(2, " ") + "\n")
            res += ("                    " + str(round(self.tRadiantEscapabilityScore)).rjust(2, " ") + "     escapability     " + str(round(self.tDireEscapabilityScore)).rjust(2, " ") + "\n")
            res += ("                    " + str(round(self.tRadiantDurabilityScore)).rjust(2, " ") + "     durability       " +   str(round(self.tDireDurabilityScore)).rjust(2, " ") + "\n")
            res += ("                    " + str(round(self.tRadiantInitiationScore)).rjust(2, " ") + "     initiation       " +   str(round(self.tDireInitiationScore)).rjust(2, " ") + "\n")
            res += ("                    " + str(round(self.tRadiantLaningScore)).rjust(2, " ") + "     laning           " +       str(round(self.tDireLaningScore)).rjust(2, " ") + "\n")
            res += ("                    " + str(round(self.tRadiantEarlygameScore)).rjust(2, " ") + "     earlygame        " +    str(round(self.tDireEarlygameScore)).rjust(2, " ") + "\n")
            res += ("                    " + str(round(self.tRadiantMidgameScore)).rjust(2, " ") + "     midgame          " +      str(round(self.tDireMidgameScore)).rjust(2, " ") + "\n")
            res += ("                    " + str(round(self.tRadiantLategameScore)).rjust(2, " ") + "     lategame         " +      str(round(self.tDireLategameScore)).rjust(2, " ") + "\n")
            res += ("                    " + str(round(self.tRadiantMetaScore)).rjust(2, " ") + "     meta             " +      str(round(self.tDireMetaScore)).rjust(2, " ") + "\n" + "\n")
            res += ("                    " + str(round(self.tRadiantAverageScore)).rjust(2, " ") + "     average          " +      str(round(self.tDireAverageScore)).rjust(2, " ") + "\n" + "\n")
            if len(self.radiantCounterpicksInfo) > 0:
                res += ("Radiant counters: " + " ".join(self.radiantCounterpicksInfo) + "\n")
            if len(self.direCounterpicksInfo) > 0:
                res += ("Dire counters: " + " ".join(self.direCounterpicksInfo) + "\n")
            res += """
░░░░░░░░░░░░░░░░░░░╔═╗░░░░░░░╔╗░░╔╗░░░╔╗░╔╗░░░░░░░╔╗░░░░░░░░░░░░
░░░░░░░░░░░░░╔╦╦╦═╗║═╣╔══╦═╗╔╝╠═╗║╚╦╦╗║╚╦╝╠╗╔╦╦╦╦═╣╠╗░░░░░░░░░░░
░░░░░░░░░░░░░║║║║╬╚╬═║║║║║╬╚╣╬║╩╣║╬║║║╚╗║╔╣╚╣║║║║═╣═╣░░░░░░░░░░░
░░░░░░░░░░░░░╚══╩══╩═╝╚╩╩╩══╩═╩═╝╚═╬╗║░╚═╝╚═╩═╩═╩═╩╩╝░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░╚═╝░░░░░░░░░░░░░░░░░░░░░░░░░░
"""
            return res


def allFuncLaunch(classSpecimen, tRadTag = " ", tDireTag = " "):
    "Function for launching main class functions and returning all func results in str type"
    if classSpecimen.checkHeroSpelling():
        classSpecimen.checkCounterpicks()
        classSpecimen.checkChemistry()
        classSpecimen.checkTeamControl()
        classSpecimen.checkTeamEscapability()
        classSpecimen.checkTeamDurability()
        classSpecimen.checkTeamInitiation()
        classSpecimen.checkTeamLaning()
        classSpecimen.checkTeamEarlygame()
        classSpecimen.checkTeamMidgame()
        classSpecimen.checkTeamLategame()
        classSpecimen.averageResultValue()
        classSpecimen.checkTeamMeta()
        return classSpecimen.allFuncResults(teamTags[0], teamTags[1])

    
def teamsCompos(rad, diret, link):
    neededfunc = dltvparser.getTeamComposition(link)
    global teamTags
    teamTags =   dltvparser.getTeamTag(link)

    global radiant, dire
    radiant = rad
    dire = diret

    if len(neededfunc[0]) == 5 and len(neededfunc[1]) == 5:
        radiant, dire = neededfunc[0], neededfunc[1]    

link = "https://ru.dltv.org/matches/406438"

radiant = ['Tiny', 'Tiny', 'Tiny', 'Tiny', 'Tiny']
dire =['Beastmaster', 'Faceless_Void', 'Crystal_Maiden', 'Lina', 'Clockwerk']

teamsCompos(radiant, dire, link)

match1 = MainFunctions(radiant, dire)
print(allFuncLaunch(match1, radiant, dire))