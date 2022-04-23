# seat-mower
A code kata, very similar to mars rover

### Building the project

In order to build the project, you need to install a couple of dependencies first. Depending on your OS, please visit the following sites to install Docker and Docker Compose, if you don't have them:

* [Get Docker](https://docs.docker.com/get-docker/)
* [Install Docker Compose](https://docs.docker.com/compose/install/)

Once you have the deps installed, build the project by `cd`-ing into the current directory and running `docker-compose up -d`


### Running the specs

This is a python project using [Mamba](https://github.com/mamba-org/mamba) as the test framework. Mamba is a spec-based testing tool, similar to Ruby's rpsec. In order to run the test suite, execute the following command:

```
docker-compose exec backend mamba -f documentation
```


### Running the mowers

Execute the following command to see the code in action:


```
docker-compose exec backend python run.py
```

If you want to test different outputs, you must edit the `run.py` file to change the instructions to the desired.


