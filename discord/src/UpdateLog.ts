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

var url = `mongodb://${db.host}:${db.port}/`;

class ContentMongoDB {
  private modelPerson = mongoose.model(
    "steams",
    new Schema({ date: String }, { collection: "steam" })
  );
  /**
   * @example
   * new ContentMongoDB().getContent("2022-03-14").then((data: any) => {
   *   data.forEach((element: any) => {
   *     console.log(element);
   *   });
   *   logger.info("Get Data");
   * });
   * @param date Set date to search
   * @returns name, address, title, content, date
   */
  getContent(date: string) {
    return new Promise((resolve, reject) => {
      mongoose.connect(
        url,
        { user: `${db.user}`, pass: `${db.password}`, dbName: "steam" },
        async (err: any) => {
          if (err) {
            reject(err);
          }
          resolve(await this.modelPerson.find({ date: date }));
          await mongoose.connection.close();
        }
      );
    });
  }
}

mongoose.connection
  .on("error", (err: any) => {
    logger.error(err);
  })
  .once("open", () => {
    logger.debug("DB Connected");
  });

new ContentMongoDB().getContent("2022-03-14").then((data: any) => {
  data.forEach((element: any) => {
    console.log(element);
  });
  logger.info("Get Data");
});

export { ContentMongoDB };
