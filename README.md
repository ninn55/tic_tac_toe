# tic_tac_toe

<a href="http://www.wtfpl.net/"><img
       src="http://www.wtfpl.net/wp-content/uploads/2012/12/wtfpl-badge-4.png"
       width="80" height="15" alt="WTFPL" /></a>

This is my attempt to make the tic-tac-toe game in python. And trying to find the perfect solution, i.e. not lose at all, by using a deep learning framework similar to GAN, see also Reference 2.

## Rules

A [Cyber Oculus web page](http://www.cyberoculus.com/tic-tac-toe.asp?Action=Rules) (Copyright 1998-2000) describes Tic-Tac-Toe as follows:

The object of Tic Tac Toe is to get three in a row. You play on a three by three game board. The first player is known as X and the second is O. Players alternate placing Xs and Os on the game board until either opponent has three in a row or all nine squares are filled. X always goes first, and in the event that no one has three in a row, the stalemate is called a cat game.

In order to run the two players game. Go in any console, and run following code.

```bash
git clone https://github.com/ninn55/tic_tac_toe
pip install -r requirments.txt
cd game
python play_core.py
```

## Enumeration

The enumeration method is used to get all possible move and result in the game. Result can be found in
`assets/result.csv` and `assets/result.xlsx`. The summery are:

|layer|first player win|second player win|total|
|-----|----------------|-----------------|-----|
|5|1440|0|1440|
|6|0|5328|5328|
|7|47952|0|47952|
|8|0|72576|72576|
|9|81792|0|81792|

|total|first player win|second player win|Tie|
|-----|----------------|-----------------|---|
|255168|131184|77904|46080|

The rerult is same as [This website](http://www.se16.info/hgb/tictactoe.htm).

The code is in `./methods`. Run following code in console to get the results yourself.

```bash
git clone https://github.com/ninn55/tic_tac_toe
pip install -r requirments.txt
cd methods
python Enumerat.py
```


## References

1. [Cyber Oculus web page](http://www.cyberoculus.com/tic-tac-toe.asp?Action=Rules)

1. [[1406.2661] Generative Adversarial Networks](https://arxiv.org/abs/1406.2661)

1. [python - How to import .py file from another directory? - Stack Overflow](https://stackoverflow.com/questions/22955684/how-to-import-py-file-from-another-directory/22955743)

1. [How many Tic-Tac-Toe (noughts and crosses) games?](http://www.se16.info/hgb/tictactoe.htm)