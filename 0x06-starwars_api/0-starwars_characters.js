#!/usr/bin/node
// Script that prints all characters of a Star Wars movie

const request = require('request');
const movieId = process.argv[2];
const filmsApiUrl = 'https://swapi-api.hbtn.io/api/films';

function fetchJSON (url) {
  return new Promise(function (resolve, reject) {
    request(url, function (error, response, body) {
      if (!error && response.statusCode === 200) {
        resolve(JSON.parse(body));
      } else {
        reject(error);
      }
    });
  });
}

async function printStarWarsCharacters (movieId) {
  try {
    const filmData = await fetchJSON(`${filmsApiUrl}/${movieId}`);
    for (const characterUrl of filmData.characters) {
      try {
        const characterData = await fetchJSON(characterUrl);
        console.log(characterData.name);
      } catch (error) {
        console.error(`Error fetching character data: ${error}`);
      }
    }
  } catch (error) {
    console.error(`Error fetching movie data: ${error}`);
  }
}

printStarWarsCharacters(movieId);
