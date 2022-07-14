import React, { useState } from "react";
import { useRouter } from "next/router";

import Typography from "../../elements/typography";
import Files from "../../modules/files";
import Process from "../../modules/process";
import Button from "../../elements/button";
import { formatRouterPushObject } from "../../../utils/formatter";
import * as Styles from "./styles";

function Dm() {
  const router = useRouter();
  const [step, setStep] = useState(1);
  const [files, setFiles] = useState([]);
  const processType = "dm";

  const nextPage = () => {
    if (files.length) {
      setStep(2);
      const stringfiedQuery = formatRouterPushObject({
        files,
        processType,
      });

      const pathname = `${process.env.BACKEND_URL}/finished`;

      setTimeout(() => {
        router.push(
          {
            pathname,
            query: { ...stringfiedQuery },
          },
          `${process.env.BACKEND_URL}/finished`
        );
      }, 5000);
    }
  };

  const shouldShow = () => {
    switch (step) {
      case 1: {
        const filesText =
          "Drag 'n' drop some files here, or click to select files\n(Only *.csv files will be accepted)";
        return <Files files={files} setFiles={setFiles} text={filesText} />;
      }
      case 2:
        return <Process processType={processType} />;
      default:
        return null;
    }
  };

  const showButton = () => {
    return step !== 2 ? (
      <Button onClick={nextPage} size="large" variant="default" width="200px">
        <Typography fontSize={20} width="auto" variant="h1" tAlign="center">
          CONFIRM
        </Typography>
      </Button>
    ) : null;
  };

  return (
    <Styles.Body>
      <Typography fontSize={35} variant="h1">
        Step {step}/2
      </Typography>
      {shouldShow()}
      {showButton()}
    </Styles.Body>
  );
}

export default Dm;
