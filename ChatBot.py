name = str(input("What is your name: "))

def greet(name):
  print("Hello, %s!" % name)

greet(name)

fav_number = int(input(f"What is your favorite number, {name}: "))

if fav_number == 10:
  print("Wow, we have the same favorite number!")
else:
  print("Nice, that is unique!")

fav_worldcup_team = str(input("Which team is your favorite world cup team? (arg, por, mor, mex, etc.): "))

if fav_worldcup_team == "arg":
  print("Argentina won the world cup, Congratulations Messi!")
elif fav_worldcup_team == "mor":
  print("I love Morocco, incredible world cup run, first african/arab nation to reach the world cup semifinals!")
elif fav_worldcup_team == "por":
  print("Portugal had a tragic loss to Morocco in the world cup, Sorry Ronaldo!")
else:
  print("Nice, I will be sure to see them next world cup")

fav_sport = str(input("What is your favorite sport? (soccer, basketball, baseball, etc.): "))

if fav_sport == "soccer":
  print("That is my favorite sport! The beautiful game!, also the most popular sport in the world, called Football!")
elif fav_sport == "basketball":
  print("Basketball can be fun sometimes, I don't enjoy it overall")
else:
  print("Nice, I will try the sport next time")

wc_prediction = str(input("What is your prediction for the world cup?: "))

print(f'{wc_prediction} has a chance in the world cup of 2026, but I think morocco will win it all and bring it home. But, will see!')

age = int(input("How old are you?: "))

if age < 18:
  print("You are not an adult yet, use your young ages wisely!")
elif age >= 18:
  print("Your an adult, work hard and achieve your goals!")

print("That is it with ChatBot, Talk to you next time!")