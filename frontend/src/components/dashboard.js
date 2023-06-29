import React, { useState, useEffect } from 'react';
import eventGraph from "./eventGraph";
import views from "./views"

const Dashboard = () => {
  const [clicks, setClicks] = useState(0);
  const [purchases, setPurchases] = useState(0);
  const [views, setViews] = useState(0);
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch('/api/analytics');
        const data = await response.json();
        setClicks(data.clicks);
        setPurchases(data.purchases);
        setViews(data.views);
        setIsLoading(false);
      } catch (error) {
        console.error('Error fetching analytics data:', error);
      }
    };

    const intervalId = setInterval(fetchData, 10000);

    return () => {
      clearInterval(intervalId);
    };
  }, []);

  return (
    <div>
      {isLoading ? (
        <p>Loading...</p>
      ) : (
        <>
          <p>Clicks: {clicks}</p>
          <p>Purchases: {purchases}</p>
          <p>Views: {views}</p>
        </>
      )}
    </div>
  );
};

export default Dashboard;
