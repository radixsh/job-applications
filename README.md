# Job applications statistics
Throughout my time at university, I've applied to many summer internships,
summer retail jobs, research labs, and full-time jobs. Internet strangers'
slightly concerning job application data from
[r/DataIsBeautiful](https://www.reddit.com/r/dataisbeautiful/) inspired me to
make this; I thought it would be nice to see how successful (or not) my
applications were. It looks like I've done tolerably well.

## Usage
1. Export your entire job applications database from Notion, keeping all default
   settings except for changing `Include content` to `No files or images`. The
   downloaded zip should contain two identical CSVs. Put one of them into the
   `/data` directory.
	- To consider only applications to career positions, run
	  `extract_career.py data/ALL_APPS.csv data/CAREER_ONLY.csv`.
2. Run `generate_sankey.py data/ALL_APPS.csv` to generate SankeyMATIC-formatted
   data.
3. Use the Sankey-formatted data to [create a Sankey
   diagram](https://www.sankeymatic.com/build/).

`extract_career.py` filters for full-time positions from a CSV.

`bayesian.py data/ALL_APPS.csv` calculates conditional probabilities of various
joint events and generates piecharts using Matplotlib.


## Results
### All applications throughout undergrad
```
All applications [55] Cover letter
Cover letter [1] Awaiting response
All applications [1] Awaiting response
Cover letter [1] Position closed
Cover letter [13] Interview/OA
Interview/OA [1] Awaiting response
All applications [19] Rejected
All applications [39] Ghosted
Cover letter [17] Ghosted
Cover letter [23] Rejected
All applications [13] Interview/OA
Interview/OA [17] Rejected
Interview/OA [3] Ghosted
All applications [1] Position closed
Interview/OA [5] Hired
All applications [1] Hired
```
![all jobs](./images/all_jobs.png)

### Career positions only
```
All applications [19] Cover letter
Cover letter [1] Awaiting response
All applications [1] Awaiting response
Cover letter [1] Position closed
Cover letter [2] Interview/OA
Interview/OA [1] Awaiting response
All applications [6] Rejected
All applications [23] Ghosted
Cover letter [6] Ghosted
Cover letter [9] Rejected
All applications [7] Interview/OA
Interview/OA [4] Rejected
Interview/OA [3] Ghosted
All applications [1] Position closed
Interview/OA [1] Hired
```
![career jobs](./images/career_jobs.png)

## Resources
- [Notion](https://www.notion.com/) - for everyday logging of my job
  applications
- [Python CSV library](https://docs.python.org/3/library/csv.html) - for parsing
  the CSV downloaded from Notion
- [SankeyMATIC](https://www.sankeymatic.com/build/) - for creating the flow
  diagrams
- [r/DataIsBeautiful](https://reddit.com/r/dataisbeautiful) - for the
  inspiration
- [Wikipedia - Bayesian
  statistics](https://en.wikipedia.org/wiki/Bayesian_statistics) - to refresh my
  understanding of conditional probability
- [Matplotlib](https://matplotlib.org/) - to create piecharts
