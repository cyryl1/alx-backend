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

//redisClient.connect().then(() => console.log('Redis client connected to the server'));

function displaySchoolValue(schoolName) {
  redisClient.get(schoolName).then((val) => {
    console.log(val);
  }).catch((err) => console.error(`Error getting ${schoolName}:`, err));
}

function setNewSchool(schoolName, value) {
  redisClient.set(schoolName, value).then((reply) => {
    console.log('Reply: Ok');
  }).catch((err) => console.error(`Error setting ${schoolName}:`, err));
}

redisClient.connect().then(() => {
  console.log('Redis client connected to the server');
  displaySchoolValue('Holberton');
  setNewSchool('HolbertonSanFrancisco', '100');
  displaySchoolValue('HolbertonSanFrancisco');
}).catch((err) => console.error('Failed to connect to Redis:', err));

//diisplaySchoolValue('Holberton');
//setNewSchool('HolbertonSanFrancisco', '100');
//displaySchoolValue('HolbertonSanFrancisco');
