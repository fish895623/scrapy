// To export Update log
const config = require("../../config.json");
const db = config.mongodb;

import mongoose from "mongoose";
const Schema = mongoose.Schema;

import log4js from "log4js";
const logger = log4js.getLogger();
log4js.configure({
  appenders: { cheese: { type: "file", filename: "cheese.log" } },
  categories: { default: { appenders: ["cheese"], level: "trace" } },
});

var url = `mongodb://${db.user}:${db.password}@${db.host}:${db.port}`;

var Person = new Schema({ data: Number });
var modelPerson = mongoose.model("steams", Person);

mongoose.connection
  .on("error", (err: any) => {
    logger.warn(err);
  })
  .once("open", () => {
    logger.debug("DB Connected");
  });

function getContent() {
  return new Promise((resolve, reject) => {
    mongoose.connect(url, async (err: any) => {
      if (err) console.error(err);
      var a = await modelPerson.find({ data: 123 });
      resolve(a);
      await mongoose.connection.close();
    });
  });
}

getContent().then((data) => {
  logger.debug(data);
  logger.info("Get Data");
});
