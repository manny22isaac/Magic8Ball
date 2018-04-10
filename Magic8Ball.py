import sys
import random

while True:          
          
          name = input('What is your name? ')
          print('Welcome '+ name +'! Welcome to Magic 8-ball. What is it that you desire to know?')
          question = input()
          if question == ('X'):
                    print('Good Bye!')
                    sys.exit()
          if name == 'X':
                    print('Good Bye!')
                    sys.exit()
                    break
          
          answers = ["It is certain", \
          "It is decidedly so " + name,\
          "Without a doubt", \
          "Yes " + name + " definitely", \
          "You may rely on it", \
          "As I see it yes", \
          "Most likely", \
          "Outlook good", \
          "Yes", \
          "Signs point to yes", \
          "Reply hazy try again", \
          "Ask again later", \
          "Better not tell you now", \
          "Cannot predict now", \
          "Concentrate and ask again", \
          "Don't count on it", \
          "My reply is no", \
          "My sources say no", \
          "Outlook not so good", \
          "Very doubtful"]
          print(answers[random.randint(0, len(answers))-1])
          print('Enter your name to try again. Otherwise, enter X to end the program.')
          continue




