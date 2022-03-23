import { channelID, token } from "./config.json";

import { Client, Intents } from "discord.js";
import { ContentMongoDB, date } from "./UpdateLog";
// const schedule = require("node-schedule");
import { Content } from "./interface/Contents";

const client = new Client({
  intents: [Intents.FLAGS.GUILDS, Intents.FLAGS.GUILD_MESSAGES],
});

client.on("ready", async (msg: any) => {
  if (client.user != null) {
    console.log(`Logged in as ${client.user.tag}!`);
    // schedule.scheduleJob("* * * * *", () => { // TODO Call from
    const Data = new ContentMongoDB();
    const a: any = await new Promise((resolve) => {
      Data.getRawData(
        `${date.getFullYear()}-${date.getMonth() + 1}-${date.getDate()}`
      ).then((data: any) => {
        resolve(data);
      });
    });
    a.forEach((element: Content) => {
      // TODO set interface content interface
      msg.channels.cache
        .get(`${channelID[0]}`)
        .send(`*${element.title}*\n\n\n${element.name}\n${element.address}`);
    });
    console.log(channelID[0]);
  }
});

client.login(token);
