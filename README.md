# PLEX DOCTOR
- Connects to plex to get a list of servers that are associated with the account set in the config.
- Tries connecting to the server, if any are successful it tries to do healthcheck.
- if healthcheck is invalid it tries to reboot.


# HEALTH CHECK
- Get first libary and tries listing it.
- More?

## Requirements 
- Plex 3.8 or above
- Python 3.7+


## Plans to add
- Notifications - Email, Discord, Slack
- Read from logs what went wrong with plex and notify user
- Scheduling so we can run it as a service
- Check for more things that could be going wrong. Possible to test a short video transcode/direct stream?
