import React, { useState } from 'react';
import '../styles.css';

function SliderQuestion(props) { 
  const [value, setValue] = useState(null)
  return (
    <div>
      <h3>{props.question}: {value}</h3>
      <div>
        <input 
          class="slider"
          type="range"
          min={props.min}
          max={props.max}
          onChange={(event) =>setValue(event.target.value)}
        />
      </div>
    </div>
  );
}

export default SliderQuestion;
