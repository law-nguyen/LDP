import React, { useState } from 'react';
import SliderQuestion from './Components/SliderQuestion';
import BinaryQuestion from './Components/BinaryQuestion';
import './styles.css'
import Questions from './Questions';
import {Link} from 'react-router-dom'


function Form() {
  const [answers, setAnswers] = useState([
    {question: "AGE", answer: null},
    {question: "SEX", answer: null},
    {question: "K2Q10", answer: null},
    {question: "K2Q13", answer: null},
    {question: "K2Q19", answer: null},
    {question: "K2Q22", answer: null},
    {question: "K4Q22", answer: null},
    {question: "K4Q23", answer: null},
    {question: "K4Q24", answer: null},
    {question: "K4Q25", answer: null},
    {question: "K5Q10", answer: null},
    {question: "K7Q05", answer: null},
    {question: "K7Q11", answer: null},
    {question: "K7Q30", answer: null},
    {question: "K7Q31", answer: null},
    {question: "K7Q32", answer: null},
    {question: "K7Q61", answer: null},
    {question: "K7Q62", answer: null},
    {question: "ACE3", answer: null},
    {question: "ACE4", answer: null},
    {question: "ACE5", answer: null},
    {question: "ACE6", answer: null},
    {question: "ACE7", answer: null},
    {question: "ACE8", answer: null},
    {question: "ACE9", answer: null},
    {question: "ACE10", answer: null},
    {question: "K9Q96", answer: null}
  ]);

  const questionAnswered = questionId => event =>{
    setAnswers(
      answers.map(answer => (
      answer.question === questionId ?
      {...answer, answer: event.target.value}
      :
      {answer}
    )));
    console.log(answers);
  }

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
                setAnswered={questionAnswered}
              />
            }
          </div>
        ))}
        <button class="primary" onClick={() =>{window.location.href= "/result"}}>Submit</button>
      </div>
    </div>
  );
}

export default Form;
