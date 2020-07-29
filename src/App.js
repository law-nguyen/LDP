import React from 'react';
import Form from './Form';
import Result from './Result';
import {BrowserRouter as Router, Route, Link} from "react-router-dom";

function App () {
  return(
    <Router>
      <Route exact path="/" component={Form}/>
      <Route exact path="/result" component={Result}/>
    </Router>
  )
}

export default App;