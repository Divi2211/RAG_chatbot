// scripts/utils.js

const { ChromaClient } = require("chromadb");
const { v4: uuidv4 } = require("uuid");

// Load Chroma client
const client = new ChromaClient({
  path: "http://localhost:8000" // If using chroma in server mode
});

// Semantic search function
async function searchQuery(userQuery) {
  const collection = await client.getCollection({ name: "langchain" });

  const results = await collection.query({
    queryTexts: [userQuery],
    nResults: 3
  });

  // Format results
  const response = results.documents[0].map((doc, idx) => {
    return {
      chunk: doc,
      similarity: results.distances[0][idx]
    };
  });

  return response;
}

// For local testing
(async () => {
  const results = await searchQuery("What is Altibbe?");
  console.log("🔍 Top Matches:", results);
})();
