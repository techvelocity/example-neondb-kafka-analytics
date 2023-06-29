import React from "react";

const views = ({ clicks, purchases, views }) => {
  // Child component rendering using the props
  return (
    <div>
      <p>Clicks in Child Component: {clicks}</p>
      <p>Purchases in Child Component: {purchases}</p>
      <p>Views in Child Component: {views}</p>
    </div>
  );
};

export default views
