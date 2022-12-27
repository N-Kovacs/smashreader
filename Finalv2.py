from PIL import Image
import os
import time
#Image Values
Banjo = (255, 218, 155)
Falcon = (10, 4, 4)
DK = (255, 201, 143)
Ice = (55, 38, 30)
Incineroar = (233, 73, 73)
Jigglypuff = (243, 194, 200)
Joker = (148, 120, 99)
Link = (245, 201, 166)
Lucina = (253, 229, 185)
Megaman = (241, 251, 252)
Palutena = (249, 214, 186)
Peach = (253, 239, 202)
Pichu = (255, 248, 115)
PKMN = (249, 229, 204)
Ridley = (139, 127, 151)
ROB = (29, 25, 24)
Robin = (255, 223, 204)
Samus = (226, 255, 204)
Shulk = (220, 158, 117)
Snake = (123, 80, 61)
Wii = (243, 239, 236)
Wolf = (95, 91, 92)
Yoshi = (81, 143, 66)

BanjoG = (215, 215, 215)
FalconG = (0, 0, 0)
DKG = (204, 204, 204)
IceG = (43, 43, 43)
IncineroarG = (131, 131, 131)
JigglypuffG = (198, 198, 198)
JokerG = (131, 131, 131)
LinkG = (201, 201, 201)
LucinaG = (218, 218, 218)
MegamanG = (235, 235, 235)
PalutenaG = (210, 210, 210)
PeachG = (228, 228, 228)
PichuG = (233, 233, 233)
PKMNG = (225, 225, 225)
RidleyG = (117, 117, 117)
ROBG = (27, 27, 27)
RobinG = (221, 221, 221)
SamusG = (233, 233, 233)
ShulkG = (165, 165, 165)
SnakeG = (88, 88, 88)
WiiG = (227, 227, 227)
WolfG = (87, 87, 87)
YoshiG = (119, 119, 119)

Ridley2 = (116, 116, 116)
Jigglypuff2 = (244, 195, 201)
Lucina2 = (249, 225, 181)
Yoshi2 = (77, 144, 65)
Pichu2 = (234, 234, 234)

#P2 Image Values
Mario = (35, 95, 219)
ICEC = (67, 45, 34)
ToonL = (98, 74, 36)
KROOL = (173, 202, 148)
LILM = (188, 91, 126)
DRM = (236, 214, 177)
Ike = (236, 214, 203)
Pikachu = (249, 139, 60)
Bowser = (251, 224, 169)
Pichu = (255, 248, 115)
Rosalina = (255, 248, 115)
Luigi = (210, 216, 204)

TOONLG = (89, 89, 89)
MarioG = (95, 95, 95)
LucarioG = (107, 107, 107)
LILMG = (119, 119, 119)
GanondorfG = (155, 155, 155)
KROOLG = (183, 183, 183)
DRMG = (203, 203, 203)
DKG = (204, 204, 204)
LuigiG = (204, 204, 204)
DededeG = (210, 210, 210)
BowserG = (216, 216, 216)
RosalinaG = (219, 219, 219)
NessG = (221, 221, 221)
PikachuG = (236, 236, 236)

Pikachu2 = (166, 166, 166)
Bowser2 = (251, 225, 166)
Ness2 = (222, 222, 222)
Lucario2 = (108, 108, 108)

BlackP = (115, 115, 115)
BlackP2 = (116, 116, 116)
BlackP3= (22, 22, 22)

Kills = [0,0,0,0,0]
Played = [0,0,0,0,0]
Characters = ["","","","",""]



# Get Kills (Left Side)
print("Enter File Names:")
Filename = input()
print("Enter Number of Games")
Numgames = int(input())

