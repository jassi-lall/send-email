# Send Email Programatically 📧🔥
A simple way to make a python script send email. Completly free.

## Step 1 - Create Gmail
Set up a Google account - *ideally just for this purpose as you will have to modify the security settings.*

## Step 2 - Configure Gmail
Configure the Gmail account (via google account settings) so that a program can use the account credentials:

- Turn on `2-step verification` in security settings
- Click on `2-step verification` within security settings and then click on `app passwords`
- Use this app password as a credential when accessing gmail programatically.

*Note: The way to do this has evolved. Previously you had to turn on 'less secure app access' which has now been depreciated for security. If the above doesn't work search youtube to find the most up-to-date method of configuring gmail.*

## Step 3 - Script away!
See python script provided in repo.
Tweak the script using your gmail credentials. **See best practice for storing credentials below:**

### Storing credentials - best practice
DO NOT store credentials in the source or anywhere in the source tree.

The best way to store credentials is as an environment variable (the same way as the PATH environment variable is stored). To access environment variables within a python script use `os.getenv('name')`.
If you really wish to store the credentials do it outside the source tree to avoid accidental leaks - e.g. accidentally pushing to GitHub.
