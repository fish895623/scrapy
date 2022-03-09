const config = require("../../config.json");
import { Client, Intents } from "discord.js";
// const schedule = require("node-schedule");

const client = new Client({
  intents: [Intents.FLAGS.GUILDS, Intents.FLAGS.GUILD_MESSAGES],
});
client.on("ready", (msg: any) => {
  if (client.user != null) {
    console.log(`Logged in as ${client.user.tag}!`);
    // schedule.scheduleJob("* * * * *", () => {
    msg.channels.cache.get("745512829188177931").send("<https://google.com/>");
    // });
  }
});

client.on("messageCreate", (msg) => {
  if (msg.content === "ping") {
    msg.reply("Pong!");
  }
});

client.login(config.token);
