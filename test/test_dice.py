from dice import Die
import pytest


def test_double_roll():
    """ 
    Check that the probability for the sum of two n-sided dice matches
    the expected distribution.
    """

    # Store the expected probabilities for the sum of two dice.
    sides=6
    rolls=1000
    expect = {}
    for x in range(2, 13):
        expect[x] = prob_double_roll(x, sides)

    # Create a dictionary to hold the tally for each outcome.
    tally = {}
    for key in expect:
        tally[key] = 0

    # Initialise the die.
    die = Die(sides)

    # Roll two dice 'rolls' times.
    for i in range(0, rolls):

        # Sum the value of the two dice rolls.
        roll_sum = die.roll() + die.roll()

        # Increment the tally for the outcome.
        tally[roll_sum] += 1

    # Compute the probabilities and check with expected values.
    for key in tally:

        average = tally[key] / rolls
        assert average == pytest.approx(expect[key], rel=0.1)
        
        
def prob_double_roll(x, n):
    """
    Expected probabilities for the sum of two dice.
    """
    # For two n-sided dice, the probability of two rolls summing to x is
    # (n − |x−(n+1)|) / n^2, for x = 2 to 2n.

    return (n - abs(x - (n + 1))) / n ** 2
