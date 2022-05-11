import datetime

def game():
    
 n = input("What do you want to do? Attack(1)|Heal(2): ")

 if n == "1":
    print("Ok, you are attacking the monster.")
    num2()
    health = 100
    monster_health = 93

 if n == "2":
    print("You already have full health!")
    health = 100

def num2():
    n2 = input("Ok, now its monsters turn(press enter)!")
    if n2 == "":
        num3()
        health = 93

def num3():
    n3 = input("Monster is attacking you. what do you want to do? Defend(1)|Attack_back(2)|Hide(3): ")

    if n3 == "1":
        print("Ok you are defending! your health is 97 monsters health is 92")
        health = 92
        monster_health = 93

    if n3 == "2":
        health = 91
        monster_health = 87
        print(f"Ok you are attacking back! Your health is {health} monsters health is {monster_health}")

    if n3 == "3":
        print("Ok you are running and hiding, be qiet!")

def num4():
    n4 = input("Monster got very angry now, His seeking for you! Now's your chance, you can attack the monster while it cant see you! Attack(1)|Keep_hiding(2)|Heal(3)")

    if n4 == "1":
        print(f"")

    if n4 == "2":
        print(f"")

    if n4 == "3":
        print(f"")

def num5():
    n5 = input("Your turn again. Attack(1)|Heal(2)|Hide(3): ")
    health = 91
    monster_health = 87

    if n5 == "1":
        print("Monster got a huge punch there! He's running away to get some more health")
        datetime.sleep(1)
        print(f"Now your health is at {health}, monsters health is at {monster_health}")
    
    if n5 == "2":
        print(f"Ok lets heal, now your health is at {health}")
    
    
    if n5 == "3":
        print(f"That hurted much! Now is your health {health} and monsters health is at {monster_health}!")
        datetime.sleep(5)
        print("d")