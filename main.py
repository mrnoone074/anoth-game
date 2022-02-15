n = input("what do you want to do? (1)Attack|Heal(2): ")

if n == "1":
    print("ok you are attacking the monster.")

if n == "2":
    print("you have already full health")

n2 = input("Ok, now its monsters turn(press enter)!")

n1 = input("monster is attacking you. what do you want to do? (1)Defend|Attack_back(2)|Hide(3): ")

if n1 == "1":
    print("Ok you are defending! your health is 97 monsters health is 92")

if n1 == "2":
    print("Ok you are attacking back! Your health is 95 monsters health is 87")

if n1 == "3":
    print("Ok you are running and hiding, be qiet!")

n3 = input("Your turn again. (1)Attack|Heal(2)|Hide(3): ")

if n3 == "1":
    print("Monster got a huge punch there!")

if n3 == "2":
    print("Ok lets heal, now your health is at 100")

if n3 == "3":
    print("Monster got very angry now!")