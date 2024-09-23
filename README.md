# Olympic Dataset Analysis

This repository contains data from the Olympic Games, covering athlete demographics, sports participation, and performance from 1896 to 2016. It also includes information about National Olympic Committees (NOCs) and their corresponding regions. This dataset is ideal for conducting analysis on Olympic history, athlete performance trends, and country-level participation insights.

## 1. Dataset Description

The dataset consists of two files:

- **`athlete_events.csv`**: This dataset contains detailed information about athletes who have participated in the Olympic Games from 1896 to 2016. It includes data on the athlete's demographics, the sport they participated in, and their performance.
  
- **`noc_regions.csv`**: This dataset maps the National Olympic Committees (NOCs) to the corresponding regions. It provides additional information about the country or region represented by the athletes.

## 2. Key Features

- Comprehensive records of athletes from both Summer and Winter Olympic Games between 1896 and 2016.
- Includes athlete-specific details such as name, gender, age, height, weight, the team they represented, and the event they competed in.
- Contains information about medals won by athletes (if any).
- Links between athletes and their respective National Olympic Committees (NOCs).
- Additional data about NOCs, such as regions and notes, found in the `noc_regions.csv` file.

## 3. Columns in the Dataset

### **athlete_events.csv**

1. **ID**: Unique identifier for each athlete.
2. **Name**: Full name of the athlete.
3. **Sex**: Gender of the athlete (`M` for Male, `F` for Female).
4. **Age**: Age of the athlete during the event.
5. **Height**: Height of the athlete (in centimeters).
6. **Weight**: Weight of the athlete (in kilograms).
7. **Team**: The country or team the athlete represented.
8. **NOC**: National Olympic Committee code representing the country.
9. **Games**: The year and season (e.g., "2016 Summer") of the Olympic event.
10. **Year**: The year the event took place.
11. **Season**: Indicates whether it was a Summer or Winter Olympics.
12. **City**: Host city for the Olympic Games.
13. **Sport**: The sport in which the athlete competed.
14. **Event**: The specific event within the sport.
15. **Medal**: The type of medal won by the athlete (Gold, Silver, Bronze), if any.

### **noc_regions.csv**

1. **NOC**: National Olympic Committee code representing the country.
2. **region**: The full name of the region or country represented by the NOC.
3. **notes**: Additional notes about the region (if applicable).
