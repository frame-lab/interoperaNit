import React, { useState } from "react";
import { useRouter } from "next/router";

import Typography from "../../elements/typography";
import Definitions from "../../modules/definitions";
import Process from "../../modules/process";
import Files from "../../modules/files";
import Queries from "../../modules/queries";
import Inferences from "../../modules/inferences";
import Button from "../../elements/button";
import { formatRouterPushObject } from "../../../utils/formatter";
import * as Styles from "./styles";

function Alignment() {
  const router = useRouter();
  const [step, setStep] = useState(1);
  const [files, setFiles] = useState([]);
  const [unique, setUnique] = useState([""]);
  const [split, setSplit] = useState([""]);
  const [approximate, setApproximate] = useState([""]);
  const [queries, setQueries] = useState([""]);
  const [inferences, setInferences] = useState([""]);
  const [options, setOptions] = useState([
    { title: "Approximate", value: false, code: "-a" },
    { title: "Synonym", value: false, code: "-s" },
    { title: "Translation", value: false, code: "-t" },
    { title: "Distance", value: false, code: "-e", percent: "75" },
    { title: "Max", value: false, code: "-max" },
    { title: "Verbose", value: false, code: "-v" },
    { title: "Validate", value: false, code: "-val" },
    { title: "Deep matcher", value: false, code: "-dm" },
  ]);
  const optionSelected = options.some((element) => element.value);
  const processType = "alignment";

  const nextStep = () => {
    switch (step) {
      case 1:
        if (optionSelected) setStep(2);
        break;
      case 2:
        if (files.length) setStep(3);
        break;
      case 3: {
        setStep(4);
        break;
      }
      case 4: {
        setStep(5);
        const stringfiedQuery = formatRouterPushObject({
          approximate,
          files,
          options,
          queries,
          inferences,
          split,
          unique,
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

  const definitionList = [
    { getter: unique, setter: setUnique, title: "Unique" },
    { getter: split, setter: setSplit, title: "Split" },
    {
      getter: approximate,
      setter: setApproximate,
      title: "Approximate",
    },
  ];

  const shouldShow = () => {
    switch (step) {
      case 1:
        return (
          <Definitions
            definitionList={definitionList}
            options={options}
            setOptions={setOptions}
          />
        );
      case 2: {
        const filesText =
          "Drag 'n' drop some files here, or click to select files\n(Only *.csv files will be accepted)";
        return <Files files={files} setFiles={setFiles} text={filesText} />;
      }
      case 3:
        return <Queries queries={queries} setQueries={setQueries} />;
      case 4:
        return (
          <Inferences inferences={inferences} setInferences={setInferences} />
        );
      case 5:
        return <Process processType={processType} />;
      default:
        return <> </>;
    }
  };

  const showButton = () => {
    return step !== 5 ? (
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
        Step {step}/5
      </Typography>
      {shouldShow()}
      {showButton()}
    </Styles.Body>
  );
}

export default Alignment;
