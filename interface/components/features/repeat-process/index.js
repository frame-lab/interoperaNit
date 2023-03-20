import React, { useState } from "react";
import { useRouter } from "next/router";

import Typography from "../../elements/typography";
import Inferences from "../../modules/inferences";
import Button from "../../elements/button";
import Process from "../../modules/process";
import Queries from "../../modules/queries";
import { formatRouterPushObject } from "../../../utils/formatter";
import * as Styles from "./styles";

function RepeatProcess() {
  const router = useRouter();
  const [step, setStep] = useState(1);
  const [queries, setQueries] = useState([""]);
  const [inferences, setInferences] = useState([""]);
  const processType = "repeat";

  const nextStep = () => {
    switch (step) {
      case 1: {
        setStep(2);
        break;
      }
      case 2: {
        setStep(3);
        const stringfiedQuery = formatRouterPushObject({
          queries,
          inferences,
          processType,
        });

        router.push(
          { pathname: "finished", query: { ...stringfiedQuery } },
          "finished"
        );
        break;
      }
      default:
        break;
    }
  };

  const shouldShow = () => {
    switch (step) {
      case 1:
        return <Queries queries={queries} setQueries={setQueries} />;
      case 2:
        return (
          <Inferences inferences={inferences} setInferences={setInferences} />
        );
      case 3:
        return <Process processType={processType} />;
      default:
        return null;
    }
  };

  const showButton = () => {
    return step !== 3 ? (
      <Button onClick={nextStep} size="large" variant="default" width="200px">
        <Typography fontSize="20px" width="auto" variant="h1" tAlign="center">
          CONFIRM
        </Typography>
      </Button>
    ) : null;
  };

  return (
    <Styles.Body>
      <Typography fontSize="35px" variant="h1">
        Step {step}/3
      </Typography>
      {shouldShow()}
      {showButton()}
    </Styles.Body>
  );
}

export default RepeatProcess;
