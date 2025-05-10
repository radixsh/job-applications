import csv
import sys

#                              P(B | A) * P(A)
#             P(A | B)   =   -------------------
#                                   P(B)
def prob_a_given_b(data, a, b):
    a_key, a_val = a
    b_key, b_val = b
    print(f'Given `{b_key}={b_val}`, what is the probability of '
          f'`{a_key}={a_val}`?')

    total_applications = len(data)
    a_count = 0
    b_count = 0
    both_count = 0
    for line in data:
        if line[a_key] == a_val:
            a_count += 1
        if line[b_key] == b_val:
            b_count += 1
        if line[a_key] == a_val and line[b_key] == b_val:
            both_count += 1

    b_given_a = both_count / a_count
    descriptor = f'P({b_key}={b_val}|{a_key}={a_val})'
    print(f'{descriptor:<40} = {b_given_a:.2f}')

    p_a = a_count / total_applications
    descriptor = f'P({a_key}={a_val})'
    print(f'{descriptor:<40} = {p_a:.2f}')

    p_b = b_count / total_applications
    descriptor = f'P({b_key}={b_val})'
    print(f'{descriptor:<40} = {p_b:.2f}')

    a_given_b = (b_given_a * p_a) / p_b
    descriptor = f'P({b_key}={b_val})'
    descriptor = f'P({a_key}={a_val}|{b_key}={b_val})'
    print(f'{descriptor:<40} = {a_given_b:.2f}')

    # Check your work
    b_count = 0
    both_count = 0
    for line in data:
        if line[b_key] == b_val:
            b_count += 1
            if line[a_key] == a_val:
                both_count += 1
    descriptor = f'both / b_count (for confirmation)'
    print(f'{descriptor:<40} = {both_count / b_count:.2f}')

    a_count = 0
    both_count = 0
    for line in data:
        if line[b_key] == b_val:
            a_count += 1
            if line[a_key] == a_val:
                both_count += 1
    descriptor = f'both / a_count (for confirmation)'
    print(f'{descriptor:<40} = {both_count / a_count:.2f}')

def main():
    try:
        all_apps_file = sys.argv[1]
    except:
        print(f"Usage: bayesian.py data/YOUR_CSV_FILE.csv")
        sys.exit()

    data = []
    with open(all_apps_file, 'r', encoding="utf-8-sig") as infile:
        reader = csv.DictReader(infile)
        for row in reader:
            ignore = ["Must apply", "Gave up"]
            if any(stage in row["Stage"] for stage in ignore):
                continue
            data.append(row)

    # prob_a_given_b(data, a=("Cover letter?", "Yes"), b=("Stage", "Hired"))
    # print()

    prob_a_given_b(data, a=("Stage", "Rejected"), b=("Interview?", "Yes"))
    # print()
    # prob_a_given_b(data, a=("Stage", "Ghosted"), b=("Interview?", "Yes"))
    # print()
    # prob_a_given_b(data, a=("Stage", "Hired"), b=("Interview?", "Yes"))
    # print()

    # prob_a_given_b(data, a=("Cover letter?", "Yes"), b=("Interview?", "Yes"))

if __name__ == "__main__":
    main()

