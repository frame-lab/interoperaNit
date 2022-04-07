import Header from "../components/features/header";
import Body from "../components/features/body";

export default function Home() {
  const headerTitle = 'Interopera';

  return (
    <>
      <Header headerTitle={headerTitle} />
      <Body />
    </>
  );
}