# Section Front-End Technical Exercise

Chew Zhi Qi. 

Testing framework: Selinum(Python)
Browser Used: Chrome Version 102.0.5005.63 (Official Build) (64-bit)

### Pre Requisite: 
 1. User account already login.(due to unable to automate login flow)
 2. Current cookies will be fetch and used  
 3. A new tab will be create for each test as it could only to done on the specific url [https://uat.sentosa.com.sg/earn-points?id=73&refreshedDate=2022/05/20](https://uat.sentosa.com.sg/earn-points?id=73&refreshedDate=2022/05/20 "https://uat.sentosa.com.sg/earn-points?id=73&refreshedDate=2022/05/20")
 4. Chrome browser is not running 
### Issue face:
 1. Unable to login 
	 - Error code: Forbidden Access (403-account-access)
 2. Unable to create new account for testing (tried with all diffrent combiantion of names, emails and password)
	 -  Error message: SORRY, THERE WAS AN ERROR.

# The Challenge
| DESCRIPTION OF TASKS |STEPS TO EXECUTE  | EXPECTED RESULTS (FUNCTIONAL REQUIREMENT)|Task fullfillment|
|--|--|--|--|
| Island Partner QR Code check (Not Logged in yet) | 1. Go to [https://uat.sentosa.com.sg/earn-points?id=73&refreshedDate=2022/05/20](https://uat.sentosa.com.sg/earn-points?id=73&refreshedDate=2022/05/20 "https://uat.sentosa.com.sg/earn-points?id=73&refreshedDate=2022/05/20")<br>2. If you are not logged in; Proceed with the login <br> 3. Need to set OTP after submit email address and password.|After logging in;<br>The user should land on the Time to Enjoy page with the Island Partner Name. | No.<br> Automating email and get otp will be a super long flow if email is not logged-in need more time|
|Island Partner QR Code check (Already Logged in)|1. Go to [https://uat.sentosa.com.sg/earn-points?id=73&refreshedDate=2022/05/20](https://uat.sentosa.com.sg/earn-points?id=73&refreshedDate=2022/05/20 "https://uat.sentosa.com.sg/earn-points?id=73&refreshedDate=2022/05/20")|The user should land on the Time to Enjoy page with the Island Partner Name.|Yes|
|Successful earning of points ( Happy flow )|1. Go to [https://uat.sentosa.com.sg/earn-points?id=73&refreshedDate=2022/05/20](https://uat.sentosa.com.sg/earn-points?id=73&refreshedDate=2022/05/20 "https://uat.sentosa.com.sg/earn-points?id=73&refreshedDate=2022/05/20"); Go through login if needed <br> 2. Key in 50.90 in amount spent; You should see 50 points in You will earn section  <br>3. Click on VERIFY WITH STAFF Button  <br>4. Enter 981277(Depending on which IP you scanned) in Enter staff PIN  <br> 5. Slide the SLIDE TO VERIFY slider|A confitee celebration screen should be shown followed by a successful screen where it will show case the folowing <br> data points:  <br>- 50 points  <br>- $S 50.90  <br>- 50 points (If you have earn any points before) <br> An eDM should be sent to you email detailing that you have earn the points.|Yes|
|Unsuccessful earning of points ( Below minumum spend )|1. Go to [https://uat.sentosa.com.sg/earn-points?id=73&refreshedDate=2022/05/20](https://uat.sentosa.com.sg/earn-points?id=73&refreshedDate=2022/05/20 "https://uat.sentosa.com.sg/earn-points?id=73&refreshedDate=2022/05/20"); Go through login if needed <br> 2. Key in a number that is lower than the minimum allowed amount spend (Less then 20)|1. An exception (Error Message) will be shown under amount spend that you need to spend at least S$20 to earn points. <br> 2. VERIFY WITH STAFF Button should be greyed off and disabled|Yes|
|Partial Unsuccessful earning of points / Pending points ( PIN locked )|1. Go to [https://uat.sentosa.com.sg/earn-points?id=73&refreshedDate=2022/05/20](https://uat.sentosa.com.sg/earn-points?id=73&refreshedDate=2022/05/20 "https://uat.sentosa.com.sg/earn-points?id=73&refreshedDate=2022/05/20"); Go through login if needed  <br>2. Key in 50.90 in amount spent; You should see 50 points in You will earn section  <br>3. Click on VERIFY WITH STAFF Button  <br>4. Enter 123456 in Enter staff PIN  <br>5. Slide the SLIDE TO VERIFY slider  <br>6. An error under Enter staff PIN should be shown  <br>7. Repeat steps 4 - 6 for 5 times|1. An error modal should be shown <br> 2. After clearing the modal; A confirmation screen will be shown saying that the points will be process in the next 3 working days <br><br>This transacation sould be set to pending inside the Administrative Portal|Yes|
|Merchant lock after PIN locked|1. Go to [https://uat.sentosa.com.sg/earn-points?id=73&refreshedDate=2022/05/20](https://uat.sentosa.com.sg/earn-points?id=73&refreshedDate=2022/05/20 "https://uat.sentosa.com.sg/earn-points?id=73&refreshedDate=2022/05/20"); Go through login if needed|The user should not be able to key in any amount; A page showing We're on it to process the points should be shown to the user|Yes|
|Points earning from another merchant after a Merchant Lock|1. Go to [https://uat.sentosa.com.sg/earn-points?id=73&refreshedDate=2022/05/20](https://uat.sentosa.com.sg/earn-points?id=73&refreshedDate=2022/05/20 "https://uat.sentosa.com.sg/earn-points?id=73&refreshedDate=2022/05/20") <br> 2; Go through login if needed|The user should be able to key in amount and go through the earning process|Yes(unable to check)|
|Successful earning of points;  <br>Reached daily maximum earning capcacity with leveling up to Piority Tier <br><br>2 Things -<br>  1. Will not exceed daily cap of 600  <br>2. Leveling up to Piority|1. Go to [https://uat.sentosa.com.sg/earn-points?id=73&refreshedDate=2022/05/20](https://uat.sentosa.com.sg/earn-points?id=73&refreshedDate=2022/05/20 "https://uat.sentosa.com.sg/earn-points?id=73&refreshedDate=2022/05/20"); Go through login if needed  <br>2. Key in 560.90 in amount spent; You should see 550 points in You will earn section  <br>3. Click on VERIFY WITH STAFF Button  <br>4. Enter 981277 in Enter staff PIN  <br>5. Slide the SLIDE TO VERIFY slider|A confitee celebration screen should be shown followed by:  <br>1. A modal congrats-ing you on promoting that you have reached Piority Tier  <br>2. If you click the grayed area, A successful screen where it will show case the folowing<br><br>data points:  <br>- 550 points  <br>- $S 560  <br>- Initial points + 550 points (If you have earn any points before) <br><br>An eDM should be sent to you email detailing that you have earn the points.|Yes(unable to check)|
|Unsuccessful earning of points ( Reached maximum earning capacity )|1. Go to [https://uat.sentosa.com.sg/earn-points?id=73&refreshedDate=2022/05/20](https://uat.sentosa.com.sg/earn-points?id=73&refreshedDate=2022/05/20 "https://uat.sentosa.com.sg/earn-points?id=73&refreshedDate=2022/05/20"); Go through login if needed|The user should not be able to key in any amount; A page showing Sweet! 600 points earned today should be shown to the user|Yes(unable to check)|
