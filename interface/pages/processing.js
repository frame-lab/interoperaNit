import PropTypes from "prop-types";

import Process from "../components/features/process";
import { unformatRouterPushObject } from "../utils/formatter";
import { fillFile, makeFolderAndFiles } from "../utils/file";
import { runProcess } from "../utils/processes";

export default function Processing({ process_type }) {
  return (
    <>
      <Process process_type={process_type} />
    </>
  );
}

Processing.propTypes = {
  process_type: PropTypes.string.isRequired,
};

export async function getServerSideProps(context) {
  const unformatedQuery = unformatRouterPushObject(context.query);
  const { files, unique, split, approximate, queries, options, process_type } =
    unformatedQuery;
  const dirPath = "../interopera";

  fillFile(unique, "unique", dirPath);
  fillFile(split, "split", dirPath);
  fillFile(approximate, "approximate", dirPath);
  fillFile(queries, "queries", dirPath);

  switch (process_type) {
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
  
  const runningProcess = runProcess(dirPath, options, process_type);

  return { props: { process_type: process_type, runningProcess: runningProcess } };
}
