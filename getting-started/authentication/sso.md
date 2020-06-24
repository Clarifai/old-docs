# Using Social SSO (Single Sign On) with Clarifai

What is Social SSO?
In general, Single Sign On (SSO) allows the clients to manage the users outside of the built-in application. 

Similar to Single Sign On (SSO), Social Login, on the other hand, allows users to access systems with login credentials that already exist on other social platforms. It’s simple and convenient. We implemented the social logins for Google and GitHub primarily because it enhances the user experience of Open Social - no need to fill out the sign-up forms or remember another password. 


Why do we need it?
There are a few benefits using Social SSO for Sign In.

Increase user sign-ups. The ease of use of social login significantly reduces the barrier to entry. Joining the platform becomes simply a click away, rather than a form away.

Accurate data. It allows us to collect more accurate data and improves the identification of the platform users since it can provide verified email addresses and names, and possibly occupational information from marketing and sales.

Increased security. Popular social platforms like Google and GitHub have a more robust layer of protection than most other IT companies. Offloading the authentication to vendors like them would make the stack more secure than building a full set of wheels in house.


Who needs it?
Nowadays almost everyone has one or more Google account(s). That makes Google social login quite popular in many places. Since Clarifai platform is also targeted for developers as one of the main audiences, making GitHub as one of the social login sources makes sense for the developers who came across us on GitHub and want to have a quick try on our platform.


How to use it?
Here will follow with a few screenshots with how to use Github/Google to sign in to the Clarifai platform.


GitHub
After clicking the “Sign in with GitHub” button user will be redirected to the Authorisation page:


If he presses Authorize Clarifai green button he will be directed back to portal, where he will be logged in. If he did not have an account before it will be created and he has to accept the privacy policy and terms:


After Authorising their account with GitHub the user will be sent an email by GitHub that looks something like this:


The link in the email will take user to his/her security page, where he/she can Revoke access to our application. This means that when they want to sign in a gain with GitHub to the Portal they have to authorise again.



Google


