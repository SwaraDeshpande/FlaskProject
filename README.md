## Applicant Test

This test is intended to go over a broad array of topics without paying too much attention to each detail. It should also demonstrate learning new things quickly.

### Frontend

You’ve been asked to build a simple site, and handed a wireframe:

![wireframe](/images/wireframe.jpg)

You need to show the homepage on desktop browsers for the client review. You can use placeholder images for now. 
Feel free to apply some style, but assume you are handing off to a front-end developer who will finish the details.
Note the full site does not need to be created, links should not go anywhere.

### Backend

Your client is indecisive and must change the name of the company every day at will. You’ve decided a minimal backend will be needed so the change can be done quickly without writing code. Pick your favorite python based web framework. The client's six year old daughter also said that everyone should use RESTful api's so ensure this is done or explain why you chose not to. Create a small backend that:

* Stores the name of the company in a database
* Features an api view that shows retrieving the name from the database
* Your website should consume the api with any tool you want. It could be plain javascript or a framework. Make sure it does use the api and doesn't just set the company name server side in a django template.
* Follows [pep8](https://www.python.org/dev/peps/pep-0008/) style guidelines
Explain all choices made and why you might do this in a real project or maybe you just wanted to play with something new.


### Devops!

Your team uses different operating systems and you need to share the project with them easily.
Use [docker](https://docs.docker.com/) and [docker-compose](https://docs.docker.com/compose/) to run the application. The web server, database, and anything else needed is up to you. The goal is that when someone receives the program they can run it easily without having to set up anything besides docker/compose. Check out the [django example](https://docs.docker.com/compose/django/) and notice how once compose is installed I can just type “docker-compose up” and it works.

After doing this briefly explain what you like and/or dislike about using docker.

### The Deliverable

Push your work up to this repo. We should be able to run “docker-compose up”, maybe run any extra commands you give us, then go to a web browser and see the finished site. Include a 'notes.md' file with your answers/notes for the above questions.

## Tips

- [Quickstart with docker compose and django](https://docs.docker.com/compose/django/)
- Ask us the same questions you would ask if you were already working here. It isn't a bad thing to ask for help.
- Depending on the speed of your computer, the database may not be available when the docker web container starts and it will error. Simply stop and start them again to fix this.
- On certain older computers the default Docker installation instructions may to work. This can happen with CPU's that don't support virtualization extentions and when using OSX. If this happens please contact us for help.
