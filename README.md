"# JavaDoc" 
<br>I hope is is final version of JavaDoc
<br>
<br>
There are 2 keys, '-c' and '-p'
<br>
<br>
run create_html.py with FULL path to .java file, path to folder where will be results of generation and '-c' parameter, the programm will create 'classname'.html file with documentation
<br>
Example:
python create_html.py /home/alex/IdeaProjects/java/src/main/java/com/pubnub/api/endpoints/objects_api/users/DeleteUser.java /home/alex/IdeaProjects -c
<br>
Full path to .html file from example will be: /home/alex/IdeaProjects/Class.html
<br>
<br>
run create_html.py with FULL path to package, path to folder where will be results of generation and '-p' parameter.
There will be all information about your code. 
<br>
Example:
python create_html.py /home/alex/IdeaProjects/java/src/main/java/com/pubnub/api /home/alex/IdeaProjects -p
<br>
Path to res folder from example: /home/alex/IdeaProjects/res
<br>
<br>
Programm will create 'res', there will be index.html file, run it.
<br>
There are 3 columns in index.html: All packages, All classes and Alphabetical index
<br>
There is alphabetical index in index.html
<br>
This program displays a directory tree. Choose package in 'All packages'. There will be folders that are in this package.
<br>
If there is .md file in your package you can read it.
