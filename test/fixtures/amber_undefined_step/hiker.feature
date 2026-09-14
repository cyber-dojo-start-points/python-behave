# The learner has written a step into the scenario and has not written its
# definition yet. behave counts the scenario as errored rather than failed
# and prints the snippet to write, and an errored scenario is one that never
# got as far as saying anything about the code.

Feature: hitch-hiker playing scrabble

Scenario: earthling playing scrabble in the past
Given the hitch-hiker selects some tiles
When they spell 6 times 7
Then the score is 42
And the score is written down
