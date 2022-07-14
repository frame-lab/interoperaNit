import { ThemeProvider } from "styled-components";

import theme from "../styles/theme";
import GlobalStyle from "../styles/globalStyles";
import Header from "../components/features/header";
import { WindowDimensionsContextProvider } from "../utils/window";

export default function MyApp({ Component, pageProps }) {
  return (
    <ThemeProvider theme={theme}>
      <WindowDimensionsContextProvider>
        <GlobalStyle />
        <Header />
        <Component {...pageProps} />
      </WindowDimensionsContextProvider>
    </ThemeProvider>
  );
}
