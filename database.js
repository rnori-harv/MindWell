// Initializing an empty array to store entries
let entries = [];

// Function to get all entries
function getAllEntries() {
  return entries;
}

// Function to create a new entry
function createEntry(title, body) {
  const newEntry = {
    id: entries.length + 1,
    title,
    body,
    date: new Date().toLocaleString()
  };
  entries.push(newEntry);
  return newEntry;
}

// Exporting functions
module.exports = {
  getAllEntries,
  createEntry
};

