#!/usr/bin/node
const request = require('request');

const apiUrl = process.argv[2];
const characterId = '18';

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const data = JSON.parse(body);
    const films = data.results;
    const count = films.filter(film =>
      film.characters.some(charUrl => charUrl.includes(`/people/${characterId}/`))
    ).length;
    console.log(count);
  }
});
