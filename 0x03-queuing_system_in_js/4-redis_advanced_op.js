//Node Redis client and advanced operations
import Redis from 'redis';

const client = Redis.createClient();

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

const KEY = 'HolbertonSchools';
const keys = ['Portland', 'Seattle', 'New York', 'Bogota', 'Cali', 'Paris'];
const values = [50, 80, 20, 20, 40, 2];

keys.forEach((key, index) => {
  client.hset(KEY, key, values[index], Redis.print);
});

client.hgetall(KEY, (err, res) => {
  if (err) {
    console.log(err);
  }
  console.log(res);
});
