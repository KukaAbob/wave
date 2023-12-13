const { MongoClient } = require('mongodb');

async function insertData() {
  const client = new MongoClient('mongodb://localhost:27017', { useNewUrlParser: true, useUnifiedTopology: true });

  try {
    await client.connect();
    console.log('Connected to the database');

    const database = client.db('your_database_name');
    const collection = database.collection('your_collection_name');

    const dataToInsert = {
      field1: "value1",
      field2: "value2",
      // Другие поля и значения
    };

    const result = await collection.insertOne(dataToInsert);
    console.log(`Inserted ${result.insertedCount} document into the collection`);
  } finally {
    await client.close();
    console.log('Connection closed');
  }
}

insertData();
ы





{


  
}