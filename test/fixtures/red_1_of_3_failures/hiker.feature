
Feature: hitch-hiker playing scrabble

Scenario: the score is two digits long
Given the hitch-hiker selects some tiles
When they spell 6 times 7
Then the score is 2 digits long

Scenario: earthling playing scrabble in the past
Given the hitch-hiker selects some tiles
When they spell 6 times 9
Then the score is 42

Scenario: earthling playing scrabble today
Given the hitch-hiker selects some tiles
When they spell 6 times 7
Then the score is 42
