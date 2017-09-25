#!usr/bin/python
import re
import urllib.request
from lxml import html
import os
from pprint import pprint
class hangman:
  __username    = 'Joe Schmo'
  __num_players = 1
  __game_word   = ''
  __num_guesses = 10
  __guessed_word = []
  def __init__(self, username, num_players):
    #do stuff
    self.__username = username
    self.__num_players - num_players
    self.__game_word  = self.__get_word()
    self.__guessed_word = ["_"] * len(self.__game_word)
    self.play()

  def play(self):
    self.refresh()
    self.build_game_board()
    self.take_turn()
    if self.__num_guesses > 0 and ''.join(self.__guessed_word) != self.__game_word:
      self.play()
    else:
      self.end_game()

  def take_turn(self):

    while True:
      userInput = input('Guess a letter:')
      if len(userInput) == 1:
        break
      print('Please enter only one character')
    letter_guess = userInput.lower()
    pprint(letter_guess)
    found = False
    for pos, char in enumerate(self.__game_word):

      if char == letter_guess:
        self.__guessed_word[pos] = letter_guess
        found = True
    if found==False:
      self.__num_guesses = self.__num_guesses - 1

  def build_game_board(self):

    print("You have " + str(self.__num_guesses) + " tries remaining.")
    pprint(''.join(self.__guessed_word))

  def refresh(self):
    os.system('cls' if os.name == 'nt' else 'clear')

  def end_game(self):
    if ''.join(self.__guessed_word) == self.__game_word:
      alive_guy= """
                (^ ^)
                  |
                 \ /
                  |
                 / \\
                ————— """
      print("Congrats!"+self.__username+" You won!\n "+ alive_guy)

    else:
      dead_guy = """
_________
|      |
|    (x x)
|      |
|     / \\
|      |
|     / \\
|_______
"""
      print("You lose. The word was "+ self.__game_word+" Try again.\n"+dead_guy)

  def __get_word(self):
    site = 'http://setgetgo.com/randomword/get.php'
    word = 'pooface'
    with urllib.request.urlopen(site) as response:
      html = response.read()
    word = html.decode("utf-8")
    return word
username = input("Welcome to the hangman game.\n Please enter your name:")

hangman(username, 1) #todo add second player
