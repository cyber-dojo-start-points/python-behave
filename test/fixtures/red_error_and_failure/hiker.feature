
Feature: hitch-hiker playing scrabble

Scenario: earthling playing scrabble in the past
Given the hitch-hiker selects some tiles
When they spell 6 times 9
Then the score is 42

Scenario: earthling adding up the tiles
Given the hitch-hiker selects some tiles
When they add up the tiles
Then the checksum is 0
