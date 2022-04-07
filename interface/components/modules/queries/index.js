import React from "react";
import PropTypes from "prop-types";

import * as Styles from "./styles";
import Input from "../../elements/input";
import Button from "../../elements/button";
import Image from "../../elements/image";
import Typography from "../../elements/typography";

function Queries({ queries, setQueries }) {
  const lastIndex = queries.length - 1;

  return (
    <Styles.Container>
      <Typography fontSize="30px" width="auto" tAlign="center" variant="h1">
        Queries
      </Typography>
      <Styles.Scroll>
        {queries.map((text, index) => {
          const onChange = (event) => {
            const arrCopy = [...queries];
            arrCopy[index] = event.target.value;
            setQueries(arrCopy);
          };

          const pop = () => {
            const arrCopy = [...queries];
            arrCopy.splice(index, index + 1);
            setQueries(arrCopy);
          };

          const add = () => {
            const arrCopy = [...queries, ""];
            setQueries(arrCopy);
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

Queries.propTypes = {
  queries: PropTypes.arrayOf(PropTypes.any),
  setQueries: PropTypes.func,
};

export default Queries;
