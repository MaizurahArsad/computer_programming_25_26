"""
Refactored Session 3 into 10 unit functions
"""

# =========================
# 1. Constants
# =========================
THRESHOLD = 2.0
FEATURE_NAME = "petal_length"
POSITIVE_LABEL = "setosa"
NEGATIVE_LABEL = "not_setosa"
LABEL_KEY = "species"


# =========================
# 2. Create flower 1
# =========================
def create_flower1():
    return {
        "id": "flower1",
        "sepal_length": 5.1,
        "sepal_width": 3.5,
        "petal_length": 1.4,
        "petal_width": 0.2,
        "species": "setosa"
    }


# =========================
# 3. Create flower 2
# =========================
def create_flower2():
    return {
        "id": "flower2",
        "sepal_length": 4.9,
        "sepal_width": 3.0,
        "petal_length": 1.4,
        "petal_width": 0.2,
        "species": "setosa"
    }


# =========================
# 4. Build dataset
# =========================
def build_dataset():
    flower1 = create_flower1()
    flower2 = create_flower2()
    return [flower1, flower2]


# =========================
# 5. Initialize metrics
# =========================
def initialize_metrics():
    return 0, 0, 0, []  # correct, wrong, total, predictions list


# =========================
# 6. Print dataset (practice loop)
# =========================
def print_dataset(dataset):
    for sample in dataset:
        print(sample["id"], sample[FEATURE_NAME], sample[LABEL_KEY])


# =========================
# 7. Predict label
# =========================
def predict(sample):
    if sample[FEATURE_NAME] < THRESHOLD:
        return POSITIVE_LABEL
    else:
        return NEGATIVE_LABEL


# =========================
# 8. Get true label
# =========================
def get_true_label(sample):
    if sample[LABEL_KEY] == POSITIVE_LABEL:
        return POSITIVE_LABEL
    else:
        return NEGATIVE_LABEL


# =========================
# 9. Update metrics
# =========================
def update_metrics(y_pred, y_true, correct, wrong, total, y_pred_list):
    if y_pred == y_true:
        correct += 1
    else:
        wrong += 1

    total += 1
    y_pred_list.append(y_pred)

    return correct, wrong, total, y_pred_list


# =========================
# 10. Print summary
# =========================
def print_summary(correct, wrong, total, y_pred_list):
    accuracy = (correct / total) * 100 if total > 0 else 0.0

    print("Correct:", correct)
    print("Wrong:", wrong)
    print("Total:", total)
    print("Accuracy (%):", round(accuracy, 2))
    print("All predictions:", y_pred_list)


# =========================
# MAIN PROGRAM (Driver Code)
# =========================
def main():
    dataset = build_dataset()
    correct, wrong, total, y_pred_list = initialize_metrics()

    print_dataset(dataset)

    for sample in dataset:
        y_pred = predict(sample)
        y_true = get_true_label(sample)

        correct, wrong, total, y_pred_list = update_metrics(
            y_pred, y_true, correct, wrong, total, y_pred_list
        )

        print(
            f"id={sample['id']} | true={y_true} | pred={y_pred} | "
            f"petal_length={sample['petal_length']}"
        )

    print_summary(correct, wrong, total, y_pred_list)


# Run program
main()