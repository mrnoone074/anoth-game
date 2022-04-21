from game import game
from rules import rules

m = input("Hi! Wonna play a game? Yes(1)|No(2): ")

if m == "2":
    print("Ok? Soooooooooo go away then!")

if m == "1":
    g = input("Wanna read the rules first or start? Start(1)|Rules(2): ")

if g == "1":
    game()

if g == "2":
    rules()