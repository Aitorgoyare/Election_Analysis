# Election_Analysis
## Project Overview 
The purpose of this project was to provide an election audit for the Colorado Board of Elections. 

1. Calculate the total number of votes casted.
2. Get a complete list of candidates who received votes.
3. Get the county who had the highest voter turnout. 
4. Calculate the total number of votes each candidate received. 
5. Calculate the percentage of votes each candidate won. 
6. Determine the winner of the election based on popular vote. 

8. ## Resources
Data Source: election_results.csv 
Software: Python 3.7.6, Visual Studio Code 

## Results 
The analysis of the election show that: 
  * There was 379,111 votes cast in the election.
    * The candidates were:
     * Charles Casper Stockham
     * Diana DeGette 
     * Raymon Anthony Doane
      
  * The candidate results were:
      * Charles Casper Stockham received 23% of the total vote with 85,213 votes.
      * Diana DeGette received 82.8% of the total vote with 272,892 votes.
      * Raymon Anthony Doane received 3.1% of the total vote with 11,606 votes. 
      * TOTAL VOTES= 369,711
      
  * The winner of the election was:
      * Candidate Diana DeGette, who recieved 82.8% of the total vote with 272,892 votes.

## Overview of Election Audit

The election commission has requested some additional data to complete the audit:

The voter turnout for each county
The percentage of votes from each county out of the total count
The county with the highest turnout

## Election Audit Results

#### Election Results

Total Votes: 369,711
	
County Results:
	
Jefferson: 10.5% (38,855)
Denver: 82.8% (306,055)
Arapahoe: 6.7% (24,801)
	
Largest County Turnout: Denver

Candidate Results:

Charles Casper Stockham: 23.0% (85,213)
Diana DeGette: 73.8% (272,892)
Raymon Anthony Doane: 3.1% (11,606)


Election Winner: 

Diana DeGette
Vote Count: 272,892
Percentage: 73.8%

## Election Audit Summary
We can modify the script to generate more detailed information. For example, we can use splitting the results by zip code.
Another way to edit the script would be in the case of having a more detailed database containing gender, age, education, etc. and be able to better segment the results.
