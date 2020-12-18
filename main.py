#import Classes and define quiz1 as an empty quiz as a placeholder
from Class import Question
from Class import Quiz
quiz1 = Quiz("Nothing here...", "Try creating a quiz!")

def main():
  # Program Variables
  
  # Main Program Loop
  loop = True
  while loop:
    selection = getMenuSelection()

    if selection == "1":
      create_quiz()
    elif selection == "2":
      take_current_quiz()
    elif selection == "3":
      save_quiz()
    elif selection == "4":
      select_quiz()
    elif selection == "5":
      remove_quiz()
    elif selection == "6":
      view_list()
    elif selection == "7":
      print("Exit")
      loop = False

  print("Goodbye")
# end main()

def getMenuSelection():
  print("\nMAIN MENU")
  print("1: Create/edit a quiz")
  print("2: Take your current quiz")
  print("3: Save current quiz")
  print("4: Select a different quiz to work on / do")
  print("5: Delete an existing quiz")
  print("6: View the list of quizes")
  print("7: Exit")
  return input("Enter menu selection:")

def create_quiz():
  #get user input
  quiz_title = input("What is the title of your quiz: ")
  quiz_description = input("Give a description for your quiz: ")
  quiz_number = int(input("How many questions: "))
  
  #make quiz1 a global variable and define it
  global quiz1
  quiz1 = Quiz(quiz_title, quiz_description) 
  for i in range(quiz_number):
    quiz1.add_question()
  
# Take quiz-----------------------------------------------------------------------------------------------------------------------

def take_current_quiz():
  quiz1.take_quiz()

# Save quiz-----------------------------------------------------------------------------------------------------------------------


def save_quiz():

  #create a file_out string to add to a file
  file_out = quiz1.title + "\n" + quiz1.description + "\n" 
  for prompt in quiz1.questions:
    file_out += prompt.question + ";;" + prompt.answer + "\n"
    

  
  #create new text file for new quiz, or update quiz if the name already exists
  quiz_storage = open(quiz1.title + ".txt", "w")

  quiz_storage.write(file_out)
  
  quiz_storage.close()

  #save the quiz names to a new document

  quiz_names = open("quiz_list.txt", "r")

  names = quiz_names.readlines()

  quiz_names.close()

  
  quiz_names = open("quiz_list.txt", "a")

  for lines in names:
    if quiz1.title + ".txt\n" == lines:
      found = True
    else:
      found = False
      
  if found == True:
    print("Quiz with that name has been updated")
  elif found == False:
    quiz_names.write(quiz1.title + ".txt\n")
    print("New quiz named " + quiz1.title + " has been created.")

  quiz_names.close()

  
  
# Select quiz-----------------------------------------------------------------------------------------------------------------------------------------------


def select_quiz():
  #take user input
  quiz_selection = input("please type the title of the quiz you wish to edit or take: ")

  selected_quiz = open(quiz_selection + ".txt", "r")

  lines = selected_quiz.readlines()
  
  global quiz1
  quiz1 = Quiz(lines[0], lines[1]) 

  for i in range(2, len(lines)):
    lines[i] = lines[i].strip()
    ques_data = lines[i].split(";;")
    quiz1.questions.append(Question(ques_data[0], ques_data[1]))
  
  
 

  selected_quiz.close

# remove quiz-------------------------------------------------------------------------------------------------------------------------------------------------


def remove_quiz():
  #delete the quiz file
  choice = input("type the title of the quiz you wish to delete: ")
  import os
  if os.path.exists(choice + ".txt"):
    os.remove(choice + ".txt")
  else:
    print("The quiz does not exist")


  #remove from quiz_list
    #make a quiz names list
  quiz_names = open("quiz_list.txt", "r")

  names = quiz_names.readlines()

  quiz_names.close()

  #clear the quiz_list file
  quiz_names = open("quiz_list.txt", "w")

  quiz_names.write("")

  quiz_names.close()

  #open the quiz_list with the ability to write and write in all lines that dont match the name of the deleted quiz
  quiz_names = open("quiz_list.txt", "a")

  for lines in names:
    #print(lines)
    if choice + ".txt\n" == lines:
      pass
    else:
      quiz_names.write(lines)
      
    
  quiz_names.close()

  # View Quizes-------------------------------------------------------------------------------------------------------------------


def view_list():
  print("\nnow viewing the list of quizes")
  quiz_list_names = open("quiz_list.txt", "r")

  names = quiz_list_names.readlines()
  for i in range(len(names)):
    names[i] = names[i].strip()
    split_name = names[i].split(".")
    print(split_name[0])

  

main()
