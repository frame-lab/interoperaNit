import React, { useState } from "react";
import { useRouter } from "next/router";

import Typography from "../../elements/typography";
import Files from "../../modules/files";
import Button from "../../elements/button";
import * as Styles from "./styles";

function Dm() {
  const router = useRouter();
  const [files, setFiles] = useState([]);

  const nextStep = () => {
    if (files.length)
      router.push(
        {
          pathname: "processing",
          query: {
            files: files,
            process: "dm",
          },
        },
        "processing"
      );
  };

  const shouldShow = () => {
    switch (step) {
      case 1:
        const filesText =
          "Drag 'n' drop some files here, or click to select files\n(Only *.csv files will be accepted)";
        return <Files files={files} setFiles={setFiles} text={filesText} />;
      default:
        break;
    }
  };

  return (
    <Styles.Body>
      <Typography fontSize="35px" variant="h1">
        Step {step}/2
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

export default Dm;
