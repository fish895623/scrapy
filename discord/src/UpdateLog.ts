// To export Update log
const config = require("../../config.json");
const db = config.mongodb;

import mongoose from "mongoose";
const Schema = mongoose.Schema;

var url = `mongodb://${db.user}:${db.password}@${db.host}:${db.port}`;

var Person = new Schema({ data: Number });
var modelPerson = mongoose.model("steams", Person);

mongoose.connect(url, async (err: any) => {
  if (err) console.error(err);
  var a = await modelPerson.find({ data: 123 });
  console.log(a);
  await mongoose.connection.close();
});

mongoose.connection
  .on("error", (err: any) => {
    console.warn(err);
  })
  .once("open", () => {
    console.log("DB Connected");
  });
