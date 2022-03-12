var { channelID, token } = require("../../config.json").config;

import { Client, Intents } from "discord.js";
// const schedule = require("node-schedule");

const client = new Client({
  intents: [Intents.FLAGS.GUILDS, Intents.FLAGS.GUILD_MESSAGES],
});

client.on("ready", (msg: any) => {
  if (client.user != null) {
    console.log(`Logged in as ${client.user.tag}!`);
    // schedule.scheduleJob("* * * * *", () => { // TODO Call from
    msg.channels.cache
      .get(`${channelID[0]}`)
      .send("asdf\n<https://google.com/>");
    // });
    console.log(channelID[0]);
  }
});

client.login(token);
