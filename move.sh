rm /var/www/html/*
mv ./output/* /var/www/html
echo copy was succesful
/etc/init.d/apache2 start
