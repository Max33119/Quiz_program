

class Question:
  #constructor
  def __init__(self, question, answer):
    self.question = question
    self.answer = answer

  #methods
  def print_question(self):
    print(self.question)

  def check_answer(self, user_answer):
    return self.answer == user_answer

  def try_question(self):
    print(self.question)
    if input("please input the answer to the question: ") == self.answer:
      print("correct")
    else:
      print("incorrect")
      

  
    
class Quiz:
  #constructor
  def __init__(self, title, description):
    self.title = title
    self.description = description
    self.questions = []
    self.correct = 0
    self.wrong = 0
  
  #methods
  def add_question(self):
    question = input("what is the question you wish to add: ")
    answer = input("what is the answer to the question: ")
    self.questions.append(Question(question, answer))
   

  def print_quiz(self):
    print(self.title)
    print(self.description)
    for question in self.questions:
      question.print_question()

  def take_quiz(self):
    print("")
    print(self.title)
    print(self.description)
    self.correct = 0
    self.wrong = 0
    for prompt in self.questions:
      ans = input(prompt.question + ": ") 
      if prompt.check_answer(ans):
        print("correct")
        self.correct += 1
      else:
        print("wrong")
        self.wrong += 1
      
    print("you got " + str(self.wrong) + " wrong and " + str(self.correct) + " correct.")
      
      
      
    

  





