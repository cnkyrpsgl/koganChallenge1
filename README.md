# Kogan Coding Challenge
**Language: Python version 3.7.1**  
To work flawlessly, project is created within a virtual environment with the help of virtualenv module. Python and related packages works independently from what is on OS.   
**Aim of the Project**  
Finding the average cubic weight for all the products in the "Air Conditioners" category from given API (paginated) endpoint.  
**Challange**  
Solution should handle large input efficiently.  
**Code Summary**  
For this project, multithreading (threading module from standard Python library) is considered for processing large amount of data because web requests can take longer than expected for big data. Initial API point is given and subsequent URLs are extracted from working threads and passed to queue (a module imported from standard library in Python). Every thread takes unprocessed URL from the queue and picks air conditioners' size information and adds to total weight (weightSum). Finally, average cubic weight is calculated by getting arithmetic mean through industry standard cubic weight conversion factor.  
## Setup Instructions
* First of all, unzip working directory folder
* Run the cmd / terminal and go to working directory (..\koganChallenge1)
* On Windows, run `\path\to\koganChallenge1\Scripts\activate` 
* On Linux, run `source /path/to/koganChallenge1/bin/activate` 
* Run `python solution.py` 
* To quit virtualenv, run `deactivate` 
