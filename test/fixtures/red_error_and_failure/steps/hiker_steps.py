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


@when(u'they add up the tiles')
def step_adds_up(context):
    douglas = Hiker()
    context.tilechecksum = douglas.checksum()


@then(u'the checksum is {value:d}')
def step_checksums(context, value):
    assert context.tilechecksum == value
