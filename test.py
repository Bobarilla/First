import random

print("Welcome to AdvTxt")

randomint = 0
hp = 500
weapon_power = 1
gold = 10
tilecount = 0
occurance = 0
game_on = 1
monsterpwr = 1
monsterhp = 1

#fight function
def monster(monsterpwr, monsterhp):
    global hp, game_on, gold
    ("---------------Monster tile-----------------")
    monsterhp=random.randint(1,((int(tilecount))*2))
    monsterpwr=random.randint(1,((int(tilecount))*5+1))
    print("A " + str(monsterpwr) + "/"  + str(monsterhp) + " monster has appeared")
    while monsterhp > 0: 
        x = input("Attack [1], Run [2], Cower [3]:  ")
        if x=="1":
            monsterhp=monsterhp-weapon_power
            hp=hp-monsterpwr
            if monsterhp <= 0 and hp <= 0:
                print("You attacked the monster and succesfully killed it, but were killed in the process")
            elif monsterhp <= 0:
                reward=random.randint(1,int(monsterpwr))
                gold= gold + reward
                print("You killed the monster!")
                print("Your hp is now " + str(hp) + " and you gained " + str(reward) + " gold. You now have " + str(gold) +" gold.")
            else:
                print("Monster Hp: " + str(monsterhp))
                print("Your HP:" + str(hp))
        elif x=="2":
            runchance=random.randint(1,5)
            if runchance==1 or runchance==2:
                print("You successfully ran away")
                monsterhp=0
            elif runchance==3 or runchance==4 or runchance==5:
                print ("you cannot run away, you fight")
                hp=hp-monsterpwr
                monsterhp=monsterhp-weapon_power
                if monsterhp <= 0 and hp <= 0:
                    print("You attacked the monster and succesfully killed it, but were killed in the process")
                    game_on=0
                elif monsterhp <= 0:
                    print("You killed the monster!")
                    print("Your hp is now " + str(hp))
                else:
                    print("Monster Hp: " + str(monsterhp))
                    print("Your HP:" + str(hp))
            else:
                print("ran an else for monster")
        elif x=="3":
            print("You cowered and you died, Game over.")
            game_on=0
            break
        else:
            print("Choose one")

#item function
def items():
    global weapon_power, gold
    print("---------------Item tile-----------------")
    item_drop=random.randint(1,100)
    if item_drop<20:
        temp_weapon_power=weapon_power+random.randint(5,(int(tilecount)+5))
        print("You found a sword with " + str(temp_weapon_power) + " attack, take it? (Current weapon is: " + str(weapon_power) + ")")
        while True:
            x=input("Y[1]/N[2]  ")
            if x=="Y" or "1":
                print("You pick up the new weapon")
                weapon_power=temp_weapon_power
                break
            elif x=="N" or "2":
                print("You leave the sword behind")
                break
            else:
                print("reply Y or N")
                break
        
    elif item_drop>=20 and item_drop<=90:
        temp_weapon_power=weapon_power+random.randint(0,(int(tilecount)+1))
        print("You found a pointy stick with " +str(temp_weapon_power)+ " attack, take it? (Current weapon is: " + str(weapon_power) + ")")
        while True:
            x=input("Y[1]/N[2]  ")
            if x=="Y" or "1":
                print("You pick up the new weapon")
                weapon_power=temp_weapon_power
                break
            elif x=="N" or "2":
                print("You leave the stick behind")
                break
            else:
                print("reply Y or N")
                break
    elif item_drop>=90:
            gold+=20
            print("Found 20 gold, you now have " + str(gold) + " gold")
    else:
            print("ran an else for items")
        #--------------------Game code---------------------
        
while game_on==1:
    
    tilecount=tilecount+1
    #turn
    
    
    #occurances
    occurance=random.randint(0,100)
    print("You have gone " + str(tilecount) + " tiles!")
    if occurance<=50:
          monster(monsterpwr, monsterhp)
    elif occurance>50 and occurance<95:
          items()
    elif occurance>=95:
        print("Found a shop! You can buy stuff. Cause thats what shops do.")
        buy=input("Type the #id of the item you want to buy and 0 to exit: #1 Heath Potion - Gain 20 health [20], #2 Keychain [80]")
        if buy=="#1" or "1":
            print("Bought Health Potion for 20 gold. Your hp is now " +str(hp)+ " and you have " +str(gold)+ " gold.")
            gold-=20
            hp+=20
        elif buy=="#2" or "2":
            print("Bought a useless keychain like a dumb toursit. You have " +str(gold)+ " gold")
            gold-=80
        elif buy==0:
            print("have a nice day")
        else:
            print()
    else:
        print("ran an else for items")
   
    #check for death
    if hp<=0:
        print("Your health has fallen to zero, you have died. Game Over")
        game_on=0

while game_on==0:
    break
