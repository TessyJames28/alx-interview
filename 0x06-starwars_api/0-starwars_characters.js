#!/usr/bin/node
/* print characters from the StarWars api */
const request = require('request');

const charSet = new Set();
const swapi = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

(async () => {
  try {
    await new Promise((resolve, reject) => {
      request(swapi, (error, response, body) => {
        if (error) {
          reject(error);
          return;
        }
        body = JSON.parse(body);
        const characters = body.characters;

        // console.log('statusCode:', response && response.statusCode);
        // console.log('body:', characters);

        characters.forEach(charUrl => {
          request(charUrl, (charErr, charResp, charBd) => {
            if (charErr) {
              console.error('CharErr:', charErr);
              return;
            }
            const charBody = JSON.parse(charBd);
            // console.log(charBody.name);
            charSet.add(charBody.name);
            if (charSet.size === characters.length) {
              const people = Array.from(charSet);
              people.forEach(name => {
                console.log(name);
              });
            }
          });
        });
      });
    });
  } catch (error) {
    console.error('Error:', error);
  }
})();
