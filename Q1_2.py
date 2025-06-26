equivalence_classes = {
    "staff_role": {
        "valid": ["Academic", "Research", "Professional", "Casual"],
        "invalid": ["InvalidRole"]
    },
    "month": {
        "valid": [1, 3, 5, 6, 8, 9, 11],
        "invalid": [0, 13]
    },
    "weekly_hours": {
        "valid": [10, 25, 40],
        "invalid": [0, 61]
    },
    "fte": {
        "valid": [0.3, 0.6, 0.9],
        "invalid": [0, 1.1]
    }
}

test_cases = set()

for s_role in equivalence_classes["staff_role"]["valid"] + equivalence_classes["staff_role"]["invalid"]:
    for m in equivalence_classes["month"]["valid"] + equivalence_classes["month"]["invalid"]:
        for w_h in equivalence_classes["weekly_hours"]["valid"] + equivalence_classes["weekly_hours"]["invalid"]:
            for fte in equivalence_classes["fte"]["valid"] + equivalence_classes["fte"]["invalid"]:
                test_cases.add((s_role, m, w_h, fte))

test_cases = list(test_cases)

with open("Q1_2_test.txt", "w") as f:
    for case in test_cases:
        f.write(f"{case[0]},{case[1]},{case[2]},{case[3]}\n")