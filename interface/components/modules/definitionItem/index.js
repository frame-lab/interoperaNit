import React from "react";
import PropTypes from "prop-types";

import * as Styles from "./styles";
import Input from "../../elements/input";
import Button from "../../elements/button";
import Image from "../../elements/image";
import Typography from "../../elements/typography";
import { Add, Remove, Change } from "../../../utils/arr";

function DefinitionItem({ definition }) {
  const { getter, setter, title } = definition;
  const lastIndex = getter.length - 1;

  return (
    <Styles.Container>
      <Typography fontSize="30px" width="auto" tAlign="center" variant="h1">
        {title}
      </Typography>
      <Styles.Scroll>
        {getter.map((text, index) => {
          const onChange = (event) =>
            Change(getter, setter, event.target.value, index);

          const remove = () => Remove(getter, setter, index);

          const add = () => Add(getter, setter, "");

          const isLastIndex = lastIndex === index;
          const buttonType = isLastIndex ? "add.svg" : "remove.svg";

          const operation = isLastIndex ? add : remove;

          const definitionItemKey = `definitionItem_${index}`;

          return (
            <Styles.HorizontalContainer key={definitionItemKey}>
              <Input value={text} onChange={onChange} />
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

DefinitionItem.propTypes = {
  definition: PropTypes.shape({}).isRequired,
};

export default DefinitionItem;
