import fs from "fs";

export const fillFile = (textArray, path, dirPath) => {
  if (textArray && textArray.length) {
    const filePath = `${dirPath}/${path}`;
    const fileText = textArray.join("\n");
    fs.writeFileSync(filePath, fileText);
  }
};

export const cleanFolder = (folderPath) => {
  const foundFiles = fs.readdirSync(folderPath);

  for (let file of foundFiles) {
    fs.unlinkSync(`${folderPath}/${file}`);
  }
};

export const makeFolderAndFiles = (folderPath, files) => {
  fs.mkdirSync(folderPath, { recursive: true });
  cleanFolder(folderPath);

  for (let file of files) {
    const filePath = `${folderPath}/${file.name}`;
    fs.writeFileSync(filePath, file.text);
  }
};
