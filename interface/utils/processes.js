import { exec } from "child_process";

export const runCode = (dirPath, options, process) => {
  const command = `cd ${dirPath}`;

  switch (process) {
    case "alignment":
      command.concat(" \n python controler.py");
      break;
    case "dm":
      command.concat(" \n python deep.py");
      break;
    case "pandas":
      command.concat(" \n python loading.py");
      break;
  }

  for (var option in options) {
    if (option.value) {
      command.concat(` ${option.code}`);
    }
  }

  exec(command, (error, _, stderr) => {
    if (error) {
      console.log(`error: ${error.message}`);
      return;
    }
    if (stderr) {
      console.log(`stderr: ${stderr}`);
      return;
    }
    return 0;
  });
};
