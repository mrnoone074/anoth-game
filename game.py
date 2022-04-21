def game():
    
 n = input("what do you want to do? Attack(1)|Heal(2): ")

 if n == "1":
    print("ok you are attacking the monster.")

 if n == "2":
    print("You already have full health!")

 n2 = input("Ok, now its monsters turn(press any key)!")
if n2 != "":
    n1()

 n1 = input("Monster is attacking you. what do you want to do? Defend(1)|Attack_back(2)|Hide(3): ")

 if n1 == "1":
    print("Ok you are defending! your health is 97 monsters health is 92")

 if n1 == "2":
    print("Ok you are attacking back! Your health is 93 monsters health is 87")

 if n1 == "3":
    print("Ok you are running and hiding, be qiet! Monster got very angry now, His seeking for you! Now's your chance, you can attack the monster while it cant see you! Attack(1)|Keep_hiding(2)|Heal(3)")

 n3 = input("Your turn again. Attack(1)|Heal(2)|Hide(3): ")

 if n3 == "1":
    print("Monster got a huge punch there! His running away to get some more health")

 if n3 == "2":
    print("Ok lets heal, now your health is at 100")


 if n3 == "3":
    h = input("")

 if h == "1":
     print("That hurted much! Now is your health 93 and monsters health is at 86!")