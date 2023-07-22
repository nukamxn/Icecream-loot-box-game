import random
restartamount = 0
restartcoins = 1
pets = []
coins = 100
points = 0
rarity = 0
P_rarity = 0
boxbought = 0
highscore = 0
petmulti = 1
r1 = 10
r2 = 25
r3 = 100
r4 = 250
r5 = 500
print("""
icecream box opening game
type x to open icecream box for 10 coins
type pet you want to buy to buy it

""")
while coins != 0:
    if coins >= 10:
        boxBought = input("buy box? ")
        if boxBought == "x":
            coins -= 10
            rarity = random.randint(1, 5)
            if rarity == 5:
                print(f"""
     Normal icecream
     +{r1} points and coins
     :)
                """)
                points += r1 * petmulti * restartcoins
                coins += r1 * petmulti * restartcoins
                print(f"points - {points}")
                print(f"coins - {coins}")
                print(f"pets - {pets}")
            elif rarity == 4:
                print(f"""
    Double scoop icecream
    +{r2} points and coins
     :)
                """)
                points += r2 * petmulti * restartcoins
                coins += r2 * petmulti * restartcoins
                print(f"points - {points}")
                print(f"coins - {coins}")
                print(f"pets - {pets}")
            elif rarity == 3:
                print(f"""
    Rainbow icecream!
     +{r3} points and coins
    :)
                """)
                points += r3 * petmulti * restartcoins
                coins += r3 * petmulti * restartcoins
                print(f"points - {points}")
                print(f"coins - {coins}")
                print(f"pets - {pets}")
            elif rarity == 2:
                print(f"""
    Double rainbow icecream!
     +{r4} points and coins
     :)
                """)
                points += r4 * petmulti * restartcoins
                coins += r4 * petmulti * restartcoins
                print(f"points - {points}")
                print(f"coins - {coins}")
                print(f"pets - {pets}")
            elif rarity == 1:
                print(f"""
     Double rainbow icecream with flake!
    +{r5} points and coins
     :)
                    """)
                points += r5 * petmulti * restartcoins
                coins += r5 * petmulti * restartcoins
                print(f"points - {points}")
                print(f"coins - {coins}")
                print(f"pets - {pets}")
        elif boxBought == "dog" and coins > 250:
            coins -= 250
            print("""
            You bought a dog
            +1 rewards from boxes
            :)
            """)
            pets.append("dog")
            petmulti += 1
            print(f"points - {points}")
            print(f"coins - {coins}")
            print(f"pets - {pets}")
        elif boxBought == "cat" and coins > 2500:
            coins -= 2500
            print("""
                You bought a cat
                +10 rewards from boxes
                :)
                """)
            pets.append("cat")
            petmulti += 10
            print(f"points - {points}")
            print(f"coins - {coins}")
            print(f"pets - {pets}")
        elif boxBought == "monster" and coins > 25000:
            coins -= 25000
            print("""
            You bought a monster
            +100 rewards from boxes
            :)
            """)
            pets.append("monster")
            petmulti += 100
            print(f"points - {points}")
            print(f"coins - {coins}")
            print(f"pets - {pets}")
        elif boxBought == "king" and coins > 250000:
            coins -= 250000
            print("""
            You bought a king
            +1000 rewards from boxes
            :)
            """)
            pets.append("king")
            petmulti += 1000
            print(f"points - {points}")
            print(f"coins - {coins}")
            print(f"pets - {pets}")
        elif boxBought == "dragon" and coins > 25000000:
            coins -= 25000000
            print("""
                 You bought a dragon
                 +1000000 rewards from boxes
                 :)
                 """)
            pets.append("dragon")
            petmulti += 1000000
            print(f"points - {points}")
            print(f"coins - {coins}")
            print(f"pets - {pets}")
        elif boxBought == "debug":
            points = 238569238659082635098672305986230958672390856029385679023856790823567908237659082367590
        elif boxBought == "restart":
            restartamount = points / 100000
            print(f"you will get {restartamount} restart coins")
            restartanswer = input("are you sure you want to? ")
            if restartanswer == "yes":
                restartcoins = restartcoins * restartamount
                print(f"restart coins - {restartcoins}")
                restartamount = 0
                points = 0
                coins = 100
                petmulti = 1
                pets.clear()
        elif boxBought == "delete":
            restartamount = 0
            restartcoins = 1
            points = 0
            coins = 100
            petmulti = 1
            pets.clear()
