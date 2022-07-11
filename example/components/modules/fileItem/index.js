import React from "react";
import PropTypes from "prop-types";

import * as Styles from "./styles";
import Button from "../../elements/button";
import Image from "../../elements/image";
import Typography from "../../elements/typography";

function FileItem({ file, removeFile }) {
  const remove =
    process.env.NODE_ENV === "production"
      ? `${process.env.BACKEND_URL}/remove.svg`
      : "remove.svg";
  const fileImage =
    process.env.NODE_ENV === "production"
      ? `${process.env.BACKEND_URL}/file.svg`
      : "file.svg";

  return (
    <Styles.Container>
      <Styles.VerticalContainer>
        <Image
          image={fileImage}
          width="50px"
          height="50px"
          size="cover"
          alt="file"
        />
        <Typography
          fontSize="20px"
          width="110px"
          variant="body1"
          whiteSpace="nowrap"
          textOverflow="ellipsis"
          overflow="hidden"
          margin="10px 100px 0 0"
        >
          {file.name}
        </Typography>
      </Styles.VerticalContainer>
      <Button size="small" variant="image" onClick={removeFile}>
        <Image
          alt="remove"
          image={remove}
          filter="brightness(0) invert(1)"
          width="30px"
          height="30px"
          size="cover"
        />
      </Button>
    </Styles.Container>
  );
}

FileItem.propTypes = {
  file: PropTypes.shape({}).isRequired,
  removeFile: PropTypes.func.isRequired,
};

export default FileItem;
