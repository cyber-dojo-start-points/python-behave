# The learner has the step definitions in place and has deleted the feature
# file, or has not written one yet. behave finds nothing to run and says so,
# which is the one empty state this start-point reports honestly: a feature
# file holding no scenario reaches green instead.
from behave import given, when, then
from hiker import Hiker


@given(u'the hitch-hiker selects some tiles')
def step_selects_tiles(context):
    pass


@when(u'they spell {tile1:d} times {tile2:d}')
def step_spells_product(context, tile1, tile2):
    douglas = Hiker()
    context.tileproduct = douglas.answer(tile1, tile2)


@then(u'the score is {answer:d}')
def step_scores(context, answer):
    assert context.tileproduct == answer
