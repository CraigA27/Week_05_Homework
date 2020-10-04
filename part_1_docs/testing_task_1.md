### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:

#line 21 - if card.value ==1:, line 23 - else statement missing :
  def check_for_ace(self, card):
    if card.value = 1:
      return True
    else
      return False
   
#line 27 - def keyword misspelled as dif, line 27 - comma required between card1 & card2, line 28-31 - Indentation required, line 29 - return card1
  dif highest_card(self, card1 card2):
  if card1.value > card2.value:
    return card
  else:
    return card2
  

# line 35-38 - Indentation required, line 36 - total is undefined (=0), line 39 - str(total) required 
def cards_total(self, cards):
  total                               
  for card in cards:
    total += card.value
    return "You have a total of" + total
  
```
