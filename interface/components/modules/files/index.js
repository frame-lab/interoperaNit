import React, { useEffect } from "react";
import PropTypes from "prop-types";
import { useDropzone } from "react-dropzone";

import * as Styles from "./styles";
import Typography from "../../elements/typography";
import FileItem from "../fileItem";
import Image from "../../elements/image";
import { Remove } from "../../../utils/arr";

function Files({ files, setFiles, text, maxFiles }) {
  const { getRootProps, acceptedFiles } = useDropzone({
    accept: ".csv",
    maxFiles: maxFiles,
  });
  const download = "download.svg";

  useEffect(() => {
    setFiles([...files, ...acceptedFiles]);
  }, [acceptedFiles]);

  return (
    <Styles.Container>
      <Typography fontSize="30px" width="auto" tAlign="center" variant="h1">
        Files
      </Typography>
      <Styles.HorizontalContainer>
        <Styles.DragArea {...getRootProps({ refKey: "innerRef" })}>
          <Image image={download} width="150px" height="150px" size="cover" />
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
              return (
                <FileItem file={file} removeFile={removeFile} key={index} />
              );
            })}
          </Styles.Scroll>
        </Styles.VerticalContainer>
      </Styles.HorizontalContainer>
    </Styles.Container>
  );
}

Files.propTypes = {
  files: PropTypes.arrayOf(PropTypes.any).isRequired,
  setFiles: PropTypes.func.isRequired,
  text: PropTypes.string.isRequired,
  maxFiles: PropTypes.number,
};

Files.defaultProps = {
  maxFiles: 0,
};

export default Files;
