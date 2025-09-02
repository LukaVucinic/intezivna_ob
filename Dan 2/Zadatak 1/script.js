"use strict";

const studenti = [
  { ime: "Marko", prezime: "Petrović", godina: 3, ocjene: [9, 8, 7, 10, 9] },
  { ime: "Ana", prezime: "Jovanović", godina: 1, ocjene: [7, 6, 8, 6, 7] },
  { ime: "Luka", prezime: "Simić", godina: 2, ocjene: [10, 9, 10, 8, 9] },
  { ime: "Maja", prezime: "Nikolić", godina: 4, ocjene: [6, 5, 7, 6, 6] },
  { ime: "Ivana", prezime: "Stanković", godina: 1, ocjene: [9, 10, 9, 8, 9] },
];

function prosjek(ocjene) {
  let suma = 0;
  for (let i = 0; i < ocjene.length; i++) {
    suma = suma + ocjene[i];
  }
  return suma / ocjene.length;
}

//a
function studentiSaVecimProsjekom(studenti) {
  for (let i = 0; i < studenti.length; i++) {
    //console.log(studenti[i].ocjene);
    const prosjekStudenta = prosjek(studenti[i].ocjene);
    //console.log(prosjekStudenta);

    if (prosjekStudenta > 8.5) console.log(studenti[i]);
    else {
      console.log(studenti[i].ime);
    }
  }
}

//b
function studentSaNajvecimProsjekom(studenti) {
  let maxProsjek = 0;
  let maxId = -1;
  for (let i = 0; i < studenti.length; i++) {
    //console.log(studenti[i].ocjene);
    const prosjekStudenta = prosjek(studenti[i].ocjene);
    console.log(prosjekStudenta);

    if (prosjekStudenta >= maxProsjek) {
      maxProsjek = prosjekStudenta;
      maxId = i;
    }
  }
  console.log(
    `Student sa najvecim prosjekom je: ${JSON.stringify(
      studenti[maxId],
      null,
      2
    )}`
  );
  console.log(studenti[maxId]);
}

//c
const prosjeciStudenata = function (studenti) {
  const niz = [];
  for (let i = 0; i < studenti.length; i++) {
    //console.log(studenti[i].ocjene);
    const prosjekStudenta = prosjek(studenti[i].ocjene);
    //console.log(prosjekStudenta);
    niz.push(prosjekStudenta);
  }
  return niz;
};

//d
function sortiraniPoProsjeku(studenti) {
  const studentiSaProsjekom = dodavanjeProsjekaStudentima(studenti);
  
  const sortirani = studentiSaProsjekom.sort((a,b) => b.prosjek-a.prosjek);
  console.log(sortirani);
  return sortirani;
}

//e
function dodavanjeProsjekaStudentima(studenti) {
  for (let i = 0; i < studenti.length; i++) {
    const prosjekStudenta = prosjek(studenti[i].ocjene);
    studenti[i].prosjek = prosjekStudenta;
  }
  return studenti;
}

console.log(prosjeciStudenata(studenti));

studentiSaVecimProsjekom(studenti);
studentSaNajvecimProsjekom(studenti);
console.log(dodavanjeProsjekaStudentima(studenti));

sortiraniPoProsjeku(studenti);
