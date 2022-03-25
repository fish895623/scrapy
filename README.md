`config.json` configuration
located on `discord/src/config.json`


steam[] https://steamcommunity.com/app/1245620

```json
{
  "channelID": ["__channelID__"],
  "mongodb": {
    "host": "127.0.0.1",
    "port": "27017",
    "user": "__username__",
    "password": "__password__"
  },
  "token": "__Discord_bot_token__",
  "steam": [
    "__community__app__number ex) 1245620, type) number"
  ]
}
```
```dotenv
TOKEN=discordapp_token
CHANNEL_ID=Text_Channel_Id_To_Upload_noti
DB_HOST=mongodb
DB_PORT=27017
DB_USER=root
DB_PASS=example
STEAM=communityAppNumber
```
## Develop Environment

- Python 3.9
- NodeJs 16.14