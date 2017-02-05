import random;
import sys;
import string

HANGMANPICS = ['''

	   +---+

	   |   |

	       |

	       |

	       |

	       |
	 =========''', '''


	   +---+

	   |   |

	   O   |

	       |

	       |

	       |

	 =========''', '''



	   +---+

	   |   |

	   O   |

	   |   |

	       |

	       |

	 =========''', '''


	   +---+

	   |   |

	   O   |

	  /|   |

	       |

	       |

	 =========''', '''


	   +---+

	   |   |

	   O   |

	  /|\  |

	       |

	       |

	 =========''', '''


	   +---+

	   |   |

	   O   |

	  /|\  |

 	  /    |

 	       |

	 =========''', '''

	   +---+

	   |   |

	   O   |

 	  /|\  |

	  / \  |

	       |
	=========''']

def playagain():
	print '\n\nWould you like to play again??  Y/N'
	play = raw_input(':')
	if(play == 'Y'):
		main()
	else:
		sys.exit()

def display(correctguess,word,hangmanindex):
	wordsofar = []
	if hangmanindex>-1:
		print HANGMANPICS[hangmanindex]
	for char in word:
		if char in correctguess:
			print char,
			wordsofar.append(char)
		else:
			print '_',
	if hangmanindex==6:
		print '\n\nGame over'
		playagain()
	if len(wordsofar) == len(word):
		print '\n\nCongratulations!!! You won'
		playagain()


def startgame(word):
	word = word.lower();
	print word
	uniqlength = len(set(word))
	length = len(word)
	print "Guess the word"
	for i in range(0,length-1):
		print '_',
	correctguess = []
	start = 0
	hangmanindex = -1;
	turnsleft = 0;
	while(turnsleft<=6):
		userInput = raw_input(':')
		if userInput in word and userInput not in correctguess:
			print "Your guess is correct"
			correctguess.append(userInput)
			display(correctguess,word,hangmanindex);
		else:
			print "Your guess is incorrect"
			hangmanindex = hangmanindex+1
			turnsleft = turnsleft+1
			display(correctguess,word,hangmanindex)
		start = start+1;


def main():
	data = [line.strip() for line in open("Dictionary.txt", 'r')]
	index = random.randint(0,63);
	hangmanpics = [];
	startgame(data[index]);



if __name__ == "__main__":
	main();
