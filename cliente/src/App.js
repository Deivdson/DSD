import {useEffect, useState} from 'react';
import './App.css';

function App() {
  const [apis, setApi] = useState([]);

  useEffect(() => {
    const loadData = () => {
      fetch('http://localhost:8000/banco/api', {mode:'no-cors'})
      .then(response => response.json())
      .then(data => setApi(data))
    }
    loadData();
  }, [])

  return (
    <div className="App">
      <header className="App-header">
        <h1>Apis:</h1>
        {apis.map(api => (
          <h1 key={api.id}>{api}</h1>
        ))}
      </header>
    </div>
  );
}

export default App;
