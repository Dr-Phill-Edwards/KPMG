# LDAP Server

dpkg-reconfigure slapd

Create a new password hash using `slappasswd`. Copy the SSHA into the password file.

Look in /etc/ldap/schema for missing attributes.

Admin password is `admin`.

Convert schema to ldif
slaptest -f ./schema_conv.conf -F /.

ldapadd -D "dc=kpmg,dc=com" -W -H ldapi:/// -f /poo/users.ldif

Data in /var/lib/ldap/data.mdb

ldapsearch -LLL -Y EXTERNAL -H ldapi:/// -b  cn=config olcRootDN=cn=admin,dc=com,dc=kpmg  dn olcRootDN olcRootPW

ldapsearch -H ldapi:/// -D cn=admin,dc=kpmg,dc=com -x -w admin -b dc=kpmg,dc=com -LLL cn=ticar

ldapsearch -H ldap://ldap -D cn=admin,dc=kpmg,dc=com -x -w admin -b dc=kpmg,dc=com -LLL cn=ticar

ldapsearch -LLL -Y EXTERNAL -H ldapi:/// -s base -b '' subschemaSubentry

ldapsearch -LLL -Y EXTERNAL -H ldapi:/// -s base -b cn=Subschema objectClasses

slapcat -n 0 -H "ldap:///???(!(entryDN:dnSubtreeMatch:=cn=schema,cn=config))"
