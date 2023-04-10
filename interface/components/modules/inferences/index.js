import React from "react";
import PropTypes from "prop-types";

import * as Styles from "./styles";
import Textarea from "../../elements/textarea";
import Button from "../../elements/button";
import Image from "../../elements/image";
import Typography from "../../elements/typography";
import { Add, Remove, Change } from "../../../utils/arr";

function Inferences({ inferences, setInferences }) {
  const lastIndex = inferences.length - 1;

  return (
    <Styles.Container>
      <Typography fontSize="30px" width="auto" tAlign="center" variant="h1">
        Inferences
      </Typography>
      <Styles.Scroll>
        {inferences.map((text, index) => {
          const onChange = (event) =>
            Change(inferences, setInferences, event.target.value, index);

          const remove = () => Remove(inferences, setInferences, index);

          const add = () => Add(inferences, setInferences, "");

          const isLastIndex = lastIndex === index;
          const buttonType = isLastIndex ? "add.svg" : "remove.svg";

          const operation = isLastIndex ? add : remove;

          const key = `query_${index}`;

          return (
            <Styles.HorizontalContainer key={key}>
              <Textarea value={text} onChange={onChange} />
              <Button size="small" variant="image" onClick={operation}>
                <Image
                  alt="button"
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

Inferences.propTypes = {
  inferences: PropTypes.arrayOf(PropTypes.string).isRequired,
  setInferences: PropTypes.func.isRequired,
};

export default Inferences;
