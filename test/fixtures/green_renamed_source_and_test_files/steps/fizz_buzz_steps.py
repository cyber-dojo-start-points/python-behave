from behave import given, when, then
from fizz_buzz import FizzBuzz


@given(u'the counter is ready')
def step_counter_ready(context):
    pass


@when(u'it multiplies {first:d} by {second:d}')
def step_multiplies(context, first, second):
    counter = FizzBuzz()
    context.said = counter.say(first, second)


@then(u'it says {said:d}')
def step_says(context, said):
    assert context.said == said
