import React, { useEffect, useState } from 'react';
import './App.css';
import { Notes } from './components/notes';

function App() {

  const[notes, setNotes] = useState([]);


  useEffect(() => {
    fetch('/notes').then(response => response.json().then(data => {
      setNotes(data.notes);
    })
    );
  }, []);

  console.log(notes)

  return (
    <div className="App">
    <Notes notes={notes}/>
    </div>
  );
}

export default App;
