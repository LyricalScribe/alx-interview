#!/usr/bin/node
//Prints all characters of a Star Wars movie

const request = require('request');

const movieId = process.argv[2];
const movieEndpoint = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

function fetchCharacters(characterNames, index) {
  if (characterNames.length === index) {
    return;
  }

  request(characterNames[index], (error, response, body) => {
    if (error) {
      console.log(error);
    } else {
      console.log(JSON.parse(body).name);
      fetchCharacters(characterNames, index + 1);
    }
  });
}

request(movieEndpoint, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const characterNames = JSON.parse(body).characters;

    fetchCharacters(characterNames, 0);
  }
});
