import React from 'react';
import '../styles.css'

function BinaryQuestion(props) {

  const questionAnswered = questionId => event =>{
    
  }

  return(
    <div class="binary">
      <h3>{props.question}</h3>
      <input type="radio" name={props.id} value="1"/>
      <label>{props.option2}</label>
      <input type="radio" name={props.id} value="0"/>
      <label>{props.option1}</label>
      <input type="radio" name={props.id} value="6"/>
      <label>Do Not Know</label>
    </div>
  );
}

export default BinaryQuestion;