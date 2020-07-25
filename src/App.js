import React, { useState } from 'react';
import SliderQuestion from './Components/SliderQuestion';
import BinaryQuestion from './Components/BinaryQuestion';
import './styles.css'


function App() {
  const [value1, set1] = useState(null);
  const [value2, set2] = useState(null);


  const Questions = [
    {
      slider: true,
      question : "How long is your index finger",
      rangeLow : 0,
      rangeHigh : 100
    },
    {
      slider: true,
      question: "How long is your hair",
      rangeLow : 0,
      rangeHigh : 100
    },
    {
      slider: true,
      question: "how stupid am i",
      rangeLow: 0,
      rangeHigh: 100
    },
    {
      slider: false,
      question: "Male or female",
      option1: "Male",
      option2: "Female"
    }
  ];

  


  return (
    <div class ="body">
      <div class = "display">
        {Questions.map(question =>(
          <div class="card">
            {question.slider ?
              <SliderQuestion
                question={question.question}
                min={question.rangeLow}
                max={question.rangeHigh}
                value={value1}
              />
              :
              <BinaryQuestion
                question={question.question}
                option1={question.option1}
                option2={question.option2}
              />
            }
          </div>
        ))}
      </div>
    </div>
  );
}

export default App;