Run = 1
while Run <= Numgames:
    Runchar= str(Run)
    im = Image.open(Filename + " (" + Runchar + ").jpg", 'r')
    Gametime = os.path.getmtime(Filename + " (" + Runchar + ").jpg")
    local_time = time.ctime(Gametime) 
    #print("ctime (Local time):", local_time) 
    width, height = im.size
    pixel_values = list(im.getdata())
    
    ## LEFT SIDE COMPLETE
    Char1 = 0
    Char2 = 5
    # X = 319, 335, 351, 367, 383
    # Y = 74 194 314 434 544
    while Char1 < 5:
        while Char2 >= 0:
            YK = 74 + (120*Char1)
            YX = 303 + (16*Char2)
            if pixel_values[width*YK+YX][0] < 200: 
                Char2 -= 1
                continue
            elif Char2 == 0:
                Kills[Char1] = 0
                break
            else:
                Kills[Char1] = Char2
                break
        Char2 = 5

        Char1 += 1
        

    #print("Kills for Left Side are:", Kills)
    SumKills = 0   
    SumKills = Kills[0] + Kills[1] + Kills[2] + Kills[3] + Kills[4]
    #print("Sum of Kills:", SumKills)    
    if SumKills == 5:
        with open('Win.txt', 'a') as f:
            f.write("%s\n" % "1")
            f.write("%s\n" % "1")
            f.write("%s\n" % "1")
            f.write("%s\n" % "1")
            f.write("%s\n" % "1")
    else:
        with open('Win.txt', 'a') as f:
            f.write("%s\n" % "0")
            f.write("%s\n" % "0")
            f.write("%s\n" % "0")
            f.write("%s\n" % "0")
            f.write("%s\n" % "0")
    SumKills = 0
    Char1 = 0
    while Char1 < 5:           
        YK = 110 + (120* Char1) 
        YX = 150
        YX1 = 360 
        YK1 = 150  + (120* Char1)
        Character1P = pixel_values[width*YK+YX]
        Character1P2 = pixel_values[width*YK+(YX+20)]
        Character1P3 = pixel_values[width*YK1+YX1]
        #print("Played value for", Char1+1, "is", Character1P3, "at", YX1, YK1)
        if Character1P3[0] > 50: Played[Char1] = 1
            
        #print("Found", Character1P, "At", YX, YK, "backup at", Character1P2)
        if Character1P == Banjo: Characters[Char1] ="Banjo"
        elif Character1P == Falcon: Characters[Char1] ="Captain Falcon"
        elif Character1P == DK: Characters[Char1] ="Donkey Kong"
        elif Character1P == Ice: Characters[Char1] ="Ice Climbers"
        elif Character1P == Incineroar: Characters[Char1] ="Incineroar"
        elif Character1P == Jigglypuff: Characters[Char1] ="Jigglypuff"
        elif Character1P == Joker: Characters[Char1] ="Joker"
        elif Character1P == Link: Characters[Char1] ="Link"
        elif Character1P == Lucina: Characters[Char1] ="Lucina"
        elif Character1P == Megaman: Characters[Char1] ="Megaman"
        elif Character1P == Palutena: Characters[Char1] ="Palutena"
        elif Character1P == Peach: Characters[Char1] ="Peach"
        elif Character1P == Pichu: Characters[Char1] ="Pichu"
        elif Character1P == PKMN: Characters[Char1] ="PKMN Trainer"
        elif Character1P == Ridley: Characters[Char1] ="Ridley"
        elif Character1P == ROB: Characters[Char1] ="ROB"
        elif Character1P == Robin: Characters[Char1] ="Robin"
        elif Character1P == Samus: Characters[Char1] ="Samus"
        elif Character1P == Shulk: Characters[Char1] ="Shulk"
        elif Character1P == Snake: Characters[Char1] ="Snake"
        elif Character1P == Wii: Characters[Char1] ="Wii Fit Trainer"
        elif Character1P == Wolf: Characters[Char1] ="Wolf"
        elif Character1P == Yoshi: Characters[Char1] ="Yoshi"
        elif Character1P == BanjoG and Character1P2 == (89, 89, 89): Characters[Char1] ="Banjo"
        elif Character1P == FalconG: Characters[Char1] ="Captain Falcon"
        elif Character1P == DKG: Characters[Char1] ="Donkey Kong"
        elif Character1P == IceG: Characters[Char1] ="Ice Climbers"
        elif Character1P == IncineroarG and Character1P2 == (151, 151, 151): Characters[Char1] ="Incineroar"
        elif Character1P == JigglypuffG: Characters[Char1] ="Jigglypuff"
        elif Character1P == JokerG: Characters[Char1] ="Joker"
        elif Character1P == LinkG: Characters[Char1] ="Link"
        elif Character1P == LucinaG: Characters[Char1] ="Lucina"
        elif Character1P == MegamanG: Characters[Char1] ="Megaman"
        elif Character1P == PalutenaG: Characters[Char1] ="Palutena"
        elif Character1P == PeachG: Characters[Char1] ="Peach"
        elif Character1P == PichuG and Character1P2 == (135, 135, 135): Characters[Char1] ="Pichu"
        elif Character1P == PKMNG: Characters[Char1] ="PKMN Trainer"
        elif Character1P == RidleyG: Characters[Char1] ="Ridley"
        elif Character1P == ROBG: Characters[Char1] ="ROB"
        elif Character1P == RobinG: Characters[Char1] ="Robin"
        elif Character1P == SamusG: Characters[Char1] ="Samus"
        elif Character1P == ShulkG: Characters[Char1] ="Shulk"
        elif Character1P == SnakeG: Characters[Char1] ="Snake"
        elif Character1P == WiiG: Characters[Char1] ="Wii Fit Trainer"
        elif Character1P == WolfG: Characters[Char1] ="Wolf"
        elif Character1P == YoshiG: Characters[Char1] ="Yoshi"
        elif Character1P == Ridley2: Characters[Char1] ="Ridley"
        elif Character1P == Jigglypuff2: Characters[Char1] ="Jigglypuff"
        elif Character1P == Lucina2: Characters[Char1] ="Lucina"
        elif Character1P == Yoshi2: Characters[Char1] ="Yoshi"
        elif Character1P == Pichu2: Characters[Char1] ="Pichu"
        else:
            Characters[Char1] = "Unknown"
            with open('Unknown.txt', 'a') as f:
                #print("Unknown Character found at position ", Char1+1, " with values", Character1P[1], "At", YX, YK, "backup at", Character1P2)
                f.write(str(Character1P[0]))
                f.write(" ")
                f.write(str(Character1P[1]))
                f.write(" ")
                f.write(str(Character1P[2]))
                f.write("\n")
            
        if Characters[Char1] != "Unknown":
            with open('Unknown.txt', 'a') as f:
                f.write("%s\n" % "0")

        Char1 +=1
        
    with open('Characters.txt', 'a') as f:
        for items in Characters:
            f.write("%s\n" % items)
    with open('Kills.txt', 'a') as f:
        for items in Kills:
            f.write("%s\n" % items)
    with open('Played.txt', 'a') as f:
        for items in Played:
            f.write("%s\n" % items)
    with open('Date.txt', 'a') as f:
        f.write("%s\n" % local_time)
        f.write("\n")
        f.write("\n")
        f.write("\n")
        f.write("\n")
    
    
    Kills = [0,0,0,0,0]
    Played = [0,0,0,0,0]
    Characters = ["","","","",""]
    MissingChar = ["","","","",""]
    ## RIGHT SIDE IN PROGRESS
        
    Char1 = 0
    Char2 = 5
    # X = 895, 911, 927, 943, 959
    # Y = 74 194 314 434 544
    while Char1 < 5:
        while Char2 >= 0:
            YK = 74 + (120*Char1)
            YX =  975 - (16*Char2)
            if pixel_values[width*YK+YX][0] < 200: 
                Char2 -= 1
                continue
            elif Char2 == 0:
                Kills[Char1] = 0
                break
            else:
                Kills[Char1] = Char2
                break
        Char2 = 5

        Char1 += 1
        

    #print("Kills for Right Side are:", Kills)
    SumKills = 0   
    SumKills = Kills[0] + Kills[1] + Kills[2] + Kills[3] + Kills[4]
    #print("Sum of Kills:", SumKills)    
    if SumKills == 5:
        with open('Win2.txt', 'a') as f:
            f.write("%s\n" % "1")
            f.write("%s\n" % "1")
            f.write("%s\n" % "1")
            f.write("%s\n" % "1")
            f.write("%s\n" % "1")
    else:
        with open('Win2.txt', 'a') as f:
            f.write("%s\n" % "0")
            f.write("%s\n" % "0")
            f.write("%s\n" % "0")
            f.write("%s\n" % "0")
            f.write("%s\n" % "0")
    SumKills = 0
    Char1 = 0
    while Char1 < 5:           
        YK = 110 + (120* Char1) 
        YX = 1128
        YX1 = 930 
        YK1 = 150  + (120* Char1)
        Character1P = pixel_values[width*YK+YX]
        Character1P2 = pixel_values[width*YK+(YX+20)]
        Character1P3 = pixel_values[width*YK1+YX1]
        #print("Played value for", Char1+1, "is", Character1P3, "at", YX1, YK1)
        if Character1P3[0] > 50: Played[Char1] = 1
            
        #print("Found", Character1P, "At", YX, YK, "backup at", Character1P2)
        if Character1P == Mario: Characters[Char1] ="Mario"
        elif Character1P == ICEC: Characters[Char1] ="ICE Climbers"
        elif Character1P == ToonL: Characters[Char1] ="Toon Link"
        elif Character1P == KROOL: Characters[Char1] ="K Rool"
        elif Character1P == LILM: Characters[Char1] ="Lil Mac"
        elif Character1P == DRM: Characters[Char1] ="Dr. Mario"
        elif Character1P == Ike: Characters[Char1] ="Ike"
        elif Character1P == Pikachu: Characters[Char1] ="Pikachu"
        elif Character1P == Bowser: Characters[Char1] ="Bowser"
        elif Character1P == Pichu: Characters[Char1] ="Pichu"
        elif Character1P == Rosalina: Characters[Char1] ="Rosalina"
        elif Character1P == TOONLG: Characters[Char1] ="Toon Link"
        elif Character1P == MarioG: Characters[Char1] ="Mario"
        elif Character1P == LucarioG: Characters[Char1] ="Lucario"
        elif Character1P == LILMG: Characters[Char1] ="Lil Mac"
        elif Character1P == GanondorfG: Characters[Char1] ="Ganondorf"
        elif Character1P == KROOLG: Characters[Char1] ="K Rool"
        elif Character1P == DRMG: Characters[Char1] ="Dr. Mario"
        elif Character1P == DKG and Character1P2 == (208, 208, 208): Characters[Char1] ="Donkey Kong"
        elif Character1P == LuigiG: Characters[Char1] ="Luigi"
        elif Character1P == DededeG: Characters[Char1] ="Dedede"
        elif Character1P == BowserG: Characters[Char1] ="Bowser"
        elif Character1P == RosalinaG: Characters[Char1] ="Rosalina"
        elif Character1P == NessG: Characters[Char1] ="Ness"
        elif Character1P == PikachuG: Characters[Char1] ="Pikachu"
        elif Character1P == Pikachu2: Characters[Char1] ="Pikachu"
        elif Character1P == Bowser2: Characters[Char1] ="Bowser"
        elif Character1P == Ness2: Characters[Char1] ="Ness"
        elif Character1P == Luigi: Characters[Char1] ="Luigi"
        elif Character1P == Lucario2: Characters[Char1] ="Lucario"
        
        else:
            Characters[Char1] = "Unknown"
            with open('Unknown2.txt', 'a') as f:
                #print("Unknown Character found at position ", Char1+1, " with values", Character1P[1], "At", YX, YK, "backup at", Character1P2)
                f.write(str(Character1P[0]))
                f.write(" ")
                f.write(str(Character1P[1]))
                f.write(" ")
                f.write(str(Character1P[2]))
                f.write("\n")
            
        if Characters[Char1] != "Unknown":
            with open('Unknown2.txt', 'a') as f:
                f.write("%s\n" % "0")
            

        
        Char1 +=1
    #print("Player 2 characters:", Characters)    
    with open('Characters2.txt', 'a') as f:
        for items in Characters:
            f.write("%s\n" % items)
    with open('Kills2.txt', 'a') as f:
        for items in Kills:
            f.write("%s\n" % items)
    with open('Played2.txt', 'a') as f:
        for items in Played:
            f.write("%s\n" % items)
    with open('Date2.txt', 'a') as f:
        f.write("%s\n" % local_time)
        f.write("\n")
        f.write("\n")
        f.write("\n")
        f.write("\n")
    
    
    print(Run, "of", Numgames)
    Run += 1
    Kills = [0,0,0,0,0]
    Played = [0,0,0,0,0]
    Characters = ["","","","",""]
    MissingChar = ["","","","",""]
          

