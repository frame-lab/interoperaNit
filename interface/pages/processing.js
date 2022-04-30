import fs from "fs";

import Process from "../components/features/process";
import { unformatRouterPushObject } from "../utils/formatter";

export default function processing() {
  return (
    <>
      <Process />
    </>
  );
}

export async function getServerSideProps(context) {
  const unformatedQuery = unformatRouterPushObject(context.query);
  const { files, unique, split, approximate, queries, options, process } =
    unformatedQuery;
  const dirPath = "../interopera";

  const fillFile = (textArray, path) => {
    if (textArray && textArray.length) {
      const filePath = `${dirPath}/${path}`;
      const fileText = textArray.join("\n");
      fs.writeFileSync(filePath, fileText);
    }
  };

  fillFile(unique, "unique");
  fillFile(split, "split");
  fillFile(approximate, "approximate");
  fillFile(queries, "queries");

  const cleanFolder = (folderPath) => {
    const foundFiles = fs.readdirSync(folderPath);

    for (var file of foundFiles) {
      fs.unlinkSync(`${folderPath}/${file}`);
    }
  };

  const makeFolderAndFiles = (folderPath) => {
    fs.mkdirSync(folderPath, { recursive: true });
    cleanFolder(folderPath);

    for (var file of files) {
      const filePath = `${folderPath}/${file.name}`;
      fs.writeFileSync(filePath, file.text);
    }
  };

  const generateFiles = (type) => {
    switch (type) {
      case "alignment":
        makeFolderAndFiles(`${dirPath}/samples`);
        break;
      case "dm":
        makeFolderAndFiles(`${dirPath}/csv`);
        break;
      case "pandas":
        makeFolderAndFiles(`${dirPath}/csv`);
        break;
    }
  };

  generateFiles(process);

  if (options) {
    return { props: { options: options, process: process } };
  }

  return { props: { process: process } };
}
