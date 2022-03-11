# Election Analysis
## Project Overview
We were tasked with preforming an audit of a recent local congressional election for a Colorado Board of Elections employee. For the audit we had to find the following:
  1. The total number of votes cast
  2. List of all the candidates who received votes
  3. Total number of votes each candidate received
  4. Percentage of votes each candidate received
  5. Determine winner of the election based on popular vote

## Resources
- Data Sources: election_results.csv
- Software: Python 3.8.10, Vidual Studio Code 1.65.1

## Summary 
The analysis shows:
- There were 369,711 votes cast
- The candidates were:
  - Charles Casper Stockham
  - Diana DeGette
  - Raymon Anthony Doane
- Results per candidate (Name: percentage of votes (vote count)):
  - Charles Casper Stockham: 23.0% (85,213)
  - Diana DeGette: 73.8% (272,892)
  - Raymon Anthony Doane: 3.1% (11,606)

- The winner of the election was:
  - Diana DeGette: 73.8% (272,892)

## Challenge Overview
The election commision reviewed the audit submitted above and has requsted more information. They wanted us to take a deeper look into the the election data and have the audit look at county data and find:
  1. The voter turnout for each county
  2. The percentage of votes from each county out of the total count
  3. The county with the highest turnout

## Challenge Summary 
The county analysis shows:
- There was data from three counties:
  - Jefferson: 10.5% (38,855)
  - Denver: 82.8% (306,055) 
  - Arapahoe: 6.7% (24,801)
- Results per county (Name: percentage of votes (vote count)):
  - Jefferson: 10.5% (38,855)
  - Denver: 82.8% (306,055) 
  - Arapahoe: 6.7% (24,801)

For future audits this code can be eaisly modified to work with just about any election data. All that needs to change in the code is below:

1. Make sure the code references the correct file name and location, line 9
 ```python
 file_to_load = os.path.join("Resources", "election_results.csv") 
 ```
 2. Set the output file name and location, line 11
 ```python
 file_to_save = os.path.join("analysis", "election_analysis.txt")
 ```
 3. Check data for which columns the candidate and county name are in, and add print statement or open data file in other program such as excel, line 41:
  ```python
    header = next(reader)
    print(header)
 ```
 4. Use correct index for column of candidate and county name, line 50 and 53:
 
 ```python
        candidate_name = row[x]
        
        county_name = row[x]
 ```
