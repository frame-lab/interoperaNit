import React, { useState } from "react";
import { useRouter } from "next/router";

import Typography from "../../elements/typography";
import Files from "../../modules/files";
import Button from "../../elements/button";
import Process from "../../modules/process";
import Queries from "../../modules/queries";
import { formatRouterPushObject } from "../../../utils/formatter";
import * as Styles from "./styles";

function Panda() {
  const router = useRouter();
  const [step, setStep] = useState(1);
  const [files, setFiles] = useState([]);
  const [queries, setQueries] = useState([""]);
  const processType = "pandas";

  const nextStep = () => {
    switch (step) {
      case 1:
        if (files.length) setStep(2);
        break;
      case 2: {
        setStep(3);
        const stringfiedQuery = formatRouterPushObject({
          files,
          queries,
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
        break;
      }
      default:
        break;
    }
  };

  const shouldShow = () => {
    switch (step) {
      case 1: {
        const filesText =
          "Drag 'n' drop one file here, or click to select a file\n(Only one *.csv file will be accepted)";
        return (
          <Files
            files={files}
            setFiles={setFiles}
            text={filesText}
            maxFiles={1}
          />
        );
      }
      case 2:
        return <Queries queries={queries} setQueries={setQueries} />;
      case 3:
        return <Process processType={processType} />;
      default:
        return null;
    }
  };

  const showButton = () => {
    return step !== 3 ? (
      <Button onClick={nextStep} size="large" variant="default" width="200px">
        <Typography fontSize={20} width="auto" variant="h1" tAlign="center">
          CONFIRM
        </Typography>
      </Button>
    ) : null;
  };

  return (
    <Styles.Body>
      <Typography fontSize={35} variant="h1">
        Step {step}/3
      </Typography>
      {shouldShow()}
      {showButton()}
    </Styles.Body>
  );
}

export default Panda;
