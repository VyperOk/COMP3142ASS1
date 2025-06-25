ranges = {
  "num_hours": {"min": 1, "max": 12},
  "entry_hour": {"min": 6, "max": 21},
  "day_of_week": {"min": 1, "max": 7}  
}

nominal = {
  "num_hours": 6,
  "entry_hour": 13,
  "day_of_week": 4,
  "vehicle_type": "standard"
}

test_cases = set()

for input_name in ["num_hours", "entry_hour", "day_of_week"]:
  min_val = ranges[input_name]["min"]
  max_val = ranges[input_name]["max"]
  nom_val = nominal[input_name]
  test_values = [min_val - 1, min_val, min_val + 1, nom_val, max_val - 1, max_val, max_val + 1]
  for val in test_values:
    case = {
      "num_hours": nominal["num_hours"],
      "entry_hour": nominal["entry_hour"],
      "day_of_week": nominal["day_of_week"],
      "vehicle_type": nominal["vehicle_type"],
    }
    case[input_name] = val
    test_cases.add((case["num_hours"], case["entry_hour"], case["day_of_week"], case["vehicle_type"]))
test_cases = sorted(list(test_cases))

with open('Q1_1_test.txt', "w") as f:
  for case in test_cases:
    f.write(f"{case[0]},{case[1]},{case[2]},{case[3]}\n")