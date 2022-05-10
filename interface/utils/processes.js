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
    }
  }
  return command;
};

export const runProcess = (dirPath, options, processType, queries) => {
  const execPromise = util.promisify(exec);
  const command = setCommandAndOptions(processType, options, queries);
  try {
    return execPromise(command, { cwd: dirPath });
  } catch (e) {
    console.error(e);
  }
};
