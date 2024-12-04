import { createClient } from 'redis';

const redisClient = createClient({
  socket: {
    host: 'localhost',
    port: 6379
  }
});

redisClient.on('error', (error) => {
  console.log(`Redis client not connected to server: ${error.message}`);
});

redisClient.connect().then(() => console.log('Redis client connected to the server'));
