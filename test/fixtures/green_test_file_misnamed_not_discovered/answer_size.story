# behave walks the whole sandbox but collects only names ending .feature, so
# this valid gherkin never runs. Every step it uses is defined, and the score
# it expects is the wrong one, so a green says it really did not run rather
# than that it ran and passed.

Feature: the size of the score

Scenario: the score is three digits long
Given the hitch-hiker selects some tiles
When they spell 6 times 7
Then the score is 3 digits long
