// Importing required modules
const express = require('express');
const bodyParser = require('body-parser');
const database = require('./database');

// Creating express app
const app = express();

// Setting up body-parser middleware
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

// Endpoint for getting all entries
app.get('/entries', (req, res) => {
  const entries = database.getAllEntries();
  res.send(entries);
});

// Endpoint for creating a new entry
app.post('/entries', (req, res) => {
  const { title, body } = req.body;
  const newEntry = database.createEntry(title, body);
  res.send(newEntry);
});

// Starting server
app.listen(3000, () => {
  console.log('Server started on port 3000');
});
