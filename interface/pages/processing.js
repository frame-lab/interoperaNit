import PropTypes from "prop-types";

import Process from "../components/features/process";
import { unformatRouterPushObject } from "../utils/formatter";
import { fillFile, makeFolderAndFiles } from "../utils/file";
import { runCode } from "../utils/processes";

export default function Processing({ process }) {
  return (
    <>
      <Process process={process} />
    </>
  );
}

Processing.propTypes = {
  process: PropTypes.string.isRequired,
};

export async function getServerSideProps(context) {
  const unformatedQuery = unformatRouterPushObject(context.query);
  const { files, unique, split, approximate, queries, options, process } =
    unformatedQuery;
  const dirPath = "../interopera";

  fillFile(unique, "unique", dirPath);
  fillFile(split, "split", dirPath);
  fillFile(approximate, "approximate", dirPath);
  fillFile(queries, "queries", dirPath);

  switch (process) {
    case "alignment":
      makeFolderAndFiles(`${dirPath}/samples`, files);
      break;
    case "dm":
      makeFolderAndFiles(`${dirPath}/csv`, files);
      break;
    case "pandas":
      makeFolderAndFiles(`${dirPath}/csv`, files);
      break;
  }

  const activeProcess = runCode(dirPath, options, process);

  return { props: { process: process } };
}
