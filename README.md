# PytestAcademyBugs
---

Playwright+pytest automation tests on https://academybugs.com/# for practice.

## 💻 Topics

Integrated with:

- [x] https://playwright.help/python/
- [x] https://allurereport.org/

## 💻 Pre-requisites

Before you use this project you have be installed Allure and Python.

### Git clone

This will clone the project,and install all required packages to run the tet. No Selenium Server is required.

```
$ git clone https://github.com/Kar1stan/PytestAcademyBugs.git
$ cd PytestAcademyBugs
$ pip install -r requirements.txt
```

## 🚀 Run the project:

Open the terminal and run:

```
pytest
```

After the tests have run to see the reports open the terminal and run:

```
allure serve allure-results
```

To run docker-compose containers open terminal and run:

```
docker compose up -d
```

To stop docker-compose containers open terminal and run:

```
docker compose down
```

To see docker-compose containers test logs open terminal and run:

```
docker-compose logs -f tests
```

To see Allure reports in browser open terminal ands run:

```
docker-compose up allure
```

Then open http://localhost:4040


## Credits

For further help or additional errors [here](https://playwright.dev/python/)

If you want help about allure [here](https://allurereport.org/)
