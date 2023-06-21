import  redis, { createClient } from 'redis';
import { promisify } from 'util';

const client = createClient();
const get = promisify(client.get).bind(client);

client.on('connect', () =>  {
  console.log('Redis client connected to the server');
})
client.on('error', (err) =>  {
  console.log('Redis client not connected to the server: $ {err}');
})
function setNewSchool(schoolName, value) {
  client.set(schoolName, value, (error, reply) =>  {
    redis.print(`Reply: ${reply}`);
  });
}
async function displaySchoolValue(schoolName)  {
  const reply = await get(schoolName);
  redis.print(`${reply}`);
}
(async function main() {
  await displaySchoolValue('Holberton');
  setNewSchool('HolbertonSanFrancisco', '100');
  await displaySchoolValue('HolbertonSanFrancisco');
}());
