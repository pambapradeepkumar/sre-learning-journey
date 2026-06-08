import React, { useState, useEffect } from "react";

function App() {
  const [tasks, setTasks] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch("/api/tasks/")
      .then((res) => res.json())
      .then((data) => {
        setTasks(data);
        setLoading(false);
      })
      .catch((err) => {
        setError("Could not connect to backend");
        setLoading(false);
      });
  }, []);

  return (
    <div style={{ maxWidth: "800px", margin: "40px auto", fontFamily: "Arial" }}>
      <h1>Task Manager</h1>
      <p>My SRE Learning Journey Tasks</p>

      {loading && <p>Loading tasks...</p>}
      {error && <p style={{ color: "red" }}>{error}</p>}

      {tasks.map((task) => (
        <div
          key={task.id}
          style={{
            border: "1px solid #ddd",
            borderRadius: "8px",
            padding: "16px",
            marginBottom: "12px",
            background: task.completed ? "#f0fff0" : "#fff",
          }}
        >
          <h3 style={{ margin: 0 }}>
            {task.completed ? "✅" : "⏳"} {task.title}
          </h3>
          <p style={{ color: "#666", margin: "8px 0 0" }}>{task.description}</p>
        </div>
      ))}
    </div>
  );
}

export default App;
