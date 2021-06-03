# vax
Covid-19 Vaccine slot availability web utility built in Python and Flask.

### About
Web utility that helps user to search for vaccine slots. Currently, supports searching by area pin code.

### Pre-requisites
Python 3+ installed

### Getting Started
In order to use the app locally, follow the below steps -

- Clone the repository 
  ```
    git clone https://github.com/nitishSr/vax.git
  ```

- Go to folder
  ```
    cd ~/vax
  ```

- Create and activate python virtual environment
  ```
    python -m venv .virt_env

    source .virt_env/bin/activate
  ```

- Install dependencies
  ```
    pip install flask

    pip install requests
  ```

- Run the app on local server
  ```
    flask run
  ```

- The app should be rendered on your localhost
