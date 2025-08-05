const axios = require("axios");

axios.post("http://localhost:5000/start")
  .then(res => console.log("Apply trigger sent:", res.data))
  .catch(err => console.error("Error triggering apply:", err));