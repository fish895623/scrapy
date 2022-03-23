import path from "path";
import { channelID, token } from "./config.json";

import { Client, Intents } from "discord.js";
import { ContentMongoDB, date } from "./UpdateLog";
// const schedule = require("node-schedule");

// NOTE Interface
import { Content } from "./interface/Contents";

import log4js from "log4js";
log4js.configure(path.join(__dirname, "log4js.json"));

const logger = log4js.getLogger("logTest");

const client = new Client({
  intents: [Intents.FLAGS.GUILDS, Intents.FLAGS.GUILD_MESSAGES],
});

client.on("ready", async (msg: any) => {
  if (client.user != null) {
    console.log(`Logged in as ${client.user.tag}!`);
    // TODO Call from
    // schedule.scheduleJob("* * * * *", () => {
    const Data = new ContentMongoDB();
    const dataFromMongo: any = await new Promise((resolve) => {
      Data.getRawData(
        `${date.getFullYear()}-${date.getMonth() + 1}-${date.getDate()}`
      ).then((data: any) => {
        resolve(data);
      });
    });
    dataFromMongo.forEach((element: Content) => {
      // TODO Set interface content interface
      logger.info("Data Send");
      msg.channels.cache
        .get(`${channelID[0]}`)
        .send(`*${element.title}*\n\n\n${element.name}\n${element.address}`);
    });
  }
});

client.login(token).then((res) => logger.info(res));
