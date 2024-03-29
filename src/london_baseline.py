# Calculates the accuracy of a baseline that simply predicts "London" for every example in the dev set.

import utils

dev_set_path = "birth_dev.tsv"
with open(dev_set_path, "r") as dev_set:
    total = sum(1 for _ in dev_set)

total, correct = utils.evaluate_places(dev_set_path, ["London"] * total)
print(f'Correct: {correct} out of {total}: {correct / total * 100}%' if total > 0 else 'No targets provided')
