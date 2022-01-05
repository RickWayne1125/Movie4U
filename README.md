# Movie4U
Movie For You is a movie recommendation system with basic functions.

Configurations are set in the `config.py` file.

```python
database = {
    'url': 'database url',  # Put Your Database URL Here
    'user': 'admin',        # User Name For Database Access
    'pwd': 'pwd'            # Password
}
spark = {
    'url': 'spark url'      # URL For Spark Requests
}
pic_folder = {
    'url': 'pic link'       # The Path For Pic Folder
    # access a picture with <pic_link['url]> + xx.jpg
}
```
