import React from 'react';
import '../styles.css';

function SliderQuestion(props) {
  return (
    <div>
      <h1>{props.question}: {props.value}</h1>
      <div>
        <input 
          class="slider"
          type="range"
          min={props.min}
          max={props.max}
          onChange={props.handleChange}
        />
      </div>
    </div>
  );
}

export default SliderQuestion;
