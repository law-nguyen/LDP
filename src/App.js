import React, { useState } from 'react';
import SliderQuestion from './Components/SliderQuestion';
import BinaryQuestion from './Components/BinaryQuestion';
import './styles.css'
import Questions from './Questions';


function App() {
  const [answers, setAnswers] = useState([]);

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
              />
              :
              <BinaryQuestion
                question={question.question}
                option1={question.option1}
                option2={question.option2}
                id={question.id}
              />
            }
          </div>
        ))}
        <button class="primary">Submit</button>
      </div>
    </div>
  );
}

export default App;
