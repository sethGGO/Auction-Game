# CS404 Agent Based

# Systems :

# Auction Games


Seth Odia
### INTRODUCTION

In this project, two different strategies need
to be made against two different auctions.
In both auctions, there are four types of
paintings from different painters that
correlate to a given value for each painter.

There are some common assumptions, each
game is finite game against other
participants and therefore has an end, each
agent move is dependant on the moves it
played previously such as which players
have won which paintings and how much
money every player has left. The
knowledge all agents have is the type of
auction, the budget left to everyone, the
items sold to each agent and for how much
it was gotten for, whether the bid winner
pays amount or second highest, the amount
of items available and the order of the
items.

The item importance differs for each player
at different rounds, as they are affected by
their budget and that of the other agents. A
strategy is then gotten using what a player
already knows as well as estimates from
what is not entirely known. Brute force is
not advised as it would be difficult or
impossible to solve the game using such
methods. Also, winning has the best
valuation followed by a draw and then a
loss which has a negative valuation.

### COLLECTION GAME

The aim of this game is to be the first agent
to have a certain collection of paintings
from the auction. In this auction, the
collection is set to [4,2] meaning that to
win the auction you have to be the first
person to have four paintings of one artist
and two of another artist.
Because every agent has the same budget, it
can be difficult to perform better than
another agent as the valuations for one
painting is just a component of the
valuation for the winning collection of
paintings.

n

## ∑


i = 1

## valuation i = budget for the

sequence of bought items[1.. n ]

The valuation for the sequence of paintings
which are won in the auction, which results
in a win should be equal to the budget since
money is not useful once the auction is
over.
Because the bidding process is competitive
the agent bid should be as large as possible
and the number of bids needed to win
should be as small as possible. The money
left at the end does not count so the aim is
to spend all the money during the auction.
To be competitive enough money will only
be spent on the smallest amount of artists
needed to win the auction. In conclusion,



the strategy should be based off the
following aims:

- Minimise the number of bids
- Minimise the money left at the end
- Maximise each bid per item
- Spend only on x painting types (where x
    is the number of painting types needed in
    the collection)

As the winning bid is the highest in each
round, bidding differently in different
rounds for example high in one round and
low in another round can cause you to lose
out overall as the low bids may lose.
Therefore the best thing to do is to bid
equally among all the rounds for your
selected painting type(s). In cases where
the bids cannot be divided equally, the
remainder is distributed between the bids.

If the level of importance on each bidding
is same and the money waste on paintings
other than the 4 of one type and 2 of
another type with a total of 6 same type is
0, then Bidding = budget/needtowin. As the
budget for each player is 1001 and ’need to
win’ is 6, the bidding is 167 in 4 instances
and 166 in 2 instances according to this
formula.

The rule for this strategy when you find the
two paintings you want, you only bid on
those two till you win. One is gotten by
finding the first paining that appears four
times in the auction first while the second is
found by finding the painting other than the
first that appears twice in the auction first.
If the first bid is not successful for either of
the paintings, then it tries to find another
winning sequence int the next round.

When the agent has two paintings, it
reaches a point where it has to decide
which of the paintings it is going to aim for
collecting four and which just two. This


decision comes when it needs to bid to
increase a painting type in its collection
from two to three. It checks the list to see if
the painting will be the first among the pair
to reach the collection aim of four first and
if it is it bids normally for it otherwise it
bids zero.

Fig.1 An Auction example.

From the auction example D and R will be
the painting type bidder for. In the 6th
round instead of bidding normally for D,
zero will be bid because the agent checks
which type of painting will reach the
maximum for the bigger collection with
first and on seeing that it will be R, it
doesn’t bid as it has reached the maximum
for the smaller collection.
Also in order to stop opponents from
winning, when they are in a round which
could be their final round to win, the agent
bids one higher than the opponents budget,
this will then stop his chance from winning
that round.

An extension to my bot to help its
performance would be to add leniency to it
so it can increase and decrease value
according to its wins and losses. Also
cooperative bots could be added, in which
one bot helps another to win by stopping
other bots from winning rounds. These bots
will look at the budget and goals of the
other bots and making bids based on theirs
to make sure they lose.

1 2 3 4 5 6 7 8
D R P D R D P R
9 10 11
R P D


### VALUE GAME

This game differs to the collection game in
the sense that all the rounds in the value
game are played out except when every bot
runs out of money whereas in the
collection, the game ends when a bot gets a
certain collection or each bot runs out of
money. The aim of this game is to have the
largest valuation at the end of the auction.
Therefore we could say that the maximum
target value is 1 + (the sum of all the
values/ two).

Although this is seen as the maximum it is
not necessarily the best to aim for as aiming
for such will give us a low value for each
painting and therefore reduce our chances
of winning.

- Therefore, the better target value will be
    1+ (sum of all the values/ number of
    bots ).
- To calculate bid for a painting we use the
    value of the painting, the remaining
    budget and the value of each player
    which is calculated as the total remaining
    value/ number of players. The bid is then
    money left * painting value / player
    value.
- Agression is used when the bot keeps
    losing to increase bids and then falls
    when the bot makes a win
- Each round the bid for the current item is
    decided by the bot.

Although it is only a calculated pursuit of
the average, but because other players are
more or less, and are likely to be too
restrained, relatively low bids, this strategy
is always possible to obtain higher value.
And still based on the remaining value and
money calculation ratio, you can get more
value as much as possible.

From lectures during the course, proof has
been given that being genuine with an
agent’s valuation is dominant[1], but only
in situations where all agents risks are
neutral. It is unlikely that the bot needs to
bid as much as the value that is selected,
however this may become more of a
problem as other aggressive bots come into
play. But since we have aggression scaling
that is taken care of. So it stops agents that
want to take advantage of the second place
bid cost.
Another thought is the target value. If only
two bots are in the auction, average value
plus 1 could assure winning and a higher
value is pointless. It is harder when there
are more players to predict the final score
of winner, Following multiple tests, 1.2 is
picked to be the coefficient of the final
target value, as it is also a bit more than the
original value.

CONCLUSION

The strategies that I have made for the
auction use game theory and mechanism
design to provide solutions which should
hold up against both risk averse rational
agents and agents with different risk
attitudes. The first auction aims to divide
the budget evenly between all bids that
make up the classification, this is the
optimal and dominant strategy although it
could end up making the winner random at
times. The second auction both aim to
distribute the budget equally over a set of
items which have a summed value of a
calculated target, one which the agent
predicts will provide a more than half of the
points.


