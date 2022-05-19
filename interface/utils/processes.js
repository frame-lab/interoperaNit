import { exec } from "child_process";
import util from "util";

const setCommandAndOptions = (processType, options, queries) => {
  let command = "";

  switch (processType) {
    case "alignment":
      command = command.concat("python controler.py");
      break;
    case "dm":
      command = command.concat("python deep.py");
      break;
    case "pandas":
      command = command.concat("python loading.py");
      for (let index = 0; index < queries.length; index++) {
        if (query[index]) {
          const splittedQuery = query.split(" ");
          if (splittedQuery[0].toUpperCase() === "SELECT") {
            command = command.concat(`\npandaSQL("${query}")`);
            command = command.concat(`\nexport2CSV("/results/query${index}")`);
          } else {
            command = command.concat(`\npandaBoolean("${query}")`);
            command = command.concat(`\nexport2CSV("/results/query${index}")`);
          }
        }
      }
      break;
  }

  for (let option of options) {
    if (option.value) {
      command = command.concat(` ${option.code}`);
      if (!isNaN(options.percent) && !isNaN(parseFloat(options.percent))) {
        command = command.concat(` ${option.percent}`);
      }
    }
  }
  return command;
};

export const runProcess = (dirPath, options, processType, queries) => {
  const command = setCommandAndOptions(processType, options, queries);
  return new Promise((resolve, reject) => {
    exec(command, { cwd: dirPath }, (error, stdout, stderr) => {
      if (error) {
        reject(error);
      }
      resolve(stdout ? stdout : stderr);
    });
  });
};
