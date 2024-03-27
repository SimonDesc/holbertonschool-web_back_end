import { createClient } from 'redis';

async function main() {
  const client = createClient();

  client.on('error', (err) => console.log('Redis Client Error', err));

  client.on('connect', () => console.log('Redis client connected to the server'));

  await client.connect();

  // Votre code pour utiliser le client Redis ici
  
  // N'oubliez pas de fermer la connexion une fois que vous avez terminé
  // await client.quit();
}

main().catch(console.error);
