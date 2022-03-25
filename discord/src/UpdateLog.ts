const host = process.env.DB_HOST;
const port = process.env.DB_PORT;
const user = process.env.DB_USER;
const pass = process.env.DB_PASS;

import mongoose, { Schema } from "mongoose";

const url = `mongodb://${host}:${port}/`;

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
   * @param date Set date to search
   * @returns name, address, title, content, date
   */
  getRawData(date: string) {
    // TODO Change types
    // TODO Set Logger
    return new Promise((resolve, reject) => {
      mongoose.connect(
        url,
        { user: `${user}`, pass: `${pass}`, dbName: "steam" },
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

const date = new Date();

export { ContentMongoDB, date };
