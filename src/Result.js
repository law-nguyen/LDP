import React, { useState, useEffect } from 'react';
import './styles.css';

function Result(){
  const [loaded, setLoaded] = useState(false);

  useEffect(() => {
    const interval = setInterval(() => {
      setLoaded(true);
    }, 5000);
    return () => clearInterval(interval);
  }, [] )

  const yes = "Based on your asnwers for the assessment, the prediction result indicates that the student has a HIGH" +
                " chance of having ADHD. Please recommend for the child to be tested by a specialist to recieve an accurate diagnosis."
  const links = [
    "https://www.cdc.gov/ncbddd/adhd/facts.html",
    "https://www.nimh.nih.gov/health/topics/attention-deficit-hyperactivity-disorder-adhd/index.shtml",
    "https://kidshealth.org/en/parents/adhd.html"
    ];
  return(
    <div class="body">
      {loaded ?
        <div class="result-card">
          <h3>{yes}</h3>
          <h4>Here are some helpful links to learn more about ADHD: </h4>
          <ul>https://www.cdc.gov/ncbddd/adhd/facts.html</ul>
          <ul>https://www.nimh.nih.gov/health/topics/attention-deficit-hyperactivity-disorder-adhd/index.shtml</ul>
          <ul>https://kidshealth.org/en/parents/adhd.html</ul>
        </div>
        :
        <h1>
          Fetching Results...
        </h1>
      }
    </div>
  );

};

export default Result;