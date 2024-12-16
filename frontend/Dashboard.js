import React, { useState, useEffect } from 'react';
import { Line } from 'react-chartjs-2';
import axios from 'axios';

const Dashboard = () => {
  const [data, setData] = useState([]);
  const [prediction, setPrediction] = useState(null);

  useEffect(() => {
    axios.get('/history').then((response) => {
      setData(response.data.history);
    });
  }, []);

  const requestPrediction = () => {
    axios
      .post('/predict', { input: data.slice(-30).map(row => row.values) })
      .then((response) => {
        setPrediction(response.data.prediction);
      });
  };

  const chartData = {
    labels: data.map((row) => row.timestamp),
    datasets: [
      {
        label: 'CO2 Levels',
        data: data.map((row) => row.co2),
        borderColor: 'rgba(75, 192, 192, 1)',
        borderWidth: 2,
      },
    ],
  };

  return (
    <div>
      <h1>Climate Dashboard</h1>
      <Line data={chartData} />
      <button onClick={requestPrediction}>Get Prediction</button>
      {prediction && <p>Next CO2 Level Prediction: {prediction[0]}</p>}
    </div>
  );
};

export default Dashboard;
