import React from "react";
import PropTypes from "prop-types";

import * as Styles from "./styles";
import DefinitionItem from "../definitionItem";
import OptionItem from "../optionItem";

function Definitions({ definitionList, options, setOptions }) {
  return (
    <Styles.Container>
      <Styles.HorizontalContainer width='80%'>
        {definitionList.map((definition, index) => (
          <DefinitionItem definition={definition} key={index} />
        ))}
      </Styles.HorizontalContainer>
      <Styles.HorizontalContainer width='30%'>
        {options.map((option, index) => {
          const onChange = (value) => {
            const arrCopy = [...options];
            arrCopy[index].value = value;
            setOptions(arrCopy);
          };

          return <OptionItem option={option} onChange={onChange} key={index} />;
        })}
      </Styles.HorizontalContainer>
    </Styles.Container>
  );
}

Definitions.propTypes = {
  definitionList: PropTypes.arrayOf(PropTypes.any),
  options: PropTypes.arrayOf(PropTypes.any),
  setOptions: PropTypes.func
};

export default Definitions;