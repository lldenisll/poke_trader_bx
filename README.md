<h3 align="center">Poke Trader</h3>

  <p align="center">
    Want to trade some pokemons, but you are not sure if you are doing the right thing? Check out this poke trader calculator
    Our calculator focus on a fair trade, that doesnt favour any sides.
    The calculator defines if the trade is fair, you only got to decide if you want to trade the pokemons
    <br />
     <a href="https://github.com/lldenisll/poke_bx_front" targe="blank">Para português, acesse o repô do front-end</a>
    <br />
    <a href="https://lldenisll.github.io/poke_bx_front/index.html" targe="blank">Open Front-end</a>
    ·
    <a href="https://calm-inlet-80092.herokuapp.com/core/" targe="blank">Open API Heroku</a>
    ·
    <a href="https://github.com/lldenisll/poke_bx_front" targe="blank">Front-End Repository</a>
    .
    <a href="http://denisdev.com/poke_bx_front/index.html" targe="blank">Open Front End (option 02)</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">About the project</h2></summary>
  <ol>
    <li>
      <a href="#about">About</a>
      <ul>
        <li><a href="#tecnologies">Tecnologies</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
    </li>
    <li><a href="#methodology">Methodology</a></li>
    <li><a href="#tests">Methodology</a></li>
    <li><a href="#my-contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About
This project aims to create a fair trade pokemon calculator. One trade consists on two players offering 1 to 6 pokemons each one.
Any source of combination is valid.
The methodology used to evaluete the pokemons is described on a section bellow
The project was developed with python and django as backend with postgresql databse, and it was deployed on heroku.
The front end in html + css + js and with some vue components to render the trade history

### Tecnologies

* []() Python + Django + Django Rest Framework
* []() Html + CSS + JS + VueJS
* []() GitHub + Postgresql + Heroku



<!-- GETTING STARTED -->
## Getting Started

If you wish for a local copy:

### Instalação back-end

1. Clone repository
   ```sh
   git clone https://github.com/lldenisll/poke_trader_bx
   ```
2. Create virtual env
   ```sh
   python3 -m venv /path/to/virtual/env
   ```
   3. Activate virtual env
   ```sh
   source/path/virtual/env/bin/activate
   ```
3. Install requirements
   ```sh
   pip install requirements.txt
   ```
3. Make migrations
   ```sh
   python manage.py makemigrations
   python manage.py migrate
   ```
3. Run server!
   ```sh
   python manage.py runserver
   ```
### Front-end install

1. Clone repository
   ```sh
   git clone https://github.com/lldenisll/poke_bx_front
   ```
2. Open index.html
   ```sh
   be happy :)
   ```
### Database
If you wish to run local with your databse, please insert your local database information on the file settings.py at config folder, and make migrations again

## Methodology
The criteria was built after a data analysis on a jupyter notebook.
In order to not use to much of the free API, and as a request of the api developers (fair use). It was utilized a dataset available at kaggle.

With this dataset, it was created 20 klusters, and it was clear the the kluster 3 included the most powerfull pokemons, and the most important features being: is_lengedary,base_exp and special attack

In order to confirm these methodolgy a pokemon master was consulted and explained that some of the pokemons uses special attack, while others the normal attack. For example a Charmander perform better on special attacks (like ember) as a Machop perform better on normal attack (like punch). Therefore these are both important features.

In conclusion the given pontuation to each pokemon follows the equation:
`((base_exp*2) + attack + special_attack)*10(if is_legendary)`
## Tests

We can evaluate how close one pokemon is from another to evaluate if the trade is fair, or not. Besides we can tests with oposits clusters, e.g: none trade evolving cluster 3 against cluster 10 can be consider fair trade. Therefore the test.py included a cluster analysis beteween cluster 10 and 3.
For a fair trade: 
2 lists of pokemons in the cluster 3 
2 lists of pokemons in the cluster 10
For a unfair trade:
1 list of pokemon in the custer 3 against 1 list of pokemon in the cluster 10
1 list of pokemon in the custer 3 against 1 list of pokemon in the cluster 10

_To know more follow (portuguese only, sorry): [Documentação](https://lldenisll.github.io/poke_bx_front/metodologia.html)_


## My contact

Dênis Gonçalves dos Santos 
[![LinkedIn][linkedin-shield]][linkedin-url]



[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/denis142/
