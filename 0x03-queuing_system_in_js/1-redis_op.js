import redis from 'redis';

const client = redis.createClient();

const setNewSchool = (schoolName, value) => {
  client.set(schoolName, value, redis.print);
};

const displaySchoolValue = (schoolName) => {
  client.get(schoolName, (error, res) => {
    if (error) {
      console.log(error.message);
    }
    console.log(res);
  });
};

client.on('connect', () => {
  console.log('Redis client connected to the server')
});

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`)
});

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
