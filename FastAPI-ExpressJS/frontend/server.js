// // server.js
const express = require("express");
const path = require("path");

const app = express();
const PORT = 3000;

// Middleware
app.use(express.json());
//app.use(express.static("public"));


// ✅ Serve static files from "public" folder
app.use(express.static(path.join(__dirname, 'public')));

// Optional: Route for root if not using index.html as static
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'index.html'));
});
// API routes
const apiRoutes = require("./routes/api");
app.use("/api", apiRoutes);
// Start server
app.listen(PORT, () => {
  console.log(`Frontend server running at http://localhost:${PORT}`);
});
