rm /var/www/html/*
mv /home/ponty/Git/PythonHtmlGetter/output/* /var/www/html
echo copy was succesful
/etc/init.d/apache2 start
