import { exec } from "child_process";

const setCommandAndOptions = (process_type, options) => {
  let command = "";

  switch (process_type) {
    case "alignment":
      command = command.concat("python controler.py");
      break;
    case "dm":
      command = command.concat("python deep.py");
      break;
    case "pandas":
      command = command.concat("python loading.py");
      break;
  }

  for (let option of options) {
    if (option.value) {
      command = command.concat(` ${option.code}`);
    }
  }
  return command;
};

export const runProcess = (dirPath, options, process_type) => {
  const command = setCommandAndOptions(process_type, options);

  return exec(command, { cwd: dirPath }, (error, stdout, stderr) => {
    if (error) {
      console.error(`exec error: ${error}`);
      return;
    }
    if (stderr) {
      console.error(`stderr: ${stderr}`);
      return;
    }
    console.log(`stdout: ${stdout}`);
  });
  console.log(potato);
};
