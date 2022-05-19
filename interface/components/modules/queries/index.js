import React from "react";
import PropTypes from "prop-types";

import * as Styles from "./styles";
import Textarea from "../../elements/textarea";
import Button from "../../elements/button";
import Image from "../../elements/image";
import Typography from "../../elements/typography";
import { Add, Remove, Change } from "../../../utils/arr";

function Queries({ queries, setQueries }) {
  const lastIndex = queries.length - 1;

  return (
    <Styles.Container>
      <Typography fontSize="30px" width="auto" tAlign="center" variant="h1">
        Queries
      </Typography>
      <Styles.Scroll>
        {queries.map((text, index) => {
          const onChange = (event) =>
            Change(queries, setQueries, event.target.value, index);

          const remove = () => Remove(queries, setQueries, index);

          const add = () => Add(queries, setQueries, "");

          const isLastIndex = lastIndex === index;
          const buttonType = isLastIndex ? "add.svg" : "remove.svg";

          const operation = isLastIndex ? add : remove;

          return (
            <Styles.HorizontalContainer key={index}>
              <Textarea
                value={text}
                onChange={onChange}
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
  queries: PropTypes.arrayOf(PropTypes.any).isRequired,
  setQueries: PropTypes.func.isRequired,
};

export default Queries;
