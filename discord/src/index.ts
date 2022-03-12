const config = require("../../config.json");
const db = config.mongodb;

import { Client, Intents } from "discord.js";
import mongoose from "mongoose";
// const schedule = require("node-schedule");

mongoose.connect(`mongodb://${db.user}:${db.password}@${db.host}:${db.port}`);

const client = new Client({
  intents: [Intents.FLAGS.GUILDS, Intents.FLAGS.GUILD_MESSAGES],
});

client.on("ready", (msg: any) => {
  if (client.user != null) {
    console.log(`Logged in as ${client.user.tag}!`);
    // schedule.scheduleJob("* * * * *", () => {
    msg.channels.cache
      .get(`${config.channelID[0]}`)
      .send("asdf\n<https://google.com/>");
    // });
    console.log(config.channelID[0]);
  }
});

// client.on("messageCreate", (msg: any) => {
//   if (msg.content === "ping") {
//     msg.reply("Pong!");
//   }
// });

client.login(config.token);
