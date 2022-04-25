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


### Notes and considerations

I could have spent a bit more of time making things "perfect" (irony), but I'm already over the expected 4 hours and I think that, more or less, what I have done expresses my way of thinking and programming skills. There are parts of the code I don't specially like and I would prefer to talk to some peer to discuss alternative implementations. For instance:

* The `mow_lawn` service is dirty. I'd refactor it a bit more to seggregate responsibilities. Possibly by creating a service class able to parse the contents and return a data structure that would then be used to deploy the mowers.
* I lack of a "Pleateau" abstraction, I'm only using a "Position" representing the top-right corner of it. I think it's kind of flaky implementation, as the 0,0 assumption for the bottom-left corner sounds like a constraint taken only for convenience. What I've done does the job for the moment, with the current specs, but a `Plateau` would possibly emerge if the exercise was less constrained.
* The responsibilities for all the objects could be discussed. For instance, the `Navigator` class contains the current position of the mower, but it passes it to a `Direction` to calculate the resulting position after moving forward. I think it does well with the "State" pattern used for the facing of the mower, but the fact is that the position object is being passed from one hand to another, making me suspect that there is some responsiblity leak.


I wasn't sure of what to do when instructing the mower to go beyond the plateau boundaries. I could have left it unimplemented, but considering the perspective of having automated mow lawners going crazy and possibly attacking innocents, I thought it deserved some kind of control. So my take has been to interrupt the execution as soon as boundaries were about to be broken.

Finally, a controversial decision has been to implement the State pattern to have one class for each direction, so that each one of them knows where to face when turning right or left, and what the resulting position was when moving forward. It implies giving `Direction` a lot of responsibility. I could instead have used the typical list of directions (as constants) and use +1 or -1 and the module operator depending on the turning direction. However, having the two options in my hands, I thought that the pointer approach was lighter but less elegant and explicit, so I decided to go ahead with the heavier pattern.

One of my goals has been to protect the main class as much as possible, exposing only the methods and attributes required for solving the problem. Thus, the mower has only three exposed methods, that could be reduced to two if `execute()` returned the result without having to call `report()`.

I've tried to commit as much as possible, adding a 'Refactoring:' prefix to help reviewers differentiate implementation steps from refactoring ones.

I've enjoyed the exercise a lot, thanks for letting me participate in the process.


Carles.
