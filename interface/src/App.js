import './App.css';
import AddIcon from '@material-ui/icons/Add'
import { useState } from 'react';

function App() {
  const [unique, setUnique] = useState([''])
  const [split, setSplit] = useState([''])
  const updateState = (event, functionUpdate, arr, index) => {
    const arrayCopy = [...arr]
    arrayCopy[index] = event.target.value
    functionUpdate(arrayCopy)
  }

  return (
    <div className="App">
      <header className="App-header">
        <p>
          Interopera
        </p>
      </header>
      <div className="App-div-preseting">
        <div className='App-div-Add'>
          <div className="App-div-unique">
            <p>
              Unique
            </p>
            <div className='App-div-button'>
              <div className='App-div-input'>
                {unique.map((text, index) =>
                  <input
                    type="text"
                    name="unique"
                    className="App-input-unique"
                    value={text}
                    onChange={event => updateState(event, setUnique, unique, index)}
                  />)}
              </div>
              <button className='App-Add-button' onClick={() => setUnique([...unique, ''])}>
                <AddIcon className="App-AddIcon" />
              </button>
            </div>
          </div>
        </div>
        <div className='App-div-Add'>
          <div className="App-div-split">
            <p>
              Split
            </p>
            <div className='App-div-button'>
              <div className='App-div-input'>
                {split.map((text, index) =>
                  <input
                    type="text"
                    name="split"
                    className="App-input-split"
                    value={text}
                    onChange={event => updateState(event, setSplit, split, index)}
                  />)}
              </div>
              <button className='App-Add-button' onClick={() => setSplit([...split, ''])}>
                <AddIcon className="App-AddIcon" />
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
