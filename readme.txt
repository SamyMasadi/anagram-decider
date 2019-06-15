File: mr_agana.py
Program Name: Mr. Agana, The Anagram Decider
Author: Samy Masadi

Mr. Agana will compare two strings you supply, and determine whether they are anagrams.
Note: Input strings must contain only lowercase letters and cannot contain any spaces.

Mr. Agana has two different methods for determining anagrams:
Brute Force: This will search through every permutation of letter order for the first 
	string you input until it exhausts all options or finds a match to the second 
	string.
	Note: It is recommended you do not exceed 11 characters for your input string,
	as greater lengths may take a prohibitively long time to process.
Linear: This will count the number of instances of each letter within each string then 
	compare the counts to determine a match.

Required for use: Python 3.6 or later version must be installed.

To run in Windows command line:
Double-click the mr_agana.py file or navigate to the file's directory and
enter "mr_agana.py".

To run in IDLE Python Shell:
1. Run IDLE.
2. Click "File" then "Open".
3. Navigate to "mr_agana.py" then click "Open".
4. To run the program, Press F5 on the keyboard, or click "Run" then "Run Module".

Instructions for use, once running:
1. Enter a number to select one of the options displayed:
	- Enter "1" for Brute Force Method
	- Enter "2" for Linear Method
	- Enter "3" for Brute Force and Linear Methods
	- Enter "4" to exit.
2. For options 1 through 3, next enter your first string when prompted, followed by
	the second string.
3. After Mr. Agana makes its determination, you can select options 1 through 3 again
	to compare another pair of strings, or enter 4 to exit.