var exec = require("child_process").exec;

exec(
  "cd crawling && scrapy crawl `scrapy list`",
  function (error, stdout, stderr) {
    console.log("stdout: " + stdout);
    console.log("stderr: " + stderr);
    if (error !== null) {
      console.log("exec error: " + error);
    }
  }
);
