# Online library
![Library preview](https://dvmn.org/media/image_TLlI3D8.png)
## Description
This is a static website for an online library
## Structure
- books - JSON metadata, book texts and cover images
- pages - generated HTML pages
- static - static files
- index.html - redirect file to main page
- template.html - Jinja2 template for every page. It need for local render with `render_website.py`
- render_website.py - python file for rendering this site in local
## Example
### Demo of library
This repository is live at: [Online library](https://svillors.github.io/library)
### Running locally
If you want to run this repository on your own device, you can use `render_website.py`:
- Navigate to the directory of this repository.
- Install dependencies using
```bash
pip install -r requirements.txt
```
- Run the script using:
```bash
python3 render_website.py
```
- Open http://127.0.0.1:8000 in your browser
### Opening the Website Without Running a Server
If you don't want to run the script or start a local server, you can simply open the pre-generated HTML pages directly in your browser:
- Navigate to the pages folder inside the project.
- Double-click on any .html file, for example, `index.html` It will open in your browser like a regular website.