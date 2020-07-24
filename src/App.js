import React, { useState } from 'react';
import SliderQuestion from './Components/SliderQuestion';
import './styles.css'


function App() {
  const [value1, set1] = useState(null);
  const [value2, set2] = useState(null);


  const SliderQuestions = [
    {
      question : "How long is your index finger",
      rangeLow : 0,
      rangeHigh : 100
    },
    {
      question: "How long is your hair",
      rangeLow : 0,
      rangeHigh : 100
    },
    {
      question: "how stupid am i",
      rangeLow: 0,
      rangeHigh: 100
    }
  ];

  function handleChange(event){
    
  }


  return (
    <div class ="body">
      <div class = "display">
        {SliderQuestions.map(question =>(
          <div>
            <SliderQuestion
              question={question.question}
              min={question.rangeLow}
              max={question.rangeHigh}
              value={value1}
              onChange={set1}
              />
          </div>
        ))}
      </div>
    </div>
  );
}

export default App;
