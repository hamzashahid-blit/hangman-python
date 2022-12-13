# A simple Hangman made in Python
There could be many improvements, especially to the wordlist.txt

Here is the "gameplay" upon running `python hangman.py` in the terminal:

```
_ _ _ _ _ _ _ _

Please enter a letter: s

Your letter is not in the word.
Failed Attempts: 1/6
_ _ _ _ _ _ _ _ 
Letters Found: 
Incorrect Letters: s

Please enter a letter: s
You have already attempted this letter.
Please enter a letter: a

You found a letter!
_ a _ _ _ _ _ _ 
Letters Found: a
Incorrect Letters: s

Please enter a letter: e

You found a letter!
_ a _ _ e _ e _ 
Letters Found: a, e
Incorrect Letters: s

Please enter a letter: i

You found a letter!
_ a i _ e _ e _ 
Letters Found: a, e, i
Incorrect Letters: s

Please enter a letter: o

Your letter is not in the word.
Failed Attempts: 2/6
_ a i _ e _ e _ 
Letters Found: a, e, i
Incorrect Letters: s, o

Please enter a letter: b

Your letter is not in the word.
Failed Attempts: 3/6
_ a i _ e _ e _ 
Letters Found: a, e, i
Incorrect Letters: s, o, b

Please enter a letter: whatever
Invalid input, please try again: w  

Your letter is not in the word.
Failed Attempts: 4/6
_ a i _ e _ e _ 
Letters Found: a, e, i
Incorrect Letters: s, o, b, w

Please enter a letter: l

Your letter is not in the word.
Failed Attempts: 5/6
_ a i _ e _ e _ 
Letters Found: a, e, i
Incorrect Letters: s, o, b, w, l

Please enter a letter: m

Your letter is not in the word.
Failed Attempts: 6/6
_ a i _ e _ e _ 
Letters Found: a, e, i
Incorrect Letters: s, o, b, w, l, m

The game has ended.
You Lost!
 ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  \
| |          ||  `/,|
| |          (\\`_.'
| |         .-`--'.
| |        /Y . . Y\
| |       // |   | \\
| |      //  | . |  \\
| |     ')   |   |   (`
| |          ||'||
| |          || ||
| |          || ||
| |          || ||
| |         / | | \
""""""""""|_`-' `-' |"""|
|"|"""""""\ \       '"|"|
| |        \ \        | |
: :         \ \       : :
. .          `'       . .

Failed Attempts: 6 / 6
The word was 'daikered'
Better luck next time!
```
