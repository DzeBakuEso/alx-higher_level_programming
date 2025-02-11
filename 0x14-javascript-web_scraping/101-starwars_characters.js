#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const filmData = JSON.parse(body);
  const characterUrls = filmData.characters;

  const fetchCharacter = (index) => {
    if (index >= characterUrls.length) return;

    request(characterUrls[index], (charError, charResponse, charBody) => {
      if (charError) {
        console.error(charError);
      } else {
        console.log(JSON.parse(charBody).name);
        fetchCharacter(index + 1);
      }
    });
  };

  fetchCharacter(0);
});
