"""Bayesian networks"""

from probability import (
    BayesNet,
    enumeration_ask,
    elimination_ask,
    rejection_sampling,
    likelihood_weighting,
    gibbs_ask,
)
from timeit import timeit, repeat
import pickle
import numpy as np

T, F = True, False


class DataPoint:
    """
    Represents a single datapoint gathered from one lap.
    Attributes are exactly the same as described in the project spec.
    """

    def __init__(self, muchfaster, early, overtake, crash, win):
        self.muchfaster = muchfaster
        self.early = early
        self.overtake = overtake
        self.crash = crash
        self.win = win


def generate_bayesnet():
    """
    Generates a BayesNet object representing the Bayesian network in Part 2
    returns the BayesNet object
    """
    bayes_net = BayesNet()
    # load the dataset, a list of DataPoint objects
    data = pickle.load(open("data/bn_data.p", "rb"))
    # BEGIN_YOUR_CODE ######################################################
    total = len(data)
    muchfaster_true_count = 0
    early_true_count = 0

    for d in data:
        if d.muchfaster == T:
            muchfaster_true_count = muchfaster_true_count + 1
        if d.early == T:
            early_true_count = early_true_count + 1

    prob_muchfaster = muchfaster_true_count / total
    prob_early = early_true_count / total

    bayes_net = BayesNet(
        [
            ("MuchFaster", "", prob_muchfaster),
            ("Early", "", prob_early),
        ]
    )

    overtake_cpt = {}
    crash_cpt = {}

    for i in [T, F]:
        for j in [T, F]:
            parent_count = 0
            overtake_true_count = 0
            crash_true_count = 0

            for d in data:
                if d.muchfaster == i and d.early == j:
                    parent_count = parent_count + 1
                    if d.overtake == T:
                        overtake_true_count = overtake_true_count + 1
                    if d.crash == T:
                        crash_true_count = crash_true_count + 1

            if parent_count == 0:
                prob_overtake = 0
                prob_crash = 0
            else:
                prob_overtake = overtake_true_count / parent_count
                prob_crash = crash_true_count / parent_count

            overtake_cpt[(i, j)] = prob_overtake
            crash_cpt[(i, j)] = prob_crash

    win_cpt = {}

    for i in [T, F]:
        for j in [T, F]:
            parent_count = 0
            win_true_count = 0

            for d in data:
                if d.overtake == i and d.crash == j:
                    parent_count = parent_count + 1
                    if d.win == T:
                        win_true_count = win_true_count + 1

            if parent_count == 0:
                prob = 0
            else:
                prob = win_true_count / parent_count

            win_cpt[(i, j)] = prob

    bayes_net.add(("Overtake", "MuchFaster Early", overtake_cpt))
    bayes_net.add(("Crash", "MuchFaster Early", crash_cpt))
    bayes_net.add(("Win", "Overtake Crash", win_cpt))
    # END_YOUR_CODE ########################################################
    return bayes_net


def find_best_overtake_condition(bayes_net):
    """
    Finds the optimal condition for overtaking the car, as described in Part 3
    Returns the optimal values for (MuchFaster,Early)
    """
    # BEGIN_YOUR_CODE ######################################################
    best_condition = None
    best_prob = -1

    for i in [T, F]:
        for j in [T, F]:
            evidence = {"MuchFaster": i, "Early": j, "Crash": F}

            result = elimination_ask("Win", evidence, bayes_net)
            prob_win = result[T]

            if prob_win > best_prob:
                best_prob = prob_win
                best_condition = (i, j)

    return best_condition

    # END_YOUR_CODE ########################################################


def main():
    bayes_net = generate_bayesnet()
    cond = find_best_overtake_condition(bayes_net)
    print("Best overtaking condition: MuchFaster={}, Early={}".format(cond[0], cond[1]))


if __name__ == "__main__":
    main()
