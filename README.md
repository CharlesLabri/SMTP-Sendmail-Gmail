This is a sendmail script that will send mail out as many times as you want to Cron it.

Put this file up on a server, set it executable, and have it run on a cron timer.

cron might look like this:

*/5 * * * * /path.to/python /path.to/SMTP-Sendmail-Gmail.py # every 5 minutes


Its going to send you an email with a 'fake' nagios message saying the current time and that your server is ok.

This will get the GMAIL POP3 timer down on your account to an acceptable timeframe.