# Meme_Generator
The final project in Udacity's Intermediate Python Nanodegree program. 

In this project, we were tasked with creating a program that superimposes quotes over images to create randomized memes. The quotes were stored in four different file types. Our goal was to properly ingest the content of these files into blank models of our own design. quotes for this project were a combination of starter code, ideas that I brainstormed, and cherry-picked entries from the following link: [DogCaptions](https://getchip.com/dog-captions/#Short_Dog_Captions_for_Instagram). I replaced the starter image files with a collection of my own dog, Moose, who unfortunately lost his battle with Leukemia in 2016. This project serves as a loving memorial to showcase the comedic, snarky, and loving nature that Moose brought to the life of anyone who met him for over a decade. 

This project was a chance to showcase the skills presented to us in the **'Large Codebases with Libraries'** Course, including: 

- Object-Oriented thinking in Python, including abstract classes, class methods, and static methods.
- DRY (don't repeat yourself) principles of class and method design
- working with modules and packages in Python.
- Working with Flask Apps, CLI, and Web Interfaces
- Keeping code and docstrings PEP-8 compliant


## Overview
At the highest level of functionality, this project must complete the following requirements (taken directly from project instructions): 
- Interact with a variety of complex filetypes. This emulates the kind of data you'll encounter in a data engineering role. 
- Load quotes from a variety of filetypes (PDF, Word Docs, CSVs, Text files). 
- Load, manipulate, and save images/ 
- Accept dynamic user input through a command-line tool and a web service. This emulates the kind of work you'll encounter as a full stack developer.


## Setup Instructions
I developed my code on a Windows laptop, running Python 3.9.8. 
For convenience and simplicity, please clone my git repository:
```
gh repo clone conjohnson712/Meme_Generator
```
Or the project can be downloaded as a ZIP from that same repo if you prefer.


Please create a virtual environment and install the necessary dependencies from the requirements.txt file using the following code: 
```
python3.5 -m venv venv2
source venv2/bin/activate
pip install -r requirements.txt
```

With these steps completed, you are ready to make some memes!


## Modules Overview

### _data
This module is responsible for housing the data and images that will be used to create memes. Inside the directory, there are three folders: 
- **DogQuotes**: A collection of quotes, spread across four different files (CSV, Docx, PDF, txt).
- **photos**: A collection of image files, defaulting to images of Instructor's dog, Xander. In this case, it contains 42 images of my dog, Moose. Excuse the blur in some of them, he was too fast for cameras a lot of the time.
- **SimpleLines**: Example files of how to structure quotes and images. One file for each of the four file types listed in DogQuotes.


### Templates
A directory containing 3  HTML template files: 
- **base**
- **meme**
- **meme_form**

These act as the formatting for the web-based memes we will make. 


### MemeEngine
This module is responsible for housing the MemeEngine and its dependencies, including: 
- **Font**: A folder containing a .ttf file for my selected font.
- **__init__.py**: File responsible for initializing MemeEngine.py

The MemeEngine is responsible for: 
- Loading an image using Pillow(PIL).
- Resizing the image to a width of 500px
- Scaling the height of the image proportionally
- Adding a quote body and author to the image
- Saving the Manipulated image
- Implement this instance: make_meme(self, img_path, text, author, width=500) -> str
- Being PEP-8 Compliant and handling Exceptions


### QuoteEngine
This module is responsible for housing the QuoteEngine and the various file ingestors necessary to extract the quotes. These include: 
- **__init__.py**: Initializes the QuoteEngine with dependencies
- **QuoteModel.py**: Creates blank models for the quotes to be extracted into.
- **CSVIngestor.py**: Ingests CSV files and returns usable quotes
- **DocxIngestor.py**: Ingests Docx files and returns usable quotes
- **PDFIngestor.py**: Ingests PDF files, uses pdftotext to translate the PDF file into a usable quote.
- **TextIngestor.py**: Ingests plain text documents and returns a usable quote.
- **IngestorInterface.py**: Defines two methods, can_ingest and parse, that it checks against each of the helpers above. If the file type is one that can be ingested, then IngestorInterface parses the file to be usable for our quotes.
- **Ingestor.py**: Realizes the IngestorInterface and encapsulates the helper classes listed above.

With all of these files and functionality, the QuoteEngine Module should be able to: 
- Determine if a filetype is supported for ingestion. 
- Parse the file if so.
- Extract the data within that file type into a usable QuoteModel. 
- Complete extractions from all of the files listed in the IngestorInterface
- Return a collection of quotes that can be randomized and superimposed of images.


## Package my Application
Larger, complex systems need an interface for users to interact with. We'll package the project as a command line tool and as a simple web service.

### app.py
This file contains the Flask App responsible for running the web-interface version of this project. The app uses the Quote Engine Module and Meme Generator Modules to generate a random captioned image.

It uses the requests package to fetch an image from a user submitted URL.

To start this program, simply enter the following code into a terminal window: 
```
python3 app.py
```


### meme.py
This file contains the Command-Line Interface (CLI) tool that we will use to interact with this project through the terminal.

The script must take three optional CLI arguments:
- body a string quote body
- author a string quote author
- path an image path

The script returns a path to a generated image. If any argument is not defined, a random selection is used. 
To run this program, simply enter the following into a terminal window:
```
python3 meme.py
```


### requirements.txt
A plain text file that contains the necessary system requirements and dependencies to run the project. Should have been installed above, but if necessary, use the following code to install: 
```
pip install -r requirements.txt
```


## License
The Meme Generator Project starter code is the property of **Udacity**. The image files in this project are my own property.


