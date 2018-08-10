import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class HttpService {
  constructor(private _http: HttpClient) {
    this.getPokemon()
  }
  allAbilities: any
  allPokemon: any

  getPokemon(){
    let growlithe = this._http.get("https://pokeapi.co/api/v2/pokemon/58/");
    growlithe.subscribe(data => {
      console.log("Got our pokemon!", data)
      this.allAbilities = data['abilities']
      for (var i of this.allAbilities) {
        console.log(i.ability.name)
      }
    });
    let ability = this._http.get("https://pokeapi.co/api/v2/ability/flash-fire/");
    ability.subscribe(data => {
      this.allPokemon = data['pokemon']
      var pokeArr = []
      for (var i of this.allPokemon) {
        pokeArr.push(i.pokemon.name)
      }
      console.log(`${pokeArr.length} pokemon share the flash-fire ability.`)
    })
  }
}