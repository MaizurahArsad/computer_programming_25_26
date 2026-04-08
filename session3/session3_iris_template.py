"""Session 3: Lists, Loops, and Conditionals for Iris classification.
This script builds on Session 2 by converting variables to dictionaries, assembling a dataset list,
iterating over it, applying a threshold rule, and computing accuracy metrics.
"""

# MAIZURAH BINTI ARSAD (BS23110083)


# Session 2 continuity variables (Rule settings). Do not change these.
THRESHOLD = 2.0
FEATURE_NAME = "petal_length"
POSITIVE_LABEL = "setosa"
NEGATIVE_LABEL = "not_setosa"
LABEL_KEY = "species"


correct = 0      # Count of correct predictions
wrong = 0        # Count of wrong predictions
total = 0        # Total samples processed
y_pred_list = []  # List of all predictions made


flower1 = {
    "id": "flower1",
    "sepal_length": 5.1,
    "sepal_width": 3.5,
    "petal_length": 1.4,
    "petal_width": 0.2,
    "species": "setosa"
}

# Task 1: Create A dictionary for second flower

flower2 = {
    "id": "flower2",
    "sepal_length": 4.9,
    "sepal_width": 3.0,
    "petal_length": 1.4,
    "petal_width": 0.2,
    "species": "setosa"
}  # remember to close me for a dict


# Task 2: Create list of dictionaries
dataset = [flower1, flower2]  # dataset to loop over


# Task 3: Create a for loop to process the dataset
# This loop was used to check dataset values (practice)
for sample in dataset:
    print(sample["id"], sample[FEATURE_NAME], sample[LABEL_KEY])


# Task 4: Use an if-else statement to classify each sample
# This loop was used to test classification rule (practice)
# for sample in dataset:
#    if sample[FEATURE_NAME] < THRESHOLD:
#        y_pred = POSITIVE_LABEL
#    else:
#        y_pred = NEGATIVE_LABEL

#    print(sample["id"], y_pred)

# 3.8.2 TASK 1: Initialize metrics and predictions list (line 2 till 5)
for sample in dataset:
    # Task 2: Compute prediction
    if sample[FEATURE_NAME] < THRESHOLD:
        y_pred = POSITIVE_LABEL  # predict setosa if petal_length<threshold
    else:
        y_pred = NEGATIVE_LABEL

    # Task 3: Convert true label
    if sample[LABEL_KEY] == POSITIVE_LABEL:
        y_true = POSITIVE_LABEL
    else:
        y_true = NEGATIVE_LABEL

    # Update metrics
    if y_pred == y_true:
        correct += 1
    else:
        wrong += 1
    total += 1  # always increment total for every sample
    y_pred_list.append(y_pred)  # store prediction in list

    # Task 4: Print per-sample summary
    print(
        f"id={sample['id']} | true={y_true} | pred={y_pred} | "
        f"petal_length={sample['petal_length']}"
    )

# Task 5: Final summary
accuracy = (correct / total) * 100 if total > 0 else 0.0

print("Correct:", correct)  # number of correct predictions
print("Wrong:", wrong)  # number of wrong predictions
print("Total:", total)  # total samples processed
print("Accuracy (%):", round(accuracy, 2))  # accuracy percentage
print("All predictions:", y_pred_list)  # list all prediction
