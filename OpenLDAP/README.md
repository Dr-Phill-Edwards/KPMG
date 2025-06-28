# LDAP Server

dpkg-reconfigure slapd

Admin password is `admin`.

ldapadd -D "dc=kpmg,dc=com" -W -H ldapi:/// -f /poo/users.ldif

Data in /var/lib/ldap/data.mdb

ldapsearch -LLL -Y EXTERNAL -H ldapi:/// -b  cn=config olcRootDN=cn=admin,dc=com,dc=kpmg  dn olcRootDN olcRootPW

ldapsearch -H ldapi:/// -D cn=admin,dc=kpmg,dc=com -x -w admin -b dc=kpmg,dc=com -LLL cn=ticar

