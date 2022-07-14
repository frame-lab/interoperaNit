/* eslint-disable react-hooks/exhaustive-deps */
import { createContext, useContext, useState, useEffect } from "react";

const WindowDimensionsContext = createContext({
  width: 0,
  height: 0,
});

export function WindowDimensionsContextProvider({ children }) {
  const hasWindow = typeof window !== "undefined";

  const getWindowDimensions = () => {
    const width = hasWindow ? window.innerWidth : null;
    const height = hasWindow ? window.innerHeight : null;

    return { width, height };
  };

  const [windowDimensions, setWindowDimensions] = useState(
    getWindowDimensions()
  );

  useEffect(() => {
    if (hasWindow) {
      const handleResize = () => {
        setWindowDimensions(getWindowDimensions());
      };

      window.addEventListener("resize", handleResize);
      return () => window.removeEventListener("resize", handleResize);
    }
    return null;
  }, [getWindowDimensions, hasWindow]);

  return (
    <WindowDimensionsContext.Provider value={windowDimensions}>
      {children}
    </WindowDimensionsContext.Provider>
  );
}

export const useWindowDimensions = () => useContext(WindowDimensionsContext);
