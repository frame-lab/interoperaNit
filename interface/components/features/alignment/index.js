import React, { useState } from "react";

import Typography from "../../elements/typography";
import Definitions from "../../modules/definitions";
import Files from "../../modules/files";
import Queries from "../../modules/queries";
import Processing from "../../modules/processing";
import Button from "../../elements/button";
import * as Styles from "./styles";

function Alignment() {
  const [step, setStep] = useState(1);
  const [files, setFiles] = useState([]);
  const [unique, setUnique] = useState([""]);
  const [split, setSplit] = useState([""]);
  const [approximate, setApproximate] = useState([""]);
  const [queries, setQueries] = useState([""]);
  const [options, setOptions] = useState([
    { title: "Approximate", value: false },
    { title: "Synonym", value: false },
    { title: "Translation", value: false },
    { title: "Distance", value: false },
    { title: "Max", value: false },
    { title: "Verbose", value: false },
    { title: "Validate", value: false },
    { title: "Deep matcher", value: false },
  ]);

  const nextStep = () => {
    setStep(step + 1);
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
      case 2:
        return <Files files={files} setFiles={setFiles} />;
      case 3:
        return <Queries queries={queries} setQueries={setQueries} />;
      case 4:
        return <Processing />;
      default:
        break;
    }
  };

  return (
    <Styles.Body>
      <Typography fontSize="35px" variant="h1">
        Step {step}/4
      </Typography>
      {shouldShow()}
      <Button onClick={nextStep} size="large" variant="default" width="200px">
        <Typography fontSize="20px" width="auto" variant="h1">
          CONFIRM
        </Typography>
      </Button>
    </Styles.Body>
  );
}

export default Alignment;
