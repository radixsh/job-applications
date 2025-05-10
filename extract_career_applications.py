import csv
import sys

def main():
    try:
        all_apps_file = sys.argv[1]
        career_only_file = sys.argv[2]
    except:
        print(f"Usage: extract_career_applications.py all_jobs.csv career_only.csv")
        sys.exit()

    with open(all_apps_file, 'r', encoding="utf-8-sig") as infile, \
        open(career_only_file, 'w', encoding="utf-8-sig") as outfile:
        reader = csv.DictReader(infile)

        writer = csv.DictWriter(outfile, reader.fieldnames)
        writer.writeheader()

        all_count = 0
        count = 0
        for row in reader:
            all_count += 1
            years = ["2025", "2024"]
            times = ["Summer 2024"]
            if any(year in row["Applied"] for year in years) \
                    and not any(time in row["Job Title"] for time in times):
                writer.writerow(row)
                count += 1

    print(f'Among {all_count} total applications, {count} were for career '
          f'positions')

if __name__ == "__main__":
    main()
