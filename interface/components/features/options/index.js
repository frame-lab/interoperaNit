import React, { useState } from "react";
import { useRouter } from "next/router";

import Typography from "../../elements/typography";
import Button from "../../elements/button";
import OptionItem from "../../modules/optionItem";
import * as Styles from "./styles";

function Options() {
  const router = useRouter();
  const [selectedOption, setselectedOption] = useState("");
  const optionsList = ["Deep matcher", "Pandas"];

  const showOptions = () => {
    return optionsList.map((optTitle, index) => {
      const onChange = (obj) => {
        if (obj.value) setselectedOption(optTitle);
        else setselectedOption("");
      };
      const opt = { title: optTitle, value: optTitle === selectedOption };
      const optionItemKey = `optionItem_${index}`;

      return (
        <OptionItem option={opt} onChange={onChange} key={optionItemKey} />
      );
    });
  };

  const goToOption = () => {
    switch (selectedOption) {
      case "Deep matcher":
        router.push("deepMatcher");
        break;
      case "Pandas":
        router.push("pandas");
        break;
      default:
        break;
    }
  };

  return (
    <Styles.Body>
      <Typography fontSize="35px" variant="h1">
        Select the desired option
      </Typography>
      <Styles.Container>{showOptions()}</Styles.Container>
      <Button onClick={goToOption} size="large" variant="default" width="200px">
        <Typography fontSize="20px" width="auto" variant="h1" tAlign="center">
          CONFIRM
        </Typography>
      </Button>
    </Styles.Body>
  );
}

export default Options;
