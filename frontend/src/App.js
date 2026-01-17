import { useEffect, useState } from "react";

function App() {
  const [status, setStatus] = useState("loading");

  useEffect(() => {
    fetch("/health")
      .then(res => res.json())
      .then(data => setStatus(data.status));
  }, []);

  return (
    <div>
      <h1>Multi-Cloud DevOps App</h1>
      <p>Backend Health: {status}</p>
    </div>
  );
}

export default App;
