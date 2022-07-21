<div id="top"></div>
<br />
<div align="center">
   </a>

  <h3 align="center">The AIRBNB Effect</h3>

  <p align="center">

</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    <li><a href="#usage">Solution</a></li>
    <li><a href="#roadmap">Dataset</a></li>
    <li><a href="#contributing">Training</a></li>
    <li><a href="#license">Deployment</a></li>
    <li><a href="#contact">Who benefits?</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

<br /><img src="images/logo.JPG" alt="map" width=100% height=100%>

### Abstract

Use AI models and ML to predict the influence of Airbnb listings in the housing market in Vienna.

### Problem

Airbnb has been a blessing and a curse. It has provided an alternative source of income for many people that enables them to do many things; at the same time, it has brought healthy competition to the hotel industry that had comfortably been charging ridiculous prices for travellers. But, on the flip side, it also has affected urban development, forcing people out of the city’s most interesting areas to make space for tourists. Without regulation, this Airbnb effect can quickly become a problem for housing. The consequences are that families and primary users of the cities are being pushed to the city’s fringes.

<br /><img src="images/problem.JPG" alt="map" width=100% height=100%>

This problem needs attention. Some of the following graphs will explain the situation:

<br /><img src="images/airbnbvsrental.JPG" alt="map" width=100% height=100%>

<br /><img src="images/aptremoved.JPG" alt="map" width=100% height=100%>

<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

Rhino, grasshopper, Javascript and Python.

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Solution

We can access Airbnb listings data and could source housing data from Statistics Vienna. By correctly using this data, we could establish a correlation between the number of listings and the housing price. 

<br /><img src="images/insideairbnb.JPG" alt="map" width=100% height=100%>

Furthermore, by training a model to identify this correlation, we could play different scenarios to illustrate the problem that Airbnb poses to housing.

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- ROADMAP -->
## Dataset

Our biggest challenge is to source the property information for Vienna. One initial attempt was to use the property purchase index available on the website for Statistics Vienna as a source for housing prices. 

However, after working with this data for a while and running different studies, we realized that this data contained property to exchange information mainly for the outer districts of Vienna and not for the central part, which is crucial for our study. Therefore midway through the development of this study, we had to rebuild our dataset from scratch. 

We decided to use a real estate agency in Austria as a source for our information. However, using this website entails data scraping, and the drawback of many properties not having their location disclosed. Also, most of the properties were newly built, so we wouldn’t have data that encompassed all markets. 

<br /><img src="images/dataset.JPG" alt="map" width=100% height=100%>

After using a scraping system to pull out the data for the different districts, we ended with a dataset of properties for sale in the 23 districts of Vienna with around 1200 data points.

We also had access to the average housing cost per square meter for each of Vienna’s districts, so we decided to convert the real estate dataset to price per square meter per property for sale to compare it with the average per district. This comparison yielded a per cent deviation from the average for the district. So now we had property points with a specific price deviation from the mean.

Next, we mapped the distances for each property point to all 8,000 Airbnb listings in Vienna. Having all this information, we could then filter the number of listings within a specified radius around the property to obtain several listings that would be relevant for our study.

We ran three different radiuses to obtain information: 200 meters, 500 meters and 1000 meters, with the results shown in the heatmaps.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Training

Once we had the dataset completed, we decided to test two types of training for the mode: a shallow learning model and an artificial neural network model.

For the shallow learning, we found that the linear regression with a polynomial function yielded the best results, around 88%.

<br /><img src="images/shallow.JPG" alt="map" width=100% height=100%>

For the ANN, the results were not as good; the model was getting confused with some of the data.

<br /><img src="images/ann.JPG" alt="map" width=100% height=100%>

<p align="right">(<a href="#top">back to top</a>)</p>

So we decided to go for the shallow learning model.

<!-- LICENSE -->
## Deployment

With a trained model, we created a Python script deployed to Mapbox; in this script, the user can specify a point in the map and a proposed number of listings around that point, and the model will predict the expected price deviation by square meter. This will be a dynamic layer as the user can specify the output.

<br /><img src="images/workflow.JPG" alt="map" width=100% height=100%>

For the static layer, we generated a heatmap of price deviation using the existing property dataset. This static layer would enable the user to quickly identify hotspots in the city where the price deviation would be more than usual. 

<br /><img src="images/mock.JPG" alt="map" width=100% height=100%>

These layers will be deployed to Mapbox as part of the more significant city project.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Who benefits?

We believe this tool will help lawmakers legislate around Airbnb to protect the city user, helping them find good properties around the city without having to pay a stratospheric amount of money due to the Airbnb listings making more money.

### User story

<br /><img src="images/family.JPG" alt="map" width=100% height=100% />

Let’s say Russ’s family is moving to Austria from Frankfurt in search of greener pastures. They are looking for a property to stay in, but they have no idea if they are paying a fair price or not. They have two ways of doing this:

+Usual way by asking a real estate agent for assistance and trusting their capabilities, or 

+Using our Airbnb Effect model, the family can quickly identify which areas are most affected by a price increase and narrow the search for properties outside of these areas. They can also predict what will happen to their property with regards to having more or fewer listings around their house. 

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

### Conclusions

Like any shared economy gig, Airbnb is a new reality that is here to stay and requires attention. However, it’s not necessarily good or bad, its needs regulation to protect the interests of the city and its urban development. 

For example, it’s not in the government’s best interest to have deserted areas in the city at specific points of the calendar year because there are no tourists. In contrast, the primary users of the city have to travel long distances to get to work and back home.

We believe the Airbnb Effect website will be a good tool for assisting regulation.

### Credits

The Airbnb effect is a project of IAAC, Institute of Advanced Architecture of Catalonia, developed at Master In Advanced Computation For Architecture & Design in 2021/2022 by students: Siddhant Choudary, Mansoor Awais, Gerald Mandevhana and Bruno Martorelli. Faculty: Angelos Chronis, Faculty assistant: Aleksander Jastrzebska, Serjoscha Duering and Nariddh Khean

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
