# Python - XML Tutorial

```
 mmmmm           m    #                           m    m m    m m
 #   "# m   m  mm#mm  # mm    mmm   m mm           #  #  ##  ## #
 #mmm#" "m m"    #    #"  #  #" "#  #"  #           ##   # ## # #
 #       #m#     #    #   #  #   #  #   #   """    m""m  # "" # #
 #       "#      "mm  #   #  "#m#"  #   #         m"  "m #    # #mmmmm
         m"
        ""
```

Thank you for coming by and checking out my fundamentals of Python tutorial. In this lesson, we will be looking at how to read and write to XML using the Python programming language.

## Objectives

In this lesson, you will:

1. learn what is XML
2. use the `os` and `xml` modules in the Python standard library
3. learn about XML elements and how to access them in python
4. use methods to get access to tags, attributes, and text
5. create new elements and write them to the XML file

With these 4 elements, you will be able to understand how to read and write to an XML file.

## Part I: Installing Python

In this tutorial, we will be using Python 3.6.1. Go to [python.org](https://www.python.org/downloads/) to download the version of Python we need to complete this tutorial. The installation process is straightforward, and when the install wizard (on Windows) asks you if you want to add Python to `PATH`, make sure you select yes. This way, you will be able to access Python anywhere on your computer in the command prompt.

Once that is done, open a new command prompt and type `python -v`. This will show you the version of Python you have installed.

Installed Python on MacOS and Linux is similar. Please see the instructions on Python.org on how to install Python on MacOS and Linux.

[Install Python on Windows](https://www.python.org/downloads/windows/)
[Install Python on MacOS](https://www.python.org/downloads/mac-osx/)
[Install Python on Linux](https://www.python.org/downloads/source/)

## Part II: Understanding XML

XML is short for Extensible Markup Language. It is similar to HTML, but XML was designed to store and transport data and to be readable by both humans and machines. The best way to say what makes HTML and XML different would be HTML defines what the data looks like (on a webpage), and XML defines what the data is. XML structures, stores, and allows for data transport for another program to read, manipulate, and use the data.

A use case example for XML would be an RSS feed. A user would like to receive updates on a blog they like to read, so they subscribe to the RSS feed of the website. Every time the client requests updates from the site, XML will be sent over the Internet to the client, and that XML will describe the details of the update, such as the titles, bodies, authors, and more of the newest blogs.

Another use case for XML is Microsoft Office. If you have ever used that productivity software and looked beneath the covers, you will see that every document is basically XML on the backend. 

The following are an example of HTML and XML, so you can see the difference between the two.

```
<!-- HTML example -->
<!doctype html>
<html>
<head>
<!-- stylesheets, metadata, and more -->
</head>
<body>
    <div id="pythonProductListing">
        <div class="product">
            <p class="name">Python Hoodie</p>
            <p class="description">This hoodie will keep your code warm and fuzzy.</p>
            <p class="cost">$49.95</p>
            <p class="shipping">$4.00</p>
        </div>
        <div class="product">
            <p class="name">Python T-Shirt</p>
            <p class="description">This shirt will make you look cool while you code.</p>
            <p class="cost">$19.95</p>
            <p class="shipping">$4.00</p>
        </div>
        <div class="product">
            <p class="name">Python Baseball Cap</p>
            <p class="description">Whatever you do, don't wear it backwards. People won't know what your favorite programming language is if you do!</p>
            <p class="cost">$14.95</p>
            <p class="shipping">$4.00</p>
        </div>
    </div>
</body>
</html>
```

```
<!-- XML example -->
<?xml version="1.0"?> 
<productListing title="Python Products"> 
    <product> 
        <name>Python Hoodie</name> 
        <description>This hoodie will keep your code warm and fuzzy.</description> 
        <cost>$49.95</cost> 
        <shipping>$4.00</shipping> 
    </product> 
    <product> 
        <name>Python T-Shirt</name>
        <description>This shirt will make you look cool while you code.</description> 
        <cost>$19.95</cost> 
        <shipping>$4.00</shipping>
    </product> 
    <product> 
        <name>Python Baseball Cap</name> 
        <description>Whatever you do, don't wear it backwards. People won't know what your favorite programming language is if you do!</description>
        <cost>$14.95</cost> 
        <shipping>$4.00</shipping> 
    </product>
</productListing>
```

## Part III: Python

As we said previously, we will be reading and writing to an XML file. The XML file will be where we store data to be read by Python. In our example, we will be updating the inventory of a store that sells products related to Python, such as hoodies, shirts, caps, and more.

Before we do that, we need to create a Python file and import some modules from the standard library to allow us to read and write to XML.

A Python module is a Python source file that exposes classes, functions, and global variables for you to use in your program. For our program, we will be using two Python modules that come with Python already. All of the modules that you have access to when using Python are called the standard library. You can add additional modules to Python using `pip`, but that is out of the scope for our tutorial.

The first module we will be importing to the Python project will be the `os` module. This will allow us to save the location of our XML file to a variable for later usage.