import React from "react";
import PropTypes from "prop-types";

import * as Styles from "./styles";
import Typography from "../../elements/typography";
import FileItem from "../fileItem";
import Image from "../../elements/image";
import { Remove } from "../../../utils/arr";

function Files({ files, setFiles, text, maxFiles }) {
  const download =
    process.env.NODE_ENV === "production"
      ? `${process.env.BACKEND_URL}/download.svg`
      : "download.svg";

  const addDummy = () => {
    if (!maxFiles || files.length < maxFiles)
      setFiles([...files, { name: "test" }]);
  };

  return (
    <Styles.Container>
      <Typography fontSize="30px" width="auto" tAlign="center" variant="h1">
        Files
      </Typography>
      <Styles.HorizontalContainer>
        <Styles.DragArea onClick={addDummy}>
          <Image
            image={download}
            width="150px"
            height="150px"
            size="cover"
            alt="download"
          />
          <Typography
            lineHeight="120%"
            fontSize="30px"
            width="65%"
            tAlign="center"
            variant="h1"
          >
            {text}
          </Typography>
        </Styles.DragArea>
        <Styles.VerticalContainer>
          <Typography
            margin="0 0 20px 0"
            fontSize="20px"
            width="150px"
            tAlign="center"
            variant="h1"
          >
            File input
          </Typography>
          <Styles.Scroll>
            {files.map((file, index) => {
              const removeFile = () => Remove(files, setFiles, index);
              const fileItemKey = `fileItem_${index}`;

              return (
                <FileItem
                  file={file}
                  removeFile={removeFile}
                  key={fileItemKey}
                />
              );
            })}
          </Styles.Scroll>
        </Styles.VerticalContainer>
      </Styles.HorizontalContainer>
    </Styles.Container>
  );
}

Files.propTypes = {
  files: PropTypes.arrayOf(PropTypes.shape({})).isRequired,
  setFiles: PropTypes.func.isRequired,
  text: PropTypes.string.isRequired,
  maxFiles: PropTypes.number,
};

Files.defaultProps = {
  maxFiles: 0,
};

export default Files;
