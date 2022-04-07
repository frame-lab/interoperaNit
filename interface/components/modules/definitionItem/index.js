import React from "react";
import PropTypes from "prop-types";

import * as Styles from "./styles";
import Input from "../../elements/input";
import Button from "../../elements/button";
import Image from "../../elements/image";
import Typography from "../../elements/typography";

function Query({ definition }) {
  const { getter, setter, title } = definition;
  const lastIndex = getter.length - 1;

  return (
    <Styles.Container>
      <Typography fontSize="30px" width="auto" tAlign="center" variant="h1">
        {title}
      </Typography>
      <Styles.Scroll>
        {getter.map((text, index) => {
          const onChange = (event) => {
            const arrCopy = [...getter];
            arrCopy[index] = event.target.value;
            setter(arrCopy);
          };

          const pop = () => {
            const arrCopy = [...getter];
            arrCopy.splice(index, index + 1);
            setter(arrCopy);
          };

          const add = () => {
            const arrCopy = [...getter, ""];
            setter(arrCopy);
          };

          const isLastIndex = lastIndex === index;
          const buttonType = isLastIndex ? "add.svg" : "remove.svg";

          const operation = isLastIndex ? add : pop;

          return (
            <Styles.HorizontalContainer key={index}>
              <Input
                value={text}
                onChange={onChange}
                border="transparent"
                borderRadius="10px"
              />
              <Button size="small" variant="image" onClick={operation}>
                <Image
                  image={buttonType}
                  filter="brightness(0) invert(1)"
                  width="30px"
                  height="30px"
                  size="cover"
                />
              </Button>
            </Styles.HorizontalContainer>
          );
        })}
      </Styles.Scroll>
    </Styles.Container>
  );
}

Query.propTypes = {
  definition: PropTypes.objectOf(PropTypes.any),
};

export default Query;
