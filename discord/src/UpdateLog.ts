import { mongodb } from "./config.json";
const db = mongodb;

import mongoose from "mongoose";
const Schema = mongoose.Schema;

var url = `mongodb://${db.host}:${db.port}/`;

class ContentMongoDB {
  private modelPerson = mongoose.model(
    "steam",
    new Schema(
      { name: String, title: String, date: String, address: String }, // NOTE need this to find type
      { collection: "steam" }
    )
  );

  /**
   * @example
   * new ContentMongoDB().getContent("2022-03-14").then((data: any) => {
   *   data.forEach((element: any) => {
   *     console.log(element);
   *   });
   *   logger.info("Get Data");
   * });
   * @param _date Set date to search
   * @returns name, address, title, content, date
   */
  getRawData(_date: string) { // TODO Change types
    return new Promise((resolve, reject) => {
      mongoose.connect(
        url,
        { user: `${db.user}`, pass: `${db.password}`, dbName: "steam" },
        async (err: any) => {
          if (err) {
            reject(err);
          }
          resolve(await this.modelPerson.find({ date: _date }));
          await mongoose.connection.close();
        }
      );
    });
  }
}

const TodayDate = new Date();

export { ContentMongoDB, TodayDate };
