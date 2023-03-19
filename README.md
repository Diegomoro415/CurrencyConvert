# <img src="images/exchange-rate.png" style="width: 40px;height:40px"> <span style="color: green">Currency</span><span style="color: yellow">Convert</span>

**Diego Moro** 

💻 [Visit live website](https://currencyconverter.herokuapp.com/)

![Mockup image](images/mockup_currencyconvert.png)

##About

A currency conversion program that allows the user to convert between different currencies.

This program uses the forex_python library to perform currency conversions. It allows the user to input a desired amount to be converted, the initial
currency and the exchange currency. It provides a list of currencies to choose from and displays the converted amount.

## Table of Contents
  - [Project Goals](#project-goals)
    - [User Goals](#user-goals)
    - [Site Owner Goals](#site-owner-goals)
  - [User Experience](#user-experience)
    - [Target Audience](#target-audience)
    - [User Requirements and Expectations](#user-requirements-and-expectations)
  - [User Stories](#user-stories)
    - [Users](#users)
    - [Site Owner](#site-owner)
  - [Technologies Used](#technologies-used)
    - [Languages](#languages)
    - [Frameworks & Tools](#frameworks--tools)
    - [Libraries](#libraries)
  - [Features](#features)
  - [Validation](#validation)
  - [Testing](#testing)
  - [Bugs](#bugs)
  - [Deployment](#deployment)
  - [Credits](#credits)
  - [Acknowledgements](#acknowledgements)

## Project Goals

### User Goals

- Check the value and quote in differents currencies
- Have a clean app and easy to use
- Fast and accurate

### Site Owner Goals

- Create a app that is easy and clear to user
- Ensure that users understand the purpose of the app
- Display the informations to make a easy understanding
- Give an accurate and fast quotation

## User Experience

### Target Audience

For those who wants to follow the prices find the best time to buy or sell your forigien currencies.

### User Requirements and Expectations

- A simple, error-free app
- Straightforward navigation
- Accurate
- Fast

[Back to Table Of Contents](#table-of-contents)

## User Stories

### Users

1. I want to have easy access to the top currencies
2. I want to be able to see the instructions
3. I want to have access to diffetent currencies
4. I want to receive a real time quotation

### Site Owner

5. I want users to have a positive experience
6. I want users to easily select options from the menu
7. I want users to see and follow the instruction for a easy navigation
8. I want the user to receive a real time result

## Technologies Used

### Languages

- [Python](https://www.python.org/) Programming language for the logic of the program

### Frameworks & Tools

- [Diagrams.net](https://app.diagrams.net/) was used to draw program flowchart
- [Git](https://git-scm.com/) was used for version control within VSCode to push the code to GitHub
- [GitHub](https://github.com/) was used as a remote repository to store project code
- [PEP8](http://pep8online.com/) was used to check my code against Python conventions
- [Heroku](https://heroku.com/) was used to deploy the project into live environment
- [Visual Studio Code (VSCode)](https://code.visualstudio.com/)

### Libraries

#### Python Libraries
- [forex-python](https://pypi.org/project/forex-python/) Forex Python is a Free Foreign exchange rates and currency conversion

[Back to Table Of Contents](#table-of-contents)

## Features

### Informantions

- Provides user the steps to follow
- Gives a fast and easy navagation to users
- User stories covered: 2, 7
 
<details>
    <summary>Instructions Screenshot</summary>

![Instructions](images/features/screenshot_information.png)
</details>

### Top Currencies
- Displays a list of top currencies
- Allows user to find easily the most popular currencies
- User stories covered: 1, 6
  
<details>
    <summary>Top currencies Screenshot</summary>

![Top currencies](images/features/screenshot_topcurrencies.png)
</details>

### Extra Currencies
- Gives a big list of currencies coverd
- User stories covered: 3

<details>
    <summary>Extra currancies Screenshot</summary>

![Extra currencies](images/features/screenshot_extra.png)
</details>

### Result
- Gives result in real time exchange rate
- User stories covered: 4, 8

<details>
    <summary>Result Screenshot</summary>

![Result](images/features/screenshot_result.png)
</details>

### User Input Validation
- Displays an error message if user input is not in a form that was expected
- Asks for a new input and provides guidance to user on how to correctly format the input
- User stories covered: 5

<details>
    <summary>input validation Screenshot</summary>

![Amount validation](images/input_validation/input_validation02.png)
</details>

<details>
    <summary>Currency validation Screenshot</summary>

![Currency validation](images/input_validation/input_validation01.png)
</details>

<details>
    <summary>Conversion validation Screenshot</summary>

![Conversion validation](images/input_validation/input_validation03.png)
</details>

[Back to Table Of Contents](#table-of-contents)

## Validation

[PEP8 Validation](https://pep8ci.herokuapp.com/) was used to check the code for PEP8 requirements. All the code passes with no errors and no warnings to show.

<details><summary>PEP3 check for run.py</summary>
<img src="images/validation/pep8.png">
</details>

## Testing

<details><summary>See user stories testing</summary>

1. I want to have easy access to the top currencies

| **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
| Top Currencies | User can select or press 0 to pick an expecific one  | easy access | Works as expected |

<details><summary>Screenshot</summary>
<img src="images/testing/testing_topcurrencies.png">
</details>

2. I want to be able to see the instructions

| **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
| Instructions | follow the steps | easy understandin fast navigation | Works as expected |

<details><summary>Screenshot</summary>
<img src="images/testing/testing_instruction.png">
</details>

3. I want to have access to diffetent currencies

| **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
| Extra Currencies | We users press 0 they can choose a larger list of currencies  | easy access | Works as expected |

<details><summary>Screenshot</summary>
<img src="images/testing/testing_extra.png">
</details>

4. I want to receive a real time quotation

| **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
| Result | follow instrction set an amount, initial currency and currency to exchange | it gives a real time result  | Works as expected |

<details><summary>Screenshot</summary>
<img src="images/testing/testing_result.png">
</details>

5. I want users to have a positive experience

| **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
| Input Validation | Invalid data | Feedback message with instructions diplayed to the user  | Works as expected |

<details><summary>Screenshot</summary>
<img src="images/testing/testing_input1.png">
<img src="images/testing/testing_input2.png">
<img src="images/testing/testing_input3.png">
</details>

6. I want users to easily select options from the menu

| **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
| Top Currencies | List of top popular currencies | easy fast access  | Works as expected |

<details><summary>Screenshot</summary>
<img src="images/testing/testing_topcurrencies.png">
</details>

7. I want users to see and follow the instruction for a easy navigation

| **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
| instruction | Follow the steps | For easy and fast understaanding  | Works as expected |

<details><summary>Screenshot</summary>
<img src="images/testing/testing_instructions.png">
</details>

8. I want the user to receive a real time result

| **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
| Result | Follow instrction set an amount, initial currency and currency to exchange | it gives a real time result  | Works as expected |

<details><summary>Screenshot</summary>
<img src="images/testing/testing_result.png">
</details>

[Back to Table Of Contents](#table-of-contents)
## Bugs

| **Bug** | **Fix** |
| ------- | ------- |
| When forex_python is down result do not work | Error message conversion rate not available |
| When press N to quit  | Error message input invalid |

## Deployment

### Heroku
This application has been deployed from GitHub to Heroku by following the steps:

1. Create or log in to your account at heroku.com
2. Make sure you have connected your GitHub account to heroku.com - follow the steps to Get Started and Sign up for Heroku. Click “New” and then select project name, and the region then you can link to your GitHub account, select if you want to deploy automatic (once you deploy on github it wil deploy automaticly on heroku), ensure to add buldpacks (heroku/python - heroku/nodejs)
3. Set the Build Command:
    ```
    pip3 freeze > requirements.txt
    ```

### Forking the GitHub Repository

1. Go to the GitHub repository
2. Click on Fork button in top right corner
3. You will then have a copy of the repository in your own GitHub account.

### Making a Local Clone
1. Go to the GitHub repository 
2. Locate the Code button above the list of files and click it
3. Highlight the "HTTPS" button to clone with HTTPS and copy the link
4. Open Git Bash
5. Change the current working directory to the one where you want the cloned directory
6. Type git clone and paste the URL from the clipboard ($ git clone <span>https://</span>github.com/YOUR-USERNAME/YOUR-REPOSITORY)
7. Press Enter to create your local clone

[Back to Table Of Contents](#table-of-contents)

## Credits

### Images
- [Flaticon](https://www.flaticon.com/free-icon/exchange-rate_6342080?term=money+exchange&page=1&position=35&origin=search&related_id=6342080) was used for the website favicon

### Code
- [forex_python documentation](https://forex-python.readthedocs.io/en/latest/usage.html) Usage Examples
- [forex_python GitHub](https://github.com/MicroPyramid/forex-python) Usage Examples
- [Stack overflow](https://stackoverflow.com/questions/68896900/strange-currency-rates-source-not-ready-forex-python-error) helped me to find solution with errors
- Youtube video on [Python currecy converter](https://www.youtube.com/watch?v=VUrmKQOa3bM) Help to fix bug seting datetime

## Acknowledgements
I would like to thank everyone who supported me in the development of this project:
- My mentor Mo for feedback and words of encouragement
- My lovely wife for her support
- Code Institute community on Slack for resources and support