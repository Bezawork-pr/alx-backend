import  redis, { createClient } from 'redis';

const client = createClient();

client.on('connect', () =>  {
  console.log('Redis client connected to the server');
})
client.on('error', (err) =>  {
  console.log('Redis client not connected to the server: $ {err}');
})

const name = 'HolbertonSchools';
//const items = new Map([
//  ['Portland', 50],
//  ['Seattle', 80],
//  ['New York', 20],
//  ['Bogota', 20],
//  ['Cali', 40],
//  ['Paris', 2]
//]);
//items.forEach((key, value) => client.hset(name, key, value, (error, reply) => redis.print(error)) 
//);
const items = {
  'Portland': 50,
  'Seattle': 80,
  'New York': 20,
  'Bogota': 20,
  'Cali': 40,
  'Paris': 2,
}
for (const [key, value] of Object.entries(items)){
  client.hset(name, key, value, redis.print);
}
client.hgetall(name, (error, object) => console.log(object));
