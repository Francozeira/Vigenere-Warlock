# Vigenère-Warlock

Vigenere-Warlock is a small (my first) python script to break a given Vigenère [Wiki](https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher) ciphered paragraph, also, this is my first really made readme (:shipit:). This might have some ~~a lot~~ of  less performatic or  out of good manners of python, but this is how i found out to implement the code to use it on the competition. Some of the code characteristics are due to the college competion rules wich this script was designed to work on. :bowtie:

**College competition rules**

- On each round of the competition, the teams would exchange a whole paragraph wich was suposed to be ciphered using the Vigenère cipher;
- The paragraph to be sent must be the "Abstract" section of an IT or technology related article or paper (our teacher defined this rule so that our latin characters weren't present - as the abstract must be in english, thus there is no need to treat this kind of characters in this code);
- The key used to decrypt the message must be a 3 letter portugue-brazilian word (non-initial, acronym, and so);
> Eg: lua, ovo, jaz, paz

**Code description**

- Note the usage of colorama to print the output on the Windows terminal, pretty fancy huh?;
- On next lines, under the *DECIPHERING FUNCTIONS* you have the heavy work of translation made with functions;
- Next you have the *TEST VARIABLES* , this variables contain ciphered paragraphs that are used to test the code;
- * VERIFICATION VARIABLES *, this section is what defines what the script will search for and the word lists used in decryption verification:
- *extendedPossibleKeys* : extended list of words that could be used as a key for Vigenère decryption, remembering that these are all portuguese words, composed of 3 letters;

	- *allPossibleKeys* : expanded list of words that could be used as a key for Vigenère decryption, despite not being exactly in accordance with the rules, so,  we will only use this list if * extendedPossibleKeys * does not find satisfactory results;

	- *securityWords* : after performing the decryption with all the words provided by *extendedPossibleKeys * or * allPossibleKeys *, the script will look for this list of words in all the results obtained, as they are words referring to information security, hardly a positive result here would not be a correct deciphering, so if the script finds a word like this in the list, the result will be printed in the terminal in green;

	- *commonWords* : if the search for * securityWords * does not return any positive results, all results will be searched again, now through this list of the most common words in the English language, but as they are most common words, a positive return here may be just a coincidence, not necessarily a successful deciphering, the result will be printed on the terminal in yellow;

- *CIPHERED TEXTS USED IN THE COMPETITIONS* and *FINALS* : these are the paragraphs we received during the competition and the final, respectively. I specifically saved it to record how an average college student can not understand simple rules and descriptions given by the teacher, if you use them, you will see that most do not meet the rules of the competition;

- *receivedCipher* : this variable receives the value of any variable you want, I use it for convenience, to assign value more easily and quickly;

- The rest of the code defines the use of the functions and variables listed above;


**Funcionamento do código**



**TL;DR:** Just change the * receivedCipher * variable to what you want to decipher, and the * extendedPossibleKeys * variables to change the possible keys and * securityWords * to change the words you want to check if they are present in the text deciphered.