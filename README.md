# Alumni-platform-backend

A web application based school project that allows all Moringa Alumni's to keep in touch with one another.For this part of the project it contains the backend
logic which also has the endpoints for each and every API that is called on the front-end.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.
ct
### Prerequisites

What things you need to install the software and how to install them

```
git clone
```
Clone the project from the git repository and run it on your terminal
### Installing

A step by step series of examples that tell you how to get a development env running


```
python3 manage.py runserver
```
## Running the tests

On VSCode terminal run the following command since i'm using the pytest method
```
pytest
```
gram is the name of the application
### Break down end to end tests

Testing if a user can save an image

```
 def test_create_method(self):
        business = self.post.create_post()
        self.assertTrue(post)
``` 
## Deployment

For deployment of the project it will depend on your hosting service as different hosting service come with different configurations of the application.

## Built With

* [Django_rest_framework](https://www.django-rest-framework.org/) - Tool used for creating WEB API's
* [Python-Django](https://docs.djangoproject.com/en/4.0/) - The web framework tool used for creating the logic

## Authors

Paul Munyao

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md)
