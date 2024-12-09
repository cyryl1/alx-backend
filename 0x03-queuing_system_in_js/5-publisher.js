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

function publishMessage(message, time) {
  setTimeout(() => {
    console.log(`About to send ${message}`);
    redisClient.publish('holberton school channel', message);
  }, time);
}

redisClient.connect().then(() => {
  console.log('Redis client connected to the server');

  publishMessage("Holberton Student #1 starts course", 100);
  publishMessage("Holberton Student #2 starts course", 200);
  publishMessage("KILL_SERVER", 300);
  publishMessage("Holberton Student #3 starts course", 400);
}).catch((err) => {
  console.error('Failed to connect:', err);
});
