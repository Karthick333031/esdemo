
### Goal

- Simple setup to play around with API around ES
- Base version : 02nd Aug 2018


### ES Demo Commands

- Run esdemo-setup.sh
  * pre-req: docker, curl, virtualenv
  * Launches docker, sets up es, loads some test data and installs python modules

- In the code path: Run
  * python esdemo.py

- In Browser:
  * http://127.0.0.1:5000/
  * Enter: first
  * Enter: second
  * Enter: test
  * Enter: es
  * Hit back button in browser to search again

- In API:
  * http://127.0.0.1:5000/search?s=test
  * http://127.0.0.1:5000/search?s=first
  * http://127.0.0.1:5000/search?s=second

