# Hrito's IPND Stage 2 Project

# Quiz text

paragraph = """
The American Civil War was an [___1___] conflict fought
in the United States from [___2___] to [___3___].
The [___4___] faced secessionists in [___5___] Southern states
grouped together as the [___6___] States of America.
The Union won the war, which remains the bloodiest in U.S. history.
"""

paragraph2 = """
Christopher Columbus discovered America in [___1___].
Columbus led his three ships - the [___2___], the [___3___] and the [___4___]
out of the [___5___] port of Palos on August 3, 1492.
His objective was to sail west until he reached [___6___]
where the riches of gold, pearls and spice awaited.
"""

paragraph3 = """
The Normandy landings codenamed Operation [___1___] were the landing operations
on Tuesday, 6 June [___2___] termed [___3___] of the Allied invasion of Normandy
in Operation [___4___] during World War II. The largest [___5___] invasion in history,
the operation began the liberation of German-occupied [___6___] Europe
from Nazi control, and contributed to the Allied victory on the Western Front.
"""

paragraph4 = """
Attila, frequently referred to as [___1___], was the ruler of the Huns
from [___2___] until his death in March [___3___]. Attila was a leader of the Hunnic Empire,
a [___4___] confederation consisting of Huns, Ostrogoths, and Alans among others,
on the territory of Central and Eastern Europe. During his reign, he was one of the
most [___5___] enemies of the Western and Eastern Roman Empires. He crossed the Danube twice
and plundered the Balkans, but was unable to take [___6___].
"""

paragraph5 = """
Easter Island, a [___1___] territory, is a remote [___2___] island in Polynesia.
Its native name is Rapa Nui. It is famed for [___3___] sites,
including nearly [___4___] monumental statues called moai, created by inhabitants during the 13th to 16th centuries.
The moai are carved human figures with oversize [___5___], often resting on massive stone pedestals called [___6___].
Ahu Tongariki has the largest group of upright moai.
"""

paragraphs = [paragraph, paragraph2, paragraph3, paragraph4, paragraph5]

blanks  = ["[___1___]", "[___2___]", "[___3___]", "[___4___]", "[___5___]", "[___6___]"]

# Quiz text answers

answers = ["internal", "1861", "1865", "Union", "11", "Confederate"]
answers2 = ["1492", "Nina", "Pinta", "Santa Maria", "Spanish", "Asia"]
answers3 = ["Neptune", "1944", "D-Day", "Overlord", "seaborne", "northwestern"]
answers4 = ["Attila the Hun", "434", "453", "tribal", "feared", "Constantinople"]
answers5 = ["Chilean", "volcanic", "archaeological", "900", "heads", "ahus"]

answersn = [answers, answers2, answers3, answers4, answers5]

# Startup welcome menu

print  "\n###################################"
print  "#Welcome to Hristo's history quiz!#"
print  "###################################\n"

print  "-------------------------------------"

print "\n######################################"
print "#Fill in the missing words quiz game.#"
print "######################################\n"

# guesses function asks user to enter number of guesses and checks if the input is right (number)

def guesses():
  tries = raw_input("\nPlease input the number of guesses you would like to have for each question: ")
  while True:
    if tries.isdigit():
      return tries
    else:
      tries = raw_input("\nPlease enter a valid number: ")

# Checking if blanks is substring of word(ml_string).

def word_in_pos(word, blanks):
    for pos in blanks:
        if pos in word:
            return pos
    return None

# Main game function choosing number of guesses, checking if answer is right or wrong,
# displaying a message for the current condition and the text with the right answer.

def play_game(ml_string, blanks, difficulty):
  # declaring variables
  lives = guesses(); i = 0; replaced = []

  # printing the quiz text based on the difficulty referred from launch_game function.
  print paragraphs[difficulty]

  # converting quiz text from string to list.
  ml_string = ml_string.split()

  # calling the word_in_pos function and checking if blanks is substring of word.
  for word in ml_string:
    replacement = word_in_pos(word, blanks)

    # if the word_in_pos function returns different than None we execute if statement
    # which asks us to enter the answer for the current blank space, for example: [___1___].
    if replacement != None:
      answer = raw_input("\nType in the answer for " + blanks[i] + ": ")

      # while the answer is wrong the program decrements lives for each wrong input,
      # where lives are referred from the guesses function and keeps the loop going
      # while the user inputs a correct answer or the user is down to 0 lives left, which returns Game Over and ends the game.
      while answer != answersn[difficulty][i]:
          lives = int(lives) - 1
          if lives == 0: return "\nGame Over"
          answer = raw_input("\nWrong answer, you have " + str(lives) + " guessing(s), try again " + blanks[i] + ": ")

      # if the answer is correct, Correct message appears and the quiz text printed
      # with the added right answer in the current blank space plus incrementing the i because of the right answer.
      print "\nCorrect, good job!\n"; paragraphs[difficulty] =paragraphs[difficulty].replace(blanks[i], answer)
      print paragraphs[difficulty]
      word = word.replace(replacement, answer); replaced.append(word); i += 1

    # replacing the word if it does not match one of the blanks.
    else:
      replaced.append(word)

  # converting the whole new list with new blanks (answers) into a string again
  replaced = " ".join(replaced)
  return replaced

# Choosing difficulty(checking if the difficulty input is right) and calling the main function play_game.

def launch_game():
  # declaring the difficulties list.
  difficulties = ["easy", "normal", "hard", "advanced", "expert"]

  # Asking the user to choose a difficulty and checking if the user input for
  # difficulty is right, if the user input is not right, the user is asked to
  # enter a valid difficulty, the lower() operator makes sure all the input is converted into
  # lower case characters for avoiding errors.
  while True:
    choice = raw_input("\nChoose your difficulty: Easy - Normal - Hard - Advanced - Expert ")
    choice = choice.lower()
    if choice not in ("easy", "normal", "hard", "advanced", "expert"):
      print "\nPlease choose a valid difficulty:"
      continue

    # if the input is right, the user gets a print with the current difficulty
    # and the main function play_game is called to play the quiz game.
    else:
      index = difficulties.index(choice)
      print "\nYou've chosen " + choice + " difficulty, good luck!"
      print play_game(paragraphs[index], blanks, index)
      break

launch_game()
