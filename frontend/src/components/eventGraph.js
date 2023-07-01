import React, { useEffect, useRef, useState } from 'react';
import Chart from 'chart.js/auto';

const AnalyticsGraph = () => {
  const chartRef = useRef(null);
  const chartInstanceRef = useRef(null);
  const [clickEvents, setClickEvents] = useState([]);
  const [viewEvents, setViewEvents] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const [clickResponse, viewResponse] = await Promise.all([
          fetch('/api/click-analytics').then((response) => response.json()),
          fetch('/api/view-analytics').then((response) => response.json()),
        ]);

        setClickEvents(clickResponse);
        setViewEvents(viewResponse);
      } catch (error) {
        console.error('Error fetching analytics data:', error);
      }
    };

    fetchData();

    const interval = setInterval(fetchData, 5000); // Fetch data every 5 seconds

    return () => {
      clearInterval(interval); // Clean up the interval on component unmount
    };
  }, []);

  useEffect(() => {
    const clickCount = clickEvents.length;
    const viewCount = viewEvents.length;

    if (chartInstanceRef.current) {
      chartInstanceRef.current.destroy(); // Destroy the previous Chart instance
    }

    if (chartRef.current) {
      chartInstanceRef.current = new Chart(chartRef.current, {
        type: 'bar',
        data: {
          labels: ['Clicks', 'Views'],
          datasets: [
            {
              data: [clickCount, viewCount],
              backgroundColor: ['blue', 'green'],
              borderWidth: 0,
            },
          ],
        },
        options: {
          responsive: false,
          maintainAspectRatio: true,
          scales: {
            y: {
              beginAtZero: true,
            },
          },
        },
      });
    }
  }, [clickEvents, viewEvents]);

  return (
    <div>
      <h2>Analytics Graph</h2>
      <canvas ref={chartRef} width={400} height={300} />
    </div>
  );
};

export default AnalyticsGraph;
