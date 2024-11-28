#By Yusef Osman

#RESOURCE: https://www.youtube.com/watch?v=0UG2x2iWerk (VIDEO FROM ASSIGNMENT PDF PROVIDED)

# dockerfile, Image, Container
    #dockerfile is a blueprint for printing images
    #Image is a template for running containers
    #Container is the running process with my app in it

FROM python:3.12

ADD osma0173-assignment4.py .

CMD ["python", "./osma0173-assignment4.py"]