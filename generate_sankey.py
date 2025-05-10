import csv
import sys

def generate_sankey(csv_reader):
    data = []
    for row in csv_reader:
        ignore = ["Must apply", "Gave up"]
        if any(stage in row["Stage"] for stage in ignore):
            continue

        if row["Cover letter?"] == "Yes":
            data.append(f'All applications, Cover letter')
            source = "Cover letter"
        else:
            source = "All applications"

        if row["Interview?"] == "No" and row["OA?"] == "No":
            data.append(f'{source}, {row["Stage"]}')
        elif row["Interview?"] == "Yes" or row["OA?"] == "Yes":
            data.append(f'{source}, Interview')
            data.append(f'Interview, {row["Stage"]}')
        else:
            data.append(f'{source}, {row["Stage"]}')

    # Translate `data` to Sankey code
    sankey_code = {}
    for item in data:
        sankey_code[item] = sankey_code.get(item, 0) + 1
    return sankey_code

def main():
    try:
        all_apps_file = sys.argv[1]
    except:
        print(f"Usage: generate_sankey.py data/YOUR_CSV_FILE.csv")
        sys.exit()

    with open(all_apps_file, 'r', encoding="utf-8-sig") as infile:
        reader = csv.DictReader(infile)
        sankey_code = generate_sankey(reader)

    # Print the Sankey-formatted flow data
    for srcdst, weight in sankey_code.items():
        src, dst = srcdst.split(', ')
        print(f'{src} [{weight}] {dst}')

if __name__ == "__main__":
    main()
