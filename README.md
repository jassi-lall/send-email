# send_email
A simple way to make a python script send email.

## Step 1 - gmail
Set up a Google account. *Ideally just for this purpose - for security reasons.*

## Step 2 - gmail app passwords
Configure the Gmail account so that a program can use the account credentials.

The way to do this has evolved. Previously you had to turn on 'less secure app access' which has now been depreciated for security. Search youtube to find the most up to date way. At time of writing this is how you do it:
- Turn on 2-step verification in security settings
- Click on 2-step verification within security settings and then click on 'app passwords'.
- Use this app password as a credential when accessing gmail programatically.

## Step 3 - script
Run python script (provided in repo).

Tweak the script using your gmail credentials. See best practice for storing credentials below:

## Storing credentials - best practice
DO NOT store credentials in the source or anywhere in the source tree.
The best way to store credentials is as an environment variable. To access enviornment variables within a python script use os.environ['name']. Similar to how you would access the PATH environment variable.
If you really wish to store the credentials do it outside the source tree to avoid accidental leaks - e.g. accidentally pushing to GitHub
