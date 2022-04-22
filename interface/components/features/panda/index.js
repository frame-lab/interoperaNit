import React, { useState } from "react";
import { useRouter } from "next/router";

import Typography from "../../elements/typography";
import Files from "../../modules/files";
import Button from "../../elements/button";
import Queries from "../../modules/queries";
import * as Styles from "./styles";

function Panda() {
  const router = useRouter();
  const [step, setStep] = useState(1);
  const [files, setFiles] = useState([]);
  const [queries, setQueries] = useState([""]);

  const nextStep = () => {
    switch (step) {
      case 1:
        if (files.length) setStep(2);
        break;
      case 2:
        router.push(
          {
            pathname: "processing",
            query: {
              files: files,
              queries: queries,
              process: "pandas",
            },
          },
          "processing"
        );
        break;
      default:
        break;
    }
  };

  const shouldShow = () => {
    switch (step) {
      case 1:
        const filesText =
          "Drag 'n' drop one file here, or click to select a file\n(Only *.csv files will be accepted)";
        return (
          <Files
            files={files}
            setFiles={setFiles}
            text={filesText}
            maxFiles={1}
          />
        );
      case 2:
        return <Queries queries={queries} setQueries={setQueries} />;
      default:
        break;
    }
  };

  return (
    <Styles.Body>
      <Typography fontSize="35px" variant="h1">
        Step {step}/3
      </Typography>
      {shouldShow()}
      <Button onClick={nextStep} size="large" variant="default" width="200px">
        <Typography fontSize="20px" width="auto" variant="h1" tAlign="center">
          CONFIRM
        </Typography>
      </Button>
    </Styles.Body>
  );
}

export default Panda;
