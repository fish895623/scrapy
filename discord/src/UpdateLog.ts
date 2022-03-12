// To export Update log
var { mongodb } = require("../../config.json").config;
const db = mongodb;
import mongoose from "mongoose";

mongoose.connect(`mongodb://${db.user}:${db.password}@${db.host}:${db.port}`);
const Fruit = mongoose.model(
  "steam",
  new mongoose.Schema({
    name: String,
    address: String,
    title: String,
    content: String,
  })
);

Fruit.find({ name: "rimworld" }, function (err, docs) {
  console.log(err, docs);
});
mongoose.connection.close();
