import React from "react";
import PropTypes from "prop-types";

import Finish from "../components/features/finish";
import { unformatRouterPushObject } from "../utils/formatter";
import { fillFile, makeFolderAndFiles } from "../utils/file";
import { runProcess } from "../utils/processes";
import { verifyToolErrors } from "../utils/errors";

export default function Finished({ processType, haveQueries, error }) {
  return (
    <>
      <Finish
        processType={processType}
        haveQueries={haveQueries}
        error={error}
      />
    </>
  );
}

Finished.propTypes = {
  processType: PropTypes.string,
  haveQueries: PropTypes.bool,
  error: PropTypes.string,
};

Finished.defaultProps = {
  processType: null,
  haveQueries: null,
  error: null,
};

export async function getServerSideProps(context) {
  const unformatedQuery = unformatRouterPushObject(context.query);
  const { files, unique, split, approximate, queries, options, processType } =
    unformatedQuery;
  const dirPath = "../interopera";

  fillFile(unique, "unique", dirPath);
  fillFile(split, "split", dirPath);
  fillFile(approximate, "approximate", dirPath);
  if (processType === "alignment") fillFile(queries, "queries", dirPath);

  switch (processType) {
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

  try {
    await runProcess(dirPath, options, processType, queries);
  } catch (error) {
    const errorText = verifyToolErrors(error);

    return {
      props: {
        error: errorText,
      },
    };
  }

  const haveQueries =
    Array.isArray(queries) &&
    queries.filter((query) => query !== "").length > 0;

  return {
    props: {
      processType: processType,
      haveQueries: haveQueries,
    },
  };
}
