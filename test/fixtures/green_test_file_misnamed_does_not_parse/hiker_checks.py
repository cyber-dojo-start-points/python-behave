# behave loads step definitions from the steps/ dir only, so a step file left
# beside the feature is never loaded, and this one is half written so it does
# not parse either. Vanishing is what it must not do: mypy reads every .py
# file in the sandbox dir and names it, and coverage gives up its whole
# report over it.
from behave import then
from hiker import Hiker


@then(u'the score is {size:d} digits long')
def step_scores_digits(context, size
    douglas = Hiker()
    assert len(str(douglas.answer(6, 7))) == size
