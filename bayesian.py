import csv
import sys
import matplotlib.pyplot as plt

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
    print(f'{descriptor:<40} = {b_given_a:.3f}')

    p_a = a_count / total_applications
    descriptor = f'P({a_key}={a_val})'
    print(f'{descriptor:<40} = {p_a:.3f}')

    p_b = b_count / total_applications
    descriptor = f'P({b_key}={b_val})'
    print(f'{descriptor:<40} = {p_b:.3f}')

    a_given_b = (b_given_a * p_a) / p_b
    descriptor = f'P({b_key}={b_val})'
    descriptor = f'P({a_key}={a_val}|{b_key}={b_val})'
    print(f'{descriptor:<40} = {a_given_b:.3f}')

    # Check your work
    b_count = 0
    both_count = 0
    for line in data:
        if line[b_key] == b_val:
            b_count += 1
            if line[a_key] == a_val:
                both_count += 1
    descriptor = f'both / b_count (for confirmation)'
    print(f'{descriptor:<40} = {both_count / b_count:.3f}')

    a_count = 0
    both_count = 0
    for line in data:
        if line[b_key] == b_val:
            a_count += 1
            if line[a_key] == a_val:
                both_count += 1
    descriptor = f'both / a_count (for confirmation)'
    print(f'{descriptor:<40} = {both_count / a_count:.3f}')
    print()


# Considering only entries where Stage=Hired, show the different Origins
# piechart(data, ("Stage", "Hired"), "Origin")
def piechart(data, conditional, outcome):
    cond_key, cond_val = conditional
    outcomes = {}
    for line in data:
        if line[cond_key] == cond_val:
            this_outcome = line[outcome]
            outcomes[this_outcome] = outcomes.get(this_outcome, 0) + 1

    outcomes_normalized = {}
    total = sum(outcomes.values())
    for key, val in outcomes.items():
        outcomes_normalized[key] = round(val / total, 3)
    print(f'Among entries where "{cond_key}={cond_val}", the "{outcome}" '
          f'values are {outcomes_normalized}')

    fig, ax = plt.subplots()
    fig.suptitle(f'Among "{cond_key}={cond_val}", the "{outcome}" values are:')
    ax.pie(outcomes.values(), labels=outcomes.keys(), autopct='%1.1f%%')
    plt.show()


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

    prob_a_given_b(data, a=("Cover letter?", "Yes"), b=("Stage", "Hired"))
    # prob_a_given_b(data, a=("Stage", "Rejected"), b=("Interview?", "Yes"))
    # prob_a_given_b(data, a=("Stage", "Ghosted"), b=("Interview?", "Yes"))
    # prob_a_given_b(data, a=("Stage", "Hired"), b=("Interview?", "Yes"))

    piechart(data, ("Stage", "Hired"), "Origin")
    piechart(data, ("Cover letter?", "No"), "Stage")
    piechart(data, ("Cover letter?", "Yes"), "Stage")

if __name__ == "__main__":
    main()

