import redis from 'redis';
import { promisify }  from 'util';

const client = redis.createClient();

const setNewSchool = (schoolName, value) => {
  client.set(schoolName, value, redis.print);
};

const displaySchoolValue = async (schoolName) => {
  try {
    const res = await promisify(client.get).bind(client)(schoolName);
    console.log(res);
  } catch (error) {
      console.error(error.message);
    }
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
