rm /var/www/html/*
mkdir /var/www/html/output
mv ./output/* /var/www/html/output
echo copy was succesful
/etc/init.d/apache2 start
