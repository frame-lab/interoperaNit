import React, { useState } from "react";
import { useRouter } from "next/router";

import Typography from "../../elements/typography";
import Files from "../../modules/files";
import Button from "../../elements/button";
import { formatRouterPushObject } from "../../../utils/formatter";
import * as Styles from "./styles";

function Dm() {
  const router = useRouter();
  const [files, setFiles] = useState([]);

  const nextPage = () => {
    if (files.length) {
      const stringfiedQuery = formatRouterPushObject({
        files: files,
        process: "dm",
      });

      router.push(
        { pathname: "processing", query: { ...stringfiedQuery } },
        "processing"
      );
    }
  };

  const shouldShow = () => {
    const filesText =
      "Drag 'n' drop some files here, or click to select files\n(Only *.csv files will be accepted)";
    return <Files files={files} setFiles={setFiles} text={filesText} />;
  };

  return (
    <Styles.Body>
      <Typography fontSize="35px" variant="h1">
        Select Files
      </Typography>
      {shouldShow()}
      <Button onClick={nextPage} size="large" variant="default" width="200px">
        <Typography fontSize="20px" width="auto" variant="h1" tAlign="center">
          CONFIRM
        </Typography>
      </Button>
    </Styles.Body>
  );
}

export default Dm;
