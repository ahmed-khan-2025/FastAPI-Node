// api.js
const express = require("express");
const fetch = require("node-fetch");

const router = express.Router();
const BASE_URL = "http://localhost:8000/movies";

// GET all movies
router.get("/movies", async (req, res) => {
  try {
    const response = await fetch(`${BASE_URL}/`);
    const data = await response.json();
    res.json(data);
  } catch (error) {
    res.status(500).json({ error: "Failed to fetch movies" });
  }
});

// POST a new movie
router.post("/movies", async (req, res) => {
  try {
    const response = await fetch(`${BASE_URL}/`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(req.body),
    });
    const data = await response.json();
    res.json(data);
  } catch (error) {
    res.status(500).json({ error: "Failed to add movie" });
  }
});

// PUT (edit) a movie by ID
router.put("/movies/:id", async (req, res) => {
  const { id } = req.params;
  try {
    const response = await fetch(`${BASE_URL}/${id}`, {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(req.body),
    });
    const data = await response.json();
    res.json(data);
  } catch (error) {
    res.status(500).json({ error: "Failed to update movie" });
  }
});

// DELETE a movie by ID
router.delete("/movies/:id", async (req, res) => {
  const { id } = req.params;
  try {
    const response = await fetch(`${BASE_URL}/${id}`, {
      method: "DELETE",
    });
    if (response.ok) {
      res.json({ message: "Movie deleted successfully" });
    } else {
      const errorData = await response.json();
      res.status(response.status).json(errorData);
    }
  } catch (error) {
    res.status(500).json({ error: "Failed to delete movie" });
  }
});

module.exports = router;
