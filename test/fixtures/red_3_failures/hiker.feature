
Feature: hitch-hiker playing scrabble

Scenario: earthling playing scrabble in the past
Given the hitch-hiker selects some tiles
When they spell 6 times 9
Then the score is 42

Scenario: the score is three digits long
Given the hitch-hiker selects some tiles
When they spell 6 times 7
Then the score is 3 digits long

Scenario: the score in the past is the answer
Given the hitch-hiker selects some tiles
When they spell 6 times 7
Then the score is 54
