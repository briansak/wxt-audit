# wxt-audit
Checks Webex Teams rooms looking for individuals registered with generic email services.

This simple script will check your Webex Teams space looking for generic email domains such as gmail.com, hotmail.com, or yahoo.com and will remove them from the room automatically.  This is used to enforce room policies that require that you join with accounts associated with specific email domains or do not allow for generic accounts.

You will need two peices of information for this script to work, your token and the room id.

You can find your bearer token by browsing to https://developer.webex.com/docs/api/getting-started, logging in, and finding your individualized "Personal Access Token" about halfway down that page.

The room id can be found by creating a GET request to https://developer.webex.com/docs/api/v1/rooms/list-rooms and identifying the "id" field associated with the room that you'd like to audit.
