import { createClient, print } from 'redis';

const redisClient = createClient({
  socket: {
    host: 'localhost',
    port: 6379
  }
});

redisClient.on('error', (error) => {
  console.log(`Redis client not connected to server: ${error.message}`);
});

redisClient.connect().then(() => {
  console.log('Redis client connected to the server');
 
  redisClient.hSet('HolbertonSchools', 'Portland', 50, print).then((reply) => console.log(`Reply: ${reply}`));
  redisClient.hSet('HolbertonSchools', 'Seattle', 80, print).then((reply) => console.log(`Reply: ${reply}`));
  redisClient.hSet('HolbertonSchools', 'New York', 20, print).then((reply) => console.log(`Reply: ${reply}`));
  redisClient.hSet('HolbertonSchools', 'Bogota', 20, print).then((reply) => console.log(`Reply: ${reply}`));
  redisClient.hSet('HolbertonSchools', 'Cali', 40, print).then((reply) => console.log(`Reply: ${reply}`));
  redisClient.hSet('HolbertonSchools', 'Paris', 2, print).then((reply) => console.log(`Reply: ${reply}`));
  redisClient.hGetAll('HolbertonSchools').then((val) => console.log({...val}));
}).catch((err) => console.error('Failed to connect to Redis:', err));
