import { Component, OnInit } from '@angular/core';

export interface Player {
  id: number;
  elo: number;
}

@Component({
  selector: 'app-playerlist', // Vérifiez que le sélecteur est correct ici
  templateUrl: './playerlist.component.html',
  styleUrls: ['./playerlist.component.css']
})

export class PlayerlistComponent implements OnInit {

  playerlist: Player[] ;
  sortBy: string = ''; 
  sortDirection: string = 'asc'; 


  constructor() {
    this.playerlist = [];

    fetch('http://localhost:5000/get_players')
    .then(response => response.json())
    .then(data => {
      console.log(data);
      for (let i = 0; i < data.length; i++) {
        this.playerlist.push({id: data[i].id, elo: data[i].elo});
      }
    });
  }

  ngOnInit(): void {
  }

 
  sortListBy(key: string) {
    if (this.sortBy === key) {
      this.sortDirection = this.sortDirection === 'asc' ? 'desc' : 'asc';
    } else {
      this.sortBy = key;
      this.sortDirection = 'asc';
    }
    if (this.sortBy === 'id') {
      this.playerlist.sort((a, b) => {
        return this.sortDirection === 'asc' ? a.id - b.id : b.id - a.id;
      }
      );
    }
    else if (this.sortBy === 'elo') {
      this.playerlist.sort((a, b) => {
        return this.sortDirection === 'asc' ? a.elo - b.elo : b.elo - a.elo;
      }
      );
  }
  }
}