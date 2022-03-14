import { channelID, token } from "./config.json";

import { Client, Intents } from "discord.js";
import { ContentMongoDB, date } from "./UpdateLog";
// const schedule = require("node-schedule");

const client = new Client({
  intents: [Intents.FLAGS.GUILDS, Intents.FLAGS.GUILD_MESSAGES],
});

client.on("ready", async (msg: any) => {
  if (client.user != null) {
    console.log(`Logged in as ${client.user.tag}!`);
    // schedule.scheduleJob("* * * * *", () => { // TODO Call from
    const Data = new ContentMongoDB();
    await Data.getRawData(
      `${date.getFullYear()}-${date.getMonth() + 1}-${date.getDate()}`
    ).then((data: any) => {
      data.forEach((element: any) => {
        console.log(element);
      });
    });
    msg.channels.cache
      .get(`${channelID[0]}`)
      .send("asdf\n<https://google.com/>");
    // });
    console.log(channelID[0]);
  }
});

client.login(token);
