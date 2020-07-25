import React from 'react';
import '../styles.css'

function BinaryQuestion(props) {
  return(
    <div class="binary">
      <h1>{props.question}</h1>
      <input type="radio" name="answer" id="option1" value="2"/>
      <label for="option1">{props.option1}</label>
      <input type="radio" name="answer" id="option2" value="2"/>
      <label for="option2">{props.option2}</label>
    </div>
  );
}

export default BinaryQuestion;