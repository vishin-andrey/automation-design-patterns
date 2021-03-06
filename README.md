# automation-design-patterns
Use the power of design patterns to solve different software automation related problems - Python

# List of design patterns covered for automation testing

## Page object pattern
### Summary
* Hide bad APIs behind better ones
* Automation related: represent each page (including elements and action over them) of an application as an object
 
### Example
* Targeted app: https://www.youtube.com
* Implement base page:
    * Currently supported:
        * open/quit the browser
        * wait for elements to be visible
    * Feature methods:
        * generic validator
        * different clicks
* Each new page created will extend the base class
* Implement a search for a video as example:
    * enter a string to query e.g. Python
    * click on search button
    * filter result list based on a keyword e.g. Python
    * select the video found based on this query
* In tests section, under page_object_pattern package, two tests are performed:
    * a simple one to perform the wait for element action from base class
    * a search flow
    * note that from now on the test implementation is hidden in a specific page; 
    * to perform some tests, you just have to call different page specific methods        

## Singleton 

###Summery
* Creational design pattern.
* Provides an easy way to create a single instance of an object.

###Example
* Access the same instance of the driver session class.
1. The entire definition of the object class is encapsulated in the builder class:
    * The outer class exposes a method that returns the instance of the inner class.

2. Design a class that handles the instantiation.
    * Inject the definition of the desired class in the singleton factory
    and the factory is responsible for returning the same instance.

## Factory pattern
### Simple factory
### Abstract factory

## Authors
* Paul Bodean
* Eugen Meltis

### License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details
