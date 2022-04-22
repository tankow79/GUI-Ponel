import React, {useEffect} from "react";
import './App.css';

function App() {

  useEffect(()=>{
    fetch('/api/users')
        .then(response => response.json())
        .then(data => console.log(data))

  })


  return (
      <h1>GUI-Ponel</h1>
  );
}

export default App;
